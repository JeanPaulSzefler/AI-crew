# Brief projektu AI-crew

Jedna strona. Zmiany zatwierdza Owner.

## Po co

Owner prowadzi kilka małych projektów z pomocą agentów AI. To repo wypracowuje **koncepcję załogi AI i gotowe struktury repo**, które da się skopiować do nowego projektu, tak żeby załoga pracowała skutecznie i możliwie samodzielnie przy małym budżecie.

## Co jest sukcesem

- Nowy projekt da się postawić z blueprintu w jednej sesji i od razu prowadzić przez tablicę zadań.
- Owner pracuje głównie z telefonu: podaje cel, wraca do gotowej zmiany, odpowiada na pytania w jednym miejscu.
- Blueprint zmienia się po pilotażach i po zmianie założeń, a każda zmiana ma zapisany powód.

## Zakres

- **Robimy:** research, raporty, rekomendacje, blueprinty repo, wnioski z pilotaży w formie uogólnionej.
- **Nie robimy:** diagnoz ani planów istniejących projektów Ownera; kodu aplikacji; niczego, co ujawnia szczegóły prywatnych projektów. Szczegóły: `docs/out-of-scope/`.

## Założenia

Punkt odniesienia, nie stała. Każde założenie ma warunek powrotu.

| Założenie | Wrócić, gdy |
| --- | --- |
| Subskrypcje: Claude Pro i ChatGPT Plus, bez płatnego API (decyzja 0006) | Zmieni się plan albo limity |
| Modele na co dzień: Sonnet i Haiku; Opus punktowo | Pojawi się nowy model albo zmienią się limity |
| Miejsce pracy: sesje chmurowe uruchamiane z aplikacji mobilnej; komputer tylko do rzeczy lokalnych | Pojawi się praca, której chmura nie obsłuży |
| GitHub w planie Free | Przejście na plan płatny |
| Projekty docelowe są różne: treściowe i z kodem | Ustali się jeden dominujący typ |

## Zawsze Owner

Lista w [`AGENTS.md`](../AGENTS.md#always-the-owner-class-c). Dodatek dla tego repo: wszystko, co dotyczy innych repozytoriów Ownera.
