# Simple Calculator

Een eenvoudige calculator in Python met losse, goed testbare functies voor:

- optellen;
- aftrekken;
- vermenigvuldigen;
- delen.

De calculator heeft op dit moment geen command-line-interface. Je gebruikt de
functies rechtstreeks vanuit Python-code.

## Vereisten

- Python 3.10 of nieuwer

Python 3.10 is nodig omdat het project type hints gebruikt zoals `int | float`.

## Installatie

Maak vanuit de projectmap een virtuele omgeving aan:

```bash
python3 -m venv .venv
```

Activeer de virtuele omgeving:

**macOS/Linux**

```bash
source .venv/bin/activate
```

**Windows**

```powershell
.venv\Scripts\Activate.ps1
```

Installeer daarna de ontwikkelafhankelijkheden:

```bash
python -m pip install -r requirements-dev.txt
```

## Gebruik

Importeer de functies uit `calculator.py`:

```python
from calculator import add, divide, multiply, subtract

add(2, 3)          # 5
subtract(8, 3)     # 5
multiply(4, 3)     # 12
divide(12, 3)      # 4.0
```

De functies ondersteunen gehele getallen en kommagetallen. Delen door nul
geeft een `ZeroDivisionError`.

## Tests uitvoeren

Voer de tests uit vanuit de projectmap:

```bash
python -m pytest -q
```

De tests staan in `tests/test_calculator.py` en controleren normale berekeningen,
negatieve getallen, nul, floating-point resultaten en delen door nul.