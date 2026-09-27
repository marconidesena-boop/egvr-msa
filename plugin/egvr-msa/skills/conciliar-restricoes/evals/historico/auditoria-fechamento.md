# Fechamento da auditoria documental — EGVR MSA 0.1.0

Data: 25/09/2026. Esta revisão complementa `work/auditoria-independente.md` e registra leitura dos arquivos corrigidos, da matriz, dos cinco exemplos e do catálogo de avaliações. Não abrange os resultados finais ainda em montagem, operações de planilha, instalação ou qualquer sistema institucional.

## Avaliação cega anterior à leitura do catálogo

As dez entradas de `work/entradas-adversariais.json` foram respondidas exclusivamente com a Skill e suas referências. As respostas foram concluídas, salvas e verificadas como JSON em `work/respostas-adversariais.json` **antes** da primeira leitura de `evals/casos.json`, `casos-de-regressao.md`, `casos-adversariais.md` ou seus resultados esperados nesta rodada.

O arquivo contém AD01–AD10, cada um com decisão, proposta, preservações, pendências e regras, e declara natureza **SIMULACAO_TEXTUAL**. O revisor não atribuiu aprovação/reprovação a essas próprias respostas. O exercício não produziu PDF real, edição de planilha, inspeção de propriedades, readback, acesso institucional ou maturidade operacional. A avaliação e o julgamento das respostas cabem ao avaliador responsável pelo histórico.

Depois do salvamento das respostas, iniciou-se a revisão documental abaixo. Não houve alteração retroativa das respostas depois de conhecer o catálogo.

## Fechamento dos quatro achados iniciais

| Achado | Leitura de confirmação | Estado |
| --- | --- | --- |
| A01 — Exemplo de dois campos com novas linhas | O README agora limita o exemplo a STATUS/OBSERVAÇÕES de linhas existentes, sem acrescentar linhas. R12 esclarece que permissão de linha não autoriza campos identificadores fora do escopo, nem usar observações como contorno. AD11 contrapõe esse bloqueio a uma variante positiva com campos de identidade autorizados. | Fechado |
| A02 — Contagens de eventos diferentes agrupadas | O modelo de relatório separa linhas, restrições novas, status, processos, tribunais e Varas. Cada medida pode ser contada e sustentada por evidência própria. | Fechado |
| A03 — Sessão expirada genericamente incerta | SEI futuro distingue falha de acesso anterior à tentativa de interrupção posterior a possível escrita. A segunda exige reconciliação antes de repetição. A capacidade continua não operacional. | Fechado |
| A04 — Negação ampla de código | O README delimita o único código incluído à validação estrutural, sem integração operacional nem reutilização de pacote anterior. | Fechado |

## Achados desta rodada

### A05 — Data da consulta transformada em momento de constatação no gabarito

Severidade: Média, restrita a dois resultados esperados do catálogo. T10 e T15 forneciam data da consulta, mas seus resultados exigiam constatação em 10/09/2026 sem informar quando ocorreu a análise. Isso contrariava a separação temporal de R10/R14 e poderia punir uma resposta conservadora correta.

O agente principal corrigiu os dois resultados esperados em JSON e Markdown. A leitura posterior confirmou que agora a redação registra a consulta de 10/09/2026, mantém a data efetiva ausente e declara que o momento da constatação pela análise não foi fornecido. As entradas anteriores do teste não precisaram ser alteradas.

**Estado: Fechado.** T11 usa menção genérica a data de constatação, sem impor data numérica; foi sugerida harmonização de redação para reforçar que o momento ausente não deve ser inventado. Essa sugestão não equivale ao erro numérico que existia em T10/T15.

### A06 — Instrução de reprodução do validador não corresponde ao caminho e à CLI

Severidade: Baixa, documentação técnica de reprodução. O texto de `EMPACOTAMENTO.md` indicava `evals/validar_pacote.py` a partir da raiz e orientava fornecer caminho do schema/validadores. O arquivo está em `skills/conciliar-restricoes/evals/validar_pacote.py`; a CLI lida aceita raiz posicional e `--out`, carregando o schema embarcado, sem argumentos para os outros caminhos.

Correção proposta ao agente principal: Indicar o caminho efetivo e um comando compatível com a CLI; distinguir a execução de outros validadores oficiais como verificações externas próprias.

**Estado na leitura desta versão do relatório: Pendente de confirmação da atualização prometida pelo agente principal.** Não afeta a coerência das decisões materiais da Skill. Se corrigido, registrar leitura de fechamento abaixo, sem apagar este histórico.

## Matriz e rastreabilidade

A matriz possui destino para as 25 seções, separa R15A–D e declara que vinculação documental não significa teste executado. O SEI da abertura/seção 1 está encaminhado à especificação futura subordinada ao limite da seção 19; o conflito de nome está explicitado nas decisões. O aprendizado persistente não foi tratado como já implementado.

Foram conferidos os **697 parágrafos não vazios** da extração contra as 697 entradas do índice granular, recomputando SHA-256 do texto UTF-8 de cada parágrafo na mesma ordem. Não houve divergência. Isso comprova correspondência do índice à extração; **não comprova tradução material de cada requisito em comportamento**. A correspondência semântica foi examinada mediante o confronto por cenários da primeira auditoria e a leitura dos casos desta rodada.

As ligações a regras e testes são adequadas como localização, mas diversos IDs são relações indiretas. Exemplos: T48 ajuda a controlar alegações de capacidade, sem provar por si só toda a política de aprendizado; T40 testa reexecução da conciliação, não atualização persistente do plugin. A matriz e R20 declaram esse limite, sem afirmar cobertura comportamental exaustiva da evolução do plugin.

## Catálogo de avaliações

Foram lidos integralmente os dados, estados iniciais, escopos, resultados esperados, ações permitidas/proibidas e critérios dos **48 testes obrigatórios**, na ordem da seção 21. As contagens conferidas são **31 casos de comportamento e 17 de ferramenta**, além de **11 adversariais** e **5 futuros SEI**. Essas contagens descrevem o catálogo, não execuções aprovadas.

A revisão encontrou os seguintes caminhos materiais coerentes:

- T03/T07/T08/T10/T11/T18/T22/T27 oferecem resultados positivos confirmados, sem tornar a Skill um mecanismo que só bloqueia.
- T01/T02 e AD01 separam diferença de sequência, diferença de representação e diferença real de dígitos. Não há gabarito que una, exclua ou crie restrição apenas por chave simplificada.
- T12–T15 distinguem falta de documento, consulta incompleta, identidade divergente e ausência qualificada. A05 corrigiu o limite temporal.
- T17/T19 e T33 exigem preservação dos atos humanos e impedem transferência de histórico para a linha nova.
- T28–T40 especificam valores, cores, propriedades, concorrência, inserção, falhas e readback. Exigem execução real de ferramenta para aprovação nesse nível; uma resposta textual não satisfaz o critério operacional.
- T41–T44 confrontam hipótese, agente anterior, segunda passagem e instrução embutida. R21 exige que o cenário de T43 forneça fontes distintas, sem entregar ao agente uma ordem de mudar a conclusão.
- T45/T46 distinguem bloqueio localizado e sistêmico; T47 veda escrita no pedido de auditoria; T48 e AD09 preservam o limite de maturidade.
- AD11 testa tanto o bloqueio por escopo insuficiente quanto a inserção proposta com identificação autorizada, compatível com a correção de R12.
- SF01–SF05 permanecem testes futuros separados, sem autorizar acesso ao SEI para aparentar execução.

R21 distingue estrutura, comportamento e ferramenta; usa resultados observados separados do catálogo; exige todas as variantes aplicáveis; não compensa violação material pela média de acertos. O script de validação lido também apresenta seus limites: caminhos e IDs não atestam qualidade da decisão nem preservação de planilha.

As fixtures textuais descrevem fatos sintéticos suficientes para seus objetivos, mas não substituem a preparação de artefatos em T03/T19/T22/T24/T28–T40 nem fontes originais representadas adequadamente nas simulações de percepção e revisão. Isso está explicitado nos critérios e nas convenções. Não se deve apresentar a simples leitura deste catálogo como execução desses cenários.

## Exemplos e ausência de exceções implícitas

Os cinco exemplos solicitados estão presentes e foram lidos. A hipótese confirmada mantém a auditoria sem escrita; a rejeitada mantém correspondência inconclusiva sem união; a conclusão revertida volta à representação visual e retira baixa indevida; o falso positivo preserva literais e distingue identidade de normalização; o exemplo de maturidade não promove edição a validada. Todos são declarados sintéticos e ilustrativos, sem relatório de execução inexistente.

## Caminhos e limites finais

Na repetição da conferência de links locais, matriz e evals agora resolvem corretamente. Restavam somente INVENTARIO.md e RESULTADOS-TESTES.md, informados como ainda em montagem. Não são considerados falha deste recorte; devem existir e ser conferidos antes de encerrar a entrega. A06 é a única instrução de caminho/reprodução ainda pendente de leitura de correção no momento deste registro.

Não houve alteração dos arquivos do pacote por este revisor. As respostas cegas e os dois relatórios foram os únicos resultados desta rodada. Não houve consulta jurídica material, edição de planilha, instalação, publicação ou operação institucional.

## Conclusão

**APROVAR A BASE DOCUMENTAL**, no recorte de regras, exemplos, matriz e critérios avaliados, com o ajuste de reprodução A06 pendente de confirmação e fechamento dos resultados/inventário fora do escopo desta rodada. A01–A05 estão fechados por leitura efetiva. Nenhuma contradição material remanescente foi identificada nesse recorte.

A recomendação decorre da coerência dos caminhos permitidos, bloqueios proporcionais e controles de evidência; não de existência de arquivos, contagem de regras ou aprovação operacional. Continua indispensável separar a avaliação das respostas textuais, os testes de ferramenta não realizados e futura validação representativa autorizada.

### Leitura posterior de A06

Após a redação acima, foi relido EMPACOTAMENTO.md. O link agora aponta ao arquivo existente e o comando `python skills/conciliar-restricoes/evals/validar_pacote.py . --out resultado-estrutural.json` corresponde à CLI inspecionada. O texto distingue validadores adicionais do script embarcado e informa que schema não é argumento. **A06 fechado quanto à reprodução.** Foi comunicada apenas correção residual de notação na frase explicativa do schema: usar `schemas/plugin.schema.json` relativo ao diretório de avaliação ou o caminho completo relativo à raiz; o comando demonstrado já carrega corretamente o schema e não depende dessa notação.

Com esse fechamento, o parecer documental do recorte é **APROVAR A BASE**, sem pendência material remanescente da auditoria. Resultados e inventário continuam fora do recorte e devem ser encerrados pelo agente principal antes da entrega completa.

## Fechamento complementar pelo agente principal

A notação residual do schema em EMPACOTAMENTO foi corrigida para schemas/plugin.schema.json relativa ao diretório de avaliação. T11 também foi harmonizado para referência da consulta sem inventar data de constatação. Estes ajustes foram lidos e conferidos antes do empacotamento.
