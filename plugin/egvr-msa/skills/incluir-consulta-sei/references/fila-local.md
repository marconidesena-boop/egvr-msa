# Fila local de inclusão

O script `scripts/fila_local.py` usa somente Python padrão e SQLite; não acessa SEI, Google ou provedor de IA. Banco e manifestos reais ficam fora do pacote do plugin. Use um banco único por campanha e preserve-o nas retomadas.

1. `python scripts/fila_local.py BANCO preparar MANIFESTO`: o manifesto é uma lista de objetos com `nup`, `placa`, `arquivo` absoluto e `sha256` esperado opcional. Calcula hash e rejeita vínculos contraditórios. Preparação não comprova identidade institucional nem integridade semântica do PDF.
2. `python scripts/fila_local.py BANCO listar`: consultar situação, inclusive antes de retomar trabalho interrompido.
3. `python scripts/fila_local.py BANCO reservar CHAVE CONTROLE`: imediatamente antes de upload. O CONTROLE usa o template existente e deve levar `INCLUIR_PDF` no decidir_etapa. A transação grava INICIADA e impede nova reserva. Não há liberação automática por tempo.
4. `python scripts/fila_local.py BANCO registrar CHAVE INCERTA "referencia de evidencia"`: registrar efeito ainda não reconciliado.
5. `python scripts/fila_local.py BANCO registrar CHAVE INCLUIDO "referencia da conferencia no processo" --documento NUMERO_SEI --arquivo-baixado PDF`: só aceita hash binário idêntico. Se SEI transformar bytes, esse caminho não finaliza: documente comparação integral e mantenha pendência para tratamento próprio.
6. JA_EXISTENTE segue a mesma exigência de readback e documento; SEM_EFEITO encerra a tentativa sem criar licença automática para tentar novamente. Restauração da mesa segue o controle existente, separadamente do resultado do arquivo.

O banco reduz repetição entre execuções que o utilizam. Ele não impede cliques fora desse fluxo, não valida por si só evidência textual e não substitui a confirmação de identidade, acesso, duplicidade, metadados ou estado da mesa. Não inclua tokens, cookies ou senhas nos controles. Testes sintéticos em `evals/test_fila_local.py` não homologam o SEI.
