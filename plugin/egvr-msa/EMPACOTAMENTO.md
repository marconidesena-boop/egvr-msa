# Empacotamento e revisão da versão local

## R23 — Estrutura enxuta e rastreável

| Campo | Regra |
|---|---|
| Finalidade | Manter uma fonte principal por assunto e uma skill acionável |
| Condições | Construção ou atualização autorizada |
| Evidência | Documento de requisitos e matriz com destino/teste por seção e parágrafo |
| Permitido | Skill principal, referências, modelos externos, exemplos sintéticos e avaliações efetivas |
| Proibido | Pacote anterior como base, duplicação normativa concorrente, arquivos decorativos ou promessa sem capacidade |
| Lacuna | Registrar o requisito sem implementação e continuar partes independentes |
| Testes | E01–E08 estruturais e revisão crítica de cobertura |

## R24 — Manifestos e distribuição

| Campo | Regra |
|---|---|
| Finalidade | Pacote portátil com identidade consistente e privacidade |
| Condições | Empacotar versão candidata |
| Evidência | Documentação oficial consultada em 25/09/2026 e schemas/validadores |
| Permitido | plugin.json na raiz e skills/; overlay Codex coerente exigido pelo validador local; marketplace pessoal autorizado pelo usuário |
| Proibido | Campos de schemas misturados, caminhos externos, symlinks, segredos, MCP/app/hook fictício; publicar ou hospedar sem autorização específica |
| Lacuna | Informar validação indisponível ou falha; não inventar ID/link hospedado |
| Testes | E01–E08; T48 |

O manifesto portátil é canônico. A extensão com.openai fornece a apresentação; o overlay separado repete identidade/apresentação para compatibilidade, sem presumir mesclagem. A entrada pessoal usa Productivity, AVAILABLE e ON_INSTALL; isso não cria autenticação. A instalação local foi autorizada posteriormente pelo usuário e não equivale a publicação, hospedagem, validação operacional ou autorização para escrever em planilhas e sistemas institucionais.

## R25 — Entrega e parecer

| Campo | Regra |
|---|---|
| Finalidade | Entrega concreta, verificável e sem alegações excedentes |
| Condições | Final de construção/revisão |
| Evidência | Arquivos, ZIP, inventário, matriz, resultados observados e limitações |
| Permitido | Parecer APROVAR A BASE, APROVAR COM CORREÇÕES ou REPROVAR A BASE, delimitado à evidência |
| Proibido | Confundir arquivos existentes, teste estrutural, teste textual e validação operacional |
| Lacuna | Marcar NÃO EXECUTADO ou BLOQUEADO e explicar a dependência |
| Testes | E01–E08; T48 e revisão dos resultados |

## Fontes técnicas

- [OpenAI — Empacotamento de plugins](https://developers.openai.com/plugins/build/plugins).
- [OpenAI — Construção de skills](https://developers.openai.com/plugins/build/skills).
- [Schema Agent Plugins 1.0](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json).

O script de desenvolvimento [validar_pacote.py](skills/conciliar-restricoes/evals/validar_pacote.py) verifica estrutura, schema, consistência, caminhos e rastreabilidade. Seus resultados não comprovam edição de planilhas nem acesso institucional. A partir da raiz do pacote, com Python, jsonschema e PyYAML disponíveis, execute:

```text
python skills/conciliar-restricoes/evals/validar_pacote.py . --out resultado-estrutural.json
```

O script usa a cópia do schema em schemas/plugin.schema.json, relativa ao próprio diretório de avaliação; não recebe argumento de schema. O relatório pode ser salvo fora do pacote. Os validadores locais oficiais de Plugin Creator e Skill Creator foram verificações adicionais separadas; sua disponibilidade não é dependência operacional da skill. Não instale dependências em nome do usuário sem necessidade da tarefa autorizada.
