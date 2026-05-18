# Kapitel 6: Brownfield: när det är klokt och när det är riskabelt

## Varför detta kapitel finns

Brownfield är ofta det mest realistiska vägvalet i en större myndighet. Det utgår från att införandet av containerplattform inte sker i ett tomrum. Det finns redan system, driftansvar, integrationer, säkerhetskrav, avtal, incidentrutiner, dokumentation, undantag och människor som håller verksamheten igång.

Det kan göra brownfield mer ansvarsfullt än greenfield. I stället för att bygga en ny värld bredvid den gamla tar organisationen sin befintliga verklighet på allvar och förändrar den stegvis.

Men brownfield har också en tydlig risk: att organisationen tar med sig för mycket av det gamla in i det nya. Om personberoenden, otydliga ansvar, manuella arbetssätt och speciallösningar följer med in i containerplattformen kan resultatet bli en modern teknikmiljö med gamla problem.

Kapitlet hjälper dig att bedöma när brownfield är klokt, när det är riskabelt och vilket beslutsunderlag som behövs innan organisationen väljer att förändra utifrån befintlig miljö.

## Lärandemål

Efter kapitlet ska du kunna:

- förklara vad brownfield innebär som förändringsväg vid införande av en containerplattform,
- identifiera brownfields viktigaste fördelar, nackdelar och risker,
- bedöma när befintlig miljö är en tillgång och när den är en belastning,
- känna igen varningssignaler som tyder på att gamla beroenden följer med in i det nya,
- använda en enkel brownfield-riskbedömning inför beslut.

## Innan vi börjar

I kapitel 5 såg vi att greenfield kan skapa handlingsutrymme, men också en risk för parallella världar. Brownfield har nästan motsatt riskprofil. Det börjar närmare den verkliga organisationen, men kan få svårt att skapa tillräcklig förändring.

Frågan är därför inte:

> Är brownfield tryggare?

Frågan är:

> Kan vi förändra det befintliga utan att bara återskapa dagens problem på en ny plattform?

För en chef är detta avgörande. Brownfield kan vara den mest verksamhetsnära vägen, men bara om organisationen vågar synliggöra arv, beroenden och personberoenden innan de byggs in i nästa generations driftmodell.

## Vad brownfield betyder i praktiken

Brownfield betyder i denna bok att organisationen inför containerplattform med utgångspunkt i befintliga system, arbetssätt, beroenden och driftmodeller.

Det kan innebära att ett eller flera befintliga system gradvis anpassas, migreras eller moderniseras så att de kan köras, förvaltas eller levereras med stöd av den nya plattformen.

I praktiken handlar brownfield ofta om att:

- börja med verkliga system i stället för en helt ny applikation,
- kartlägga beroenden innan förändringen startar,
- involvera befintlig driftkompetens tidigt,
- anpassa säkerhets- och driftprocesser stegvis,
- bygga ny förmåga samtidigt som daglig drift fortsätter,
- hantera gamla och nya arbetssätt under en övergångsperiod.

Brownfield är alltså inte att “bara flytta över” befintliga system. Det är ett förändringsarbete där organisationen behöver avgöra vad som ska bevaras, vad som ska förenklas och vad som måste byggas om.

## Brownfields viktigaste fördelar

Brownfield kan vara klokt när organisationen behöver säkerställa att den nya plattformen fungerar i den faktiska myndighetsmiljön, inte bara i en avgränsad testsituation.

### Närhet till verkliga behov

Brownfield tvingar fram kontakt med verkliga system och verkliga beroenden. Det gör att organisationen tidigt får svar på frågor som annars kan skjutas upp:

- Vilka säkerhetskrav måste plattformen faktiskt möta?
- Hur ser integrationsberoendena ut?
- Vilka driftmönster behöver stödjas?
- Vilka applikationsteam behöver förändra sitt arbetssätt?
- Vilka delar av dagens organisation måste vara med för att införandet ska lyckas?

Denna närhet kan göra beslutsunderlaget bättre. Plattformen formas inte bara efter en idealbild, utan efter de krav som följer av myndighetens uppdrag och systemportfölj.

### Bättre koppling till ordinarie drift

Eftersom brownfield utgår från befintlig miljö blir det svårare att låtsas att drift, support, incidenthantering och förvaltning kan lösas senare.

Det är en styrka. För en myndighet med kritiska tjänster är införande inte färdigt när plattformen fungerar tekniskt. Införandet är först meningsfullt när ansvar, övervakning, felsökning, behörigheter, patchning, backup, återställning och incidentrutiner fungerar i vardagen.

Brownfield kan därför ge en mer realistisk bild av vad organisationen behöver klara innan plattformen betraktas som produktionsduglig.

### Kompetensöverföring sker i verkligt arbete

När befintliga system används som utgångspunkt kan ny plattformskompetens och befintlig driftkompetens mötas i praktiken.

Det kan minska personberoenden om arbetet organiseras rätt. Nyckelpersoner får inte bara “hjälpa till vid sidan av”, utan deras kunskap dokumenteras, delas och översätts till gemensamma arbetssätt.

Det är särskilt viktigt i organisationer där vissa typer av driftskompetens finns hos få personer. Brownfield kan då bli ett sätt att synliggöra och sprida kunskap innan de gamla lösningarna förändras.

### Lägre risk för att bygga fel förmåga

Eftersom brownfield börjar i befintliga behov minskar risken att plattformen optimeras för teoretiska användningsfall som inte matchar organisationens verklighet.

Det betyder inte att brownfield alltid är säkrare. Men det gör att organisationen tidigt upptäcker om målbilden inte håller mot:

- säkerhetsklassning,
- nätverkskrav,
- integrationsmönster,
- upphandlade leveranser,
- bemanning,
- driftfönster,
- incidentkrav,
- dokumentationskrav.

För en chef kan detta vara en stor fördel. Det är bättre att upptäcka svåra beroenden tidigt än att upptäcka dem efter att en ny plattform redan har presenterats som lösningen.

## Brownfields viktigaste nackdelar

Brownfield kan ge god verklighetsförankring, men det kan också bli tungt. Särskilt i organisationer där alla redan är upptagna med daglig drift.

### Hög belastning på nyckelpersoner

Brownfield kräver ofta medverkan från de personer som redan kan den befintliga miljön. Det är också ofta samma personer som hanterar incidenter, undantag, driftproblem och löpande förbättringar.

Om organisationen inte frigör deras tid blir brownfield snabbt ett sidoarbete. Då händer två saker samtidigt:

- förändringen går långsamt,
- risken i daglig drift ökar eftersom nyckelpersoner dras åt flera håll.

Detta är en av brownfields största risker. Ett brownfield-beslut utan kapacitetsbeslut är ofta ett otydligt beslut.

### Arvet kan styra för mycket

Brownfield börjar i det befintliga. Det är en styrka, men också en fara. Om varje gammalt krav, undantag och arbetssätt får följa med utan prövning blir resultatet inte modernisering, utan teknisk omlokalisering.

Då kan organisationen hamna i en situation där den nya plattformen måste stödja nästan alla gamla mönster:

- manuella godkännanden,
- specialbyggda driftsrutiner,
- unika nätverkslösningar,
- lokala undantag,
- otydliga ägarskap,
- bristande dokumentation,
- personliga arbetssätt.

I värsta fall byggs en containerplattform som är lika svårstyrd som den miljö den skulle förbättra.

### Långsammare synlig framdrift

Greenfield kan ofta visa upp något nytt ganska snabbt. Brownfield är mer mödosamt. Mycket arbete sker i kartläggning, beroendeanalys, riskreducering, dokumentation och prioritering.

Det kan skapa otålighet i ledning eller styrgrupp. Om chefen inte har förklarat varför detta arbete behövs kan brownfield uppfattas som trögt, försiktigt eller defensivt.

Här krävs tydlig kommunikation. Brownfield kan vara långsammare i början men minska risken för dyra överraskningar senare.

### Kompromissplattformen

En särskild brownfield-risk är att plattformen blir en kompromiss mellan för många gamla och nya krav. Den ska vara modern, men också stödja alla gamla arbetssätt. Den ska standardisera, men också acceptera alla undantag. Den ska minska personberoenden, men samtidigt byggas av samma få personer som redan bär den gamla miljön.

Resultatet kan bli en plattform som varken är tydligt modern eller tydligt förankrad. Den blir tekniskt ny men organisatoriskt oklar.

## När brownfield är klokt

Brownfield är ofta klokt när organisationen behöver förändra verklig drift, inte bara etablera en ny plattformsidé.

Det talar för brownfield när:

- befintliga system är verksamhetskritiska och måste hanteras varsamt,
- organisationen behöver minska personberoenden genom dokumentation och gemensamt arbete,
- säkerhetskrav och integrationsberoenden är komplexa,
- det finns ett starkt behov av att koppla införandet till ordinarie drift,
- organisationen har mandat att prioritera tid från nyckelpersoner,
- ett verkligt system kan väljas som avgränsat första fall,
- ledningen accepterar att kartläggning och riskreducering är en del av framdriften.

Brownfield passar särskilt väl när organisationen vill använda införandet för att förbättra både teknik och arbetssätt stegvis.

## När brownfield är riskabelt

Brownfield är riskabelt när organisationen inte har kraft att utmana det befintliga.

Det talar emot brownfield när:

- befintlig miljö är så otydligt dokumenterad att förändringen blir beroende av muntlig kunskap,
- nyckelpersoner inte kan frigöras från daglig drift,
- varje gammalt undantag betraktas som obligatoriskt,
- styrningen saknar mod att prioritera bort eller förenkla,
- organisationen vill ha snabb effekt men inte kan acceptera övergångsarbete,
- det saknas tydlig målbild för vad som ska bli annorlunda,
- plattformen riskerar att bli en ny plats för gamla problem.

I sådana lägen kan brownfield kännas tryggt men i praktiken vara mycket riskfyllt.

## Viktigt beslutsunderlag för brownfield

Innan en chef godkänner ett brownfield-spår bör följande underlag finnas på bordet.

| Underlag | Varför det behövs | Minimikrav |
|---|---|---|
| Systemportfölj | Visar vilka system som kan vara aktuella och hur kritiska de är | Lista över kandidatsystem, kritikalitet och ägare |
| Beroendekarta | Synliggör integrationer, driftberoenden och säkerhetskrav | De viktigaste tekniska och organisatoriska beroendena |
| Kompetens- och personberoendeanalys | Visar vilka personer eller team som är nödvändiga | Nyckelroller, sårbara beroenden och plan för kunskapsdelning |
| Kapacitetsbedömning | Visar om organisationen har tid att genomföra förändringen | Tydligt beslut om frigjord tid och prioritering |
| Målbild för modernisering | Hindrar att allt gammalt följer med | Principer för vad som ska bevaras, ändras och avvecklas |
| Riskanalys | Gör konsekvenserna synliga innan start | Risker, ägare, åtgärder och beslutspunkter |

Om detta underlag saknas bör beslutet inte beskrivas som ett genomförandebeslut. Då är nästa steg snarare att ta fram underlaget.

## Brownfield-riskbedömning

Använd frågorna nedan som en enkel workshop med styrgrupp, drift, säkerhet, arkitektur och berörda systemägare.

### Steg 1: Bedöm nuläget

Svara på varje fråga med låg, medel eller hög risk.

| Fråga | Låg risk | Medelrisk | Hög risk |
|---|---|---|---|
| Är kandidatsystemets beroenden kända? | Ja, dokumenterade | Delvis kända | Främst muntlig kunskap |
| Finns nyckelpersoner tillgängliga? | Ja, tid är prioriterad | Delvis | Nej, de är låsta i daglig drift |
| Finns tydlig systemägare och beslutsmandat? | Ja | Delvis | Oklart |
| Är säkerhetskraven förstådda? | Ja, tidigt involverade | Delvis | Oklara eller sena |
| Finns målbild för vad som ska förändras? | Ja | Delvis | Nej, fokus är bara flytt |
| Kan driftansvar hanteras under övergången? | Ja | Delvis | Oklart eller personberoende |

### Steg 2: Tolka resultatet

- **Mest låg risk:** Brownfield kan vara ett rimligt första vägval.
- **Flera medelrisker:** Brownfield kan fungera, men kräver tydliga riskåtgärder innan start.
- **En eller flera höga risker i kapacitet, beroenden eller mandat:** Pausa genomförandebeslutet och stärk underlaget först.

### Steg 3: Besluta om åtgärder före start

För varje medel- eller högriskpunkt bör styrgruppen besluta:

- vem som äger risken,
- vilken åtgärd som krävs,
- när åtgärden ska vara klar,
- vad som händer om risken kvarstår.

Det viktiga är att riskbedömningen leder till beslut, inte bara dokumentation.

## Vanliga misstag

- **Misstag: Att kalla en teknisk flytt för modernisering.**
  - Varför det händer: Det känns som framsteg när ett system hamnar på en ny plattform.
  - Hur du undviker det: Kräv en målbild för vad som faktiskt ska bli bättre i arbetssätt, drift, säkerhet och livscykelhantering.

- **Misstag: Att inte frigöra nyckelpersoner.**
  - Varför det händer: Organisationen vill både behålla full daglig leverans och genomföra förändring.
  - Hur du undviker det: Gör kapacitetsbeslutet lika formellt som teknikbeslutet.

- **Misstag: Att låta alla gamla undantag följa med.**
  - Varför det händer: Undantag uppfattas som krav eftersom ingen har mandat att ifrågasätta dem.
  - Hur du undviker det: Skilj mellan verkliga krav, historiska vanor och tillfälliga lösningar som blivit permanenta.

- **Misstag: Att välja fel första system.**
  - Varför det händer: Organisationen väljer antingen det enklaste systemet eller det mest synliga.
  - Hur du undviker det: Välj ett system som är tillräckligt verkligt för lärande men inte så kritiskt att varje problem blir en kris.

- **Misstag: Att skjuta upp driftmodellen.**
  - Varför det händer: Fokus hamnar på migrering och tekniska beroenden.
  - Hur du undviker det: Definiera driftansvar, support, övervakning, incidenthantering och livscykelhantering innan första produktionssättning.

## Övning: Brownfield-riskbedömning

Använd denna övning i en ledningsgrupp, styrgrupp eller förberedande workshop.

### Del 1: Välj ett kandidatsystem

Välj ett befintligt system som skulle kunna bli första eller tidigt brownfield-fall.

Beskriv kort:

- verksamhetsnytta,
- systemägare,
- kritikalitet,
- viktigaste integrationer,
- nuvarande driftmodell,
- kända personberoenden.

### Del 2: Bedöm systemet

Bedöm kandidatsystemet utifrån fem frågor.

| Fråga | Bedömning | Kommentar |
|---|---|---|
| Är systemets beroenden tillräckligt kända? | Låg/medel/hög risk | |
| Kan rätt personer frigöras? | Låg/medel/hög risk | |
| Finns tydligt mandat att förenkla? | Låg/medel/hög risk | |
| Är säkerhets- och driftkrav kända? | Låg/medel/hög risk | |
| Finns en tydlig målbild bortom teknisk flytt? | Låg/medel/hög risk | |

### Del 3: Fatta ett förberedande beslut

Välj ett av följande beslut:

- Gå vidare med brownfield för detta system.
- Gå vidare först efter riskreducerande åtgärder.
- Välj ett annat kandidatsystem.
- Använd greenfield eller hybrid som första steg i stället.

Skriv också ned varför beslutet är rimligt. Det gör att styrgruppen kan följa upp beslutet senare.

## Snabb sammanfattning

- Brownfield utgår från befintliga system, arbetssätt, beroenden och driftmodeller.
- Brownfield kan ge stark verklighetsförankring och bättre koppling till ordinarie drift.
- Den största risken är att gamla problem byggs in i den nya plattformen.
- Brownfield kräver frigjord tid från nyckelpersoner, tydligt mandat och god beroendekartläggning.
- Ett brownfield-beslut utan kapacitetsbeslut är ofta ett otydligt beslut.
- Första systemet bör vara verkligt nog för lärande men inte så kritiskt att risknivån blir orimlig.
- Målet är inte att flytta system, utan att bygga bättre organisatorisk och teknisk förmåga.

## Quiz/reflektionsfrågor

1. Vilka delar av er befintliga miljö är tillgångar som bör tas med in i ett brownfield-spår?
2. Vilka delar är arv som bör förenklas, avvecklas eller ersättas?
3. Vilka nyckelpersoner skulle ett brownfield-spår bli beroende av?
4. Har dessa personer faktiskt tid att delta utan att daglig drift riskeras?
5. Vilket befintligt system skulle vara ett klokt första brownfield-fall?
6. Vad skulle göra att brownfield i er organisation bara blir en teknisk flytt?

## Nästa steg

Brownfield visar styrkan i att börja nära verkligheten. Greenfield visar styrkan i att skapa handlingsutrymme. I många myndigheter räcker inte något av vägvalen ensamt.

Nästa kapitel handlar därför om hybridvägen: hur organisationen kan bygga ny plattformsförmåga samtidigt som befintliga system moderniseras stegvis, utan att hybrid blir ett sätt att skjuta upp svåra beslut.
