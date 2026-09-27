"""Testes sinteticos do auxiliar, sem navegador, rede ou dados institucionais."""
import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("sei_decision", ROOT / "scripts/decidir_etapa.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def ready(initial="ABERTO"):
    c = json.loads((ROOT / "templates/controle-inclusao.json").read_text(encoding="utf-8"))
    c.update(modo="PILOTO", autorizacao_inclusao=True, autorizacao_restaurar_mesa=True,
             referencia_autorizacao="Pedido sintetico de inclusao e restauracao",
             nup="00000.000001/2026-00", unidade="UNIDADE_TESTE", placa="AAA0000",
             arquivo_sha256="a" * 64, identidade_confirmada=True, arquivo_conferido=True,
             metadados_confirmados=True, ferramenta_disponivel=True, acesso_confirmado=True,
             estado_inicial_mesa=initial, estado_atual_mesa=initial,
             duplicidade="AUSENTE", intervencao_externa="NAO_DETECTADA",
             metadados={"tipo": "Consulta sintetica", "data": "01/01/2026",
                        "descricao": "Consulta ficticia", "formato": "Nato-digital",
                        "acesso": "Classificacao sintetica fundamentada"})
    c["evidencias"] = {k: "Fixture sintetica: " + k for k in (
        "identidade", "arquivo", "ferramenta", "acesso", "mesa_inicial", "mesa_atual",
        "duplicidade", "metadados", "concorrencia")}
    return c


def reopened():
    c = ready("CONCLUIDO")
    c.update(estado_atual_mesa="ABERTO", reaberto_nesta_execucao=True)
    c["evidencias"]["reabertura"] = "Fixture: reabertura pelo executor nesta unidade"
    return c


def included(c):
    c = copy.deepcopy(c)
    c.update(tentativa="INICIADA", documento_confirmado=True,
             numero_documento_sei="12345678", leitura_posterior_conferida=True)
    c["evidencias"].update(registro_documento="Fixture: registro no mesmo NUP",
                         conteudo_pos="Fixture: SHA-256 identico")
    return c


class DecisionTests(unittest.TestCase):
    def step(self, c, expected):
        result = MODULE.decide(c)
        self.assertEqual(result["etapa"], expected, result)
        self.assertIs(result["executa_acao"], False)

    def test_01_open_ready(self):
        self.step(ready(), "INCLUIR_PDF")

    def test_02_closed_ready(self):
        self.step(ready("CONCLUIDO"), "REABRIR_NA_UNIDADE")

    def test_03_reopened_ready(self):
        self.step(reopened(), "INCLUIR_PDF")

    def test_04_closed_included_restore(self):
        self.step(included(reopened()), "CONCLUIR_NA_UNIDADE")

    def test_05_initially_open_never_close(self):
        self.step(included(ready()), "FINALIZAR_INCLUIDO")

    def test_06_final_closed(self):
        c = included(reopened()); c["estado_atual_mesa"] = "CONCLUIDO"
        self.step(c, "FINALIZAR_INCLUIDO")

    def test_07_timeout_no_resubmit_no_close(self):
        c = reopened(); c["tentativa"] = "INCERTA"
        self.step(c, "RECONCILIAR_SOMENTE_LEITURA")

    def test_08_started_without_confirmation(self):
        c = reopened(); c["tentativa"] = "INICIADA"
        self.step(c, "RECONCILIAR_SOMENTE_LEITURA")

    def test_09_existing_no_reopen(self):
        c = included(ready("CONCLUIDO"))
        c.update(tentativa="NAO_INICIADA", documento_confirmado=False, duplicidade="PRESENTE")
        self.step(c, "FINALIZAR_JA_EXISTENTE")

    def test_10_existing_found_after_reopen(self):
        c = included(reopened())
        c.update(tentativa="NAO_INICIADA", documento_confirmado=False, duplicidade="PRESENTE")
        self.step(c, "CONCLUIR_NA_UNIDADE")

    def test_11_unknown_initial_state(self):
        c = ready(); c["estado_inicial_mesa"] = "DESCONHECIDO"
        self.step(c, "BLOQUEADO")

    def test_12_other_actor_opened(self):
        c = ready("CONCLUIDO"); c["estado_atual_mesa"] = "ABERTO"
        self.step(c, "BLOQUEADO")

    def test_13_external_intervention_after_inclusion(self):
        c = included(reopened()); c["intervencao_externa"] = "DETECTADA"
        self.step(c, "PENDENCIA_MESA")

    def test_14_unknown_concurrency(self):
        c = included(reopened()); c["intervencao_externa"] = "DESCONHECIDA"
        self.step(c, "PENDENCIA_MESA")

    def test_15_stop_even_when_restore_pending(self):
        c = included(reopened()); c["parar"] = True
        self.step(c, "PARAR")

    def test_16_no_authorization(self):
        c = ready(); c["autorizacao_inclusao"] = False
        self.step(c, "BLOQUEADO")

    def test_17_no_restore_authorization(self):
        c = ready("CONCLUIDO"); c["autorizacao_restaurar_mesa"] = False
        self.step(c, "BLOQUEADO")

    def test_18_no_identity(self):
        c = ready(); c["identidade_confirmada"] = False
        self.step(c, "BLOQUEADO")

    def test_19_no_duplicate_evidence(self):
        c = ready(); c["duplicidade"] = "INCONCLUSIVA"
        self.step(c, "BLOQUEADO")

    def test_20_missing_metadata(self):
        c = ready(); c["metadados_confirmados"] = False
        self.step(c, "BLOQUEADO")

    def test_21_missing_readback(self):
        c = included(reopened()); c["leitura_posterior_conferida"] = False
        self.step(c, "BLOQUEADO")

    def test_22_missing_document_number(self):
        c = included(reopened()); c["numero_documento_sei"] = None
        self.step(c, "BLOQUEADO")

    def test_23_failed_without_effect_restore(self):
        c = reopened(); c["tentativa"] = "SEM_EFEITO_COMPROVADO"
        c["evidencias"]["ausencia_de_efeito"] = "Fixture: ausencia apos leitura completa"
        self.step(c, "CONCLUIR_NA_UNIDADE")

    def test_24_claimed_failure_is_not_proof(self):
        c = reopened(); c["tentativa"] = "SEM_EFEITO_COMPROVADO"
        self.step(c, "BLOQUEADO")

    def test_25_wrong_boolean_type(self):
        c = ready(); c["arquivo_conferido"] = "true"
        self.step(c, "BLOQUEADO")

    def test_26_preparation_no_institutional_access(self):
        c = ready(); c["modo"] = "PREPARACAO"
        self.step(c, "PREPARAR_SEM_OPERAR_SEI")

    def test_27_no_scaling_from_unit_tests(self):
        c = ready(); c["modo"] = "LOTE_QUALIFICADO"
        self.step(c, "BLOQUEADO")

    def test_28_unknown_state_and_malformed_input(self):
        for c in ([], {}, dict(ready(), tentativa="SALVO")):
            with self.subTest(c=c):
                self.step(c, "BLOQUEADO")

    def test_29_every_required_evidence_matters(self):
        for key in ready()["evidencias"]:
            c = ready(); del c["evidencias"][key]
            with self.subTest(key=key):
                self.step(c, "BLOQUEADO")

    def test_30_timeout_resolved_by_readback_no_resubmit(self):
        c = included(reopened()); c["tentativa"] = "INCERTA"
        self.step(c, "CONCLUIR_NA_UNIDADE")

    def test_31_failed_close_never_reinserts(self):
        c = included(reopened()); c["estado_atual_mesa"] = "DESCONHECIDO"
        self.step(c, "BLOQUEADO")

    def test_32_identity_format_and_hash(self):
        for key, value in (("nup", "12345678"), ("arquivo_sha256", "invalid"), ("unidade", "")):
            c = ready(); c[key] = value
            with self.subTest(key=key):
                self.step(c, "BLOQUEADO")


if __name__ == "__main__":
    unittest.main(verbosity=2)
