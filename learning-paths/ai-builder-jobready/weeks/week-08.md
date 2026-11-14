# Week 08 — Security, logging en betrouwbare systemen

**8–12 uur | Eindresultaat:** Threat model, testplan en runbook.

## Begrippen
1. authenticatie, autorisatie en least privilege
2. OWASP API-risico's
3. secrets, omgevingsvariabelen, privacy
4. timeouts, retries, logging en observability

## Leerbronnen
- [OWASP API Security](https://owasp.org/API-Security/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)

## Dagplanner
| Dag | Activiteit |
|---|---|
| Ma — 1,5u | Lees eerste bron, schrijf in 10 zinnen wat je begreep |
| Di — 1,5u | Herhaal theorie en doe twee begeleide voorbeelden |
| Wo — 2u | Maak het lab; vraag maximaal hints, geen complete oplossing |
| Do — 1,5u | Inspecteer je eigen code, documenteer fouten en tradeoffs |
| Vr — 1u | Beantwoord quiz en leg drie concepten mondeling uit zonder AI |
| Weekend — 2,5u | Test, documenteer, commit en reflecteer |

## Lab / praktijkopdracht
Maak een threat model met 5 risico's en mitigaties. Ontwerp testcases voor 401/403 en toegang per ticket. Laat een foutlog zien zonder echte persoonsgegevens. Claim nooit dat de demo productiegeschikt is.

## Definition of Done
- [ ] Labopdracht uitgevoerd.
- [ ] Bewijs gecommit of gelinkt: Threat model, testplan en runbook.
- [ ] Mijn eigen architectuur-/beslissingsuitleg toegevoegd.
- [ ] Belangrijkste fout en aanpak genoteerd in het learning journal.
- [ ] Weekquiz beantwoord zonder AI.

## Vijf interviewvragen
1. Authenticatie versus autorisatie?
2. Wat is BOLA?
3. Wat hoort niet in logs?
4. Waarom zijn retries risicovol?
5. Hoe beperk je secret leakage?

## Gate
> Je benoemt duidelijk welke securitycontrols nog ontbreken.

## Stretch
Ontwerp een edge case waarin jouw oplossing faalt. Beschrijf impact voor gebruiker, beheerder én bedrijf. Laat AI de aannames bekritiseren nadat je het zelf hebt uitgewerkt.

## Mentoropdracht
'Wees mijn strenge docent voor **Security, logging en betrouwbare systemen**. Stel vragen één voor één, geef hints maar nooit direct de volledige oplossing. Evalueer wat ik onafhankelijk begrijp en maak een herhalingsoefening.'
