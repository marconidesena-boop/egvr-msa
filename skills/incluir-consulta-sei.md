---
name: incluir-consulta-sei
description: Preparar e executar inclusões expressamente autorizadas de PDFs de consultas veiculares em processos individuais do SEI, com conferência de vínculo, duplicidade, leitura posterior e restauração do estado da mesa. Usar em pedidos de anexar ou inserir consulta no SEI. Não usar para assinar, tramitar, gerar ofícios, analisar recebimentos ou desvincular multas. Fluxo candidato a piloto; depende de ferramenta externa disponível.
---

> Edição para Skills da equipe, derivada do EGVR MSA 0.2.1. As referências e modelos necessários estão incorporados abaixo. Os links para outros módulos apontam para os arquivos irmãos desta pasta. Importar texto não instala conectores, autentica serviços nem autoriza operações institucionais. Código Python anexado é recurso de referência: para executá-lo, é necessário materializar os arquivos com os nomes indicados em um ambiente autorizado com Python disponível; preserve a estrutura relativa dos scripts. Se o ambiente não oferecer essa capacidade, informe a dependência e não afirme que a fila ou o auxiliar foram executados. Relatos antigos de maturidade nos anexos são históricos; não ampliam a autorização nem substituem evidência atual.


# Inclusão de consultas no SEI — EGVR MSA

Esta skill acrescenta um fluxo de inclusão ao plugin; não fornece conector, credenciais ou acesso institucional próprio. Sua instalação não autoriza uma inclusão. Em 26/09/2026 foi concluído um piloto real no perfil SEI PRF 4.1.5/SEI Pro via Computer Use: inclusão, download idêntico ao original e restauração da mesa. Isso não homologa outros ambientes nem libera automaticamente os demais envios. Não confunda testes locais com operações reais.

## Escopo e autorização

- Diferencie configurar o plugin, preparar o envio, consultar um processo e efetivamente incluir o PDF. Pedido de configuração ou preparação não autoriza navegar no SEI nem enviar arquivo. Pedido só de consulta autoriza apenas leitura.
- Para executar, identifique a autorização do usuário para os arquivos/consultas e processos do piloto ou lote. Dados já fornecidos podem resolver o escopo; peça apenas informação material ausente. Uma autorização clara cobre os passos normais desse fluxo, sem pedir aprovação por campo ou documento, respeitando confirmações obrigatórias da plataforma.
- A regra de mesa aprovada pelo usuário é: se concluído na unidade-alvo, reabrir antes da inclusão e concluir novamente após confirmar o documento; se já aberto, preservar aberto. A regra vale dentro de uma inclusão autorizada, nunca para encerrar outros trabalhos, outras unidades ou processos não incluídos no pedido.
- Não assine, autentique documento, envie, tramite, crie processo, exclua/substitua documento, altere acesso preexistente, edite planilha ou produza comunicação institucional. Não obtenha consultas novas no DETRAN. Essas operações exigem outro escopo.
- Se o usuário mandar parar, interrompa imediatamente; não execute nem uma conclusão de processo como “limpeza”. Informe a situação conhecida e qualquer restauração pendente.

## Execução

Antes de qualquer operação institucional, leia integralmente [Fluxo e evidências](#recurso-02). Use as instruções da ferramenta efetivamente disponível para navegador/computador, PDFs ou planilha. Não presuma APIs, seletores, credenciais, unidade ou botões. Não instale recurso nem crie integração para contornar limitação sem pedido próprio.

No SEI PRF/SEI Pro, leia antes da primeira interação o [perfil observado](#recurso-03). Use a rota comprovada e o ciclo enxuto ali descrito; não repita a investigação completa do piloto em cada item. Refaça a inspeção detalhada somente diante de mudança de estrutura, identidade ambígua ou erro.

1. Registre o escopo e o estado no [controle externo](#recurso-04), fora do plugin distribuído, da planilha e do SEI. Preencha por item; não imponha ao usuário um manifesto técnico. Não grave senhas, cookies ou URLs com tokens.
2. Confirme acesso ao arquivo, conteúdo integral, origem/data, placa e identificador corroborante disponível. Calcule SHA-256; preserve o arquivo original. Não escolha o PDF só pelo nome.
3. Localize o NUP individual na origem indicada e confirme no SEI o vínculo com o mesmo veículo. Não confunda NUP, processo judicial, número SEI de documento ou ID interno. Uma linha ou processo citado em conversa não dispensa conferência atual.
4. Capture o estado inicial na unidade-alvo e os documentos pertinentes, incluindo pastas/páginas da árvore. Investigue duplicidade por conteúdo, data e identidade, mesmo sob outro título. Um PDF contendo várias restrições é um documento, não um envio por linha de planilha.
5. Confirme tipo documental, data do documento, nome/descrição, formato e acesso conforme contexto comprovado. Faça segunda conferência do conjunto arquivo–veículo–NUP–unidade–metadados. Se informação obrigatória não puder ser fundamentada, preserve e relate a pendência.
6. Só quando o envio estiver pronto, reabra o processo se inicialmente concluído na unidade autorizada; confira o resultado. Não reabra outra unidade nem conclua um processo inicialmente aberto.
7. Antes de qualquer ação que possa persistir arquivo/documento, registre tentativa iniciada. Envie e salve uma única vez. Releia árvore, número SEI, metadados e arquivo efetivamente armazenado. Mensagem “salvo” isolada não comprova inclusão correta.
8. Se inicialmente concluído e reaberto por esta execução, verifique ausência de intervenção externa e conclua somente na mesma unidade após confirmar o documento. Confira a conclusão. Se inicialmente aberto, confirme que permaneceu aberto.
9. Relate NUP, placa, arquivo/data, resultado, número SEI confirmado, duplicidades evitadas, estado inicial/final da mesa e pendências. Separe “documento incluído” de “mesa restaurada”. Não coloque o relatório dentro do processo ou da planilha.

## Resultado incerto, retomada e controle local

Para SEI PRF com SEI Pro, leia [Perfil observado](#recurso-03), especialmente recarga dos formulários, upload e diferença entre lotes por processo e distribuição dos mesmos arquivos. Não aplique seletores sem conferir a página atual.

Para lotes autorizados ou retomadas, use a [fila local transacional](#recurso-01) além do controle por item. Ela conserva tentativas, detecta arquivo alterado e impede reservas repetidas no mesmo banco; não é um conector nem um bloqueio técnico da interface do SEI.

Timeout, interrupção após possível escrita, sessão expirada depois do envio ou readback incompleto exigem reconciliação somente leitura antes de qualquer repetição ou conclusão. Não interprete tela vazia como ausência de documento. Preserve o registro da tentativa; reconsulte a árvore/conteúdo e resolva o efeito, sem novo envio às cegas.

O auxiliar [decidir_etapa.py](#recurso-05) lê o controle local e aponta uma próxima etapa ou impedimento. Ele não acessa o SEI, não executa ações e não comprova a veracidade das evidências declaradas. Use-o como checagem adicional antes de uma mutação e após sua confirmação, nunca como autorização ou substituto da conferência da fonte.

Execute com um Python já disponível: `python scripts/decidir_etapa.py caminho-do-controle.json`. Campos vazios/desconhecidos devem bloquear o avanço pertinente. Detalhes de evidência e retomada ficam na referência principal; [testes locais](../plugin/egvr-msa/skills/incluir-consulta-sei/evals/test_decidir_etapa.py) exercitam somente as decisões do auxiliar.

## Fronteira de validação

O primeiro uso real deve ser um piloto expressamente solicitado, limitado a um PDF e um processo, com verificação antes/depois. A configuração deste módulo não executa esse piloto. Registre ferramenta, caso e resultados reais antes de qualificar o perfil. Um sucesso não libera automaticamente escala, outro ambiente ou outras operações. Veja [cenários do piloto](../plugin/egvr-msa/skills/incluir-consulta-sei/evals/cenarios-piloto.md).


---

<a id="recurso-01"></a>

## Recurso incorporado: skills/incluir-consulta-sei/references/fila-local.md

# Fila local de inclusão

O script `scripts/fila_local.py` usa somente Python padrão e SQLite; não acessa SEI, Google ou provedor de IA. Banco e manifestos reais ficam fora do pacote do plugin. Use um banco único por campanha e preserve-o nas retomadas.

1. `python scripts/fila_local.py BANCO preparar MANIFESTO`: o manifesto é uma lista de objetos com `nup`, `placa`, `arquivo` absoluto e `sha256` esperado opcional. Calcula hash e rejeita vínculos contraditórios. Preparação não comprova identidade institucional nem integridade semântica do PDF.
2. `python scripts/fila_local.py BANCO listar`: consultar situação, inclusive antes de retomar trabalho interrompido.
3. `python scripts/fila_local.py BANCO reservar CHAVE CONTROLE`: imediatamente antes de upload. O CONTROLE usa o template existente e deve levar `INCLUIR_PDF` no decidir_etapa. A transação grava INICIADA e impede nova reserva. Não há liberação automática por tempo.
4. `python scripts/fila_local.py BANCO registrar CHAVE INCERTA "referencia de evidencia"`: registrar efeito ainda não reconciliado.
5. `python scripts/fila_local.py BANCO registrar CHAVE INCLUIDO "referencia da conferencia no processo" --documento NUMERO_SEI --arquivo-baixado PDF`: só aceita hash binário idêntico. Se SEI transformar bytes, esse caminho não finaliza: documente comparação integral e mantenha pendência para tratamento próprio.
6. JA_EXISTENTE segue a mesma exigência de readback e documento; SEM_EFEITO encerra a tentativa sem criar licença automática para tentar novamente. Restauração da mesa segue o controle existente, separadamente do resultado do arquivo.

O banco reduz repetição entre execuções que o utilizam. Ele não impede cliques fora desse fluxo, não valida por si só evidência textual e não substitui a confirmação de identidade, acesso, duplicidade, metadados ou estado da mesa. Não inclua tokens, cookies ou senhas nos controles. Testes sintéticos em `evals/test_fila_local.py` não homologam o SEI.


---

<a id="recurso-02"></a>

## Recurso incorporado: skills/incluir-consulta-sei/references/fluxo-e-evidencias.md

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


---

<a id="recurso-03"></a>

## Recurso incorporado: skills/incluir-consulta-sei/references/perfil-sei-prf.md

# Perfil observado: SEI PRF 4.1.5 e SEI Pro

Verificado em 26/09/2026. Revalidar na sessão atual. Este perfil registra comportamento observado, não fornece uma API nem homologa escala.

Piloto concluído neste perfil em 26/09/2026: PDF de 22 páginas incluído, registro SEI confirmado, arquivo baixado com SHA-256 integral igual ao original e mesa restaurada na unidade. Evidências e identificadores do caso ficam na fila externa do operador, não são destinos padrão do plugin.

## Execução normal após o piloto

Preferência expressa do usuário: não repetir a investigação extensa em cada inclusão. Com escopo autorizado e perfil inalterado, use uma passagem antes e uma depois:

1. Reutilize o manifesto e as conferências documentadas da sessão; confirme o par veículo/PDF/NUP, unidade, estado inicial da mesa e duplicidade no processo atual. Não refaça leitura integral de arquivos inalterados já conferidos; confirme o hash. Não consulte novamente o DETRAN.
2. Reabra apenas quando necessário; preencha e releia os metadados do formulário atual. Anexe e espere o nome exato na lista de anexos. Salve uma vez.
3. Faça uma conferência final conjunta: documento/SEI no processo certo, metadados e arquivo armazenado. Use um download/hash, sem abrir páginas repetidas para provar o mesmo fato. Se necessário, restaure a mesa após conferir os eventos posteriores à reabertura. Atualize a fila e siga para o próximo item autorizado.

Inventário completo, snapshots extensos e investigação de locators ficam para o primeiro uso ou uma falha concreta. Uma captura focada no marco da etapa é suficiente; não repita snapshots sem mudança de estado. Reaproveitar o perfil não autoriza reaproveitar identidade, acesso ou destino de outro veículo.

## Rota de interface comprovada

Todos os seletores abaixo foram observados; confira que correspondem à tela atual. Construa Locators/FrameLocators reavaliáveis, não guarde ElementHandles nem índices AX após transições.

| Marco | Escopo/controle observado | Condição para seguir |
|---|---|---|
| Árvore | `iframe#ifrArvore` | NUP e identidade do veículo atual |
| Ações | `iframe#ifrConteudoVisualizacao` | Ação pertinente à tela atual |
| Formulário externo | Dentro das ações, `iframe#ifrVisualizacao`, `form#frmDocumentoCadastro` | Título Registrar Documento Externo e campos atuais |
| Tipo | `#selSerie`, aprimorado por `#selSerie_chosen` | Consulta selecionada; aguardar recarga antes dos demais campos |
| Data/nome/número | `#txtDataElaboracao`, `#txtNomeArvore`, `#txtNumero` | Valores conferidos no formulário novo |
| Formato | `label#lblNato[for="optNato"]` | Input `#optNato` marcado após clicar no label |
| Acesso, quando comprovado | `label#lblPublico[for="optPublico"]` | Input `#optPublico` marcado; não impor Público a todos os casos |
| Upload | `form#frmAnexos`, `input#filArquivo`, label `#lblArquivo` | Arquivo esperado na `#tblAnexos`; upload não pertence ao form principal |
| Salvar documento | `#divInfraBarraComandosInferior button#btnSalvar` | Único, visível, habilitado, anexo correto confirmado |
| Documento armazenado | Link observado `aqui` no visualizador interno | Download confirmado e SHA-256 igual ao original |
| Restaurar mesa | Concluir Processo → Somente concluir → Salvar | EGVR deixa de constar aberta; outras unidades preservadas |

Há dois botões `#btnSalvar` nesta tela, superior e inferior. O ID sozinho não garante unicidade. Salvar documento e Salvar na tela Conclusão de Processo são ações diferentes. Não repita a primeira porque o segundo ainda é necessário.

No Computer Use desta execução, upload é `waitForEvent('filechooser')` antes do clique no label visível, depois `chooser.setFiles(caminho_absoluto)`. Capture também a rejeição da promessa. Essa API não oferece `locator.setInputFiles`; não invente o método nem use shell/CDP para contornar o navegador. No Playwright nativo, use somente o mecanismo suportado pela ferramenta disponível.

Após `setFiles`, aguarde o arquivo exato aparecer na Lista de Anexos e o fim do progresso. Nome na caixa de seleção local não comprova upload. Depois de Salvar, o snapshot imediato pode ainda mostrar o formulário anterior ou botões desabilitados: espere o marco da nova tela e não clique novamente.

O download foi comprovado com `downloadMedia()` sobre o link observado; um clique comum pode abrir uma nova aba de PDF sem emitir evento de download. Não interprete a ausência desse evento como falha da inclusão. Neste perfil, algumas leituras `locator.evaluate()` aninhadas expiraram apesar de a interface estar disponível; snapshot acessível e locators de ação funcionaram. Isso não prova expiração de login.

## Permissão de arquivo e retomada

Antes de reabrir processos, confira a disponibilidade do navegador/perfil correto e a preparação do acesso local. Se a extensão exigir “Permitir acesso a URLs de arquivo”, respeite a confirmação da ferramenta. Quando `chrome://extensions` for bloqueado pela política, oriente o usuário pelo menu do Chrome; não contorne por outro mecanismo.

Habilitar a permissão pode reconectar a extensão com novo identificador de navegador. Somente diante de desconexão confirmada, siga a documentação de recuperação e localize o mesmo perfil/aba/NUP. Não migre para outra conta e não recarregue um formulário preservado.

Se o primeiro `setFiles` foi rejeitado antes de transferir, e nova captura confirma zero anexos e nenhum Salvar, registre essa ausência de efeito e a mudança que removeu o bloqueio. Uma continuação deve preservar a reserva e o histórico da mesma tentativa; nunca zerar a fila para forçar nova inclusão. Se há arquivo, número SEI, Salvar anterior ou qualquer dúvida, reconcilie somente por leitura antes de enviar novamente.

## Navegação e formulários

- A árvore está em `ifrArvore`. A área de ações está em `ifrConteudoVisualizacao`; o formulário/documento está no iframe interno `ifrVisualizacao`.
- A pesquisa rápida aceita o NUP. Espere a identidade do processo no conteúdo; uma resposta do clique pode ainda conter a tela anterior.
- Selecionar o tipo Consulta no formulário externo recarrega o formulário. Aguarde a opção selecionada no formulário novo antes de preencher data, nome e formato. Uma sequência rápida pode perder os campos preenchidos.
- `Nome na Árvore` e `Número` têm limite de 50 caracteres neste perfil. Deixe Número vazio se não houver identificador documental próprio. Use nome explícito com origem, placa e data.
- O seletor de arquivos tem input `filArquivo` coberto pelo label `lblArquivo` (Anexar Arquivo). Quando o clique no input não produzir filechooser, confira o DOM e use o label visível. Sempre trate a rejeição da promessa para não perder o controle da sessão.
- A extensão de navegador exige acesso a URLs de arquivos para anexar arquivos locais. Na falha de permissão, não salve registro vazio. Registre ausência de anexo, reconcilie a árvore e restaure a mesa se cabível. Não repita esse erro em todos os processos.
- O link `aqui` no visualizador externo permitiu download pela ferramenta documentada. Compare o arquivo armazenado ao original. A leitura de só uma página não valida o PDF inteiro.

## Lotes: três funções diferentes

- Ações em lote do SEI Pro lista documentos do processo corrente, inclusive os de pastas recolhidas. Foi observada a opção Excluir; exclusão real não foi testada. Não presume exclusão entre processos ou recuperação posterior.
- Enviar documentos em processos, conforme documentação SEI Pro, distribui os mesmos arquivos aos processos selecionados. NÃO usar para um conjunto em que cada veículo tem um PDF diferente. Preparar pares explícitos arquivo/NUP e operar a fila um a um.
- Documentos em Lote gera documentos a partir de modelo e variáveis; não equivale a anexar PDFs externos. Não substituir placeholders de modelo sem conferir sua sintaxe e autorização.
- O upload automático do SEI Pro pode derivar tipo do nome e data do arquivo. Não aceitar esses padrões sem conferência: DETRAN não é tipo documental e data de modificação não é necessariamente data da consulta.

## Mesa e concorrência

- Um processo concluído na EGVR pode continuar aberto em outra unidade. Preserve a unidade alheia.
- Reabertura pode atribuir automaticamente ao usuário atual. Registre essa consequência observada e não altere atribuições de terceiros.
- Antes de restaurar a conclusão, leia o andamento desde a reabertura e confira ausência de documentos/atos de terceiros. Se o upload falhou antes de selecionar arquivo e a lista está vazia, documente isso antes de sair.

## Agente de IA e custo

O robô abre painel lateral de outra extensão; esse painel não foi exposto à ferramenta de controle desta sessão. Não anunciar teste do agente com base no clique no ícone. Não configurar provedor, chave ou gastos por inferência. O módulo EGVR é orientação e controle local: não é um modelo de IA nem um conector próprio do SEI.

Prefira scripts locais para hashes, comparação, fila e relatórios. Use IA para interpretação dos documentos e exceções; evite reler integralmente o mesmo processo a cada restrição. Conte custo por veículo concluído e por intervenção, não apenas por chamada. Nenhum preço ou economia percentual foi aferido neste teste.

Fontes de comportamento documentado: https://github.com/SEI-Pro/sei-pro/blob/master/pages/BARRAACOES.md ; https://github.com/SEI-Pro/sei-pro/blob/master/pages/UPLOADDOCS.md ; https://github.com/SEI-Pro/sei-pro/blob/master/pages/DOCUMENTOSEMLOTE.md ; https://github.com/SEI-Pro/sei-pro/blob/master/pages/AGENTEIA.md


---

<a id="recurso-04"></a>

## Recurso incorporado: skills/incluir-consulta-sei/templates/controle-inclusao.json

````json
{
  "versao_controle": "1",
  "modo": "PREPARACAO",
  "parar": false,
  "autorizacao_inclusao": false,
  "autorizacao_restaurar_mesa": false,
  "referencia_autorizacao": null,
  "nup": null,
  "unidade": null,
  "placa": null,
  "chassi_ou_renavam": null,
  "origem_associacao": null,
  "arquivo": null,
  "arquivo_sha256": null,
  "paginas": null,
  "data_consulta": null,
  "identidade_confirmada": false,
  "arquivo_conferido": false,
  "metadados_confirmados": false,
  "ferramenta_disponivel": false,
  "acesso_confirmado": false,
  "estado_inicial_mesa": "DESCONHECIDO",
  "estado_atual_mesa": "DESCONHECIDO",
  "reaberto_nesta_execucao": false,
  "duplicidade": "NAO_VERIFICADA",
  "intervencao_externa": "DESCONHECIDA",
  "tentativa": "NAO_INICIADA",
  "documento_confirmado": false,
  "numero_documento_sei": null,
  "leitura_posterior_conferida": false,
  "metadados": {},
  "evidencias": {},
  "historico": [],
  "pendencias": []
}

````


---

<a id="recurso-05"></a>

## Recurso incorporado: skills/incluir-consulta-sei/scripts/decidir_etapa.py

````python
"""Checagem local de consistencia. Nao acessa rede, SEI ou navegador.

Le somente o JSON informado e sugere uma etapa; nao valida a verdade da evidencia,
nao concede autorizacao e nao executa a etapa sugerida.
"""
import argparse
import json
import re
from pathlib import Path


BOOLS = (
    "parar", "autorizacao_inclusao", "autorizacao_restaurar_mesa",
    "identidade_confirmada", "arquivo_conferido", "metadados_confirmados",
    "ferramenta_disponivel", "acesso_confirmado", "reaberto_nesta_execucao",
    "documento_confirmado", "leitura_posterior_conferida",
)
ENUMS = {
    "modo": {"PREPARACAO", "PILOTO", "LOTE_QUALIFICADO"},
    "estado_inicial_mesa": {"ABERTO", "CONCLUIDO", "DESCONHECIDO"},
    "estado_atual_mesa": {"ABERTO", "CONCLUIDO", "DESCONHECIDO"},
    "duplicidade": {"NAO_VERIFICADA", "AUSENTE", "PRESENTE", "INCONCLUSIVA"},
    "intervencao_externa": {"NAO_DETECTADA", "DETECTADA", "DESCONHECIDA"},
    "tentativa": {"NAO_INICIADA", "INICIADA", "SEM_EFEITO_COMPROVADO", "INCERTA"},
}


def filled(value):
    return isinstance(value, str) and bool(value.strip())


def decide(c):
    def result(step, reason):
        return {"etapa": step, "motivo": reason, "executa_acao": False}

    def block(reason):
        return result("BLOQUEADO", reason)

    if not isinstance(c, dict):
        return block("Controle deve ser um objeto JSON.")
    if c.get("parar") is True:
        return result("PARAR", "Pedido de parada: nenhuma acao, inclusive restauracao.")
    if c.get("versao_controle") != "1":
        return block("Versao de controle ausente ou desconhecida.")
    if any(type(c.get(key)) is not bool for key in BOOLS):
        return block("Booleano ausente/invalido; texto nao comprova uma checagem.")
    if any(not isinstance(c.get(k), str) or c[k] not in values for k, values in ENUMS.items()):
        return block("Estado ausente ou desconhecido.")
    evidence = c.get("evidencias")
    if not isinstance(evidence, dict):
        return block("Evidencias devem ser um objeto.")
    def has(*keys):
        return all(filled(evidence.get(k)) for k in keys)

    if c["modo"] == "PREPARACAO":
        return result("PREPARAR_SEM_OPERAR_SEI", "Configuracao/preparacao nao autoriza acesso institucional.")
    if c["modo"] == "LOTE_QUALIFICADO" and not has("qualificacao_do_perfil"):
        return block("Lote depende de qualificacao real do perfil/ferramenta, nao so deste auxiliar.")
    if not c["autorizacao_inclusao"] or not filled(c.get("referencia_autorizacao")):
        return block("Falta autorizacao vigente e identificavel para a inclusao delimitada.")
    if not isinstance(c.get("nup"), str) or not re.fullmatch(r"\d{5}\.\d{6}/\d{4}-\d{2}", c["nup"]):
        return block("NUP individual ausente ou formato indefinido; nao fabricar identificadores.")
    if not filled(c.get("unidade")) or not filled(c.get("placa")):
        return block("Falta unidade ou placa individual.")
    if not isinstance(c.get("arquivo_sha256"), str) or not re.fullmatch(r"[0-9a-fA-F]{64}", c["arquivo_sha256"]):
        return block("Falta identificacao de integridade do arquivo.")
    if not c["identidade_confirmada"] or not c["arquivo_conferido"] or not has("identidade", "arquivo"):
        return block("Vinculo ou arquivo sem confirmacao documentada.")
    if not c["ferramenta_disponivel"] or not c["acesso_confirmado"] or not has("ferramenta", "acesso"):
        return block("Ferramenta/acesso nao conferidos; nao tentar escrita ou restauracao.")

    initial, current = c["estado_inicial_mesa"], c["estado_atual_mesa"]
    if initial == "DESCONHECIDO" or current == "DESCONHECIDO" or not has("mesa_inicial", "mesa_atual"):
        return block("Estado da mesa nao comprovado na unidade-alvo.")
    if c["reaberto_nesta_execucao"] and (initial != "CONCLUIDO" or not has("reabertura")):
        return block("Reabertura declarada incompativel ou sem evidencia.")

    if c["tentativa"] in {"INICIADA", "INCERTA"} and not c["documento_confirmado"]:
        return result("RECONCILIAR_SOMENTE_LEITURA", "Efeito possivel: nao reenviar nem concluir antes de verificar.")

    outcome = None
    if c["documento_confirmado"]:
        if c["tentativa"] not in {"INICIADA", "INCERTA"}:
            return block("Inclusao confirmada sem tentativa correspondente; preservar historico.")
        outcome = "INCLUIDO"
    elif c["duplicidade"] == "PRESENTE":
        if c["tentativa"] != "NAO_INICIADA":
            return block("Documento existente e tentativa divergem; reconciliar historico.")
        outcome = "JA_EXISTENTE"
    elif c["tentativa"] == "SEM_EFEITO_COMPROVADO":
        if not has("ausencia_de_efeito") or c.get("numero_documento_sei") is not None:
            return block("Ausencia de efeito sem evidencia ou contradita por numero de documento.")
        outcome = "FALHA_SEM_EFEITO"

    if outcome in {"INCLUIDO", "JA_EXISTENTE"}:
        doc = c.get("numero_documento_sei")
        if not isinstance(doc, str) or not re.fullmatch(r"\d+", doc):
            return block("Numero SEI de documento ainda nao confirmado.")
        if not c["leitura_posterior_conferida"] or not has("registro_documento", "conteudo_pos"):
            return block("Falta leitura do registro e conteudo efetivamente armazenado.")
        if outcome == "JA_EXISTENTE" and not has("duplicidade"):
            return block("Equivalencia de documento existente sem evidencia.")

    if outcome:
        if initial == "ABERTO":
            if current != "ABERTO":
                return result("PENDENCIA_MESA", "Processo inicialmente aberto mudou; nao reabrir por suposicao.")
            return result("FINALIZAR_" + outcome, "Preservar a mesa aberta; nao concluir.")
        if current == "CONCLUIDO":
            return result("FINALIZAR_" + outcome, "Mesa concluida confirmada; nao atribuir ato de terceiro ao agente.")
        if not c["reaberto_nesta_execucao"]:
            return result("PENDENCIA_MESA", "Abertura nao atribuida a esta execucao; nao concluir trabalho alheio.")
        if not c["autorizacao_restaurar_mesa"]:
            return block("Restauracao nao autorizada; relatar mesa pendente.")
        if c["intervencao_externa"] != "NAO_DETECTADA" or not has("concorrencia"):
            return result("PENDENCIA_MESA", "Intervencao externa detectada ou nao esclarecida; nao concluir.")
        return result("CONCLUIR_NA_UNIDADE", "Restaurar somente a unidade que esta execucao reabriu; conferir depois.")

    if c["leitura_posterior_conferida"] or c.get("numero_documento_sei") is not None:
        return block("Registro posterior sem resultado reconciliado; nao iniciar outro envio.")
    if c["duplicidade"] != "AUSENTE" or not has("duplicidade"):
        return block("Ausencia de duplicidade nao demonstrada.")
    if not c["metadados_confirmados"] or not c.get("metadados") or not has("metadados"):
        return block("Tipo, data, descricao, formato e acesso nao fundamentados.")
    if c["intervencao_externa"] != "NAO_DETECTADA" or not has("concorrencia"):
        return block("Concorrencia nao esclarecida antes de mutacao.")
    if initial == "CONCLUIDO":
        if not c["autorizacao_restaurar_mesa"]:
            return block("Falta autorizacao do ciclo reabrir/incluir/concluir.")
        if current == "CONCLUIDO":
            if c["reaberto_nesta_execucao"]:
                return block("Mesa mudou apos reabertura; investigar antes de repetir o ciclo.")
            return result("REABRIR_NA_UNIDADE", "Envio preparado; reabrir somente a unidade-alvo e confirmar.")
        if not c["reaberto_nesta_execucao"]:
            return block("Abertura por outra intervencao; nao assumir controle do processo.")
    elif current != "ABERTO":
        return block("Estado da mesa mudou desde o inicio; nao alterar para forcar inclusao.")
    return result("INCLUIR_PDF", "Precondicoes declaradas completas; registrar tentativa antes de persistir e conferir depois.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("controle", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.controle.read_text(encoding="utf-8-sig"))
        output = decide(data)
    except (OSError, ValueError) as exc:
        output = {"etapa": "BLOQUEADO", "motivo": str(exc), "executa_acao": False}
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 2 if output["etapa"] == "BLOQUEADO" else 0


if __name__ == "__main__":
    raise SystemExit(main())

````


---

<a id="recurso-06"></a>

## Recurso incorporado: skills/incluir-consulta-sei/scripts/fila_local.py

````python
"""Diario transacional LOCAL por NUP/PDF. Nao controla navegador nem acessa rede.

Impede reservas repetidas neste banco. A ferramenta de UI nao fica tecnicamente
bloqueada; todos os executores devem usar o mesmo banco e respeitar o controle.
Nenhum estado local comprova sozinho a verdade das evidencias institucionais.
"""
import argparse
import hashlib
import json
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from decidir_etapa import decide


def digest(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def connect(path):
    db = sqlite3.connect(path, timeout=10)
    db.row_factory = sqlite3.Row
    db.executescript('''
        CREATE TABLE IF NOT EXISTS itens(
          chave TEXT PRIMARY KEY, nup TEXT NOT NULL, placa TEXT NOT NULL,
          arquivo TEXT NOT NULL, sha256 TEXT NOT NULL, estado TEXT NOT NULL,
          documento TEXT, UNIQUE(nup,sha256));
        CREATE TABLE IF NOT EXISTS eventos(
          id INTEGER PRIMARY KEY, instante TEXT NOT NULL, chave TEXT NOT NULL,
          estado TEXT NOT NULL, evidencia TEXT NOT NULL);
    ''')
    return db


def event(db, key, state, evidence):
    if not isinstance(evidence, str) or not evidence.strip():
        raise ValueError('Referencia de evidencia obrigatoria.')
    db.execute('INSERT INTO eventos(instante,chave,estado,evidencia) VALUES(?,?,?,?)',
               (datetime.now(timezone.utc).isoformat(), key, state, evidence))


def prepare(db, items):
    """Valida todo o lote antes de inserir. Repeticoes identicas nao duplicam fila."""
    validated = []
    for item in items:
        nup, plate = item['nup'], item['placa']
        if not re.fullmatch(r'\d{5}\.\d{6}/\d{4}-\d{2}', nup):
            raise ValueError('NUP invalido.')
        if not re.fullmatch(r'[A-Z]{3}\d[A-Z0-9]\d{2}', plate):
            raise ValueError('Placa invalida.')
        path = Path(item['arquivo']).resolve(strict=True)
        with path.open('rb') as stream:
            if stream.read(5) != b'%PDF-':
                raise ValueError('Arquivo sem cabecalho PDF.')
        sha = digest(path)
        if item.get('sha256', sha).lower() != sha:
            raise ValueError('Arquivo diverge do hash esperado.')
        key = hashlib.sha256((nup+'|'+sha).encode()).hexdigest()
        validated.append((key, nup, plate, str(path), sha))
    with db:
        db.execute('BEGIN IMMEDIATE')
        for key, nup, plate, path, sha in validated:
            conflict = db.execute('SELECT placa,nup FROM itens WHERE sha256=? OR nup=?', (sha,nup)).fetchall()
            if any(row['placa'] != plate or row['nup'] != nup for row in conflict):
                raise ValueError('Associacao conflitante de PDF, placa ou NUP.')
            cur = db.execute('INSERT OR IGNORE INTO itens VALUES(?,?,?,?,?,?,NULL)',
                             (key,nup,plate,path,sha,'PREPARADO'))
            if cur.rowcount:
                event(db,key,'PREPARADO','Integridade local; identidade no SEI ainda nao atestada.')
    return [row[0] for row in validated]


def reserve(db, key, control):
    """Grava antes do upload. Sem expiracao automatica: queda exige reconciliacao."""
    with db:
        db.execute('BEGIN IMMEDIATE')
        row = db.execute('SELECT * FROM itens WHERE chave=?',(key,)).fetchone()
        if row is None or row['estado'] != 'PREPARADO':
            raise ValueError('Item ausente, reservado ou ja encerrado; reconciliar antes de repetir.')
        if any(control.get(k) != row[v] for k,v in [('nup','nup'),('placa','placa'),('arquivo_sha256','sha256')]):
            raise ValueError('Controle pertence a outro item.')
        if digest(row['arquivo']) != row['sha256']:
            raise ValueError('PDF alterado desde a preparacao.')
        decision = decide(control)
        if decision['etapa'] != 'INCLUIR_PDF':
            raise ValueError('Precondicoes nao satisfeitas: '+decision['etapa'])
        if db.execute("SELECT 1 FROM itens WHERE nup=? AND estado IN ('INICIADA','INCERTA')",(row['nup'],)).fetchone():
            raise ValueError('Outra tentativa nao reconciliada no processo.')
        db.execute("UPDATE itens SET estado='INICIADA' WHERE chave=?",(key,))
        event(db,key,'INICIADA',json.dumps(control,ensure_ascii=False))


def reconcile(db, key, state, evidence, document=None, downloaded=None):
    if state not in {'INCERTA','SEM_EFEITO','INCLUIDO','JA_EXISTENTE'}:
        raise ValueError('Estado de reconciliacao invalido.')
    with db:
        db.execute('BEGIN IMMEDIATE')
        row = db.execute('SELECT * FROM itens WHERE chave=?',(key,)).fetchone()
        if row is None:
            raise ValueError('Item inexistente.')
        allowed = {'PREPARADO'} if state == 'JA_EXISTENTE' else {'INICIADA','INCERTA'}
        if row['estado'] not in allowed:
            raise ValueError('Transicao invalida; resultado final preservado.')
        if state in {'INCLUIDO','JA_EXISTENTE'}:
            if not isinstance(document,str) or not re.fullmatch(r'\d+',document):
                raise ValueError('Numero SEI real obrigatorio.')
            if not downloaded or digest(downloaded) != row['sha256']:
                raise ValueError('Readback binario divergente/ausente; manter pendente para analise.')
        elif document is not None:
            raise ValueError('Numero de documento contradiz resultado informado.')
        event(db,key,state,evidence)
        db.execute('UPDATE itens SET estado=?,documento=? WHERE chave=?',(state,document,key))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('banco',type=Path)
    sub = parser.add_subparsers(dest='acao',required=True)
    p = sub.add_parser('preparar'); p.add_argument('manifesto',type=Path)
    p = sub.add_parser('reservar'); p.add_argument('chave'); p.add_argument('controle',type=Path)
    p = sub.add_parser('registrar'); p.add_argument('chave'); p.add_argument('estado'); p.add_argument('evidencia'); p.add_argument('--documento'); p.add_argument('--arquivo-baixado')
    sub.add_parser('listar')
    args = parser.parse_args()
    try:
        with connect(args.banco) as db:
            if args.acao == 'preparar':
                result = prepare(db,json.loads(args.manifesto.read_text(encoding='utf-8-sig')))
            elif args.acao == 'reservar':
                reserve(db,args.chave,json.loads(args.controle.read_text(encoding='utf-8-sig'))); result={'estado':'INICIADA'}
            elif args.acao == 'registrar':
                reconcile(db,args.chave,args.estado,args.evidencia,args.documento,args.arquivo_baixado); result={'estado':args.estado}
            else:
                result=[dict(r) for r in db.execute('SELECT * FROM itens ORDER BY nup')]
        print(json.dumps(result,ensure_ascii=False,indent=2))
    except (ValueError, OSError, KeyError, TypeError, sqlite3.Error) as exc:
        print(json.dumps({'erro':str(exc),'executa_sei':False},ensure_ascii=False)); return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

````
