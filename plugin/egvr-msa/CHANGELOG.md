# Histórico de versões

## Atualização local de 26/09/2026 — piloto SEI confirmado

- Inclusão real e restauração da mesa comprovadas no perfil SEI PRF 4.1.5/SEI Pro, usando Computer Use e controle local: um documento, arquivo baixado idêntico por SHA-256, nenhuma extensão da autorização aos demais itens.
- Mapeados frames aninhados, forms separados de metadados/upload, labels de rádio, dois botões Salvar e seletor único da barra inferior.
- Documentada recuperação após permissão de arquivos e reconexão da extensão, preservando aba/formulário/tentativa; proibido resetar histórico para forçar repetição.
- Registrado ciclo enxuto por item: conferência inicial, inclusão e conferência final; inspeção extensa apenas diante de erro ou mudança concreta.
- 43 testes locais do módulo aprovados novamente. Esses testes verificam controle local; o piloto real tem evidências externas próprias. Escala e outros perfis continuam sem homologação.

## 0.2.1 — 26/09/2026 — Rastreabilidade e fila SEI

- Harmonizados os manifestos e corrigidos prompts que sugeriam cópia sem considerar o destino autorizado.
- Documentado perfil real SEI PRF/SEI Pro: recarga do formulário após tipo, rótulo do upload, permissão local, distinção entre distribuição em massa e vínculo um a um.
- Implementada fila local SQLite com integridade, reserva transacional e reconciliação sem repetição automática.
- Adicionados 11 testes locais; 43 testes do módulo SEI aprovados.
- Registrada preferência por edição na original quando determinada, vermelho e histórico acrescentado sem apagar observações humanas.
- Escrita de planilha exercitada em piloto real; upload SEI bloqueado antes da anexação. Sem declaração de aptidão para escala.

## 0.1.1 — 25/09/2026 — Correção de linha-base e observações

- Autorização expressa do usuário para atualizar a instalação local.
- Linha-base de veículo em planilha existente passa a registrar ausência comprovada de restrição judicial ativa em O/P, sem criação de linha, exclusão ou apagamento de históricos.
- Mantida a proibição de criar linha judicial fictícia no modo de criação quando o modelo não prevê linha-base ou campo próprio.
- Consolidado o vocabulário canônico da coluna O: nova inserção, inserção, baixa e ausência de restrição judicial ativa.
- Reforçada a separação entre data de inserção/baixa e datas de consulta, emissão, leitura, constatação ou alteração da planilha.
- Acrescentados T49–T55 e uma rodada textual específica; testes de ferramenta continuam não executados.
- Instalação local não foi promovida a VALIDADA nem APTA PARA ESCALA; SEI permanece apenas especificado.

## 0.1.0 — 25/09/2026 — Candidata local

- Criada base independente a partir de PLUGIN.docx, com nome EGVR MSA conforme pedido direto.
- Estruturados núcleo, perfis documentais, modos de planilha, preservação, duas passagens, auditoria e quarentena.
- Acrescentados modelos externos, exemplos sintéticos e catálogo de avaliações.
- Registrados conflitos de nome, SEI, zeros, melhoria de ferramentas e publicação.
- Preparados manifesto portátil e compatibilidade Codex coerentes; sem integração operacional.
- Resultados executados e pendentes separados em RESULTADOS-TESTES.md. Nenhuma capacidade de produção declarada validada.
- Revisão candidata: corrigidos quatro pontos de clareza da auditoria; R12 reforçada após B02 reprovado por propor linha sem campos identificadores autorizados. Acrescentada regressão AD11 com variantes restrita e completa; primeira falha preservada no histórico.
