# EGVR MSA — perfis de consulta, status e novidade

Referência principal das seções 10, 11 e 12. Estes perfis são regras documentais do fluxo especificado, não afirmações universais sobre toda consulta que um órgão possa emitir. Aplicar primeiro [Identidade e evidência](identidade-e-evidencia.md). Um perfil descrito ainda depende da qualificação prevista em [Estados de maturidade](estados-de-maturidade.md).

## R10 — Interpretar atividade e baixa segundo a origem e a cobertura

**Finalidade.** Determinar a situação de uma restrição corretamente identificada, sem transferir comportamento entre documentos ou confundir falta de fonte com ausência qualificada.

**Condições de aplicação.** Origem conhecida, veículo e restrição vinculados, referência temporal pertinente e leitura suficiente para a conclusão. Registrar qual perfil e qual variante documental foram utilizados. Para origens ainda não caracterizadas, permanecer em análise ou proposta até estabelecer campos, limitações e testes.

**Evidência necessária.**

| Perfil | Evidência que sustenta a decisão | Resultado documental |
| --- | --- | --- |
| DETRAN-BA | Data válida no campo `DATA BAIXA` da restrição correspondente | Restrição baixada |
| DETRAN-BA | Literal `N/D` no campo `DATA BAIXA` da restrição correspondente | Restrição ativa |
| Outros DETRANs | Documento do tipo que mostra as restrições atuais e deixa de exibir as baixadas; restrição anterior ausente após todas as verificações de cobertura | Baixa constatada por ausência qualificada |
| SERPRO | Mesmas verificações de ausência qualificada, demonstradas para o documento concreto | Baixa constatada por ausência qualificada |

Para ausência qualificada, demonstrar cumulativamente: veículo correto; origem identificada; consulta pertinente à data de referência; cobertura da seção judicial; inexistência de filtro, corte ou página faltante que prejudique a conclusão; leitura suficiente para localizar variações de apresentação; e ausência de erro ou resultado incompleto. A origem, sozinha, não prova que o documento contenha apenas restrições atuais.

**Ação permitida.**

- No DETRAN-BA, aplicar a interpretação apenas ao campo `DATA BAIXA` da linha identificada. Conferir no original qualquer leitura decisiva ambígua.
- Considerar informação explícita presente no documento antes de cogitar ausência. Uma restrição encontrada com apresentação diferente não é ausente.
- Na comparação, procurar abreviações, grafias, pontuação e outras formas de apresentação segundo [R13](identificadores-e-historicos.md#r13--identificadores-processos-e-normalização-judicial). O mesmo número de processo pode ajudar a demonstrar variação de nome, mas não resolve sozinho toda identidade definida por R04.
- Reconhecer baixa por ausência qualificada sem exigir uma data explícita de baixa inexistente no tipo de consulta.
- Encaminhar a baixa confirmada para a transição de status de R11. Se observações estiverem autorizadas, registrar texto que contenha a frase **“Restrição não informada no PDF consultado”**, a referência da consulta e a data comprovada de constatação, sem inventar a data efetiva da baixa.

Forma de observação permitida, somente com os dados correspondentes comprovados: `Restrição não informada no PDF consultado. Baixa constatada em [data da constatação] na consulta de [data da consulta]; data efetiva da baixa não informada.` Se as datas forem diferentes, mantê-las distintas. Se uma data não estiver disponível, não preencher o marcador com uma suposição: registrar a lacuna no controle externo e adaptar o texto aos fatos existentes. Marcadores de exemplo nunca são dados a gravar literalmente. A inclusão e preservação de observações seguem [R14](identificadores-e-historicos.md#r14--históricos-humanos-observações-e-datas).

**Ação proibida.**

- Usar `N/D` ou data de outra coluna ou linha como prova da situação da restrição analisada.
- Equiparar campo vazio, ilegível, incerto ou data ambígua a `N/D` ou a baixa.
- Aplicar ausência qualificada a qualquer DETRAN indiscriminadamente ou presumir que todo arquivo SERPRO tenha cobertura suficiente.
- Concluir baixa a partir de documento faltante, vazio, ilegível, corrompido, parcial, de outro veículo, página de erro, sessão expirada ou captura sem resultado pertinente.
- Ignorar informação explícita encontrada para aplicar mecanicamente a ausência.
- Usar data da consulta, da leitura ou da alteração da planilha como data efetiva de baixa.
- Descrever a conclusão documental como baixa executada no sistema de origem.

**Tratamento da lacuna.** Manter a situação material sem alteração, registrar a condição faltante e aplicar R17 quando necessário. Não exigir metadado que seja irrelevante à ação comprovada, mas não declarar ausência qualificada se faltar elemento essencial da cobertura. Se somente o campo de observações estiver fora do escopo, registrar a justificativa externamente; a autorização do status não autoriza escrita naquela coluna.

**Testes correspondentes.** [T02, T07, T08, T09, T10, T11, T12, T13, T14, T15 e T16](../evals/casos-de-regressao.md). T10 e T11 devem ser controles positivos de baixa por ausência qualificada; T15 deve distinguir constatação de data efetiva; T02 deve incluir procura por apresentação equivalente antes de concluir ausência.

## R11 — Status material individual e preservação do tratamento humano

**Finalidade.** Aplicar as transições definidas sem inventar vocabulário, transferir status entre restrições ou destruir histórico.

**Condições de aplicação.** Status dentro do escopo autorizado, restrição individual identificada e conclusão classificada segundo [Critérios de confiança](criterios-de-confianca.md). A evidência deve ser específica para o status daquela linha.

**Evidência necessária.** Situação documental conforme R10, valor anterior, lista de validação da célula e eventual tratamento humano comprovado da própria restrição. Exemplos de status compatíveis, quando já existentes e aplicáveis: `NOTIFICADO - AGUARDANDO PRAZO`, `RESOLVENDO PENDÊNCIA` e `AGUARDANDO RESPOSTA`.

**Ação permitida.** Aplicar exatamente a tabela:

| Situação comprovada | Tratamento |
| --- | --- |
| Restrição daquela linha baixada | Alterar para `SEM RESTRIÇÃO` |
| Restrição ativa comprovadamente nova | Usar `NOVA RESTRIÇÃO (NOTIFICAR)` |
| Restrição ativa indevidamente marcada `SEM RESTRIÇÃO` | Corrigir para `NOVA RESTRIÇÃO (NOTIFICAR)`, salvo tratamento humano compatível e comprovado da própria restrição |
| Restrição ativa com status humano compatível | Preservar o status humano |
| Status humano intermediário e baixa comprovada | Alterar para `SEM RESTRIÇÃO`, preservando os atos históricos conforme R14 |
| Planilha existente com linha-base já destinada ao veículo e consulta completa que comprova ausência de qualquer restrição judicial ativa | Preservar a linha-base e, se O/P estiverem autorizadas, usar observação `Sem restrição judicial ativa.` e status `SEM RESTRIÇÃO`, sem apagar identificadores ou históricos preexistentes |
| Resultado provável, inconclusivo ou contraditório | Preservar o status e relatar a pendência |

**Ação proibida.**

- Inventar status ou forçar situação sem regra suficiente em uma categoria apenas parecida.
- Alterar silenciosamente a lista de seleção ou a validação quando ela não admitir o valor exigido.
- Converter `falha de leitura`, `resultado incerto` ou outra condição técnica em status material de uma restrição.
- Criar linha fictícia para representar um veículo sem registros judiciais no modo de criação quando o modelo não previr linha-base ou campo próprio. Essa proibição não impede atualizar O/P de uma linha-base que já exista na planilha autorizada, nos termos da tabela.
- Tratar ausência comprovada de restrição judicial ativa na linha-base como autorização para apagar processo, tribunal, Vara, histórico ou outras linhas do veículo.

**Tratamento da lacuna.** Preservar o alvo e registrar o status não contemplado, a validação incompatível ou o tratamento humano cuja aplicação não pôde ser provada. A confirmação exigida para correção é suficiência documental e revisão crítica; a regra não cria pedido de aprovação por célula depois de um lote já autorizado.

**Testes correspondentes.** [T03, T04, T07, T08, T10, T11, T17, T18, T19 e T20](../evals/casos-de-regressao.md). T18 só passa com identidade, atividade e transição confirmadas; T19 deve preservar o histórico, ainda que o status mude.

## R12 — Determinar novidade sem duplicação e tratar o histórico solicitado

**Finalidade.** Separar restrição realmente nova de registro existente com apresentação diferente, e separar situação atual de reconstrução histórica.

**Condições de aplicação.** Conciliação com planilha existente ou criação a partir de origem e modelo. Registrar se a finalidade autorizada é situação atual ou histórico completo e verificar se inclusão de linhas foi autorizada.

**Evidência necessária.** Para declarar nova, demonstrar cumulativamente: natureza judicial; vínculo com o veículo correto; atividade conforme R10; inexistência de correspondência em todos os registros pertinentes dentro da área de leitura autorizada; diferença material além de abreviação, pontuação, espaço, acento ou apresentação; e sobrevivência da conclusão à revisão crítica.

**Ação permitida.**

- Examinar todos os registros pertinentes disponíveis dentro do escopo de leitura, não apenas a primeira linha do veículo.
- Inserir uma nova restrição confirmada no bloco correto, quando autorizado, preenchendo somente dados comprovados. Status, autoria, estrutura e histórico seguem, respectivamente, R11, [R07 e R08](modos-preservacao-e-escrita.md) e R14.
- Antes de propor a inserção como executável, confirmar que os campos autorizados permitem preencher a identificação mínima da restrição nas colunas próprias do modelo. Permissão para acrescentar linhas, isoladamente, não autoriza identificadores fora do escopo. Se somente status e observações estiverem autorizados, não criar linha sem identificação e não usar observações para contornar campos identificadores não autorizados; registrar a proposta externamente e a ampliação de escopo necessária.
- Atualizar restrição existente somente nos campos autorizados cuja mudança esteja comprovada.
- Em tarefa de situação atual ou identificação de mudanças novas, preservar baixadas já existentes na planilha sem importar baixadas antigas nunca representadas.
- Em criação expressamente destinada a histórico completo, registrar também restrições baixadas ausentes e comprovadas, com situação e datas sustentadas pelas fontes.
- Em planilha existente, se o veículo já tiver uma linha-base e a ausência de qualquer restrição judicial ativa estiver confirmada por consulta completa, preservar essa linha e aplicar O/P conforme R11/R14 quando autorizadas. Não criar outra linha só para repetir a ausência.

**Ação proibida.**

- Declarar uma restrição nova quando falta autorização ou acesso suficiente para verificar sua representação anterior.
- Importar restrição administrativa como judicial, inclusive em PDF que contenha ambas.
- Converter diferença visual em novidade material ou substituir histórico anterior pela nova linha.
- Tratar autorização genérica de atualização como autorização para importar todo histórico de baixadas ausentes.

**Tratamento da lacuna.** Registrar candidato à nova restrição sem inseri-lo enquanto faltar confirmação de novidade, natureza, identidade, atividade ou autorização de linha. Se houver dúvida apenas em um campo independente, manter esse campo pendente e avaliar os demais pelos critérios de confiança, sem inventar informação para completar a linha.

**Testes correspondentes.** [T01, T02, T03, T05, T06, T21, T22, T33 e T40](../evals/casos-de-regressao.md). T03 e T22 demonstram capacidade positiva de incluir casos seguros dentro de finalidades diferentes; T21 impede a expansão silenciosa de situação atual para histórico completo.
