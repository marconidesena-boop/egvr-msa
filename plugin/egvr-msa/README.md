# EGVR MSA

Versão 0.1.1, instalada localmente para revisão e testes controlados. Plugin de instruções para conferir documentos veiculares e conciliar restrições judiciais com planilhas. Foi construído do zero a partir do documento fornecido. Não reutiliza código nem depende de pacotes EGVR anteriores. O único código incluído serve à validação estrutural do pacote, sem integração operacional.

O pacote contém uma skill principal, regras por assunto, modelos de controle externo, exemplos sintéticos e avaliações. A skill orienta um agente que já disponha das ferramentas necessárias. Ela não fornece um editor de planilhas nem acesso próprio a sistemas.

## Como começar

1. Revise [Limitações e decisões](LIMITACOES-E-DECISOES.md), [Matriz dos requisitos](MATRIZ-RASTREABILIDADE.md) e [Resultado dos testes](RESULTADOS-TESTES.md).
2. Para uma avaliação local sem instalação, peça ao agente: “Leia skills/conciliar-restricoes/SKILL.md deste pacote e aplique suas referências a um teste sintético, sem operar sistemas institucionais”.
3. Indique a pasta ou anexe os documentos; informe o arquivo, a aba, o lote e os campos. O agente inventaria o material e pede apenas dados essenciais ainda ausentes.
4. Comece por auditoria ou proposta de mudanças. A edição em produção depende da qualificação do perfil e de uma ferramenta cuja preservação tenha sido verificada. Um teste controlado pode usar arquivos sintéticos ou cópias autorizadas.

Exemplos de pedidos:

- “Audite estes PDFs e a aba indicada. Não escreva. Mostre fonte, linha e pendências.”
- “Em teste controlado nesta cópia, atualize somente STATUS e OBSERVAÇÕES das linhas existentes do lote indicado. Preserve os demais campos e não acrescente linhas.”
- “Crie uma nova planilha neste destino separado, usando este modelo estritamente e somente as restrições comprovadas. O objetivo é situação atual.”

Ao autorizar um lote, os casos confirmados seguem sem pedidos repetitivos por célula. Dúvidas localizadas ficam preservadas. A operação inteira só fica bloqueada quando o problema afeta sua base, como arquivo errado ou mapeamento inválido.

## Dependências por tarefa

| Tarefa | Recurso necessário | Condição de uso |
|---|---|---|
| Ler arquivos | Acesso autorizado ao local ou anexos | Abrir e confirmar os arquivos efetivamente lidos |
| Conferir PDF/imagem | Extração e visualização; OCR quando necessário | Verificar campos decisivos no original se ambíguos |
| Editar arquivo de planilha | Ferramenta que preserve a estrutura encontrada | Conferir antes/depois; não converter formatos com perda |
| Editar Google Sheets | Conector ou sessão autorizada com leitura/escrita precisa | Confirmar permissão e ler novamente o intervalo |
| Normalizar unidade | Pesquisa em fonte judicial oficial | Comprovar equivalência no contexto |
| Revisar pacote | Python, PyYAML e jsonschema | Recursos só de desenvolvimento; não são integração operacional |

No ambiente da construção foram identificadas skills de PDF, planilhas, Google Drive/Sheets e uso do computador. Não foram vinculadas como integrações do pacote e sua disponibilidade não comprova acesso ao destino de um trabalho. Escolha apenas a ferramenta necessária no momento; verifique permissões e fidelidade. Falha de um recurso bloqueia somente a operação dependente.

## Entrega e uso posterior

O plugin está instalado no marketplace pessoal local por autorização posterior do usuário; isso não é publicação, criação hospedada nem homologação operacional. Não existe plugin_id ou release_id hospedado para esta entrega.

Atualizações futuras exigem tarefa expressa, controle de versão, cachebuster e reinstalação local. Criação hospedada ou publicação continuam fora do escopo e só poderão ocorrer por pedido separado.

Consulte [Capacidades](CAPACIDADES.md) para maturidade e dependências; [Empacotamento](EMPACOTAMENTO.md) para formato e verificação; [Inventário](INVENTARIO.md) para arquivos e [CHANGELOG](CHANGELOG.md) para histórico.
