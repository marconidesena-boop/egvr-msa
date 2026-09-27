---
name: incluir-consulta-sei
description: Preparar e executar inclusões expressamente autorizadas de PDFs de consultas veiculares em processos individuais do SEI, com conferência de vínculo, duplicidade, leitura posterior e restauração do estado da mesa. Usar em pedidos de anexar ou inserir consulta no SEI. Não usar para assinar, tramitar, gerar ofícios, analisar recebimentos ou desvincular multas. Fluxo candidato a piloto; depende de ferramenta externa disponível.
---

# Inclusão de consultas no SEI — EGVR MSA

Esta skill acrescenta um fluxo de inclusão ao plugin; não fornece conector, credenciais ou acesso institucional próprio. Sua instalação não autoriza uma inclusão. Em 26/09/2026 foi concluído um piloto real no perfil SEI PRF 4.1.5/SEI Pro via Computer Use: inclusão, download idêntico ao original e restauração da mesa. Isso não homologa outros ambientes nem libera automaticamente os demais envios. Não confunda testes locais com operações reais.

## Escopo e autorização

- Diferencie configurar o plugin, preparar o envio, consultar um processo e efetivamente incluir o PDF. Pedido de configuração ou preparação não autoriza navegar no SEI nem enviar arquivo. Pedido só de consulta autoriza apenas leitura.
- Para executar, identifique a autorização do usuário para os arquivos/consultas e processos do piloto ou lote. Dados já fornecidos podem resolver o escopo; peça apenas informação material ausente. Uma autorização clara cobre os passos normais desse fluxo, sem pedir aprovação por campo ou documento, respeitando confirmações obrigatórias da plataforma.
- A regra de mesa aprovada pelo usuário é: se concluído na unidade-alvo, reabrir antes da inclusão e concluir novamente após confirmar o documento; se já aberto, preservar aberto. A regra vale dentro de uma inclusão autorizada, nunca para encerrar outros trabalhos, outras unidades ou processos não incluídos no pedido.
- Não assine, autentique documento, envie, tramite, crie processo, exclua/substitua documento, altere acesso preexistente, edite planilha ou produza comunicação institucional. Não obtenha consultas novas no DETRAN. Essas operações exigem outro escopo.
- Se o usuário mandar parar, interrompa imediatamente; não execute nem uma conclusão de processo como “limpeza”. Informe a situação conhecida e qualquer restauração pendente.

## Execução

Antes de qualquer operação institucional, leia integralmente [Fluxo e evidências](references/fluxo-e-evidencias.md). Use as instruções da ferramenta efetivamente disponível para navegador/computador, PDFs ou planilha. Não presuma APIs, seletores, credenciais, unidade ou botões. Não instale recurso nem crie integração para contornar limitação sem pedido próprio.

No SEI PRF/SEI Pro, leia antes da primeira interação o [perfil observado](references/perfil-sei-prf.md). Use a rota comprovada e o ciclo enxuto ali descrito; não repita a investigação completa do piloto em cada item. Refaça a inspeção detalhada somente diante de mudança de estrutura, identidade ambígua ou erro.

1. Registre o escopo e o estado no [controle externo](templates/controle-inclusao.json), fora do plugin distribuído, da planilha e do SEI. Preencha por item; não imponha ao usuário um manifesto técnico. Não grave senhas, cookies ou URLs com tokens.
2. Confirme acesso ao arquivo, conteúdo integral, origem/data, placa e identificador corroborante disponível. Calcule SHA-256; preserve o arquivo original. Não escolha o PDF só pelo nome.
3. Localize o NUP individual na origem indicada e confirme no SEI o vínculo com o mesmo veículo. Não confunda NUP, processo judicial, número SEI de documento ou ID interno. Uma linha ou processo citado em conversa não dispensa conferência atual.
4. Capture o estado inicial na unidade-alvo e os documentos pertinentes, incluindo pastas/páginas da árvore. Investigue duplicidade por conteúdo, data e identidade, mesmo sob outro título. Um PDF contendo várias restrições é um documento, não um envio por linha de planilha.
5. Confirme tipo documental, data do documento, nome/descrição, formato e acesso conforme contexto comprovado. Faça segunda conferência do conjunto arquivo–veículo–NUP–unidade–metadados. Se informação obrigatória não puder ser fundamentada, preserve e relate a pendência.
6. Só quando o envio estiver pronto, reabra o processo se inicialmente concluído na unidade autorizada; confira o resultado. Não reabra outra unidade nem conclua um processo inicialmente aberto.
7. Antes de qualquer ação que possa persistir arquivo/documento, registre tentativa iniciada. Envie e salve uma única vez. Releia árvore, número SEI, metadados e arquivo efetivamente armazenado. Mensagem “salvo” isolada não comprova inclusão correta.
8. Se inicialmente concluído e reaberto por esta execução, verifique ausência de intervenção externa e conclua somente na mesma unidade após confirmar o documento. Confira a conclusão. Se inicialmente aberto, confirme que permaneceu aberto.
9. Relate NUP, placa, arquivo/data, resultado, número SEI confirmado, duplicidades evitadas, estado inicial/final da mesa e pendências. Separe “documento incluído” de “mesa restaurada”. Não coloque o relatório dentro do processo ou da planilha.

## Resultado incerto, retomada e controle local

Para SEI PRF com SEI Pro, leia [Perfil observado](references/perfil-sei-prf.md), especialmente recarga dos formulários, upload e diferença entre lotes por processo e distribuição dos mesmos arquivos. Não aplique seletores sem conferir a página atual.

Para lotes autorizados ou retomadas, use a [fila local transacional](references/fila-local.md) além do controle por item. Ela conserva tentativas, detecta arquivo alterado e impede reservas repetidas no mesmo banco; não é um conector nem um bloqueio técnico da interface do SEI.

Timeout, interrupção após possível escrita, sessão expirada depois do envio ou readback incompleto exigem reconciliação somente leitura antes de qualquer repetição ou conclusão. Não interprete tela vazia como ausência de documento. Preserve o registro da tentativa; reconsulte a árvore/conteúdo e resolva o efeito, sem novo envio às cegas.

O auxiliar [decidir_etapa.py](scripts/decidir_etapa.py) lê o controle local e aponta uma próxima etapa ou impedimento. Ele não acessa o SEI, não executa ações e não comprova a veracidade das evidências declaradas. Use-o como checagem adicional antes de uma mutação e após sua confirmação, nunca como autorização ou substituto da conferência da fonte.

Execute com um Python já disponível: `python scripts/decidir_etapa.py caminho-do-controle.json`. Campos vazios/desconhecidos devem bloquear o avanço pertinente. Detalhes de evidência e retomada ficam na referência principal; [testes locais](evals/test_decidir_etapa.py) exercitam somente as decisões do auxiliar.

## Fronteira de validação

O primeiro uso real deve ser um piloto expressamente solicitado, limitado a um PDF e um processo, com verificação antes/depois. A configuração deste módulo não executa esse piloto. Registre ferramenta, caso e resultados reais antes de qualificar o perfil. Um sucesso não libera automaticamente escala, outro ambiente ou outras operações. Veja [cenários do piloto](evals/cenarios-piloto.md).
