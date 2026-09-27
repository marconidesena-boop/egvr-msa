# Inclusão externa, evidência e estado da mesa

Referência principal do módulo `incluir-consulta-sei`, introduzido em 0.2.0 por pedido de ampliação. Não altera as regras de conciliação de planilhas e não habilita os demais módulos SEI previstos para o futuro.

## Identidade e arquivo

No controle da tarefa, registre origem da associação (arquivo/aba/célula quando houver), placa, chassi ou RENAVAM disponível, NUP individual exato, unidade-alvo, arquivo, tamanho, páginas, SHA-256, origem e data da consulta. Não fixe letras de colunas: “última coluna” precisa ser verificada na planilha atual. Preserve zeros; NUP não é CNJ nem número de documento SEI.

Confirme placa e identificadores no conteúdo do PDF, na origem e no processo. O número da planilha é um localizador, não prova autossuficiente do vínculo. Use documentos ou cadastro do processo para corroborar; uma divergência de identidade impede a inclusão. Não transfira dados entre veículos. Uma correspondência apenas provável fica pendente.

Leia todas as páginas necessárias para verificar identidade e integridade, inclusive eventuais anexos. Não remova páginas, restrições administrativas ou dados do original: a regra de não importar restrições administrativas para planilha não autoriza editar o PDF que o usuário mandou incluir. Se o escopo exige uma versão filtrada, solicite definição própria e não altere silenciosamente o documento.

A data da consulta deve refletir o material fornecido. Data de baixa/inserção de restrição não é data do documento; a data de hoje não substitui a data da consulta. Se a data estiver apenas no nome informado pelo usuário, registre essa proveniência e procure corroboração no documento/metadados; inconsistência material impede preencher uma data como comprovada. Nunca alegue consulta nova ao incluir PDF antigo.

## Ferramenta, sessão e unidade

Prefira ferramenta específica disponível; caso contrário, use controle de navegador com as instruções atuais da ferramenta e sessão institucional do usuário. Confirme domínio, NUP carregado e unidade selecionada. Chrome aberto não prova acesso, identidade ou permissão de escrita. Falta de ferramenta/upload/readback confiável bloqueia apenas o passo dependente; não crie servidor, extraia cookies nem use automação alternativa não autorizada.

Login, certificado, CAPTCHA ou permissão que exija intervenção humana deve ser tratado segundo a plataforma. Não prometa trabalho totalmente desacompanhado. Uma regra do plugin não remove aprovações obrigatórias. Não copie seletores ou URLs com tokens de uma sessão antiga; observe novamente antes de agir.

Ausência do processo na lista da mesa não significa “concluído”. Diferencie aberto, concluído na unidade, fechado/recolhido na árvore, sigiloso sem acesso e estado desconhecido. Confirme por indicador ou andamento inequívoco da unidade-alvo. Não reabra processo em outra unidade. Processo sem acesso, indisponível, sobrestado ou cujo fluxo exija ação extra fica pendente; não desfaça o impedimento por conta própria.

## Prevenção de duplicidade

- Inventarie árvore completa e documentos candidatos por títulos, datas e tipo; expanda pastas/paginação. Nomes diferentes ou “Anexo” genérico não afastam equivalência. Examine o conteúdo dos candidatos, não só o nome.
- Mesmo NUP + mesmo SHA-256 significa candidato a duplicidade binária; confirme documento vinculado ao processo e conteúdo. Hash diferente não comprova novidade: compare consulta/origem/data, veículo, páginas e conteúdo material.
- Mesma placa com consulta de data anterior não é, por si só, duplicidade. Mesma data com conteúdo efetivamente diferente exige análise e delimitação, não descarte nem repetição automática.
- Se já existir documento idêntico ou equivalente, informe seu número SEI e não inclua novamente. Se ainda não reabriu, não reabra só para concluir depois.
- Repetições de linhas, números judiciais ou restrições em uma planilha não multiplicam envios de um mesmo PDF no mesmo processo.
- Se a cobertura dos documentos for incompleta ou houver candidato não verificável, registre duplicidade inconclusiva e não envie. Uma lista vazia causada por falha não libera o envio.
- Antes de salvar, confira novamente a ausência de inserção concorrente e o destino atual. Se aparecer o documento, reconcilie e não duplique.

## Metadados da inclusão

Observe os campos realmente exigidos no formulário. Escolha espécie/tipo, formato, data, número, nome na árvore/descrição e acesso com fundamento, sem presumir rótulos, inventar número oficial ou reaproveitar dados de outro documento.

Para uma consulta extraída diretamente de sistema e preservada em PDF, “nato-digital” pode ser aplicável se a proveniência estiver confirmada; PDF de digitalização exige tratamento diferente. Não declare autenticação, assinatura, cópia autenticada ou validade jurídica que não foi demonstrada.

Um padrão de nome pode combinar origem, placa e data, por exemplo “DETRAN — PLACA — DD/MM/AAAA”, adaptado aos campos e limites reais. Não fixe “Número” igual à placa se o campo tiver outra finalidade ou se o contexto institucional não comprovar esse uso. Não copie histórico de notificações para a descrição.

Nível de acesso e eventual hipótese legal exigem evidência institucional aplicável ou orientação explícita do usuário. Não escolher público por padrão, não copiar restrição de documento heterogêneo e não inventar fundamento legal. Classificar o novo documento não autoriza alterar acesso do processo nem de documentos existentes. Uma dúvida material nesses campos requer esclarecimento agrupado, não uma suposição para terminar o envio.

Registre os metadados efetivamente conferidos em `metadados` e as fontes em `evidencias.metadados`. A checagem local não verifica a adequação jurídica; se ela exigir análise jurídica, use as regras de pesquisa oficial aplicáveis.

## Regra de mesa: restaurar, não encerrar indiscriminadamente

Esta política decorre da instrução do usuário: abrir o processo que estiver fechado na mesa antes de inserir e concluir novamente depois, para não deixá-lo aberto.

| Estado inicial comprovado na unidade-alvo | Antes da inclusão | Depois de confirmar o documento |
| --- | --- | --- |
| Aberto | Manter aberto | Manter aberto; não concluir |
| Concluído | Reabrir na mesma unidade e conferir que ficou aberto | Concluir nessa unidade e conferir que voltou a concluído |
| Desconhecido ou sem acesso | Somente leitura para esclarecer | Não reabrir, não incluir nem concluir por suposição |

Registre a autorização de restauração do estado da mesa no controle, junto da autorização de inclusão vigente. No fluxo configurado, essa restauração faz parte do pedido de inclusão e não demanda aprovação a cada clique. Se o usuário pedir só leitura/preparação, excluir reabertura/conclusão ou mandar parar, essa autorização não existe ou deixa de valer. A configuração não altera a exigência de confirmação da plataforma quando aplicável.

Reabra somente depois de arquivo, vínculo, duplicidade e metadados estarem resolvidos, reduzindo tempo de processo aberto. Registre e confirme a reabertura; não presuma sucesso pelo clique. Se o processo inicialmente concluído aparecer aberto por outra intervenção, não atribua a reabertura ao agente nem conclua ao final. Suspenda mutações nesse item e esclareça a concorrência.

Antes de concluir, revalide NUP/unidade, documento confirmado, estado atual e atividade desde o marco inicial, por árvore e histórico/indicadores disponíveis. Não conclua com conteúdo ou trabalho de terceiros surgido durante o fluxo; se não for possível verificar concorrência suficiente, registre pendência. Não altere atribuição, marcadores, prazos, sobrestamento, relacionamentos ou tramitação como parte da restauração.

Se o processo foi reaberto por esta execução, mas o envio foi abandonado com ausência de efeito comprovada, restaure o estado concluído apenas se a autorização continua válida e não houve intervenção externa. Registre “não incluído; mesa restaurada”. Se o efeito é incerto, não conclua até reconciliar. Se o usuário mandou parar, não faça restauração automática: informe a pendência.

## Persistência, confirmação e retomada

Antes de upload/salvamento que possa persistir documento, registre `tentativa=INICIADA`, horário e marco da árvore. Trate o upload como possível escrita quando a ferramenta/sistema puder criar rascunho ou documento antes de “Salvar”. Não execute duas tentativas concorrentes para o mesmo NUP/PDF.

Após salvar, abra a árvore novamente, localize o novo registro e capture o número SEI real. Confira processo, unidade, metadados e o conteúdo armazenado. Baixe por recurso suportado e compare o SHA-256 com o original, se disponível. Se o sistema legitimamente transformar os bytes, demonstre equivalência do conteúdo integral, páginas, identidade e data; não use só a primeira página. Sem conferência suficiente, resultado incerto.

Timeout ou perda de sessão após possível escrita não significam fracasso. Não repita upload/salvar/reabertura/conclusão às cegas. Primeiro recupere somente leitura: processo, árvore, documento/cadastro e estado da mesa. Se o documento está correto, confirme sem reenvio; se ausência está comprovada, registre a falha sem efeito. Se houve inclusão parcial ou errada, não exclua, substitua ou “corrija” fora do escopo: relate e peça direção. Uma tentativa incerta bloqueia novas mutações nesse processo, mas não casos independentes com identidade segura.

Após uma falha, não entre em loop automático de reenvio. Qualquer tentativa posterior deve reler o controle anterior, resolver o efeito e refazer precondições; preserve o vínculo com a tentativa anterior. Para retomada, nunca zere estado “incerto” por criar outro controle. Busque o controle da tarefa e documentos pelo mesmo NUP/arquivo/consulta.

Depois da conclusão, confirme estado final na mesma unidade. Se inclusão foi confirmada mas fechamento falhou, informe separadamente “incluído; restauração pendente”, sem reenviar o PDF. Se o processo foi concluído por terceiro, não atribua essa ação ao agente.

## Controle e relato

`evidencias` contém caminhos/locais e descrições verificáveis das observações; `historico` conserva eventos com horário real e ação/resultado. Não use somente booleanos para alegar confirmação. Não guarde conteúdo sensível além do necessário nem inclua controles reais dentro do pacote distribuível. Não salve tokens, cookies, senhas ou dados de autenticação.

O auxiliar local valida consistência e sugere etapa, mas um campo `true` não é evidência autônoma. Seu uso não assegura exclusão mútua entre agentes nem bloqueia tecnicamente cliques: deve haver um único executor por processo. Se outro executor estiver ativo, preserve o item e esclareça antes de agir.

Relate quantos documentos foram realmente incluídos, quais já existiam, quais ficaram pendentes e os respectivos números SEI confirmados. Informe também reaberturas e conclusões executadas, estado inicial/final e falhas de restauração. Um resultado pode ter inclusão confirmada e pendência de mesa. Não diga apenas “concluído” sem distinguir documento e processo.
