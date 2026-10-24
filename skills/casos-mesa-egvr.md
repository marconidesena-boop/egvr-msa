---
name: casos-mesa-egvr
description: Livro de casos da mesa da EGVR-BA (veículos removidos, restrições judiciais, leilão). Situações reais já resolvidas pelo chefe da unidade, com o raciocínio, a providência adotada e o texto de Observações usado. Consultar sempre que um veículo tiver decisões judiciais conflitantes, mandado de segurança, ordem de depósito do valor do leilão, restrição que a consulta não explica, veículo antigo com restrição só na base estadual, ou qualquer situação fora do ciclo simples notificar → prazo → apto → sem restrição.
---

# Livro de casos da mesa EGVR-BA

Este arquivo cresce com o tempo. Cada caso registra **como a unidade decidiu agir**; o agente usa o caso parecido como modelo, cita o número do caso na análise e nunca inventa um desfecho que não esteja aqui ou no processo.

Regras gerais que os casos ilustram:
- Decisão judicial que afeta o destino do veículo (liberar, leiloar, depositar valor) **não é baixa de restrição** e não muda o status da linha. Ela entra em Observações e no veredito do veículo (CONFERIR).
- Quando duas ou mais autoridades apontam destinos diferentes, a unidade **não escolhe**: documenta, pergunta ao NAT-BA (Núcleo de Análise Técnica e Controle Interno da SPRF-BA) e aguarda a orientação. O NAT pode acionar a representação judicial da União.
- Processos relacionados no SEI são parte do caso: a resposta ou a decisão costuma estar neles.
- Veículo antigo (recolhido há muitos anos) pode ter restrição anterior ao RENAJUD, registrada só na base do DETRAN de origem. Nesse caso a unidade pede ao NAT do estado a consulta à base estadual.
- Toda providência da unidade vira documento no SEI (Informação ou Despacho) e uma frase em Observações, com nº SEI e data.

---

## Caso 01 — Mandado de segurança mandando liberar o veículo × Vara pedindo leilão com depósito × restrições novas na consulta

**Veículo**: caminhão recolhido em 27/07/2015 e ainda no pátio em 2026 (mais de 11 anos). Planilha de aptos para leilão, 4 linhas (TJSE, TRF5, TRT20, TJSP).

**O que havia no processo individual (e nos relacionados)**:
1. Mandado de segurança (2ª Vara Federal Cível e Criminal de Itabuna), trânsito em julgado em 17/04/2026: concedeu a **liberação do veículo ao proprietário mediante pagamento da estada limitada aos 30 primeiros dias**, preservando as demais restrições. O proprietário **não compareceu** para retirar. Documento no processo individual + processo relacionado próprio do MS.
2. A 1ª Vara Cível de Aracaju (TJSE), em execução de título extrajudicial, **requisitou informações sobre o andamento e a data do leilão** e determinou **depósito do saldo líquido em conta judicial** após a arrematação. Chegou pela SPRF-BA, que abriu processo próprio ("Pessoal: Cumprimento de Decisão Judicial") e encaminhou ao NAT-BA; o NAT-BA repassou à EGVR-BA com prazo para resposta.
3. A consulta mais recente (SENATRAN) mostrava restrições judiciais **ativas** de TJSE e TJSP, enquanto TRF5 e TRT20 já haviam baixado as suas. Ou seja: juízes diferentes com ordens diferentes, e restrições ainda sendo mantidas por alguns.
4. O veículo é antigo: a dúvida de restrições anteriores ao RENAJUD, registradas só na base estadual, era real.

**Como a unidade agiu (sequência, toda documentada no SEI)**:
- Delegacia (DEL05-BA) fez **despacho ao NAT-BA** pedindo orientação sobre o cumprimento do MS (procedimentos administrativos e operacionais), em vez de liberar ou leiloar por conta própria.
- Quando a Vara de Aracaju pediu informações sobre o leilão, a EGVR-BA respondeu ao NAT-BA com um **despacho de solicitação de orientação jurídica**, expondo os três fatos juntos (MS com liberação condicionada, proprietário que não compareceu, Vara determinando leilão com depósito) e pedindo **interlocução do NAT com os juízos envolvidos, inclusive pela representação judicial da União**, para esclarecer se o leilão pode prosseguir, qual providência cabe, e se é preciso **intimar previamente o proprietário** para retirada.
- No processo individual, a EGVR-BA deixou uma **Informação** curta dizendo que a possibilidade do leilão está sendo tratada no processo relacionado (nº do processo de cumprimento de decisão judicial), para quem abrir o processo do veículo saber onde está a discussão.
- Como o veículo é antigo e de outro estado (SE), a EGVR-BA fez **despacho ao NAT-SE** pedindo consulta à base do DETRAN/SE das restrições judiciais do veículo (e de outro veículo na mesma situação), com juízes responsáveis, números de processo, datas de inclusão e situação atual, porque restrições anteriores ao RENAJUD podem constar só na base estadual.

**O que o agente deve fazer num caso assim**:
- Veredito do veículo: **CONFERIR**, nunca APTO nem NÃO APTO por conta própria.
- Status das linhas: cada restrição segue a fase da sua cadeia (ex.: TJSE e TJSP ativas e notificadas há mais de 60 dias → `APTO PARA LEILÃO (P 60 DIAS VENCIDO)`; TRF5 e TRT20 baixadas e confirmadas na consulta → `SEM RESTRIÇÃO`). O MS e a ordem de depósito **não** alteram status.
- Observações da(s) linha(s) afetada(s), acrescentando ao texto existente, em vermelho, no padrão:
  `DIRIMINDO DÚVIDAS ACERCA DE MANIFESTAÇÃO DO JUIZ DA <Vara> (SEI <nº>, dd/mm/aaaa); CONSULTA AO NAT-BA (SEI <nº>, dd/mm/aaaa) | AGUARDANDO ORIENTAÇÃO`
  e, quando houver, `MS <nº CNJ> TRANSITADO EM JULGADO EM dd/mm/aaaa: LIBERAÇÃO AO PROPRIETÁRIO MEDIANTE ESTADA DE 30 DIAS (SEI <nº>); PROPRIETÁRIO NÃO COMPARECEU`.
- Relatório: listar as manifestações (quem, o quê, nº SEI, data), o despacho ao NAT e o processo relacionado onde a discussão corre. Se já houver resposta do NAT, resumi-la e propor o próximo passo que ela indicar.

---

## Caso 02 — Restrição ativa no DETRAN-BA que não aparece no RENAJUD/SENATRAN (restrição anterior ao RENAJUD)

**Veículo**: utilitário em planilha de aptos, 3 linhas de restrição (duas Varas do Trabalho de Salvador e uma Vara do Trabalho do interior).

**O que havia**: a consulta DETRAN-BA nova (e a anterior, meses antes) mostrava **duas restrições ativas** (DATA BAIXA = N/D), inclusive uma de 2006 da Vara do interior; a consulta SENATRAN só listava a da Vara de Salvador. A linha da Vara do interior estava como `SEM RESTRIÇÃO` na planilha, e o número do processo judicial dessa linha estava em notação científica (dígitos finais perdidos).

**Leitura certa**: não é contradição entre fontes. Processo de 2006 é **anterior ao RENAJUD** (2008); a restrição vive só na base estadual, e por isso o SENATRAN/RENAJUD não a mostra. O DETRAN-BA prevalece: a restrição é **ativa**. Os 15 dígitos preservados do número em notação científica bastam para casar a linha com a restrição da consulta (prefixo `0183800-84.2006.5.05`), e o ofício da linha traz o número completo para a correção.

**Como a unidade age**: a linha sai de `SEM RESTRIÇÃO` para o status da fase da cadeia (aqui, ofício enviado e recebido em setembro de 2025 → `APTO PARA LEILÃO (P 60 DIAS VENCIDO)`); o número do processo é corrigido como texto a partir do ofício; Observações recebe `RESTRIÇÃO ATIVA NA CONSULTA DETRAN-BA (SEI <nº>, data): SEQ <n>, DATA BAIXA N/D; SÓ NA BASE ESTADUAL, AUSENTE NO RENAJUD/SENATRAN (SEI <nº>); 60 DIAS VENCIDOS EM dd/mm/aaaa`.

**O que o agente deve fazer**: nunca tratar "DETRAN ativa × SENATRAN ausente" como motivo de CONFERIR; casar a linha por prefixo e pelo ofício; propor status, correção do processo e observação na mesma tabela; veredito do veículo pela regra dos 60 dias (aqui, APTO, se as outras linhas também cumprirem).

---

## Caso 03 — Veículo na planilha de aptos com restrições ativas que nunca foram notificadas

**Veículo**: motocicleta recolhida em 2017, na planilha de aptos com 4 linhas (uma Vara do Trabalho do interior, a Vara da Fazenda Pública da comarca, e duas Varas Federais de execução fiscal). Três linhas `APTO PARA LEILÃO (P 60 DIAS VENCIDO)` e uma `SEM RESTRIÇÃO`.

**O que a consulta DETRAN-BA nova mostrou**: 24 registros. 22 judiciais, dos quais 12 baixados e **10 ativos**; 2 não judiciais (bloqueio de licenciamento por comunicação de venda e **arrolamento de bens pela Receita Federal**). Das 10 ativas, só 4 tinham linha na planilha e ofício enviado (todas com recebimento acusado e 60 dias vencidos). As outras **6 nunca foram notificadas e não têm linha**: 3 da Vara Única da Subseção Federal da comarca (incluídas em 2023), 2 de uma Vara do Trabalho da comarca (2024) e 1 da Vara da Fazenda Pública (dezembro de 2024). A consulta SENATRAN confirmava as mesmas 10 ativas. Nenhum dos ofícios do processo citava esses 6 processos: a planilha foi montada a partir de uma consulta antiga e as restrições incluídas depois nunca entraram no ciclo.

**Dois detalhes que confundem**:
- **Recadastro**: duas restrições ativas eram o **mesmo processo** de restrições baixadas minutos antes (a Vara baixou e incluiu de novo, com nova sequência). Para a planilha, é a mesma restrição da mesma linha, não uma restrição nova; a linha segue a cadeia de ofício dela.
- **Nome do órgão**: o DETRAN guarda o órgão no momento da inclusão ("Vara Única da Subseção"); a planilha traz a Vara atual, informada na resposta ao ofício ("8ª Vara Federal de Execução Fiscal"). A ligação é pelo **número do processo**, nunca pelo nome da Vara.
- **Mesmo devedor, dois veículos**: três dos seis processos sem ofício já tinham linha na planilha, mas no bloco de **outro veículo** do mesmo devedor, com ofício enviado e recebido. Lidos os dois ofícios no SEI, eles citam apenas a placa do outro veículo. Conclusão: as Varas e os e-mails já são conhecidos (aproveitar), mas a notificação não se estende a este veículo; é preciso ofício próprio citando esta placa.

**Como a unidade age**: o veículo **não vai a leilão** enquanto houver restrição ativa sem notificação. Para cada uma das 6: inserir a linha completa no bloco do veículo (regra de 21/10/2026: toda restrição ativa fica informada integralmente na planilha), com tribunal, Vara e processo da consulta, status `NOVA RESTRIÇÃO (NOTIFICAR)`; expedir o ofício; registrar envio e recebimento; contar 60 dias da notificação. As 4 linhas já notificadas mantêm o status e recebem a observação da consulta nova. O arrolamento da Receita Federal e o bloqueio por venda ficam fora do controle judicial, mas entram no relatório como pendência administrativa para a chefia decidir antes do leilão.

**O que o agente deve fazer**: veredito **NÃO APTO**, com a lista das restrições não notificadas (Vara, processo, data de inclusão); propor a inserção das linhas (ou, em modo auditoria, listar o que seria inserido); observação na linha da placa `6 RESTRIÇÕES ATIVAS SEM OFÍCIO NA CONSULTA DETRAN-BA (SEI <nº>, data) — NOTIFICAR`; nas linhas existentes, a observação da consulta nova com a data dos 60 dias contada da notificação; tratar recadastro como a mesma restrição; apontar a restrição administrativa como pendência, sem mudar status.

---

## Como registrar um caso novo

Copie o bloco acima e preencha: veículo (sem placa nem CPF, se este arquivo for público), o que havia no processo, como a unidade agiu, o que o agente deve fazer (veredito, status, Observações, relatório). Cite sempre os tipos de documento (Despacho, Informação, Ofício) e as unidades (DEL, EGVR-BA, NAT-BA, NAT-UF, SPRF-BA), nunca nomes de pessoas.
