# Capacidades e dependências

## Atualização 0.2.1 — 26/09/2026

- Planilha original: piloto real concluído por UI do Chrome, com leitura independente pelo conector; nove correções e nove registros de histórico, todas as 18 células vermelhas e nenhum outro valor alterado na aba comparada. Isso não libera alterações ambíguas nem outras planilhas.
- Fila SQLite local: implementada, sem rede, com reserva transacional, hash do arquivo, prevenção de tentativa repetida e readback binário para finalização. 11 testes novos, 43 testes do módulo SEI aprovados no total. Não controla o navegador nem valida a veracidade de evidência declarada.
- SEI PRF: navegação, inventário, download de PDF, reabertura e restauração da conclusão observados em uso real. Inclusão bloqueada pela permissão de arquivos locais da extensão; zero documentos novos no teste. Upload, salvamento de documento e exclusão continuam sem validação real.
- Agente de IA SEI Pro: documentação analisada; painel lateral não acessível pela ferramenta desta sessão. Nenhum benchmark de qualidade/custo executado.
- Escala: não qualificada. Meta de campanha não equivale a autorização para incluir documentos de veículos sem vínculo individual comprovado.

A tabela abaixo conserva a avaliação histórica da base 0.1.1; o estado atual das capacidades alteradas é o descrito acima.

| Capacidade | Perfil e operação | Ambiente | Versão | Maturidade e evidência | Limite e próximo requisito |
|---|---|---|---|---|---|
| Estrutura portátil e skill | Pacote | Validadores locais/schema | 0.1.1 | IMPLEMENTADA; TESTADA estruturalmente | Instalação local não implica comportamento de edição |
| Decisões documentais | DETRAN-BA, outros DETRANs, SERPRO; análise/proposta | Simulações textuais | 0.1.1 | TESTADA no alcance dos casos T e AD; ver RESULTADOS-TESTES | Qualificar variante real da consulta e leitura visual |
| Autorização, correspondência, revisão e quarentena | Núcleo comum | Instruções e cenários sintéticos | 0.1.1 | IMPLEMENTADA; TESTADA textualmente | Não é homologação de um lote real |
| Atualizar planilha existente | Valores alterados em vermelho, linha-base O/P e preservação | Ferramenta externa ainda não selecionada | 0.1.1 | Instruções IMPLEMENTADAS; 17 testes de ferramenta pertinentes sem execução | Pilotar com antes/depois, propriedades e readback verificáveis |
| Criar planilha por modelo | Reprodução estrita e dados iniciais pretos | Ferramenta externa/modelo do usuário | 0.1.1 | Instruções IMPLEMENTADAS; decisão textual exercitada | Testar cópia, estilos, fórmulas, validações e continuidade do modo |
| Normalização judicial | Tribunal e Vara | Pesquisa oficial contextual | 0.1.1 | Procedimento TESTADO em fixture sintética | Nenhuma equivalência real homologada; pesquisar por caso |
| Ferramentas e melhorias | Diagnóstico e proposta | Recursos disponíveis a cada execução | 0.1.1 | IMPLEMENTADA como instrução; AD08/AD09 textuais | Nenhuma instalação ou autoedição persistente automática |
| SEI, recebimentos e instrução de multas | Processos individuais e inclusão futura | Nenhuma integração | 0.1.1 | ESPECIFICADA | Nova tarefa autorizada, implementação e testes próprios |

Evidência detalhada e resultados estão em [Resultados dos testes](RESULTADOS-TESTES.md); critérios de maturidade em [R22](skills/conciliar-restricoes/references/estados-de-maturidade.md). Não há capacidade classificada como VALIDADA ou APTA PARA ESCALA nesta entrega.
