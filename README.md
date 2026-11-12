# Simple Calculator

Een eenvoudige Python-calculator voor beginners. Het project bevat losse
functies die rechtstreeks vanuit Python kunnen worden gebruikt en een
command-line-interface (CLI) voor berekeningen vanuit een terminal.

## Ondersteunde bewerkingen

De CLI ondersteunt deze vijf bewerkingen:

| Bewerking | Voorbeeld | Resultaat |
|---|---|---:|
| `add` | `add 2 3` | `5` |
| `subtract` | `subtract 8 3` | `5` |
| `multiply` | `multiply 4 3` | `12` |
| `divide` | `divide 12 3` | `4.0` |
| `power` | `power 2 3` | `8` |

De Python-API bevat daarnaast `percentage` en `classify_number`. Deze functies
zijn niet als CLI-bewerking beschikbaar.

## Vereisten

- Python 3.11 of nieuwer
- `pip`

Python 3.11 of nieuwer is nodig voor de type hints in de calculatorcode, zoals
`int | float`. De productiecode gebruikt alleen de Python-standaardbibliotheek.

## Installatie

Ga in een terminal naar de projectmap:

```bash
cd /pad/naar/copilot-leerpad
```

Vervang `/pad/naar/copilot-leerpad` door het echte pad naar deze repository.

### Virtuele omgeving: macOS en Linux

Maak een virtuele omgeving aan en activeer deze:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Gebruik daarna `python` vanuit deze geactiveerde omgeving.

### Virtuele omgeving: Windows PowerShell

```powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
```

Gebruik je de klassieke Windows-opdrachtprompt (`cmd.exe`), activeer dan met:

```bat
.venv\Scripts\activate.bat
```

### Installeerbare distributie

Installeer lokaal vanuit de projectmap:

```bash
python -m pip install .
```

Daarna is de console-opdracht beschikbaar:

```bash
calculator-cli add 2 3
# stdout: 5
```

Je kunt ook eerst distributiebestanden bouwen:

```bash
python -m build
python -m pip install dist/calculator_cli-1.0.0-py3-none-any.whl
```

Deze repository publiceert geen pakketten naar PyPI. De bestaande
`python -m calculator`-aanroep en imports vanuit `calculator.py` blijven
beschikbaar na installatie.

## Release 1.0.0

Deze release bevat de bestaande calculator-API, de CLI-bewerkingen `add`,
`subtract`, `multiply`, `divide` en `power`, en installatie als
`calculator-cli`-distributie. De functies `percentage` en `classify_number`
blijven beschikbaar via de Python-API, maar zijn geen CLI-bewerkingen.

Zie [CHANGELOG.md](CHANGELOG.md) voor de volledige release notes. Er wordt in
deze release niets naar PyPI gepubliceerd.

## Ontwikkelafhankelijkheden installeren

Installeer pytest en de vastgelegde ontwikkelafhankelijkheden:

```bash
python -m pip install -r requirements-dev.txt
```

## Python-API gebruiken

De bestaande functies blijven beschikbaar vanuit `calculator.py`:

```python
from calculator import add, divide, multiply, percentage, power, subtract

add(2, 3)             # 5
subtract(8, 3)        # 5
multiply(4, 3)        # 12
divide(12, 3)         # 4.0
power(2, 3)           # 8
percentage(25, 200)   # 12.5
```

De functies accepteren gehele getallen en kommagetallen:

```python
add(2, 0.5)           # 2.5
divide(5, 2.0)        # 2.5
percentage(12.5, 50)  # 25.0
```

## CLI gebruiken

Voer de calculator uit als Python-module:

```bash
python -m calculator <bewerking> <getal1> <getal2>
```

De CLI accepteert gehele getallen, kommagetallen en negatieve waarden.
Succesvolle resultaten worden naar stdout geschreven.

### Voorbeelden

```bash
python -m calculator add 2 3
# stdout: 5.0

python -m calculator subtract 8 3
# stdout: 5.0

python -m calculator multiply 4 3
# stdout: 12.0

python -m calculator divide 12 3
# stdout: 4.0

python -m calculator power 2 3
# stdout: 8.0
```

Voorbeelden met negatieve waarden en decimalen:

```bash
python -m calculator add -2.5 0.5
# stdout: -2.0

python -m calculator divide -12 2.5
# stdout: -4.8

python -m calculator power 2.5 2
# stdout: 6.25
```

Een machtsbewerking gebruikt een gehele exponent. Een waarde zoals `0.5` als
exponent wordt als ongeldige rekeninvoer afgewezen.

### Help

Toon de syntax en de beschikbare bewerkingen met:

```bash
python -m calculator --help
```

De helptekst wordt naar stdout geschreven en gebruikt exitcode `0`.

## Foutafhandeling en exitcodes

De CLI geeft geen Python-traceback voor verwachte invoerfouten.

| Situatie | Stream | Exitcode |
|---|---|---:|
| Berekening geslaagd | resultaat naar stdout | `0` |
| Ontbrekende of ongeldige argumenten | argparse-fout naar stderr | `2` |
| Onbekende bewerking | argparse-fout naar stderr | `2` |
| Niet-numerieke invoer | argparse-fout naar stderr | `2` |
| Delen door nul | rekenfout naar stderr | `1` |
| Niet-gehele exponent voor `power` | rekenfout naar stderr | `1` |
| `power 0 -1` | rekenfout naar stderr | `1` |

Voorbeelden:

```bash
python -m calculator add 2
# stderr: usage: ...
# exitcode: 2

python -m calculator divide 10 0
# stderr: calculation error: Cannot divide by zero.
# exitcode: 1
```

## Tests uitvoeren

Voer de volledige pytest-suite uit vanuit de projectmap:

```bash
python -m pytest -v
```

Voer alleen de Python-API-unit-tests uit:

```bash
python -m pytest -v tests/test_calculator.py
```

Voer alleen de CLI-integratietests uit:

```bash
python -m pytest -v tests/test_cli.py
```

De CLI-tests starten echte subprocessen met `sys.executable -m calculator`.
Daarmee controleren ze niet alleen de berekening, maar ook exitcodes, stdout,
stderr, argparse-fouten en helptekst.

Voor een korte testuitvoer kan `-q` worden gebruikt:

```bash
python -m pytest -q
```

Een aparte coverage-plugin is niet opgenomen in `requirements-dev.txt`.
De bovenstaande commando's voeren daarom de beschikbare unit- en
integratietests uit; ze berekenen geen percentage broncode-dekking.

## Projectstructuur

```text
copilot-leerpad/
├── calculator.py              # Publieke Python-functies en module-entrypoint
├── calculator_cli.py          # argparse CLI en foutafhandeling
├── pyproject.toml             # PEP 517/621 packagingconfiguratie
├── CHANGELOG.md               # Wijzigingen per versie
├── tests/
│   ├── test_calculator.py     # Tests voor de Python-functies
│   └── test_cli.py            # Subprocess-integratietests voor de CLI
├── requirements-dev.txt       # Vastgelegde ontwikkelafhankelijkheden
├── README.md                  # Projectdocumentatie
└── .gitignore                 # Bestanden die Git negeert
```

## Bekende beperkingen

- De CLI ondersteunt alleen `add`, `subtract`, `multiply`, `divide` en `power`.
  `percentage` en `classify_number` zijn alleen beschikbaar via Python.
- `power` vereist een gehele exponent. Fractionele exponenten worden niet door
  de CLI uitgevoerd.
- Resultaten gebruiken Python's normale representatie van `float`; de CLI
  rondt resultaten niet kunstmatig af.
- De CLI is bedoeld voor twee getallen per opdracht en heeft geen interactieve
  modus of geschiedenis.
- `divide` en `percentage` geven een `ZeroDivisionError` bij een nul-deler of
  nul-totaal wanneer ze rechtstreeks vanuit Python worden aangeroepen. De CLI
  vertaalt de relevante rekenfouten naar een foutmelding en exitcode.

Verlaat de virtuele omgeving wanneer je klaar bent:

```bash
deactivate
```
