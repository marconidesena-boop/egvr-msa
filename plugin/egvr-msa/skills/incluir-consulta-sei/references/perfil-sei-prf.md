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
