# Inventário local — EGVR MSA 0.1.1

Inventário da fonte local autorizada e instalada para revisão e testes controlados. São **61 arquivos**. A contagem inclui este inventário, os dois manifestos e o ativo visual. Arquivos históricos da versão 0.1.0 foram preservados como evidência; não representam a versão ativa.

## Raiz e metadados — 13 arquivos

- `.codex-plugin/plugin.json`
- `assets/distintivo.png`
- `CAPACIDADES.md`
- `CHANGELOG.md`
- `COBERTURA-GRANULAR.json`
- `EMPACOTAMENTO.md`
- `INVENTARIO.md`
- `LIMITACOES-E-DECISOES.md`
- `MATRIZ-RASTREABILIDADE.md`
- `plugin.json`
- `PROVENIENCIA.json`
- `README.md`
- `RESULTADOS-TESTES.md`

## Entrada da skill — 1 arquivo

- `skills/conciliar-restricoes/SKILL.md`

## Catálogo, critérios e validadores — 7 arquivos

- `skills/conciliar-restricoes/evals/casos-adversariais.md`
- `skills/conciliar-restricoes/evals/casos-de-regressao.md`
- `skills/conciliar-restricoes/evals/casos.json`
- `skills/conciliar-restricoes/evals/criterios-de-aprovacao.md`
- `skills/conciliar-restricoes/evals/estado-dos-testes.json`
- `skills/conciliar-restricoes/evals/schemas/plugin.schema.json`
- `skills/conciliar-restricoes/evals/validar_pacote.py`

## Histórico de testes e auditorias — 19 arquivos

- `skills/conciliar-restricoes/evals/historico/auditoria-fechamento.md`
- `skills/conciliar-restricoes/evals/historico/auditoria-independente.md`
- `skills/conciliar-restricoes/evals/historico/avaliacao-adversariais.json`
- `skills/conciliar-restricoes/evals/historico/avaliacao-catalogo.json`
- `skills/conciliar-restricoes/evals/historico/avaliacao-primeira-rodada.json`
- `skills/conciliar-restricoes/evals/historico/avaliacao-reteste.json`
- `skills/conciliar-restricoes/evals/historico/avaliacao-v0.1.1.json`
- `skills/conciliar-restricoes/evals/historico/cenarios-comportamento.json`
- `skills/conciliar-restricoes/evals/historico/entradas-adversariais.json`
- `skills/conciliar-restricoes/evals/historico/entradas-catalogo.json`
- `skills/conciliar-restricoes/evals/historico/estrutural-final.json`
- `skills/conciliar-restricoes/evals/historico/estrutural-primeira.json`
- `skills/conciliar-restricoes/evals/historico/respostas-adversariais.json`
- `skills/conciliar-restricoes/evals/historico/respostas-catalogo.json`
- `skills/conciliar-restricoes/evals/historico/respostas-comportamento.json`
- `skills/conciliar-restricoes/evals/historico/respostas-reteste.json`
- `skills/conciliar-restricoes/evals/historico/respostas-v0.1.1.json`
- `skills/conciliar-restricoes/evals/historico/snapshot-final-instrucoes.json`
- `skills/conciliar-restricoes/evals/historico/validadores-locais.json`

## Exemplos — 5 arquivos

- `skills/conciliar-restricoes/examples/capacidade-implementada-mas-nao-validada.md`
- `skills/conciliar-restricoes/examples/conclusao-revertida-na-segunda-passagem.md`
- `skills/conciliar-restricoes/examples/falso-positivo-evitado.md`
- `skills/conciliar-restricoes/examples/hipotese-do-usuario-confirmada.md`
- `skills/conciliar-restricoes/examples/hipotese-do-usuario-rejeitada.md`

## Referências — 11 arquivos

- `skills/conciliar-restricoes/references/criterios-de-confianca.md`
- `skills/conciliar-restricoes/references/escopo-e-evolucao.md`
- `skills/conciliar-restricoes/references/estados-de-maturidade.md`
- `skills/conciliar-restricoes/references/hierarquia-das-fontes.md`
- `skills/conciliar-restricoes/references/identidade-e-evidencia.md`
- `skills/conciliar-restricoes/references/identificadores-e-historicos.md`
- `skills/conciliar-restricoes/references/modos-preservacao-e-escrita.md`
- `skills/conciliar-restricoes/references/perfis-e-status.md`
- `skills/conciliar-restricoes/references/politica-de-analise-critica.md`
- `skills/conciliar-restricoes/references/protocolo-de-discordancia.md`
- `skills/conciliar-restricoes/references/sei-futuro.md`

## Modelos de controle e relato — 5 arquivos

- `skills/conciliar-restricoes/templates/alteracoes.csv`
- `skills/conciliar-restricoes/templates/controle-execucao.json`
- `skills/conciliar-restricoes/templates/correcao-validada.md`
- `skills/conciliar-restricoes/templates/pendencias.csv`
- `skills/conciliar-restricoes/templates/relatorio.md`

## Estado da versão

- As regras novas de 0.1.1 estão cobertas por T49–T55 e por seus dois arquivos de resposta e avaliação.
- As três validações locais estão registradas em `validadores-locais.json`.
- A instalação local não equivale a homologação de produção.
- Os 17 testes de edição em ferramenta e os 5 cenários institucionais futuros permanecem não executados.
