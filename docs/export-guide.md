# Exportguide

Den här projektmappen innehåller en lokal exportpipeline för EPUB och PDF.

## Förutsättningar

Installera följande lokalt:

- Python 3
- PyYAML
- Pandoc
- För PDF: en Pandoc-kompatibel PDF-motor, till exempel XeLaTeX via MacTeX eller TinyTeX

Installera PyYAML vid behov:

```bash
pip install pyyaml
```

## Validera projektet

Kör från projektroten:

```bash
./scripts/export-book.sh validate
```

## Skapa EPUB

```bash
./scripts/export-book.sh epub
```

Resultatet skrivs till `exports/greenfield-eller-brownfield.epub`.

## Skapa PDF

```bash
./scripts/export-book.sh pdf
```

Resultatet skrivs till `exports/greenfield-eller-brownfield.pdf`.

## Skapa både EPUB och PDF

```bash
./scripts/export-book.sh all
```

## Viktigt

Exporten använder `docs/export-metadata.yaml` för titel, författare, språk, identifierare, omslagsbild och kapitelordning.
