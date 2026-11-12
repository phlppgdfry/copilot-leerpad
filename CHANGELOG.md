# Changelog

Alle belangrijke wijzigingen in dit project worden in dit bestand beschreven.
Dit bestand volgt de conventies van [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.0.0] - 2026-11-12

### Added

- Een Python-API in `calculator.py` voor:
  - optellen, aftrekken, vermenigvuldigen en delen;
  - machtsverheffen met gehele exponenten;
  - percentages berekenen;
  - getallen classificeren als positief, negatief of nul.
- Een CLI in `calculator_cli.py` met de opdrachten `add`, `subtract`,
  `multiply`, `divide`, `power` en `percentage`.
- Gebruik als module met `python -m calculator`.
- Een installeerbare `calculator-cli`-distributie met de console-opdracht
  `calculator-cli`.
- Wheel- en source-distribution-builds via `pyproject.toml` en setuptools.
- Geautomatiseerde pytest-tests voor de Python-API en CLI, inclusief
  foutpaden, floating-point-gevallen, negatieve waarden, nulwaarden en grote
  gehele getallen.
- Logging voor succesvolle delingen en pogingen om door nul te delen.

### Changed

- De distributie gebruikt standaarden-gebaseerde PEP 517/621-packaging.
- De bestaande top-level modules en publieke imports blijven behouden.

### Fixed

- Delen door nul geeft in de Python-API een expliciete `ZeroDivisionError` en
  de CLI geeft hiervoor een gebruikersgerichte foutmelding zonder traceback.

### Compatibility

- Python 3.11 en nieuwer.
- De productiecode heeft geen runtime-afhankelijkheden buiten de Python
  standaardbibliotheek.

### Known limitations

- De CLI ondersteunt `add`, `subtract`, `multiply`, `divide`, `power` en
  `percentage`; `classify_number` is alleen beschikbaar via de Python-API.
- `power` accepteert via de CLI alleen gehele exponenten.
- De CLI werkt met twee getallen per opdracht en heeft geen interactieve modus
  of geschiedenis.
- Resultaten gebruiken Python's normale representatie van `float` en worden
  niet kunstmatig afgerond.
- Er is geen PyPI-publicatie opgenomen in deze release.
