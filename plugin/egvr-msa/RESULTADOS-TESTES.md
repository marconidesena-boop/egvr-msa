# Resultados de verificação do EGVR MSA 0.1.1

Parecer: **APROVAR A BASE**, restrito à candidata documental e ao uso em análise, propostas e testes controlados. A base não está homologada para edição autônoma em produção.

## Resultados e limites

| Conjunto | Resultado | Alcance |
|---|---|---|
| Manifesto portátil e verificações estruturais E01–E08 | Consultar o registro estrutural final abaixo | Schema, identidade, referências, regras, catálogo, componentes e rastreabilidade |
| Validadores locais de Plugin Creator e Skill Creator | Aprovados nas duas verificações | Manifesto de compatibilidade e estrutura/frontmatter da skill |
| Casos T de comportamento | 31 de 31 aprovados em simulação textual | Propostas, preservações e pendências sobre entradas sintéticas |
| Regressões T49–T55 da correção 0.1.1 | 7 de 7 aprovadas em simulação textual | Linha-base existente, frases canônicas, datas, documento insuficiente e reexecução |
| Casos adversariais AD01–AD10 | 10 de 10 aprovados em simulação textual | Zeros, vínculo, escopo, fontes, melhoria e quarentena |
| AD11, variantes restrita e completa | 2 de 2 respostas aprovadas no reteste | Escopo dos identificadores e caminho positivo de nova linha |
| Exploração B01–B16 anterior ao ajuste de R12 | 15 aprovados e 1 reprovado | A falha B02 foi preservada no histórico, corrigida e retestada |
| Casos T de ferramenta | 17 não executados | Exigem seleção de ferramenta e execução mensurada em arquivos de teste |
| SEI SF01–SF05 | 5 não executados | São especificações futuras; nenhuma operação institucional realizada |

Os 55 casos T dividem-se em 38 de comportamento e 17 de ferramenta. Os 11 casos AD incluem a regressão AD11 acrescentada durante a construção. Há 49 resultados comportamentais aprovados no total: 38 casos T e 11 casos AD. Esses totais não somam cenários exploratórios B nem significam validação real. O [estado consolidado](skills/conciliar-restricoes/evals/estado-dos-testes.json) aponta para a evidência de cada caso.

## Falha encontrada e correção

B02 tinha novidade comprovada, permissão para linha nova e autorização somente para status/observações. A resposta inicial propôs inserir a linha e acomodar identificação na observação. Isso violava a separação dos campos e poderia criar registro incompleto. R12 e a condição essencial da skill passaram a explicitar que identificadores devem estar autorizados em suas colunas próprias. B02-R2 bloqueou corretamente a proposta executável; B17, com autorização completa, propôs a linha individual, o status exato, os cinco valores em vermelho e histórico humano vazio. O primeiro resultado reprovado não foi apagado.

A revisão documental corrigiu ainda exemplo de autorização, contagens agrupadas no relatório, descrição de código, tratamento de sessão expirada e instrução de reprodução da validação. Os gabaritos T10/T15 foram alinhados às datas efetivamente fornecidas, e T11 harmonizado: data da consulta não preenche momento da constatação nem data efetiva de baixa. As entradas entregues ao avaliador permaneceram iguais.

## Evidências conservadas

- [Primeira rodada e falha B02](skills/conciliar-restricoes/evals/historico/avaliacao-primeira-rodada.json).
- [Reteste B02-R2 e controle positivo B17](skills/conciliar-restricoes/evals/historico/avaliacao-reteste.json).
- [Avaliação das 31 respostas T](skills/conciliar-restricoes/evals/historico/avaliacao-catalogo.json).
- [Avaliação dos dez adversariais iniciais](skills/conciliar-restricoes/evals/historico/avaliacao-adversariais.json).
- [Verificação estrutural final](skills/conciliar-restricoes/evals/historico/estrutural-final.json).
- [Verificações locais adicionais](skills/conciliar-restricoes/evals/historico/validadores-locais.json).
- [Auditoria documental inicial](skills/conciliar-restricoes/evals/historico/auditoria-independente.md).
- [Fechamento da auditoria](skills/conciliar-restricoes/evals/historico/auditoria-fechamento.md).
- [Respostas da correção 0.1.1](skills/conciliar-restricoes/evals/historico/respostas-v0.1.1.json).
- [Avaliação da correção 0.1.1](skills/conciliar-restricoes/evals/historico/avaliacao-v0.1.1.json).

As entradas e respostas integrais estão na mesma pasta de histórico. O catálogo conserva NAO_EXECUTADO como estado inicial, separado do histórico e do estado consolidado. A primeira verificação estrutural detectou dois links de arquivos de entrega ainda não gerados; seu registro também foi preservado. A rodada final é a referência para o pacote entregue.

## O que permanece sem comprovação operacional

Não foram abertos PDFs veiculares reais nem editadas planilhas para demonstrar fidelidade. A simulação da segunda passagem comprova resposta à contraprova textual fornecida; não comprova descoberta visual em um documento real. Cores, fórmulas, validações, proteções, concorrência e timeout foram raciocinados nas simulações, sem reproduzir eventos em um aplicativo. Os 17 testes de ferramenta permanecem pendentes até a escolha e disponibilidade de uma ferramenta para um piloto controlado. O pacote não inclui um editor operacional que pudesse ser validado isoladamente.

Não houve instalação, criação hospedada, publicação, acesso ao SEI ou alteração de dados institucionais. O parecer favorável à base não autoriza esses passos nem promove capacidades a VALIDADA ou APTA PARA ESCALA.
