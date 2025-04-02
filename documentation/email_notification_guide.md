# E-mail Notificatie Configuratie Handleiding

Dit document beschrijft hoe het e-mail notificatiesysteem voor het GoldForex4All autonome contentgoedkeuringssysteem werkt en hoe u het kunt configureren.

## Overzicht

Het e-mail notificatiesysteem bestaat uit de volgende componenten:

1. **Wekelijkse notificatie workflow** - Stuurt elke maandag om 9:00 uur een e-mail met content die op goedkeuring wacht
2. **Issue comment verwerking** - Verwerkt uw reacties op GitHub Issues (GOEDGEKEURD of REVISIE NODIG)
3. **E-mail formattering** - Genereert duidelijke, gebruiksvriendelijke e-mails met alle benodigde informatie

## Configuratie Stappen

### 1. GitHub Secrets Instellen

Om het e-mail notificatiesysteem te laten werken, moet u de volgende geheimen (secrets) instellen in uw GitHub repository:

1. Ga naar uw repository op GitHub
2. Klik op "Settings" (tandwiel icoon)
3. Klik op "Secrets and variables" in het linkermenu
4. Klik op "Actions"
5. Klik op "New repository secret"
6. Voeg de volgende secrets toe:

   - `SMTP_SERVER`: De SMTP server voor uitgaande e-mail (bijv. smtp.gmail.com)
   - `SMTP_PORT`: De SMTP poort (meestal 587 voor TLS)
   - `SMTP_USERNAME`: Uw e-mail gebruikersnaam
   - `SMTP_PASSWORD`: Uw e-mail wachtwoord of app-specifiek wachtwoord
   - `SENDER_EMAIL`: Het e-mailadres dat als afzender wordt gebruikt

### 2. E-mail Provider Configureren

Voor het verzenden van e-mails kunt u verschillende providers gebruiken:

#### Gmail
- SMTP_SERVER: smtp.gmail.com
- SMTP_PORT: 587
- Vereist een app-specifiek wachtwoord (niet uw normale Gmail wachtwoord)

#### Outlook/Office 365
- SMTP_SERVER: smtp.office365.com
- SMTP_PORT: 587

#### Transactionele E-mail Services
Voor betrouwbaardere levering kunt u ook services zoals SendGrid of Mailgun gebruiken.

### 3. Testen van het Notificatiesysteem

Na configuratie kunt u het notificatiesysteem testen door:

1. Ga naar uw repository op GitHub
2. Klik op "Actions" in de bovenste navigatiebalk
3. Selecteer de "Weekly Content Approval Notification" workflow
4. Klik op "Run workflow"
5. Klik op de groene "Run workflow" knop in het popup venster

U zou binnen enkele minuten een test e-mail moeten ontvangen op info@goldforex4all.eu.

## Hoe Het Werkt

### Wekelijkse Notificaties

Elke maandag om 9:00 uur (UTC) voert GitHub Actions automatisch het volgende proces uit:

1. Het script controleert GitHub Issues met het label "Ter Goedkeuring"
2. Het genereert een HTML e-mail met een lijst van deze items
3. De e-mail wordt verzonden naar info@goldforex4all.eu

### Verwerking van Goedkeuringen

Wanneer u reageert op een Issue met "GOEDGEKEURD" of "REVISIE NODIG", gebeurt het volgende:

1. GitHub Actions detecteert uw reactie
2. Het script update het label van het Issue (van "Ter Goedkeuring" naar "Goedgekeurd" of "Revisie Nodig")
3. Het script voegt een bevestigingscommentaar toe aan het Issue
4. Bij goedkeuring wordt de content klaargezet voor publicatie

## Problemen Oplossen

### E-mails Worden Niet Ontvangen

1. Controleer of de GitHub Secrets correct zijn ingesteld
2. Controleer uw spam/junk folder
3. Verifieer dat uw e-mail provider uitgaande SMTP toestaat
4. Bekijk de workflow logs in GitHub Actions voor foutmeldingen

### Goedkeuringen Worden Niet Verwerkt

1. Zorg dat u precies "GOEDGEKEURD" of "REVISIE NODIG" gebruikt in uw reactie
2. Controleer of de GitHub Actions workflows zijn ingeschakeld
3. Bekijk de workflow logs voor eventuele fouten

## Aanpassingen

Als u de frequentie of timing van de notificaties wilt wijzigen:

1. Bewerk het bestand `.github/workflows/weekly_notification.yml`
2. Pas de `cron` waarde aan in de `schedule` sectie
   - Standaard: `0 9 * * 1` (elke maandag om 9:00 UTC)
   - Formaat: `minute hour day-of-month month day-of-week`

## Contact

Als u hulp nodig heeft met het configureren van het e-mail notificatiesysteem, kunt u contact opnemen met het ondersteuningsteam.
