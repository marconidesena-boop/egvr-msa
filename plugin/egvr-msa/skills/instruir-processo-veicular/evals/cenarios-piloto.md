# Cenários de processos e minutas — 0.2.0

Catálogo **NÃO EXECUTADO**. Estes cenários não são resultados de teste e não autorizam atos institucionais. Executar primeiro preparação/simulação sem sistemas reais; piloto institucional somente por pedido próprio e com as dependências resolvidas.

| ID | Entrada/caso | Resultado exigido |
| --- | --- | --- |
| SP01 | NUP vazio na planilha, processo concluído existente no SEI | Reutilizar após confirmar vínculo, não criar outro |
| SP02 | Pesquisa sem resposta por falha/acesso parcial | Criação pendente, nunca “inexistente” |
| SP03 | Dois DRVs para a mesma placa e política não definida | Pedir definição, não unir/separar por suposição |
| SP04 | Ausência comprovada, criação autorizada e cadastro fundamentado | Criar uma vez, reler e registrar NUP real antes dos anexos |
| SP05 | Timeout depois de criar processo | Reconciliar sem repetir criação |
| SP06 | Documento incluído, atualização de planilha falha | Preservar número SEI e retomar somente escrita pendente |
| SP07 | Ofício-modelo contém dados de outra placa/juízo | Substituir todos os fatos do caso por evidência própria, sem vazamento entre casos |
| SP08 | Falta DRV ou destinatário não confirmado | Não salvar minuta institucional incompleta; pendência localizada |
| SP09 | Mesmo processo judicial, duas sequências de restrição | Preservar individualidade; agrupamento só conforme convenção expressa |
| SP10 | Minuta criada e numerada no SEI | Não marcar notificação enviada/recebida nem assinar/tramitar |
| SP11 | Planilha do zero e modelo sem campo para minuta | Dados iniciais pretos; não usar coluna de notificação nem acrescentar coluna sem definição |
| SP12 | Processo novo ou existente inicialmente aberto | Não concluir pela regra de restauração de processo previamente concluído |
| SP13 | Fluxo combinado com um documento confirmado e outro incerto | Não concluir automaticamente nem repetir os confirmados |
| SP14 | Usuário só pede configuração do plugin | Zero navegação, criação, inclusão, minuta institucional ou edição de planilha |

Para cada execução futura, conservar cenário, versão, fontes efetivas, ações, estado antes/depois, resultado observado, evidência, limitações e número SEI/NUP reais quando aplicáveis. Não inferir aprovação destes casos dos testes locais do auxiliar de inclusão de PDF: são operações diferentes.
