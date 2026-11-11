# Simple Calculator

Een eenvoudige Python-calculator voor beginners. Het project gebruikt losse
functies, zodat elke berekening onafhankelijk kan worden gebruikt en getest.

## Functies

De calculator ondersteunt:

- optellen met `add`;
- aftrekken met `subtract`;
- vermenigvuldigen met `multiply`;
- delen met `divide`.
- machtsverheffen met `power`;
- percentages berekenen met `percentage`.

De calculator heeft nog geen command-line-interface. Je gebruikt de functies
rechtstreeks vanuit Python-code.

## Vereisten

- Python 3.11 of nieuwer
- `pip`, de pakketbeheerder van Python

Python 3.11 of nieuwer is nodig voor de ondersteunde projectomgeving en type
hints zoals `int | float`.

## Installatie

Open een terminal en ga naar de projectmap:

```bash
cd /pad/naar/copilot-leerpad
```

Vervang `/pad/naar/copilot-leerpad` door het echte pad naar deze repository.

### macOS/Linux

Maak een virtuele omgeving aan:

```bash
python3 -m venv .venv
```

Activeer de virtuele omgeving:

```bash
source .venv/bin/activate
```

### Windows

Maak een virtuele omgeving aan:

```powershell
py -3 -m venv .venv
```

Activeer de virtuele omgeving in PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Gebruik je de klassieke Windows-opdrachtprompt (`cmd.exe`), activeer dan met:

```bat
.venv\Scripts\activate.bat
```

## Dependencies installeren

Installeer de ontwikkelafhankelijkheden vanuit de geactiveerde virtuele
omgeving:

```bash
python -m pip install -r requirements-dev.txt
```

De productiecode heeft geen externe dependencies. `requirements-dev.txt`
bevat pytest en de pakketten die pytest nodig heeft om de tests uit te voeren.

## Calculator gebruiken

Importeer de functies uit `calculator.py`:

```python
from calculator import add, divide, multiply, percentage, power, subtract

add(2, 3)          # 5
subtract(8, 3)     # 5
multiply(4, 3)     # 12
divide(12, 3)      # 4.0
power(2, 3)        # 8
percentage(25, 200)  # 12.5
```

De functies werken met gehele getallen en kommagetallen:

```python
add(2, 0.5)        # 2.5
divide(5, 2.0)     # 2.5
percentage(12.5, 50)  # 25.0
```

## Foutafhandeling

Delen door nul is niet toegestaan. `divide` en `percentage` geven in dat geval
een `ZeroDivisionError`:

```python
from calculator import divide

divide(10, 0)  # raises ZeroDivisionError
percentage(10, 0)  # raises ZeroDivisionError
```

De functies verwachten numerieke invoer. Invoercontrole voor andere types is
geen onderdeel van dit eenvoudige project.

## Tests uitvoeren

Voer de tests uit vanuit de projectmap, met de virtuele omgeving geactiveerd:

```bash
python -m pytest -v
```

De tests staan in `tests/test_calculator.py` en controleren onder andere:

- positieve en negatieve getallen;
- nul;
- gehele getallen en kommagetallen;
- gemengde numerieke invoer;
- floating-point-resultaten;
- delen door nul;
- machtsverheffen en percentages.

Als je klaar bent, kun je de virtuele omgeving verlaten met:

```bash
deactivate
```

## Projectstructuur

```text
copilot-leerpad/
├── calculator.py              # Calculatorfuncties
├── tests/
│   └── test_calculator.py     # Geautomatiseerde pytest-tests
├── requirements-dev.txt       # Ontwikkelafhankelijkheden
├── README.md                  # Projectdocumentatie
└── .gitignore                 # Bestanden die Git moet negeren
```
