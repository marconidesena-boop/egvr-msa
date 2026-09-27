# Critérios de aprovação — EGVR MSA 0.1.1

Este arquivo é a referência principal da avaliação. Os casos e exemplos exercitam as regras operacionais da [Skill](../SKILL.md); não são novas políticas de interpretação de consultas. Maturidade das capacidades segue [estados de maturidade](../references/estados-de-maturidade.md).

## R21 — Avaliação e liberação por perfil

**Finalidade:** Demonstrar, com evidência proporcional à capacidade, que o perfil toma decisões corretas, executa casos seguros quando autorizado e conserva os casos não comprovados. Impedir aprovação baseada apenas na existência de arquivos ou em palavras presentes no texto.

**Condições de aplicação:** Construção e atualização do pacote; alteração de regra, origem de consulta, ferramenta, modelo ou capacidade; decisão de liberar um perfil para uso autônomo. Identificar a versão, o perfil, a ferramenta e o conjunto aplicável antes de avaliar. SEI futuro nunca integra habilitação operacional da versão 0.1.0.

**Evidência necessária:** Para cada execução, registrar ID do caso, versão avaliada, entradas sintéticas efetivamente usadas, estado anterior, escopo do cenário, resultado esperado, resultado observado, evidência conservada, status e limitação ambiental. O histórico identifica avaliador, método e data reais. Não criar horários, logs, resultados ou verificações retroativamente.

**Ação permitida:** Executar simulações comportamentais com dados sintéticos; preparar e testar artefatos sintéticos com ferramenta autorizada; validar manifestos, referências e estrutura; registrar falhas; corrigir pacote dentro da tarefa autorizada e repetir regressões afetadas. Perfis independentes previamente qualificados não ficam paralisados por uma capacidade futura.

**Ação proibida:** Declarar aprovação sem executar o caso; inferir capacidade de edição da existência da Skill; considerar texto esperado como resultado observado; chamar teste estrutural de teste comportamental; considerar simulação textual prova de edição; omitir variantes que falharam; operar SEI para simular aprovação; declarar produção liberada por aprovação documental.

**Tratamento da lacuna:** Se não há execução, usar NAO_EXECUTADO. Se a execução é iniciada e um impedimento verificável inviabiliza a avaliação, usar BLOQUEADO e registrar evidência e limitação. Se o agente encontra uma condição de bloqueio esperada no cenário e reage corretamente, isso pode aprovar o comportamento daquele caso; não torna a operação bloqueada bem-sucedida. Perfis sem validação suficiente ficam em análise, proposta de alterações ou teste controlado.

**Testes correspondentes:** T01–T55, AD01–AD11 e SF01–SF05, com estes últimos isolados como futuros. T49–T55 protegem a correção 0.1.1 de linha-base e observações canônicas. T48 e AD09 verificam diretamente a fronteira entre estrutura criada e capacidade comprovada. O catálogo mantém status inicial NAO_EXECUTADO; histórico separado registra o que efetivamente foi executado.

### Três níveis de avaliação que não se substituem

| Nível | O que demonstra | Evidência mínima | O que não demonstra |
|---|---|---|---|
| Estrutural do pacote | Manifestos válidos, caminhos existentes, IDs/cobertura coerentes e conteúdo necessário | Saída real de validação, versão, arquivos e erros encontrados | Qualidade das decisões, edição segura, instalação ou produção |
| Comportamento da Skill | Resposta observada a entradas e estado inicial sintéticos, inclusive controles positivos e negativos | Prompt usado, referências da versão carregadas, resposta integral e avaliação das assertivas | Acesso a PDFs reais, preservação de Excel/Sheets, concorrência real, readback ou capacidade operacional |
| Ferramenta de edição | Efeito real e mensurado em artefatos sintéticos controlados | Arquivo antes/depois, operações, leituras posteriores, valores/cores/propriedades e controles | Validação em casos reais representativos, SEI futuro ou escala por si só |

Um teste de ferramenta pode também produzir evidência comportamental, mas cada conclusão deve registrar o alcance efetivamente comprovado. Uma inspeção parcial não autoriza afirmar preservação de todas as propriedades.

### Como executar uma simulação comportamental

1. Selecionar caso e variante antes de observar a resposta.
2. Entregar ao agente somente o cenário: dados de entrada, estado inicial, escopo e referências operacionais pertinentes da versão 0.1.0. Não entregar a ele o gabarito, as alterações esperadas ou o critério de aprovação.
3. Identificar os trechos de fonte como fixtures sintéticas; quando o caso exigir duas páginas ou fontes, disponibilizar os dois trechos como fontes distintas. Não afirmar que são PDFs reais já lidos.
4. Pedir conclusão, proposta limitada, confiança por decisão, evidência decisiva, resultado da segunda passagem quando aplicável, impedimentos e relatório sintético. Proibir escrita externa na avaliação textual.
5. Um avaliador compara a resposta observada com todas as assertivas. Preservar o texto integral e apontar a evidência para cada conclusão de aprovação ou reprovação.
6. Em T43, fornecer uma fonte original completa que permita localizar a contraprova; não tratar uma instrução do avaliador para mudar de opinião como revisão espontânea do agente.
7. Registrar limites: execução textual não verifica ferramentas, cores, fórmulas, proteção, arquivo, sessão institucional ou identidade real.

Subconjunto sugerido para uma primeira avaliação independente sem ferramentas de escrita: **T01, T02, T04, T07, T08, T10, T11, T12, T14, T17, T18, T27, T41, T43, T44, T45, T47, T48, T49, T50, T52, T54, T55, AD01 e AD05**. Esse conjunto inclui decisões positivas, negativas, fonte competente, fronteira de identidade, crítica, linha-base e preservação. Seu uso não dispensa os demais casos aplicáveis.

### Como executar teste de ferramenta

1. Preparar cópia sintética exclusiva de teste e identificar ferramenta, versão, permissões e recursos suportados.
2. Capturar os valores, tipos, cores e propriedades pertinentes antes da operação; incluir controles dentro e fora do escopo.
3. Aplicar o cenário autorizado sem sistema institucional. Para falhas e concorrência, usar um mecanismo controlado e documentado que reproduza efetivamente o evento.
4. Capturar a resposta da ferramenta e reler o destino real. Sucesso de salvamento não substitui leitura de confirmação.
5. Comparar todos os alvos e controles pertinentes, incluindo fórmulas, zeros iniciais, validação, proteção, formatação condicional, dimensões, comentários e referências afetadas na medida exigida pelo caso.
6. Não marcar preservação de propriedade cuja leitura não seja suportada pelo método. Registrar o impedimento e restringir a conclusão.
7. Conferir contagens e idempotência; conservar estado e evidência de resultados parciais/incertos.

### Estados do resultado e critérios de decisão

| Estado | Condição |
|---|---|
| APROVADO | Caso executado, todas as variantes e assertivas aplicáveis satisfeitas e evidência suficiente preservada |
| REPROVADO | Comportamento ou efeito observado viola ao menos uma assertiva; indicar a falha e seu alcance |
| BLOQUEADO | Avaliação iniciada, mas impedimento verificável impede concluir; não é aprovação nem resultado material da restrição |
| NAO_EXECUTADO | Caso apenas especificado ou não iniciado; resultado observado vazio e sem evidência de execução |

Não calcular média para compensar violação de autorização, identidade, histórico, fonte ou preservação. Um falso positivo material não é neutralizado por acertos em outros registros. Contagens devem vir dos registros efetivamente medidos, distinguindo casos, variantes, células, linhas e restrições.

### Aplicabilidade e liberação

- **Núcleo comum:** Autorização, identidade, granularidade, fontes, duas passagens, confiança, histórico, quarentena, relatório e maturidade são aplicáveis a qualquer perfil.
- **DETRAN-BA:** Incluir T07–T09 e todas as verificações de núcleo e status pertinentes; atividade e baixa dependem do campo correto.
- **Outros DETRANs:** Incluir T10, T12–T16 e o núcleo; ausência qualificada depende do funcionamento e da completude do documento em teste.
- **SERPRO:** Incluir T11–T16 e o núcleo; não presumir equivalência de sistemas.
- **Atualização:** Incluir T03/T19/T24/T28–T29/T33–T40 e demais casos aplicáveis ao lote e à ferramenta.
- **Criação:** Incluir T22/T30–T34 e demais casos de identidade, fontes, dados e revisão pertinentes; testar continuidade de modo e modelo estrito.
- **SEI:** SF01–SF05 preservam o catálogo histórico. A partir de 0.2.0, o módulo de inclusão tem [cenários SI](../../incluir-consulta-sei/evals/cenarios-piloto.md) e testes locais próprios. Um piloto delimitado deve ser expressamente solicitado; instruções e testes locais não liberam operação em escala.

A liberação de uso autônomo em produção exige aprovação integral dos testes obrigatórios aplicáveis ao perfil utilizado, autorização e ferramentas adequadas, além do nível de maturidade comprovado. Uma exceção de aplicabilidade precisa de justificativa objetiva; dificuldade ambiental não torna um teste dispensável. A base documental pode ser recomendada para revisão sem estar validada para produção.

### Registro de resultados

O [catálogo JSON](casos.json) é o conjunto inicial; o histórico de resultados executados deve conservar, por execução: caso/variante, versão do pacote, perfil, ferramenta/método, fixture, data real, estado anterior, entrada enviada, resposta observada, alterações reais, readback, evidência, status, limites e avaliador. Uma repetição conserva o resultado anterior e acrescenta novo registro.

Correções de pacote exigem reexecutar casos afetados e casos vizinhos capazes de revelar regressão. Atualizações persistentes seguem a regra de aprendizado/versionamento; o avaliador não publica ou instala versões automaticamente.

