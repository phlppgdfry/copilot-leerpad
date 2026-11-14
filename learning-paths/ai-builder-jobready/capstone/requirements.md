# Service Hub — requirements op basis van fictieve organisatie

## Personas
- Medewerker: aanvraag registreren en opvolgen.
- Reviewer: AI-voorstel beoordelen, goedkeuren/afwijzen.
- Manager: trends, doorlooptijd en fouten opvolgen.

## User stories
1. Als medewerker wil ik een ticket indienen met titel, beschrijving en categorie.
2. Als medewerker wil ik ticketstatus kunnen inzien.
3. Als reviewer wil ik een AI-voorstel expliciet goedkeuren voordat externe acties plaatsvinden.
4. Als manager wil ik op hoofdlijnen aantallen en doorlooptijden zien.

## Startacceptatiecriteria
- Titel 3–120 tekens, beschrijving 5–2000.
- Categorie alleen question/incident/request.
- POST /tickets resulteert in 201 bij geldige invoer.
- GET onbekend ticket geeft 404.
- Ongeldige input geeft 422.
- Tickets worden lokaal in SQLite opgeslagen.

## Nog niet gebouwd — beveiliging en productie
Login, object-level permissions, auditlog, abuse control, privacybewaartermijnen, CI-deployment, production monitoring. Deze moeten beoordeeld worden voordat er echte gebruikers zouden komen.

## Buiten scope
Echte klantgegevens, externe AI-API's, betalingen, e-mails naar derden en automatische agentacties.
