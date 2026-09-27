"""Verificação estrutural; não executa planilhas, rede, instalação ou SEI.

Uso: python validar_pacote.py [raiz-plugin] [--out resultado.json]
Dependências de desenvolvimento: jsonschema e PyYAML.
"""
from pathlib import Path
import json,re,sys,argparse,hashlib
from datetime import datetime,timezone
import jsonschema,yaml

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('root',nargs='?',default=str(Path(__file__).resolve().parents[3]))
    ap.add_argument('--out')
    args=ap.parse_args()
    root=Path(args.root).resolve(); skill=root/'skills/conciliar-restricoes'; ev=skill/'evals'
    results=[]
    def record(id,name,fn):
        try:
            detail=fn(); results.append({'id':id,'nome':name,'resultado':'APROVADO','observado':detail})
        except Exception as exc:
            results.append({'id':id,'nome':name,'resultado':'REPROVADO','observado':str(exc)})
    def readj(p): return json.loads(p.read_text(encoding='utf-8'))
    manifest=readj(root/'plugin.json')
    def portable():
        schema=readj(ev/'schemas/plugin.schema.json'); jsonschema.Draft202012Validator.check_schema(schema)
        jsonschema.Draft202012Validator(schema).validate(manifest)
        assert re.fullmatch(r'\d+\.\d+\.\d+',manifest['version'])
        assert root.name==manifest['name']=='egvr-msa'
        return {'schema_sha256':hashlib.sha256((ev/'schemas/plugin.schema.json').read_bytes()).hexdigest(),'versao':manifest['version']}
    record('E01','Manifesto portátil contra schema oficial',portable)
    def overlay():
        compat=readj(root/'.codex-plugin/plugin.json')
        for k in ['name','description','author']: assert compat[k]==manifest[k], k
        assert re.fullmatch(re.escape(manifest['version'])+r'\+codex\.[A-Za-z0-9._-]+',compat['version']), 'version'
        assert compat['interface']==manifest['extensions']['com.openai']['interface']
        assert compat['interface']['displayName']=='EGVR MSA'
        assert compat['skills']=='./skills/'
        assert not ({'apps','mcpServers','hooks'} & set(compat))
        return {'identidade':'Idêntica entre os manifestos','versao_portatil':manifest['version'],'versao_codex':compat['version'],'componentes':'Portáteis mantidos na raiz'}
    record('E02','Coerência de compatibilidade',overlay)
    def frontmatter():
        text=(skill/'SKILL.md').read_text(encoding='utf-8')
        match=re.match(r'^---\n(.*?)\n---\n',text,re.S); assert match
        fm=yaml.safe_load(match[1]); assert fm['name']==skill.name
        assert 0<len(fm['description'])<=1024
        assert len(text.splitlines())<500
        return {'skill':fm['name'],'linhas':len(text.splitlines())}
    record('E03','Frontmatter e tamanho da skill',frontmatter)
    def links():
        n=0; errors=[]
        for f in root.rglob('*.md'):
            t=f.read_text(encoding='utf-8')
            for dest in re.findall(r'\[[^\]]+\]\(([^)]+)\)',t):
                dest=dest.strip('<>'); path=dest.split('#')[0]
                if not path or re.match(r'^[a-zA-Z]+:',path): continue
                n+=1; target=(f.parent/path).resolve()
                if not target.is_relative_to(root) or not target.exists(): errors.append(f'{f.relative_to(root)} -> {dest}')
        assert not errors, errors
        return {'links_locais':n,'limite':'Confere arquivos; não verifica âncoras de cabeçalho ou URLs externas.'}
    record('E04','Destinos de referências locais',links)
    def rules():
        ids=[]
        for f in root.rglob('*.md'):
            for rid in re.findall(r'^##+\s+(R\d{2}[A-D]?)\b',f.read_text(encoding='utf-8'),re.M): ids.append(rid)
        expected={f'R{i:02}' for i in range(1,26) if i!=15}|{'R15A','R15B','R15C','R15D'}
        assert set(ids)==expected, {'faltantes':sorted(expected-set(ids)),'extras':sorted(set(ids)-expected)}
        assert len(ids)==len(set(ids)), 'Definição normativa duplicada'
        return {'regras_unicas':len(ids)}
    record('E05','Identificadores e ausência de definição duplicada',rules)
    def cases():
        d=readj(ev/'casos.json')
        c=d if isinstance(d,list) else d['casos_obrigatorios']
        ts=[x for x in c if re.fullmatch(r'T\d{2}',x['id'])]
        assert [x['id'] for x in ts]==[f'T{i:02}' for i in range(1,56)]
        assert len({x['id'] for x in c})==len(c)
        required=['dados_de_entrada','estado_inicial','escopo_autorizado','resultado_esperado','alteracoes_permitidas','alteracoes_proibidas','criterio_de_aprovacao']
        missing={x['id']:[k for k in required if not x.get(k)] for x in ts}; missing={k:v for k,v in missing.items() if v}
        assert not missing,missing
        assert [x['id'] for x in d['casos_adversariais']]==[f'AD{i:02}' for i in range(1,12)]
        assert [x['id'] for x in d['sei_futuros']]==[f'SF{i:02}' for i in range(1,6)]
        examples=['hipotese-do-usuario-confirmada','hipotese-do-usuario-rejeitada','conclusao-revertida-na-segunda-passagem','capacidade-implementada-mas-nao-validada','falso-positivo-evitado']
        for name in examples: assert (skill/'examples'/f'{name}.md').stat().st_size>250
        return {'cenarios_obrigatorios':len(ts),'comportamento':38,'ferramenta':17,'adversariais':11,'sei_futuros':5,'exemplos':5,'limite':'Valida catálogo; não aprova comportamento nem escrita.'}
    record('E06','Catálogo de aceitação completo',cases)
    def privacy():
        forbidden={'mcp.json','.mcp.json','.app.json','hooks.json','.env'}
        files=[f for f in root.rglob('*') if f.is_file()]
        assert all(not f.is_symlink() for f in root.rglob('*'))
        assert not [str(f.relative_to(root)) for f in files if f.name in forbidden]
        assert not [str(f) for f in files if 'node_modules' in f.parts or '__pycache__' in f.parts]
        suspicious=[]
        for f in files:
            if f.suffix in ['.md','.json','.csv']:
                t=f.read_text(encoding='utf-8')
                if re.search(r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----|sk-[A-Za-z0-9]{32,}|Bearer\s+[A-Za-z0-9._-]{32,}',t): suspicious.append(str(f.relative_to(root)))
        assert not suspicious,suspicious
        return {'arquivos_verificados':len(files),'limite':'Ausência de componentes proibidos e padrões comuns de segredos; complementada por revisão humana do conteúdo.'}
    record('E07','Componentes, links simbólicos e padrões de segredos',privacy)
    def coverage():
        d=readj(root/'COBERTURA-GRANULAR.json')['paragrafos']
        assert {x['secao'] for x in d if x['secao']}==set(range(1,26))
        assert len({x['paragrafo_extraido'] for x in d})==len(d)
        for x in d: assert (root/x['referencia_principal']).is_file()
        return {'secoes':25,'paragrafos':len(d),'limite':'Vinculação formal; suficiência da tradução das regras revisada separadamente.'}
    record('E08','Rastreabilidade e existência dos destinos',coverage)
    result={'versao':manifest['version'],'tipo':'ESTRUTURAL','executado_em':datetime.now(timezone.utc).isoformat(),'testes':results,'aprovados':sum(x['resultado']=='APROVADO' for x in results),'reprovados':sum(x['resultado']=='REPROVADO' for x in results),'homologacao_operacional':False}
    out=json.dumps(result,ensure_ascii=False,indent=2)
    if args.out: Path(args.out).write_text(out+'\n',encoding='utf-8')
    print(out)
    sys.exit(bool(result['reprovados']))

if __name__=='__main__': main()
