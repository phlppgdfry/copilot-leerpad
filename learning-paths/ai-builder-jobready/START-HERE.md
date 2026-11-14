# Start hier — 60 tot 90 minuten

## 1. Nulmeting
Vul [assessments/diagnostic.md](assessments/diagnostic.md) in: 0 = onbekend, 1 = met AI, 2 = zelfstandig uitleggen/toepassen met documentatie, 3 = zelfstandig uitvoeren, testen en verdedigen.

## 2. Installeer
Git, VS Code en Python 3.11 of hoger. Open een terminal in `capstone/service_hub`.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
python -m pytest -q
python -m uvicorn app.main:app --reload
```

Op Windows activeer je de venv met `.venv\Scripts\Activate.ps1`. Bekijk daarna lokaal `http://127.0.0.1:8000/docs`.

## 3. Vast weekritme (10 uur)
| Dag | Werk | Tijd |
|---|---|---|
| Ma | Theorie + eigen samenvatting | 1,5u |
| Di | Begeleide oefeningen | 1,5u |
| Wo | Zelf uitvoeren, AI alleen voor hints | 2u |
| Do | Bestaande code analyseren, testen | 1,5u |
| Vr | Quiz en mondeling uitleggen zonder AI | 1u |
| Weekend | Lab afwerken, bewijs en reflectie | 2,5u |

## 4. Wanneer mag je naar de volgende week?
- Alle verplichte bewijsmaterialen opgeleverd.
- Minimaal niveau 2 op begrip en praktische uitvoering.
- De week-gate haal je aantoonbaar zonder AI.
- Noteer open zwaktes en herhaal die na 7 dagen.

## 5. Gebruik bestaande projecten
Analyseer regelmatig een project uit je eigen Copilot-leerpad. Niet de hoeveelheid nieuwe apps telt, maar het aantoonbare begrip van architectuur, tests, security en businesswaarde.
