"""Checagem local de consistencia. Nao acessa rede, SEI ou navegador.

Le somente o JSON informado e sugere uma etapa; nao valida a verdade da evidencia,
nao concede autorizacao e nao executa a etapa sugerida.
"""
import argparse
import json
import re
from pathlib import Path


BOOLS = (
    "parar", "autorizacao_inclusao", "autorizacao_restaurar_mesa",
    "identidade_confirmada", "arquivo_conferido", "metadados_confirmados",
    "ferramenta_disponivel", "acesso_confirmado", "reaberto_nesta_execucao",
    "documento_confirmado", "leitura_posterior_conferida",
)
ENUMS = {
    "modo": {"PREPARACAO", "PILOTO", "LOTE_QUALIFICADO"},
    "estado_inicial_mesa": {"ABERTO", "CONCLUIDO", "DESCONHECIDO"},
    "estado_atual_mesa": {"ABERTO", "CONCLUIDO", "DESCONHECIDO"},
    "duplicidade": {"NAO_VERIFICADA", "AUSENTE", "PRESENTE", "INCONCLUSIVA"},
    "intervencao_externa": {"NAO_DETECTADA", "DETECTADA", "DESCONHECIDA"},
    "tentativa": {"NAO_INICIADA", "INICIADA", "SEM_EFEITO_COMPROVADO", "INCERTA"},
}


def filled(value):
    return isinstance(value, str) and bool(value.strip())


def decide(c):
    def result(step, reason):
        return {"etapa": step, "motivo": reason, "executa_acao": False}

    def block(reason):
        return result("BLOQUEADO", reason)

    if not isinstance(c, dict):
        return block("Controle deve ser um objeto JSON.")
    if c.get("parar") is True:
        return result("PARAR", "Pedido de parada: nenhuma acao, inclusive restauracao.")
    if c.get("versao_controle") != "1":
        return block("Versao de controle ausente ou desconhecida.")
    if any(type(c.get(key)) is not bool for key in BOOLS):
        return block("Booleano ausente/invalido; texto nao comprova uma checagem.")
    if any(not isinstance(c.get(k), str) or c[k] not in values for k, values in ENUMS.items()):
        return block("Estado ausente ou desconhecido.")
    evidence = c.get("evidencias")
    if not isinstance(evidence, dict):
        return block("Evidencias devem ser um objeto.")
    def has(*keys):
        return all(filled(evidence.get(k)) for k in keys)

    if c["modo"] == "PREPARACAO":
        return result("PREPARAR_SEM_OPERAR_SEI", "Configuracao/preparacao nao autoriza acesso institucional.")
    if c["modo"] == "LOTE_QUALIFICADO" and not has("qualificacao_do_perfil"):
        return block("Lote depende de qualificacao real do perfil/ferramenta, nao so deste auxiliar.")
    if not c["autorizacao_inclusao"] or not filled(c.get("referencia_autorizacao")):
        return block("Falta autorizacao vigente e identificavel para a inclusao delimitada.")
    if not isinstance(c.get("nup"), str) or not re.fullmatch(r"\d{5}\.\d{6}/\d{4}-\d{2}", c["nup"]):
        return block("NUP individual ausente ou formato indefinido; nao fabricar identificadores.")
    if not filled(c.get("unidade")) or not filled(c.get("placa")):
        return block("Falta unidade ou placa individual.")
    if not isinstance(c.get("arquivo_sha256"), str) or not re.fullmatch(r"[0-9a-fA-F]{64}", c["arquivo_sha256"]):
        return block("Falta identificacao de integridade do arquivo.")
    if not c["identidade_confirmada"] or not c["arquivo_conferido"] or not has("identidade", "arquivo"):
        return block("Vinculo ou arquivo sem confirmacao documentada.")
    if not c["ferramenta_disponivel"] or not c["acesso_confirmado"] or not has("ferramenta", "acesso"):
        return block("Ferramenta/acesso nao conferidos; nao tentar escrita ou restauracao.")

    initial, current = c["estado_inicial_mesa"], c["estado_atual_mesa"]
    if initial == "DESCONHECIDO" or current == "DESCONHECIDO" or not has("mesa_inicial", "mesa_atual"):
        return block("Estado da mesa nao comprovado na unidade-alvo.")
    if c["reaberto_nesta_execucao"] and (initial != "CONCLUIDO" or not has("reabertura")):
        return block("Reabertura declarada incompativel ou sem evidencia.")

    if c["tentativa"] in {"INICIADA", "INCERTA"} and not c["documento_confirmado"]:
        return result("RECONCILIAR_SOMENTE_LEITURA", "Efeito possivel: nao reenviar nem concluir antes de verificar.")

    outcome = None
    if c["documento_confirmado"]:
        if c["tentativa"] not in {"INICIADA", "INCERTA"}:
            return block("Inclusao confirmada sem tentativa correspondente; preservar historico.")
        outcome = "INCLUIDO"
    elif c["duplicidade"] == "PRESENTE":
        if c["tentativa"] != "NAO_INICIADA":
            return block("Documento existente e tentativa divergem; reconciliar historico.")
        outcome = "JA_EXISTENTE"
    elif c["tentativa"] == "SEM_EFEITO_COMPROVADO":
        if not has("ausencia_de_efeito") or c.get("numero_documento_sei") is not None:
            return block("Ausencia de efeito sem evidencia ou contradita por numero de documento.")
        outcome = "FALHA_SEM_EFEITO"

    if outcome in {"INCLUIDO", "JA_EXISTENTE"}:
        doc = c.get("numero_documento_sei")
        if not isinstance(doc, str) or not re.fullmatch(r"\d+", doc):
            return block("Numero SEI de documento ainda nao confirmado.")
        if not c["leitura_posterior_conferida"] or not has("registro_documento", "conteudo_pos"):
            return block("Falta leitura do registro e conteudo efetivamente armazenado.")
        if outcome == "JA_EXISTENTE" and not has("duplicidade"):
            return block("Equivalencia de documento existente sem evidencia.")

    if outcome:
        if initial == "ABERTO":
            if current != "ABERTO":
                return result("PENDENCIA_MESA", "Processo inicialmente aberto mudou; nao reabrir por suposicao.")
            return result("FINALIZAR_" + outcome, "Preservar a mesa aberta; nao concluir.")
        if current == "CONCLUIDO":
            return result("FINALIZAR_" + outcome, "Mesa concluida confirmada; nao atribuir ato de terceiro ao agente.")
        if not c["reaberto_nesta_execucao"]:
            return result("PENDENCIA_MESA", "Abertura nao atribuida a esta execucao; nao concluir trabalho alheio.")
        if not c["autorizacao_restaurar_mesa"]:
            return block("Restauracao nao autorizada; relatar mesa pendente.")
        if c["intervencao_externa"] != "NAO_DETECTADA" or not has("concorrencia"):
            return result("PENDENCIA_MESA", "Intervencao externa detectada ou nao esclarecida; nao concluir.")
        return result("CONCLUIR_NA_UNIDADE", "Restaurar somente a unidade que esta execucao reabriu; conferir depois.")

    if c["leitura_posterior_conferida"] or c.get("numero_documento_sei") is not None:
        return block("Registro posterior sem resultado reconciliado; nao iniciar outro envio.")
    if c["duplicidade"] != "AUSENTE" or not has("duplicidade"):
        return block("Ausencia de duplicidade nao demonstrada.")
    if not c["metadados_confirmados"] or not c.get("metadados") or not has("metadados"):
        return block("Tipo, data, descricao, formato e acesso nao fundamentados.")
    if c["intervencao_externa"] != "NAO_DETECTADA" or not has("concorrencia"):
        return block("Concorrencia nao esclarecida antes de mutacao.")
    if initial == "CONCLUIDO":
        if not c["autorizacao_restaurar_mesa"]:
            return block("Falta autorizacao do ciclo reabrir/incluir/concluir.")
        if current == "CONCLUIDO":
            if c["reaberto_nesta_execucao"]:
                return block("Mesa mudou apos reabertura; investigar antes de repetir o ciclo.")
            return result("REABRIR_NA_UNIDADE", "Envio preparado; reabrir somente a unidade-alvo e confirmar.")
        if not c["reaberto_nesta_execucao"]:
            return block("Abertura por outra intervencao; nao assumir controle do processo.")
    elif current != "ABERTO":
        return block("Estado da mesa mudou desde o inicio; nao alterar para forcar inclusao.")
    return result("INCLUIR_PDF", "Precondicoes declaradas completas; registrar tentativa antes de persistir e conferir depois.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("controle", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.controle.read_text(encoding="utf-8-sig"))
        output = decide(data)
    except (OSError, ValueError) as exc:
        output = {"etapa": "BLOQUEADO", "motivo": str(exc), "executa_acao": False}
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 2 if output["etapa"] == "BLOQUEADO" else 0


if __name__ == "__main__":
    raise SystemExit(main())
