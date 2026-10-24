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

## Como registrar um caso novo

Copie o bloco acima e preencha: veículo (sem placa nem CPF, se este arquivo for público), o que havia no processo, como a unidade agiu, o que o agente deve fazer (veredito, status, Observações, relatório). Cite sempre os tipos de documento (Despacho, Informação, Ofício) e as unidades (DEL, EGVR-BA, NAT-BA, NAT-UF, SPRF-BA), nunca nomes de pessoas.
