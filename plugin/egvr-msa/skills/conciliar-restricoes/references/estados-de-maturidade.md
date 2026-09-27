# Estados de maturidade — EGVR MSA

Esta é a referência principal de R22. A maturidade é registrada separadamente por capacidade, perfil de documento, operação e ferramenta quando essas diferenças alterarem o resultado. O manifesto e a estrutura da Skill não demonstram funcionamento operacional.

## R22 — Maturidade demonstrada por evidência

| Dimensão | Regra |
| --- | --- |
| Assunto e finalidade | Descrever honestamente o que foi especificado, construído, exercitado e conferido, impedindo promessas derivadas apenas da existência de arquivos. |
| Condições de aplicação | Construção do pacote, entrega, alteração de versão, qualificação de perfis, seleção de ferramenta, proposta de uso autônomo e relato de testes. |
| Evidência necessária | Capacidade e versão identificadas; perfil, operação, ferramenta e ambiente; testes aplicáveis; entradas; resultados esperados e observados; evidência de execução; limitações; conferência anterior e posterior quando exigida pelo estado. |
| Ação permitida | Atribuir o estado correspondente à tabela abaixo e registrar separadamente o resultado dos testes. Descrever exatamente o alcance da avaliação. Qualificar perfis independentes sem estender seu resultado a outros perfis ou ferramentas. Aplicar o critério de liberação de R21 em [critérios de aprovação](../evals/criterios-de-aprovacao.md). |
| Ação proibida | Dizer que TESTADA significa aprovada; classificar a versão inteira como VALIDADA porque o manifesto passou; apresentar arquivos criados como edição de planilha validada; simular teste real por declaração; declarar aptidão operacional ou escala do SEI apenas por instruções ou testes do auxiliar local de R19. |
| Lacuna ou conflito | Registrar o teste como não executado ou bloqueado, conforme o que efetivamente ocorreu. Perfil sem qualificação suficiente permanece em análise, proposta de alterações ou teste controlado; não paralisar perfis independentes já qualificados. |
| Testes relacionados | T48 e o conjunto obrigatório aplicável ao perfil, conforme [R21](../evals/criterios-de-aprovacao.md). O resultado de uma inspeção estrutural não substitui T01–T48 de comportamento ou os testes reais da ferramenta. |

| Estado | Evidência mínima e limite |
| --- | --- |
| ESPECIFICADA | Procedimento descrito. Não afirma que exista implementação correspondente. |
| IMPLEMENTADA | Estrutura correspondente criada. Não presume funcionamento real. |
| TESTADA | Capacidade submetida a teste controlado, com resultado informado. Pode ter sido aprovada, reprovada ou parcialmente bloqueada. |
| VALIDADA | Resultado conferido antes e depois em casos reais representativos e autorizados, com delimitação do perfil e da operação. |
| APTA PARA ESCALA | Regressões, tratamento de falhas e auditoria suficientes para o perfil declarado, além das evidências de validação. |

A liberação para uso autônomo em produção depende da aprovação integral dos testes obrigatórios aplicáveis ao perfil, de autorização e de ferramentas adequadas. Uma análise documental favorável do pacote não concede essa liberação.

O inventário de capacidades deve usar as colunas: capacidade, perfil, operação, ferramenta/ambiente, versão, maturidade, testes e resultados, evidência, limitações e próximo requisito. Registros efetivos de execução ficam nos artefatos de avaliação; este arquivo define os critérios, sem antecipar resultados.
