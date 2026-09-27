# Critérios de confiança — EGVR MSA

Esta é a referência principal de R15C. Confiança é atribuída a cada decisão, incluindo seu campo, alvo e ação. Ela não é uma nota geral do veículo, do arquivo ou do lote.

## R15C — Suficiência por decisão

| Dimensão | Regra |
| --- | --- |
| Assunto e finalidade | Impedir que uma conclusão segura em um assunto justifique alterações não comprovadas em outros campos. |
| Condições de aplicação | Toda conclusão material, proposta de alteração e reavaliação decorrente da segunda passagem. |
| Evidência necessária | Elementos essenciais para a ação específica; identidade e correspondência pertinentes; fonte competente; resultado da revisão crítica; contradições e lacunas registradas. |
| Ação permitida | Classificar a decisão pela tabela abaixo. Permitir alteração autônoma apenas em decisão CONFIRMADA, desde que os controles independentes de autorização, capacidade, preservação, maturidade e execução também estejam satisfeitos. Continuar decisões independentes já comprovadas. |
| Ação proibida | Elevar confiança para terminar o lote; usar confiança global no veículo; converter PROVÁVEL ou INCONCLUSIVO em status material; tomar CONFIRMADO como autorização de escrita ou como prova de que a ferramenta salvou corretamente. |
| Lacuna ou conflito | Identificar o elemento faltante e o conjunto de decisões que depende dele. Dúvida sobre identidade bloqueia os alvos dependentes; dúvida localizada sobre expansão de uma Vara pode deixar outro campo independente apto à análise ou à alteração autorizada. Comunicar conforme R15D. |
| Testes relacionados | T03, T07, T08, T12, T13, T14, T26, T27, T43, T45 e T46 em [casos de regressão](../evals/casos-de-regressao.md). |

| Classificação | Significado | Consequência |
| --- | --- | --- |
| CONFIRMADO | Evidência suficiente para a ação específica, sem contradição relevante. | Pode seguir aos demais controles; não implica escrita automática. |
| PROVÁVEL | Indicação forte, mas falta elemento essencial. | Preservar o alvo e apresentar proposta ou pendência. |
| INCONCLUSIVO | Insuficiência, ilegibilidade, ambiguidade ou contradição não resolvida. | Preservar o alvo e indicar o que falta para decidir. |

Confiança material, estado técnico da tentativa de escrita e maturidade da capacidade são dimensões diferentes. Os estados de execução pertencem a [R16](modos-preservacao-e-escrita.md); a qualificação da capacidade pertence a [R22](estados-de-maturidade.md).
