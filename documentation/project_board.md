# Content Planning Project Board

Dit document beschrijft de structuur van het GitHub Project Board dat wordt gebruikt voor content planning in het GoldForex4All autonome contentgoedkeuringssysteem.

## Project Board Structuur

Het project board is ingedeeld in de volgende kolommen:

### 1. Ideeën
Content ideeën die nog moeten worden uitgewerkt. Elke kaart bevat:
- Titel van het content idee
- Type content (blog, social media, video, product review)
- Doelplatform
- Korte beschrijving
- Potentiële publicatiedatum

### 2. In Ontwikkeling
Content die momenteel wordt geschreven of ontwikkeld. Kaarten bevatten:
- Titel van de content
- Type content
- Doelplatform
- Link naar het bestand in de repository
- Verwachte opleverdatum
- Toegewezen aan

### 3. Ter Goedkeuring
Content die klaar is voor review en goedkeuring door de eigenaar. Kaarten bevatten:
- Titel van de content
- Type content
- Doelplatform
- Link naar het bestand in de repository
- Link naar het bijbehorende Issue
- Voorgestelde publicatiedatum

### 4. Goedgekeurd
Content die is goedgekeurd maar nog niet is gepubliceerd. Kaarten bevatten:
- Titel van de content
- Type content
- Doelplatform
- Link naar het bestand in de repository
- Geplande publicatiedatum
- Eventuele voorbereidende taken voor publicatie

### 5. Gepubliceerd
Content die is gepubliceerd. Kaarten bevatten:
- Titel van de content
- Type content
- Publicatieplatform
- Publicatiedatum
- Link naar de gepubliceerde content
- Prestatiemetrieken (indien beschikbaar)

## Labels

Het project board gebruikt de volgende labels om content te categoriseren:

- **Type: Blog** - Voor blogartikelen
- **Type: Social Media** - Voor social media posts
- **Type: Video** - Voor videocontent
- **Type: Product Review** - Voor product reviews

- **Platform: Website** - Voor content op goldforex4all.eu
- **Platform: TikTok** - Voor TikTok content
- **Platform: YouTube** - Voor YouTube content
- **Platform: Twitter** - Voor Twitter/X content
- **Platform: Facebook** - Voor Facebook content
- **Platform: Instagram** - Voor Instagram content

- **Prioriteit: Hoog** - Voor urgente content
- **Prioriteit: Medium** - Voor standaard content
- **Prioriteit: Laag** - Voor niet-urgente content

- **Status: Concept** - Voor eerste versies
- **Status: Review** - Voor content in review
- **Status: Klaar** - Voor afgeronde content

## Automatisering

Het project board maakt gebruik van de volgende automatiseringen:

1. **Nieuwe Issues** met het label "Ter Goedkeuring" worden automatisch toegevoegd aan de "Ter Goedkeuring" kolom

2. **Issues met het label "Goedgekeurd"** worden automatisch verplaatst naar de "Goedgekeurd" kolom

3. **Issues met het label "Gepubliceerd"** worden automatisch verplaatst naar de "Gepubliceerd" kolom

4. **Gesloten Issues** worden automatisch verwijderd uit het project board

## Wekelijkse Planning

Elke week wordt het project board bijgewerkt met nieuwe content ideeën en planning voor de komende periode. Dit gebeurt volgens het volgende proces:

1. Nieuwe content ideeën worden toegevoegd aan de "Ideeën" kolom
2. Content voor de komende week wordt verplaatst naar "In Ontwikkeling"
3. Voltooide content wordt verplaatst naar "Ter Goedkeuring"
4. Een wekelijks overzicht wordt gedeeld met de eigenaar

## Toegang en Rechten

- **Eigenaar (fx1960)**: Volledige toegang, inclusief goedkeuring
- **Content Team**: Kan kaarten toevoegen en bewerken in alle kolommen behalve "Goedgekeurd" en "Gepubliceerd"
- **Viewers**: Kunnen het board bekijken maar niet bewerken
