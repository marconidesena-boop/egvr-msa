# EGVR MSA — identificadores, normalização e históricos humanos

Referência principal das seções 13 e 14. A correspondência material entre restrições pertence a [R04](identidade-e-evidencia.md#r04--uma-linha-corresponde-a-uma-restrição-judicial-individual); o status pertence a [R11](perfis-e-status.md#r11--status-material-individual-e-preservação-do-tratamento-humano). Este arquivo governa o significado e a representação dos campos, a normalização comprovada e a preservação dos atos humanos.

## R13 — Identificadores, processos e normalização judicial

**Finalidade.** Impedir associação por aparência numérica, fabricação de dados e expansão não comprovada de unidades judiciais, permitindo comparação auxiliar sem adulterar identificadores.

**Condições de aplicação.** Leitura, correspondência, formatação ou correção de placa, RENAVAM, chassi, DRV, sequência, processo, dados SEI, ofício, protocolo, tribunal e Vara. A presença de número SEI em um arquivo fornecido não habilita consulta ou operação no sistema.

**Evidência necessária.** Campo e rótulo de origem, valor literal, contexto, veículo e restrição a que o dado pertence. Para normalizar unidade, fonte competente e pertinente ao tribunal, comarca, município, especialidade, processo e período do registro. Registrar a localização e os limites da equivalência demonstrada.

**Ação permitida — separação dos identificadores.** Manter separados os significados de placa, RENAVAM, chassi, número DRV, número ou sequência da restrição, número do processo judicial, NUP do SEI, número do documento SEI, identificadores internos de páginas ou sistemas, número de ofício e protocolo administrativo. Armazenar processos e outros identificadores suscetíveis a perda de zeros como texto, conservando o valor da fonte e os zeros iniciais.

**Ação permitida — comparação e representação do processo.**

- Preservar todos os dígitos. Conservar processos antigos no padrão original quando não houver suporte para outra apresentação.
- Comparar uma representação auxiliar sem pontuação ou separadores, mantendo todos os dígitos e conservando o literal de cada fonte. Essa comparação ajuda a encontrar candidatos e não é uma transformação automática da célula.
- Aplicar máscara CNJ somente quando os dígitos existentes e a validação pertinente sustentarem a máscara. A validação matemática não prova vínculo com veículo, restrição ou Vara.
- Tratar divergências de zeros como candidatas a correspondência, nunca como identidade automática. Exigir evidência independente suficiente de que os registros se referem à mesma restrição, e registrar a divergência mesmo quando o vínculo for confirmado.
- Distinguir identidade material confirmada de correção do texto do processo: confirmar a primeira não autoriza modificar o segundo sem fonte para o valor exato e autorização do campo.

**Decisão conservadora de conciliação entre as seções 10 e 13.** A seção 10 admite investigar apresentações aparentemente distintas, inclusive zeros adicionais; a seção 13 proíbe completar dígitos e exige preservá-los. No EGVR MSA, igualdade da cadeia integral de dígitos após retirada de pontuação é comparação auxiliar. Cadeias com zeros diferentes permanecem diferentes até prova independente da correspondência. Não remover, acrescentar ou completar zeros para forçar equivalência, nem transportar essa equivalência para casos futuros sem seu contexto. Quando essa prova faltar, a divergência impede concluir tanto duplicidade quanto baixa por suposta ausência daquela candidata.

**Ação permitida — tribunais e Varas.** Quando o campo estiver autorizado e a equivalência comprovada, adotar nomes completos em letras maiúsculas, mantendo acentos, cedilha e ordinais corretos. Uniformizar somente ocorrências realmente equivalentes dentro do escopo. Pesquisar prioritariamente fontes oficiais, especialmente domínios `.jus.br`, verificando contexto temporal e, quando relevantes, renomeações, extinções e renumerações. Registrar fonte, contexto e limites de reutilização de cada equivalência validada. O pacote não inicia com um catálogo de equivalências presumidas.

**Ação proibida.**

- Converter um tipo de identificador em outro porque os números se parecem.
- Acrescentar dígitos ausentes, inventar dígitos verificadores, eliminar zeros iniciais ou fabricar um número CNJ para processo antigo.
- Tratar máscara ou cálculo do CNJ como prova substantiva de pertencimento.
- Adivinhar expansão de abreviação, número de Vara, especialidade ou comarca.
- Usar a nomenclatura atual para reescrever automaticamente registro histórico.
- Tratar coincidência de nome ou número como evidência suficiente de todos os elementos de identidade definidos por R04.

**Tratamento da lacuna.** Preservar o texto original, registrar a divergência e a informação que falta. Uma dúvida sobre a expansão da Vara pode bloquear apenas essa normalização; uma dúvida sobre identidade bloqueia todas as decisões que dela dependam. Fontes de unidade judicial não comprovam, por si sós, que a restrição pertence a ela; aplicar [Hierarquia das fontes](hierarquia-das-fontes.md) e [Critérios de confiança](criterios-de-confianca.md).

**Testes correspondentes.** [T01, T02, T23, T24, T25, T26 e T27](../evals/casos-de-regressao.md). T02 deve distinguir variação de separador de divergência de dígito; T24 deve manter zeros no armazenamento, na escrita e no readback; T26 deve bloquear expansão sem fonte; T27 deve permitir a normalização comprovada dentro do escopo.

## R14 — Históricos humanos, observações e datas

**Finalidade.** Conservar os atos humanos atribuídos a cada restrição e redigir observações verificáveis sem transportar histórico entre linhas ou confundir datas de naturezas diferentes.

**Condições de aplicação.** Nova linha, alteração de status, preenchimento de observações, registro de ato humano ou revisão de divergência entre anotação anterior e fonte atual. Aplicar em ambos os modos, conforme os campos autorizados.

**Evidência necessária.** Para ato humano, documento ou registro próprio do ato, vínculo com a restrição e autorização daquele campo. Para observação, fato comprovado, data com significado conhecido e eventual sequência efetivamente documentada. Igualdade de veículo, processo, tribunal ou Vara não é prova de que o ato se aplica a outra restrição.

**Ação permitida.**

- Preservar históricos existentes inclusive após baixa comprovada.
- Iniciar nova linha sem atos humanos não comprovados para aquela restrição. Aproveitamento de estrutura segue R08, não transfere valores humanos.
- Registrar ato humano somente com fonte própria e campo autorizado.
- Escrever observações curtas, objetivas e vinculadas à restrição da linha, mantendo o texto humano relevante já existente.
- Quando fonte atual e anotação anterior forem incompatíveis, registrar a divergência de modo rastreável, sem apagar o histórico silenciosamente.
- Usar datas e sequências somente se comprovadas e designar explicitamente sua natureza quando houver risco de confusão.

**Campos que não podem ser copiados de outra linha.** Data de notificação, e-mail, destinatário, número de ofício, número de documento SEI, data de inclusão no SEI, resposta do juízo, prazo, responsável, providência humana, texto de contato e histórico de notificação. Cada um exige prova própria para a restrição atual.

**Semântica das datas.**

| Data | Fato que representa |
| --- | --- |
| Consulta | Referência temporal da consulta, quando informada |
| Emissão do documento | Produção ou emissão do documento |
| Leitura | Momento em que o material foi examinado |
| Inserção da restrição | Registro da restrição, quando documentalmente informado |
| Baixa efetiva | Momento da baixa informado pela fonte competente |
| Constatação da baixa | Momento em que a análise constatou a baixa com a evidência disponível |
| Alteração da planilha | Momento da escrita no destino |

Essas datas não são intercambiáveis. A consulta pode ser anterior à leitura, à constatação e à alteração da planilha. Data da execução não completa retroativamente metadado ausente na fonte.

**Vocabulário canônico da coluna de observações.** Quando o modelo usar a coluna O para observações judiciais, adotar exatamente uma das frases abaixo sempre que os respectivos fatos estiverem comprovados:

| Situação comprovada | Texto canônico |
| --- | --- |
| Restrição ativa comprovadamente nova na planilha, com data de inserção cadastral e sequência comprovadas | `Nova restrição inserida em DD/MM/AAAA. Sequência N.` |
| Restrição já conhecida ou sem afirmação de novidade, com data de inserção cadastral e sequência comprovadas | `Restrição inserida em DD/MM/AAAA. Sequência N.` |
| Restrição baixada, com data efetiva de baixa e sequência comprovadas | `Restrição baixada em DD/MM/AAAA. Sequência N.` |
| Linha-base de planilha existente e consulta completa que comprova ausência de qualquer restrição judicial ativa | `Sem restrição judicial ativa.` |

`Nova restrição inserida` e `Restrição inserida` descrevem a inserção cadastral da restrição na fonte, não a data em que a planilha foi alterada. `Restrição baixada` exige data efetiva de baixa. A data da consulta, emissão, leitura, constatação ou alteração da planilha não substitui a data de inserção ou baixa. `Sequência N` somente pode ser usada quando a sequência estiver documentada para a mesma restrição. Nunca grave marcadores como `DD/MM/AAAA` ou `N` literalmente nem complete dado ausente por inferência.

Se nenhuma frase canônica representar fielmente os fatos comprovados, preserve a célula ou use redação alternativa estritamente factual apenas quando o campo estiver autorizado, registrando no controle externo a razão da exceção. Para baixa por ausência qualificada em perfis que omitem baixadas, a redação e os metadados obrigatórios continuam exclusivamente em [R10](perfis-e-status.md#r10--interpretar-atividade-e-baixa-segundo-a-origem-e-a-cobertura); não fabrique data efetiva. Em reexecução, não repita frase já presente. Texto humano relevante deve ser preservado e, se for necessário acrescentar a frase canônica, a composição não pode apagar ou atribuir a outra restrição o histórico anterior.

**Ação proibida.**

- Transportar qualquer histórico humano de linha vizinha por coincidência de identificadores.
- Apagar observação relevante para padronizar a apresentação.
- Usar mudança autorizada de status como autorização implícita para editar observações ou outro campo.
- Inventar data, sequência, envio, recebimento ou responsável para completar o registro.
- Repetir observação já presente em reexecução; a confirmação e a idempotência seguem R16.

**Tratamento da lacuna.** Deixar o dado humano não comprovado sem preenchimento novo e registrar a pendência externa. Quando observações estiverem fora do escopo, manter a justificativa no relatório, inclusive a da baixa constatada por ausência. Se houver conflito com histórico existente, preservar o registro anterior e explicar o conflito até haver suporte para tratamento autorizado.

**Testes correspondentes.** [T15, T16, T17, T19, T25, T33 e T40](../evals/casos-de-regressao.md). T19 deve preservar os atos depois da mudança de status; T33 deve deixar vazios os atos não comprovados da nova linha; T40 deve impedir observação repetida.
