# EGVR MSA — modos, preservação, escrita e confirmação

Referência principal das seções 6, 7, 8 e 16. Aplicar estas regras depois de identificar o escopo autorizado e a decisão material. Os valores de status são definidos em [Perfis e status](perfis-e-status.md); os fatos documentais, em [Identidade e evidência](identidade-e-evidencia.md).

## R06 — Fixar o modo e preservar a finalidade do destino

**Finalidade.** Distinguir atualização de registros anteriores e criação de um novo destino, para aplicar corretamente preservação, autoria e limites do modelo.

**Condições de aplicação.** No início do trabalho e em toda retomada. Registrar no controle externo um dos modos abaixo, a tarefa e o arquivo de destino.

**Evidência necessária.** Pedido do usuário, estado e finalidade do destino, origem dos dados e eventual modelo. A mera presença ou ausência de conteúdo em uma célula não determina o modo.

**Ação permitida.**

| Modo | Quando aplicar | Consequência |
| --- | --- | --- |
| `ATUALIZAR_PLANILHA_EXISTENTE` | Destino com registros anteriores a preservar, mesmo parcialmente preenchido | Preservar esses registros e aplicar R07 a cada valor efetivamente inserido ou alterado |
| `CRIAR_PLANILHA_DO_ZERO` | Pedido de novo arquivo a partir de origem, consultas e modelo | Criar saída separada e aplicar R07 aos dados iniciais |

- Tratar células vazias de destino preexistente como atualização; seu preenchimento não é criação do zero.
- Em destino existente, preservar uma linha-base já destinada ao veículo. Se uma consulta completa e suficiente comprovar ausência de restrição judicial ativa, essa linha pode receber observação e status conforme R11/R14, desde que O/P estejam autorizadas; não apagar processo, tribunal, Vara ou histórico preexistente para convertê-la em linha genérica.
- Tratar a cópia de uma planilha preenchida, feita para atualizar seus registros, como atualização.
- Tratar um novo destino como criação, ainda que a origem tenha dados e o modelo contenha cabeçalhos, fórmulas, listas, estilos ou outros elementos estruturais.
- Manter o modo de criação durante o preenchimento e suas retomadas. Depois da criação concluída, uma tarefa futura de atualização daquele arquivo usa o modo de atualização.
- Quando a instrução for apenas “use este modelo”, aplicar reprodução estrita: preservar nomes e ordem das abas, cabeçalhos, ordem das colunas, fórmulas, validações, listas, formatação, dimensões e blocos.
- Ampliar a estrutura somente por pedido expresso e dentro da lista de campos autorizados.

**Ação proibida.**

- Modificar o modelo original ou a planilha de origem ao criar uma nova planilha.
- No modo de criação, criar uma linha judicial fictícia com processo vazio apenas para representar veículo sem restrição, quando o modelo for uma linha por restrição e não previr linha-base ou campo próprio para essa ausência.
- Alternar de criação para atualização no meio da execução porque as primeiras linhas já foram preenchidas.
- Presumir autorização para acrescentar colunas úteis, mesmo em criação ampliada.
- Chamar de criação do zero uma cópia destinada a atualizar dados anteriores para evitar as exigências de autoria.

**Tratamento da lacuna.** Usar o pedido, a finalidade e o estado observado para resolver classificações inequívocas sem repetir perguntas já respondidas. Se a finalidade do destino permanecer materialmente ambígua, registrar a pendência e preservar o alvo até defini-la; continuar inventário e análise independentes. Não misturar os dois critérios de cor para contornar a dúvida.

**Testes correspondentes.** [T28, T29, T30, T31 e T32](../evals/casos-de-regressao.md). T31 mantém o modo entre retomadas; T32 verifica reprodução estrita e integridade do modelo original.

## R07 — Cor de autoria por valor efetivamente modificado

**Finalidade.** Tornar identificáveis as intervenções em planilha existente sem reformatar células apenas conferidas ou atribuir ao agente alterações de execução anterior.

**Condições de aplicação.** Modo já fixado por R06; valores e campos autorizados; ferramenta capaz de aplicar e verificar a cor requerida sem violar R08.

**Evidência necessária.** Comparação entre valor anterior e proposto, propriedades de fonte relevantes, estado da formatação condicional e proteção, e registro da alteração da execução atual. Cor vermelha preexistente não é evidência de autoria atual.

**Ação permitida.**

- Em `ATUALIZAR_PLANILHA_EXISTENTE`, usar fonte vermelha em todo valor realmente inserido ou alterado pelo agente: em linha existente, célula antes vazia ou nova linha autorizada. A regra alcança identificadores, tribunal, Vara, processo, observação, status, datas, sequência e demais campos autorizados.
- Alterar somente a propriedade de cor necessária à autoria, conservando família, tamanho e demais atributos da fonte e as outras propriedades de R08.
- Manter a formatação original das células apenas conferidas, inclusive as que já estejam vermelhas.
- Em `CRIAR_PLANILHA_DO_ZERO`, escrever os dados iniciais em fonte preta normal, salvo convenção expressa do modelo. Preservar as cores e convenções estruturais do modelo, como cabeçalhos; o preto dos dados não autoriza redefinir estilos estruturais.

**Ação proibida.**

- Regravar valor idêntico apenas para mudar a cor.
- Pintar a linha inteira indiscriminadamente ou usar vermelho como marcador de autoria em criação do zero.
- Interpretar vermelho como garantia de correção material, aprovação humana ou autoria da execução atual sem registro de antes e depois.
- Remover proteção, alterar silenciosamente formatação condicional ou gravar quando não for possível cumprir a marcação obrigatória.

**Tratamento da lacuna.** Se proteção, regra condicional ou limitação da ferramenta impedir a cor correta, bloquear somente a mudança dependente, explicar o impedimento e continuar os itens independentes. Não declarar uma alteração concluída com marcação válida sem a confirmação exigida por R16.

**Testes correspondentes.** [T28, T29, T30, T31 e T35](../evals/casos-de-regressao.md). T28 deve comparar células alteradas e apenas conferidas; T29 deve incluir célula correta já vermelha; T35 não pode remover regra condicional para fazer o teste passar.

## R08 — Preservação estrutural e edição mínima

**Finalidade.** Conservar o arquivo e seus históricos ao realizar apenas a menor alteração autorizada, detectando os efeitos de inserções e as limitações da ferramenta.

**Condições de aplicação.** Toda edição ou criação com modelo, inclusive nova linha, cópia de elementos estruturais e salvamento em formato que possa perder recursos.

**Evidência necessária.** Estado anterior dos elementos atingidos e capacidade real da ferramenta de preservá-los. O alcance da inspeção deve ser suficiente para a edição proposta e declarado no relatório. Para uma inserção, examinar ainda referências e coordenadas afetadas.

**Ação permitida.** Preservar, salvo autorização expressa aplicável:

- Fórmulas e formatos numéricos; zeros iniciais e representação de identificadores segundo R13.
- Família, tamanho e demais atributos da fonte, com a única mudança de cor prevista por R07 quando aplicável.
- Preenchimentos, bordas, alinhamentos, comentários e notas.
- Listas de seleção, validações, proteções e formatação condicional.
- Mesclagens, alturas de linha, larguras de coluna, filtros, tabelas e organização dos blocos.
- Nomes e estrutura das abas, campos e abas fora do escopo.

Quando houver autorização para inserir linhas, preservar os elementos estruturais e as referências pertinentes, verificar o efeito da inserção e reidentificar as linhas e células antes de qualquer escrita seguinte. Reutilizar somente a estrutura apropriada; os atos humanos exigem a disciplina de [R14](identificadores-e-historicos.md#r14--históricos-humanos-observações-e-datas).

**Ação proibida.**

- Excluir linhas, veículos, processos ou registros históricos como forma de conciliação.
- Acrescentar ou excluir colunas sem autorização.
- Substituir fórmula pelo valor exibido ou reconstruir toda a planilha para editar poucas células.
- Continuar usando coordenadas antigas depois de inserções que deslocaram os alvos.
- Copiar uma linha inteira com seus valores e históricos para aproveitar sua aparência.
- Declarar preservação que a ferramenta ou o método utilizado não conseguem verificar.

**Tratamento da lacuna.** Se a edição segura exigir mudança estrutural não autorizada, registrar a dependência antes de realizá-la. Se o formato ou a ferramenta não preservarem os recursos exigidos, bloquear somente a operação dependente e manter análise e proposta disponíveis. Uma cópia de segurança não autoriza perda de estrutura nem restauração sobre trabalho humano concorrente.

**Testes correspondentes.** [T24, T28, T32, T33, T34, T35 e T36](../evals/casos-de-regressao.md). T33 deve verificar que a nova linha tenha estrutura adequada sem atos humanos copiados; T34 e T35 devem expor incompatibilidades reais; T36 deve confirmar os alvos após deslocamento.

## R16 — Escrita mínima, controle externo e leitura de confirmação

**Finalidade.** Garantir rastreabilidade por célula, detectar concorrência e resultados parciais, e tornar a reexecução segura sem presumir sucesso a partir do retorno de uma ferramenta.

**Condições de aplicação.** Para cada alteração proposta, tentada ou executada dentro de um lote autorizado. Somente decisões confirmadas, nos termos dos [Critérios de confiança](criterios-de-confianca.md), podem avançar autonomamente. A qualificação da ferramenta e do perfil segue [Estados de maturidade](estados-de-maturidade.md).

**Evidência necessária.** Manter, fora da planilha, os seguintes elementos de cada alteração:

| Elemento do registro | Conteúdo necessário |
| --- | --- |
| Identificação | Execução, arquivo, aba, registro, célula e identidade da restrição |
| Proposta | Valor anterior, valor proposto e regra aplicada |
| Fundamento | Documento e localização da evidência, grau de confiança e resultado da revisão crítica |
| Tentativa | Resultado da escrita, incluindo erro, timeout ou aplicação parcial |
| Confirmação | Valor efetivamente relido, cor e alcance de verificação das propriedades pertinentes |

**Ação permitida.**

1. Revalidar imediatamente antes da escrita que o alvo e seu conteúdo ainda correspondem ao estado analisado. Se houver inserção anterior, usar a identidade reconstituída segundo R08.
2. Se houver mudança humana concorrente, comparar a divergência com a proposta e reavaliar o caso; preservar a alteração humana enquanto a incompatibilidade não for resolvida.
3. Aplicar o conjunto mínimo de mudanças comprovadas e autorizadas, sem regravar as células que já estejam corretas.
4. Após salvar, ler novamente os campos alterados; conferir valores, cores e as propriedades relevantes; verificar inserções e referências afetadas; registrar o alcance real do exame.
5. Registrar separadamente concluído e confirmado, falha, bloqueio, aplicação parcial e resultado incerto, sem confundir esses estados técnicos com o status material da restrição.
6. Depois de timeout ou falha posterior à tentativa, consultar o destino real antes de decidir qualquer nova tentativa. Somente repetir as alterações comprovadamente não aplicadas e ainda autorizadas.
7. Na reexecução, verificar registros e observações já existentes e propor somente a diferença ainda necessária. Um lote reprocessado não deve criar duplicações nem repetir observações.

**Ação proibida.**

- Sobrescrever automaticamente mudança humana concorrente.
- Declarar sucesso apenas porque a ferramenta respondeu “salvo”.
- Repetir cegamente uma escrita após timeout ou falha com possível efeito.
- Tratar atualização parcial como sucesso integral ou como falha integral sem leitura do destino.
- Restaurar a planilha inteira por cima de alterações humanas concorrentes.
- Gravar estados técnicos, como `resultado incerto`, no lugar do status material da restrição.

**Tratamento da lacuna.** Se o destino não puder ser relido, registrar resultado incerto e quais alterações podem ter ocorrido; não repetir a tentativa até identificar o estado real. Se apenas parte do lote estiver confirmada, relatar cada parcela e manter pendente o restante. Se a capacidade ainda não foi testada ou validada, descrever o estágio real e manter a atuação compatível com ele, sem simular conclusão.

**Testes correspondentes.** [T28, T29, T34, T36, T37, T38, T39, T40, T46, T47 e T48](../evals/casos-de-regressao.md). T37 exige detecção de concorrência; T38 exige readback antes de retry; T39 identifica a parcela aplicada; T40 demonstra idempotência; T47 assegura que análise não se converta em escrita.
