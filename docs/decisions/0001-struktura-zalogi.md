# 0001: Sonnet prowadzi, Haiku wykonuje małe zadania, Opus doradza punktowo, Codex niezależnie

- **Data:** 2026-11-11
- **Status:** propozycja. Stosowana roboczo w tym repo i w blueprincie do czasu wyboru Ownera
- **Podstawa:** [raport z 11.11.2026](../../outputs/2026-11-11-koncepcja-ai-crew-i-blueprint-repo.md), rozdziały 2–4. Owner poprosił o ocenę swojej propozycji i rekomendację; wyboru jeszcze nie dokonał

## Decyzja

Sesję główną prowadzi Sonnet: rozmawia z Ownerem, planuje i sam wykonuje większość pracy. Haiku jako subagent `worker` dostaje małe, w pełni opisane zadania sprawdzalne automatem. Opus jako subagent `advisor` daje drugą opinię w trzech momentach: koncepcja, wydanie albo ważne scalenie, dwie nieudane próby. Codex pracuje niezależnie: recenzja, teksty dla ludzi, obrazy.

## Powód

Propozycja Ownera (Opus jako lead, Sonnet definiuje zadania, Haiku wykonuje) dobrze dobiera modele do rodzaju pracy, ale układa je w łańcuch z dwoma przekazaniami i stawia model o najciaśniejszym limicie w miejscu o największej liczbie tur. Źródła pokazują, że praca sekwencyjna traci na wielu agentach, a mocny model daje najwięcej jako doradca tańszego. Odpadł też układ „Sonnet tylko rozdziela zadania”: każde przekazanie kosztuje kontekst.

## Kiedy wrócić

Gdy Opus przestanie trafiać w limit; po pierwszym pilotażu; przy nowej generacji modeli; gdy zadania Wykonawcy wracają do poprawki częściej niż co trzecie.
