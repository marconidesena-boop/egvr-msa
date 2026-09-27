# Limitações e decisões de projeto

## Decisões desta candidata

| ID | Questão do anexo | Tratamento |
|---|---|---|
| D01 | Nome EGVR TURBO no título e seção 24; EGVR MSA no pedido e abertura | EGVR MSA, nome técnico egvr-msa; pedido direto prevalece |
| D02 | A seção 19 original reservava todas as operações SEI para o futuro | Pedido posterior de 26/09/2026 autoriza acrescentar fluxo de inclusão de consultas ao plugin e regra de reabrir/concluir restaurando a mesa. 0.2.0 acrescenta instruções e controle local, sem conector próprio ou piloto institucional executado. Demais atividades SEI continuam futuras. |
| D03 | Seção 10 menciona números com zeros a mais; seção 13 exige preservar dígitos | Comparação auxiliar de pontuação; diferença de dígitos/zeros gera candidato, exige prova independente; nunca alterar número por suposição |
| D04 | Autonomia para melhorar ferramentas; seções 2 e 20 vedam integração e alteração persistente não autorizadas | Descoberta, diagnóstico e proposta; instalação, autenticação e mudança de versão dependem de tarefa própria |
| D05 | Criar plugin e preparar catálogo, mas revisar antes de instalar/publicar | Candidata local e catálogo inativo; criação hospedada não executada |
| D06 | Manifesto portátil e compatibilidade Codex | Raiz Agent Plugins 1.0; overlay coerente para o validador local e clientes legados. Os manifestos não são mesclados |
| D07 | Uso do modelo sem extensão pedida | Reprodução estrita; modelo e origem intactos, arquivo separado |
| D08 | Regra geral do relato “frase equivalente” versus seção11 com status exato | SEM RESTRIÇÃO e NOVA RESTRIÇÃO (NOTIFICAR), sujeitos à validação; não escolher sinônimo para contornar lista |
| D09 | Linha-base existente sem restrição versus uma linha por restrição no novo destino | Em planilha existente, preservar a linha-base e preencher O/P quando a ausência estiver comprovada e autorizada; em criação sem linha-base prevista, não criar restrição fictícia |
| D10 | Padrão da coluna O versus risco de confundir datas | Usar as quatro frases canônicas somente com fatos comprovados; data de consulta/leitura/alteração não substitui inserção ou baixa |

## Lacunas materiais e fronteiras

- Não há modelo de planilha nem consultas reais nesta tarefa; layout, fórmulas, validações, dados e nomes reais não foram homologados.
- Não existe uma regra universal para todos os DETRANs. Cada formato requer prova de abrangência, semântica e testes aplicáveis. SERPRO também exige qualificação do documento concreto.
- Não há dicionário inicial de Varas: normalizações dependem de pesquisa contextual em fontes oficiais.
- Nenhuma habilidade de editar planilhas com preservação integral foi validada em operação real nesta construção. Casos textuais não verificam fidelidade de Excel ou Google Sheets.
- Não há serviço, MCP, hook, rotina em segundo plano, credencial ou autenticação própria no pacote. A descoberta de ferramentas não significa conexão ao serviço.
- O módulo `incluir-consulta-sei` é um fluxo de instruções com auxiliar local de decisão, não uma integração SEI autônoma. Depende da ferramenta e sessão disponíveis; seu primeiro uso real é piloto delimitado e solicitado. Configurar ou instalar não envia documento.
- A restauração da mesa só conclui, na mesma unidade, processo inicialmente concluído e reaberto pela execução, após confirmar inclusão ou ausência de efeito. Intervenção externa, resultado incerto e pedido de parada impedem restauração automática. Processo inicialmente aberto permanece aberto.
- CTB art. 328 e “Resolução CONTRAN 1025/2026” são referências mencionadas pelo anexo, não normas com teor e vigência certificados por esta construção. Não há conclusão jurídica incorporada. Para aplicar norma, consultar texto oficial vigente, data, alterações e âmbito; para jurisprudência, verificar STF/STJ/CNJ pertinentes e não extrapolar precedentes. Se não confirmado, usar “TEMA NÃO CONFIRMADO COM PRECISÃO NAS FONTES”. Em uma pergunta jurídica, verificar também eventual questão FGV e separar questão da banca de fonte normativa.
- A análise de recebimentos, datas, andamento e instrução de desvinculação de multas no SEI está apenas especificada. Não se deve apresentar isso como módulo funcional.

## Pontos para avaliação do usuário

O alcance limitado de D02 foi ampliado por pedido posterior; sua execução real e eventual escala continuam pendentes de evidência. D03 permanece inalterada: diferenças de zeros exigem prova. Confirmar o modelo real e o perfil documental no primeiro piloto; não converter hipótese em regra geral.

As decisões conservadoras acima registram conflitos do próprio anexo; não modificam silenciosamente a política do usuário. Uma instrução posterior expressa poderá ajustar o escopo por mudança versionada.
