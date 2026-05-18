# Greenfield eller Brownfield?

Detta är ett bokprojekt för en kort och direkt praktisk beslutshandbok om valet mellan greenfield, brownfield och hybrid vid införande av containerplattformar i en större myndighetsmiljö.

## Status

Manuset är innehållsligt helhetsgranskat, språkligt slutredigerat och exportförberett.

## Rekommenderat arbetssätt

1. Granska bokspecifikation och kapitelplan i `docs/`.
2. Läs rapporterna `docs/helhetsgranskning.md`, `docs/spraklig-slutredigering.md` och `docs/export-readiness-report.md`.
3. Exportera lokalt med `scripts/export-book.sh` när manus är redo.

## Lokal export

Projektet innehåller en reproducerbar exportpipeline baserad på Pandoc.

```bash
chmod +x scripts/export-book.sh
./scripts/export-book.sh epub
./scripts/export-book.sh pdf
./scripts/export-book.sh all
```

EPUB skrivs till `exports/`. PDF kräver att Pandoc och en PDF-engine, exempelvis xelatex, finns installerade.

## Omslag

Omslagsbilden finns i `assets/cover/cover.png` och är registrerad i `docs/export-metadata.yaml`.

## Granskning

- Innehållslig helhetsgranskning: `docs/helhetsgranskning.md`
- Språklig slutredigering: `docs/spraklig-slutredigering.md`
- Exportberedskap: `docs/export-readiness-report.md`
