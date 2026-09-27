# Capacidades SEI ainda futuras e limite do módulo de inclusão

Este detalhamento integra R19 em [Escopo e evolução](escopo-e-evolucao.md). Desde 0.2.0, a inclusão delimitada de PDFs tem fluxo próprio em [incluir-consulta-sei](../../incluir-consulta-sei/SKILL.md), candidato a piloto dependente de ferramenta externa e pedido específico. Esta referência não concede autorização e não deve bloquear nem duplicar as regras desse fluxo. As demais capacidades abaixo permanecem ESPECIFICADAS, sem integração ou execução habilitada.

## Casos desejados

- Confrontar documentos de processo com os registros da planilha: número do documento que comprova recebimento, data do recebimento e status compatível com seu conteúdo.
- Examinar instrução de processos destinados à desvinculação de multas; separar fatos do processo, pendências documentais e exigências normativas oficialmente verificadas.
- Ampliar a inclusão para outras espécies ou operações não abrangidas pelo fluxo de consultas, mediante tarefa própria; nunca por rótulos presumidos.

## Condições para futura implementação

1. Definir autorização específica por lote e operação, acesso institucional adequado e separação entre leitura e escrita.
2. Demonstrar correspondência veículo–processo individual. Separar NUP, número de documento SEI e IDs internos. Não criar processo porque um índice esteja incompleto.
3. Ler o conteúdo integral pertinente; emissão ou inclusão de um documento não prova recebimento. Cada data e ato precisam da fonte específica, com página/seção e vínculo à restrição.
4. Elaborar matriz documental da instrução exigida, vinculada a fontes oficiais vigentes. CTB art. 328 e a resolução citada no anexo precisam de pesquisa própria; não presumir conteúdo, existência ou vigência pela citação.
5. Para inclusão, confirmar arquivo, integridade, processo, tipo e descrição; verificar documentos duplicados e equivalentes mesmo com nomes/arquivos diferentes.
6. Salvar somente dentro do escopo. Reabrir a árvore documental, conferir conteúdo e registrar o número efetivamente incluído.
7. Tratar sessão expirada antes de tentativa como falha de acesso. Se houver timeout ou sessão interrompida após possível escrita, classificar o efeito como incerto; consultar o estado real antes de repetir e não simular sucesso.
8. Separar autorizações para assinar, enviar, tramitar, criar processos; excluir, substituir ou remover documentos; colocar em bloco de assinatura; gerar ofício em nome do usuário ou enviar comunicação externa. A única exceção delimitada de mesa é reabrir/concluir para restaurar o estado inicial dentro de inclusão autorizada, conforme a skill própria. Ela não autoriza concluir processo inicialmente aberto nem outras unidades.

Os testes SF01–SF05 preservam a especificação/histórico original não executado nos [Casos de regressão](../evals/casos-de-regressao.md). A extensão 0.2.0 tem catálogo próprio SI; não opere o sistema para encerrar uma tarefa de configuração. Um piloto real exige solicitação específica. Multas e débitos não determinam status de restrição judicial.
