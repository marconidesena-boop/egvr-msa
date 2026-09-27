"""Diario transacional LOCAL por NUP/PDF. Nao controla navegador nem acessa rede.

Impede reservas repetidas neste banco. A ferramenta de UI nao fica tecnicamente
bloqueada; todos os executores devem usar o mesmo banco e respeitar o controle.
Nenhum estado local comprova sozinho a verdade das evidencias institucionais.
"""
import argparse
import hashlib
import json
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from decidir_etapa import decide


def digest(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def connect(path):
    db = sqlite3.connect(path, timeout=10)
    db.row_factory = sqlite3.Row
    db.executescript('''
        CREATE TABLE IF NOT EXISTS itens(
          chave TEXT PRIMARY KEY, nup TEXT NOT NULL, placa TEXT NOT NULL,
          arquivo TEXT NOT NULL, sha256 TEXT NOT NULL, estado TEXT NOT NULL,
          documento TEXT, UNIQUE(nup,sha256));
        CREATE TABLE IF NOT EXISTS eventos(
          id INTEGER PRIMARY KEY, instante TEXT NOT NULL, chave TEXT NOT NULL,
          estado TEXT NOT NULL, evidencia TEXT NOT NULL);
    ''')
    return db


def event(db, key, state, evidence):
    if not isinstance(evidence, str) or not evidence.strip():
        raise ValueError('Referencia de evidencia obrigatoria.')
    db.execute('INSERT INTO eventos(instante,chave,estado,evidencia) VALUES(?,?,?,?)',
               (datetime.now(timezone.utc).isoformat(), key, state, evidence))


def prepare(db, items):
    """Valida todo o lote antes de inserir. Repeticoes identicas nao duplicam fila."""
    validated = []
    for item in items:
        nup, plate = item['nup'], item['placa']
        if not re.fullmatch(r'\d{5}\.\d{6}/\d{4}-\d{2}', nup):
            raise ValueError('NUP invalido.')
        if not re.fullmatch(r'[A-Z]{3}\d[A-Z0-9]\d{2}', plate):
            raise ValueError('Placa invalida.')
        path = Path(item['arquivo']).resolve(strict=True)
        with path.open('rb') as stream:
            if stream.read(5) != b'%PDF-':
                raise ValueError('Arquivo sem cabecalho PDF.')
        sha = digest(path)
        if item.get('sha256', sha).lower() != sha:
            raise ValueError('Arquivo diverge do hash esperado.')
        key = hashlib.sha256((nup+'|'+sha).encode()).hexdigest()
        validated.append((key, nup, plate, str(path), sha))
    with db:
        db.execute('BEGIN IMMEDIATE')
        for key, nup, plate, path, sha in validated:
            conflict = db.execute('SELECT placa,nup FROM itens WHERE sha256=? OR nup=?', (sha,nup)).fetchall()
            if any(row['placa'] != plate or row['nup'] != nup for row in conflict):
                raise ValueError('Associacao conflitante de PDF, placa ou NUP.')
            cur = db.execute('INSERT OR IGNORE INTO itens VALUES(?,?,?,?,?,?,NULL)',
                             (key,nup,plate,path,sha,'PREPARADO'))
            if cur.rowcount:
                event(db,key,'PREPARADO','Integridade local; identidade no SEI ainda nao atestada.')
    return [row[0] for row in validated]


def reserve(db, key, control):
    """Grava antes do upload. Sem expiracao automatica: queda exige reconciliacao."""
    with db:
        db.execute('BEGIN IMMEDIATE')
        row = db.execute('SELECT * FROM itens WHERE chave=?',(key,)).fetchone()
        if row is None or row['estado'] != 'PREPARADO':
            raise ValueError('Item ausente, reservado ou ja encerrado; reconciliar antes de repetir.')
        if any(control.get(k) != row[v] for k,v in [('nup','nup'),('placa','placa'),('arquivo_sha256','sha256')]):
            raise ValueError('Controle pertence a outro item.')
        if digest(row['arquivo']) != row['sha256']:
            raise ValueError('PDF alterado desde a preparacao.')
        decision = decide(control)
        if decision['etapa'] != 'INCLUIR_PDF':
            raise ValueError('Precondicoes nao satisfeitas: '+decision['etapa'])
        if db.execute("SELECT 1 FROM itens WHERE nup=? AND estado IN ('INICIADA','INCERTA')",(row['nup'],)).fetchone():
            raise ValueError('Outra tentativa nao reconciliada no processo.')
        db.execute("UPDATE itens SET estado='INICIADA' WHERE chave=?",(key,))
        event(db,key,'INICIADA',json.dumps(control,ensure_ascii=False))


def reconcile(db, key, state, evidence, document=None, downloaded=None):
    if state not in {'INCERTA','SEM_EFEITO','INCLUIDO','JA_EXISTENTE'}:
        raise ValueError('Estado de reconciliacao invalido.')
    with db:
        db.execute('BEGIN IMMEDIATE')
        row = db.execute('SELECT * FROM itens WHERE chave=?',(key,)).fetchone()
        if row is None:
            raise ValueError('Item inexistente.')
        allowed = {'PREPARADO'} if state == 'JA_EXISTENTE' else {'INICIADA','INCERTA'}
        if row['estado'] not in allowed:
            raise ValueError('Transicao invalida; resultado final preservado.')
        if state in {'INCLUIDO','JA_EXISTENTE'}:
            if not isinstance(document,str) or not re.fullmatch(r'\d+',document):
                raise ValueError('Numero SEI real obrigatorio.')
            if not downloaded or digest(downloaded) != row['sha256']:
                raise ValueError('Readback binario divergente/ausente; manter pendente para analise.')
        elif document is not None:
            raise ValueError('Numero de documento contradiz resultado informado.')
        event(db,key,state,evidence)
        db.execute('UPDATE itens SET estado=?,documento=? WHERE chave=?',(state,document,key))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('banco',type=Path)
    sub = parser.add_subparsers(dest='acao',required=True)
    p = sub.add_parser('preparar'); p.add_argument('manifesto',type=Path)
    p = sub.add_parser('reservar'); p.add_argument('chave'); p.add_argument('controle',type=Path)
    p = sub.add_parser('registrar'); p.add_argument('chave'); p.add_argument('estado'); p.add_argument('evidencia'); p.add_argument('--documento'); p.add_argument('--arquivo-baixado')
    sub.add_parser('listar')
    args = parser.parse_args()
    try:
        with connect(args.banco) as db:
            if args.acao == 'preparar':
                result = prepare(db,json.loads(args.manifesto.read_text(encoding='utf-8-sig')))
            elif args.acao == 'reservar':
                reserve(db,args.chave,json.loads(args.controle.read_text(encoding='utf-8-sig'))); result={'estado':'INICIADA'}
            elif args.acao == 'registrar':
                reconcile(db,args.chave,args.estado,args.evidencia,args.documento,args.arquivo_baixado); result={'estado':args.estado}
            else:
                result=[dict(r) for r in db.execute('SELECT * FROM itens ORDER BY nup')]
        print(json.dumps(result,ensure_ascii=False,indent=2))
    except (ValueError, OSError, KeyError, TypeError, sqlite3.Error) as exc:
        print(json.dumps({'erro':str(exc),'executa_sei':False},ensure_ascii=False)); return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
