# Capstone: AI Service Operations Hub

**Fictieve use case:** een serviceafdeling registreert tickets, wil aanvragen opvolgen en eventueel later een AI-classificatie met menselijke goedkeuring toevoegen.

## Opbouw per fase
- W01–02: browser, REST API, Python, SQLite.
- W03–04: Power Platform/Dataverse alternatief en approval-flow ontwerpen.
- W05–06: AI-classificatie met toolcontract, RAG/FAQ en 20 evaluatiegevallen.
- W07–08: tests, CI, threat model, logging en fouten.
- W09–10: requirements, process map en businesscase.
- W11–12: demo, ADR, mock interview, bewijs.

## Installeren en starten
```bash
cd capstone/service_hub
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
python -m pytest -q
python -m uvicorn app.main:app --reload
```
Windows PowerShell: `.venv\Scripts\Activate.ps1`.
Open: http://127.0.0.1:8000/docs en http://127.0.0.1:8000/health.

## Probeer zelf
```bash
curl -s http://127.0.0.1:8000/health
curl -s -X POST http://127.0.0.1:8000/tickets \
  -H 'Content-Type: application/json' \
  -d '{"title":"Demo printer","description":"Printer op tweede verdieping reageert niet","category":"incident"}'
curl -s http://127.0.0.1:8000/tickets
```

## Oefeningen: implementeer deze zelf
1. Filteren op status/categorie met validatie.
2. PATCH-status met geldige overgangen.
3. Mock classificatie die nooit zelf extern schrijft.
4. Review/approve/reject met audit trail.
5. Securitydesign voor authenticatie en object-level autorisatie (geen fake security als snelle fix).

## Strikte grenzen
Deze start-API heeft **geen authenticatie, autorisatie, rate limits of beveiligd deployment**. Gebruik alleen verzonnen data, alleen lokaal. Er zijn geen betaalde AI-calls. Noem dit geen production-ready project.
