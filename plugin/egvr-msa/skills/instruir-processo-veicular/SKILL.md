---
name: instruir-processo-veicular
description: Preparar ou executar, mediante pedido específico e ferramentas disponíveis, criação de processos individuais de veículos no SEI, inclusão dos documentos vinculados e registro dos números SEI na planilha; elaborar minutas de ofícios às unidades judiciais a partir de modelo fornecido, com veículo, restrição e DRV comprovados. Usar sobretudo em planilhas iniciadas do zero sem NUP informado. Não assina, envia ofícios, opera o SILVER nem desvincula multas. Módulo candidato a piloto, sem validação institucional.
---

# Processos individuais e minutas de ofícios — EGVR MSA

Este módulo coordena identificação, criação de processo, documentos, minuta e planilha. Não inclui conector próprio nem transforma instruções em capacidade já testada. Configurar o plugin não autoriza trabalhar no SEI. Antes de operar, diferencie pedido de preparação, de criação de processo, de inclusão, de minuta no SEI e de edição da planilha; só execute as etapas efetivamente autorizadas.

Leia [Vínculos e execução](references/vinculos-e-execucao.md) antes de uma proposta executável. Use o [controle por veículo e restrição](templates/controle-processo.json) para registrar fontes, decisões e efeitos fora do SEI/planilha. Os campos são preenchidos pelo agente com o material disponível; não imponha preparação técnica ao usuário.

## Operações suportadas como fluxo candidato

### Criar processo individual quando necessário

1. Identifique arquivo/aba/modelo, modo de criação ou atualização e colunas autorizadas. Na planilha do zero, preserve o modelo e escreva dados iniciais em preto. Em planilha já preenchida, alterações comprovadas seguem a convenção vermelha da skill de conciliação. Não trate uma célula vazia como planilha nova.
2. Inventarie os PDFs, DRVs e outros documentos fornecidos. Leia placa, chassi/RENAVAM, número e data do DRV e documentos associados. Não opere o SILVER nem gere um DRV; use o DRV fornecido ou peça o arquivo faltante.
3. Confirme a unidade de organização do processo: por veículo ou por recolhimento/DRV. Se uma placa tiver mais de um recolhimento e a regra ainda não estiver definida, não os reúna nem separe por suposição. O processo judicial não substitui o NUP individual do SEI.
4. Se não houver NUP informado, pesquise no SEI pelos identificadores e pelo contexto do recolhimento, incluindo processos concluídos acessíveis. Célula em branco e busca sem resposta não provam inexistência. Examine os candidatos e registre a cobertura; reutilize o processo correto quando confirmado. Múltiplos candidatos ou acesso parcial deixam a criação pendente.
5. Somente com ausência suficientemente comprovada e criação autorizada, confirme tipo de processo, especificação, unidade, interessados/assuntos obrigatórios e classificação de acesso segundo modelo/padrão institucional aplicável. Não invente fundamento legal, interessado, prioridade ou unidade. Registre tentativa antes de criar.
6. Crie uma única vez e releia NUP e metadados efetivos. Se houver timeout, pesquise/reconcilie o efeito antes de repetir. Não crie outro processo para contornar um estado incerto. Registre imediatamente o NUP confirmado no controle de retomada.
7. Para documentos, carregue [incluir-consulta-sei](../incluir-consulta-sei/SKILL.md). PDFs de consulta seguem sua verificação completa. DRV e outros anexos exigem tipo/formato/acesso próprios comprovados; não classifique todos como “Consulta”. Cada novo perfil documental precisa de piloto e readback próprios.
8. Grave NUP e números SEI dos documentos somente nos campos autorizados e semanticamente corretos da planilha, após confirmação no SEI. Releia as células. Falha de planilha não autoriza recriar processo/documento; retome apenas a atualização pendente.

### Preparar ofícios individualizados

1. Obtenha um ofício-modelo real indicado/aprovado pelo usuário e a finalidade do expediente. Leia estrutura, texto, destinatário, campos variáveis e anexos; não invente um modelo institucional nem copie fatos do caso usado como exemplo.
2. Monte uma ficha por vínculo veículo–recolhimento/DRV–restrição judicial individual, conforme fontes. Distinga sequência, processo judicial, tribunal, Vara, datas e situação atual na data da consulta. Mesmo processo judicial não torna duas restrições uma só.
3. Como padrão de preparação, mantenha um item por vínculo individual. Não agrupe várias restrições, placas ou DRVs em um ofício sem uma convenção expressa que permita essa consolidação. Se o modelo admitir agrupamento, ainda relacione cada restrição e a sua evidência, sem suprimir identidades.
4. Confira a unidade destinatária atual e a correspondência com a restrição; abreviações ou mudanças históricas exigem fonte oficial contextual, usando as regras da skill de conciliação. Não deduza competência atual só pelos dígitos do CNJ. Se necessário, pesquisar contatos em fonte oficial; não enviar comunicação.
5. Preencha apenas fatos comprovados: placa, chassi/RENAVAM, identificação do veículo, número/data do DRV, local/data do recolhimento e demais campos realmente exigidos pelo modelo; processo judicial, sequência, tribunal, Vara e situação da restrição. Campo indispensável não comprovado impede a criação da minuta institucional, mas não a análise dos outros casos.
6. Revise a minuta contra fontes e modelo em segunda passagem. Pesquise fundamento jurídico vigente quando o trabalho exigir conteúdo jurídico; texto de modelo não comprova vigência. Não mude silenciosamente o pedido institucional, acrescente acusações ou afirme baixa/recebimento sem prova.
7. Criar rascunho local não é salvar no SEI. Se salvar minuta no SEI estiver autorizado, confirme processo individual, espécie/modelo, destinatário, referências e corpo integral, salve sem assinatura/envio e capture o número SEI efetivo. Não fabrique número de ofício, data oficial ou assinatura. A numeração gerada pelo sistema não prova expedição.
8. Atualize as linhas correspondentes da planilha conforme seu modelo. Minuta salva não significa notificação enviada nem recebida: não preencher data de notificação, confirmação ou status dependente de expedição/recebimento só pela criação do ofício. Se não houver campo próprio para minuta, relate fora da planilha; não acrescente coluna sem autorização.

## Estado de mesa e limites

Para processo existente, preserve o estado inicial na unidade. Se concluído, a reabertura e restauração autorizadas seguem o fluxo de inclusão; no trabalho combinado com anexos e ofícios, só restaure após todas as etapas autorizadas no processo terem efeito conhecido e documentos conferidos. A regra de fechamento não autoriza assinar ou tramitar uma minuta.

Um processo recém-criado não tinha estado anterior “concluído”: não aplique a ele essa regra por analogia. Registre como novo e mantenha aberto, salvo política específica do usuário para sua conclusão. Informe o estado ao final.

Não inclua, exclua, substitua, assine, envie ou tramite documentos fora do pedido. Não mude o acesso de processo/documento existente. Não crie links públicos nem altere permissões da planilha. Não use o módulo para decidir destinação/leilão/desvinculação de multas ou para interpretar recebimento como fato sem evidência.

## Validação e entrega

O módulo ainda não foi exercitado no SEI. Modelos e parâmetros institucionais faltantes bloqueiam apenas a operação dependente. O primeiro uso real precisa ser pedido como piloto delimitado, com captura antes/depois; não executar um lote para “testar” o plugin.

No relatório, separe processos criados ou reutilizados, documentos incluídos ou existentes, minutas locais ou salvas no SEI, células efetivamente atualizadas, pendências, estados da mesa e resultados incertos. Para cada número SEI, identifique o documento e a restrição/veículo a que corresponde. Não apresente minuta como ofício expedido. Veja [cenários de aceitação](evals/cenarios-piloto.md).
