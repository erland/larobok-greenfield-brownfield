# Exportförberedelse och helhetsgranskning

## Sammanfattning

Projektet är genomgånget inför export. Manus har kontrollerats på strukturell nivå och exportpipeline har validerats.

Status: **Exportförberett**

## Kontroller som är utförda

- Kapitelordning kontrollerad mot `docs/export-metadata.yaml`.
- `chapters/00-inledning.md` ligger först i kapitelordningen.
- Alla planerade kapitel 1–10 finns i projektet.
- Varje kapitel har exakt en H1-rubrik.
- Inga H4-rubriker eller djupare rubriker hittades.
- Kodblock har jämnt antal kodstängsel.
- Tabeller har kontrollerats för separatorrad och cellantal.
- Bildreferenser har kontrollerats.
- Omslagsbild finns på `assets/cover/cover.png`.
- Metadata innehåller titel, undertitel, författare, språk, datum, version och identifierare.
- Lokal exportpipeline finns i `scripts/` och `styles/`.

## Korrigeringar

- Exportscriptets tabellvalidering har justerats så att giltiga flerradiga markdown-tabeller inte felaktigt flaggas som fel.
- Version har uppdaterats till `1.0.1`.
- Omslagsbildens sökväg har säkerställts i `docs/export-metadata.yaml` och `book.yaml`.
- Projektstatus har uppdaterats från kapitelgenerering till granskning/exportförberedelse.
- En kort exportguide har lagts till.

## Resultat från validering

`python3 scripts/export-book.py validate`

Resultat: **Validering klar.**

## Rekommenderad nästa åtgärd

Skapa EPUB och PDF från den exportförberedda projekt-zippen, eller gör först en språklig slutredigering om boken ska publiceras externt.
