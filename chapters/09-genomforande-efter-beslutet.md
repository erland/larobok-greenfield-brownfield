# Kapitel 9: Genomförande efter beslutet

## Varför detta kapitel finns

Ett beslut om greenfield, brownfield eller hybrid är bara värdefullt om det leder till ett genomförande som organisationen klarar av. I en större myndighet är det vanligt att själva beslutet får stor uppmärksamhet, medan genomförandet behandlas som något som kan lösas av projektet, tekniken eller några få nyckelpersoner.

Det är en risk.

Införande av containerplattform, exempelvis OpenShift, påverkar ansvar, arbetssätt, säkerhetsprocesser, drift, incidenthantering, kompetensförsörjning och styrning. Om genomförandet inte utformas efter det vägval som gjorts kan organisationen hamna i just de problem som beslutet skulle undvika.

Ett greenfield-beslut kan skapa en modern men isolerad miljö om kopplingen till ordinarie verksamhet är svag.

Ett brownfield-beslut kan fastna i befintliga beroenden om förändringen inte får tillräckligt mandat.

Ett hybridbeslut kan bli otydligt om det inte finns en tydlig övergångsplan.

Kapitlet visar hur genomförandet bör läggas upp efter beslutet. Fokus ligger på de första praktiska stegen, de vanligaste riskerna och vad chefen behöver följa upp tidigt.

## Lärandemål

Efter kapitlet ska du kunna:

- översätta vägvalet till en tydlig genomförandeplan,
- förstå vad som skiljer greenfield-, brownfield- och hybridgenomförande,
- formulera mandat, ansvar och övergångsplan på chefsnivå,
- välja första pilot eller första system utan att skapa onödig risk,
- planera kompetensöverföring så att personberoenden minskar,
- skapa en enkel 90-dagarsplan för de första stegen.

## Innan vi börjar

Beslutsmodellen i förra kapitlet gav en rekommendation. Den rekommendationen bör innehålla villkor. Dessa villkor är startpunkten för genomförandet.

Exempel på villkor kan vara:

- plattformsteamet ska ha tydligt mandat,
- driftorganisationen ska avsätta namngiven tid,
- säkerhetsfunktionen ska vara med från början,
- första pilot ska väljas utifrån dokumenterade kriterier,
- ansvar för incidenter och support ska vara beskrivet innan produktion,
- nyckelpersoner ska inte bära genomförandet ensamma,
- beslutspunkter ska finnas där införandet kan bromsas, ändras eller förstärkas.

Om beslutet saknar sådana villkor bör de tas fram innan genomförandet startar. Annars riskerar organisationen att gå från ett otydligt beslut till ett ännu otydligare projekt.

## Den första styrfrågan efter beslutet

När beslutet är fattat bör ledningen inte börja med frågan:

> När är plattformen klar?

Den första frågan bör vara:

> Vilken organisatorisk förmåga ska vara på plats först, och vem ansvarar för att den fungerar?

Det skiftar fokus från installation till användbarhet.

En containerplattform kan vara tekniskt installerad men organisatoriskt ofärdig. Den kan sakna tydliga regler för vem som får använda den, hur applikationer tas ombord, hur incidenter hanteras, hur sårbarheter åtgärdas, hur kostnader följs upp och hur driftansvar fördelas.

Därför behöver genomförandet börja med ansvar och förmåga, inte bara med teknik.

## Genomförande om ni väljer greenfield

Greenfield innebär att organisationen bygger en ny miljö eller förmåga med begränsad direkt koppling till befintlig miljö. Det kan ge fart, tydlighet och möjlighet att etablera moderna arbetssätt. Men risken är att den nya miljön inte blir mottagen av den ordinarie organisationen.

### Säkra mandatet

Ett greenfield-initiativ behöver ett tydligt uppdrag. Det ska inte bara vara ett tekniskt experiment.

Mandatet bör svara på följande frågor:

- Varför bygger vi nytt?
- Vilken verksamhetsnytta ska den nya plattformen skapa?
- Vilka system eller team ska plattformen först stödja?
- Vem äger plattformen efter införandeprojektet?
- Vilka beslut får plattformsteamet fatta själv?
- Vilka beslut kräver styrgrupp eller linjeorganisation?
- Vilka gamla arbetssätt får inte följa med in i den nya miljön?

Om mandatet är otydligt kan greenfield snabbt bli ett attraktivt sidospår. Det kan fungera väl för demonstrationer men svagt för verklig produktion.

### Välj pilot som prövar verkligheten

Ett greenfield-spår behöver ett pilotfall, men piloten får inte vara för bekväm. Om piloten bara visar att tekniken fungerar visar den för lite.

En bra pilot bör pröva flera saker samtidigt:

- hur applikationsteam använder plattformen,
- hur säkerhetskrav hanteras,
- hur drift och övervakning fungerar,
- hur incidenter eskaleras,
- hur behörigheter styrs,
- hur dokumentation och standarder används,
- hur stöd ges till team som inte är containerspecialister.

Piloten ska inte nödvändigtvis vara det mest kritiska systemet. Den ska vara tillräckligt verklig för att avslöja organisatoriska problem, men inte så kritisk att minsta lärande blir oacceptabelt dyrt.

### Bygg mottagande organisation tidigt

Den största greenfield-risken är att den nya plattformen byggs snabbare än organisationen kan ta emot den. Därför bör mottagande organisation definieras tidigt.

Det handlar om:

- vem som tar över driftansvar,
- vem som äger standarder,
- vem som prioriterar vidareutveckling,
- vem som stödjer applikationsteam,
- vem som godkänner säkerhetsmönster,
- vem som följer upp kostnad och kapacitet,
- vem som beslutar om undantag.

Om dessa frågor lämnas till slutet kan plattformen bli tekniskt klar men organisatoriskt hemlös.

### Undvik greenfield-fällorna

Vanliga greenfield-fällor är:

- **Fälla: Att mäta framgång i installerad teknik.**
  - Motåtgärd: Mät i stället användbar förmåga, fungerande ansvar och verifierade arbetssätt.

- **Fälla: Att välja en pilot utan organisatorisk friktion.**
  - Motåtgärd: Välj en pilot som prövar drift, säkerhet, support och styrning.

- **Fälla: Att skapa ett expertberoende i det nya.**
  - Motåtgärd: Kräv dokumentation, pararbete, utbildning och rotationsmöjligheter.

- **Fälla: Att skjuta upp överlämning till linjen.**
  - Motåtgärd: Definiera mottagande organisation och överlämningskriterier från start.

## Genomförande om ni väljer brownfield

Brownfield innebär att organisationen utgår från befintliga system, arbetssätt, beroenden och driftmodeller. Det kan ge stark verklighetskoppling och minska risken för att plattformen blir ett sidospår. Men det kan också göra förändringen långsam, tung och beroende av samma personer som redan är hårt belastade.

### Välj första system med omsorg

Det första systemet i ett brownfield-genomförande är viktigt. Det blir ofta mönsterbildande.

Ett olämpligt första system kan skapa fel slutsatser. Ett för enkelt system kan ge falsk trygghet. Ett för komplext system kan skapa motstånd och överbelastning. Ett system som ägs av fel team kan göra genomförandet politiskt eller praktiskt svårt.

Ett bra första system bör ha:

- tydlig ägare,
- rimlig verksamhetsbetydelse,
- kända beroenden,
- hanterbar teknisk komplexitet,
- tillgängliga nyckelpersoner,
- tydliga säkerhetskrav,
- nytta av containerplattformens förmågor,
- möjlighet att dokumentera lärande.

Det behöver inte vara det system som tekniskt passar bäst. Det bör vara det system som ger mest användbart lärande med acceptabel risk.

### Frigör nyckelpersoner

Brownfield kräver ofta personer som redan är centrala i den dagliga driften. Om dessa personer bara får bidra vid sidan av sina ordinarie uppgifter blir förändringen skör.

Chefen behöver därför säkerställa faktisk tid, inte bara formellt deltagande.

Frågor att ställa:

- Vilka nyckelpersoner behövs?
- Vad gör de i dag?
- Vad kan prioriteras ned eller flyttas?
- Vem ersätter dem i löpande drift?
- Hur dokumenteras deras kunskap?
- Hur sprids kunskapen till fler?
- Vilken risk uppstår om de blir otillgängliga?

Om svaret är att ingen kan frigöras bör brownfield-planen omprövas. Ett brownfield-genomförande utan frigjord kompetens blir ofta en belastningsövning, inte en kontrollerad förändring.

### Dokumentera medan ni förändrar

Brownfield är ett tillfälle att minska personberoenden. Det sker inte automatiskt. Det kräver att dokumentation, standardisering och kunskapsöverföring byggs in i arbetet.

Dokumentationen bör fokusera på sådant som faktiskt behövs för att drifta och förändra systemet:

- beroenden,
- integrationspunkter,
- driftsteg,
- incidentrutiner,
- övervakning,
- behörigheter,
- säkerhetskrav,
- undantag,
- kända risker,
- beslut som fattats under migreringen.

Syftet är inte att skriva perfekta dokument. Syftet är att göra organisationen mindre beroende av att rätt person alltid är tillgänglig.

### Undvik brownfield-fällorna

Vanliga brownfield-fällor är:

- **Fälla: Att låta gamla undantag bli nya standarder.**
  - Motåtgärd: Besluta vilka undantag som får följa med och vilka som ska avvecklas.

- **Fälla: Att underskatta belastningen på driftorganisationen.**
  - Motåtgärd: Frigör tid, minska parallella initiativ och följ upp faktisk belastning.

- **Fälla: Att migrera utan lärande.**
  - Motåtgärd: Dokumentera beslut, beroenden och återanvändbara mönster efter varje steg.

- **Fälla: Att kalla allt för modernisering.**
  - Motåtgärd: Skilj mellan flytt, teknisk anpassning, arbetssättsförändring och verklig förmågeförbättring.

## Genomförande om ni väljer hybrid

Hybrid innebär att organisationen kombinerar greenfield och brownfield. Det är ofta den mest realistiska vägen i större myndigheter, men den kräver tydlig styrning. Annars blir hybrid bara ett sätt att säga ja till allt.

### Definiera vad som är nytt och vad som förändras stegvis

Ett hybridgenomförande bör börja med en enkel uppdelning:

- Vad bygger vi nytt?
- Vad förändrar vi i befintlig miljö?
- Vad ska koppla ihop det gamla och det nya?
- Vad ska avvecklas?
- Vad får leva kvar under en övergång?
- När ska vi ompröva planen?

Utan denna uppdelning blir det svårt att se om hybridvägen faktiskt minskar risk eller bara sprider risk över fler spår.

### Skapa en övergångsplan

Hybrid kräver en övergångsplan. Den bör beskriva hur organisationen går från dagens läge till målbilden utan att tappa styrbarhet.

En enkel övergångsplan bör innehålla:

- målbild för plattformsförmågan,
- vilka system eller team som omfattas i första vågen,
- vilka arbetssätt som gäller direkt,
- vilka arbetssätt som införs senare,
- vilka beroenden som måste hanteras,
- vilka undantag som accepteras tillfälligt,
- när undantag ska omprövas,
- vem som äger övergången,
- vilka beslutspunkter som finns.

Övergångsplanen ska vara tillräckligt konkret för att styra prioriteringar. Den ska inte vara en allmän ambitionsbild.

### Styr dubbelheten öppet

Hybrid innebär nästan alltid att gammalt och nytt existerar parallellt. Det är inte ett misslyckande. Det är en förutsättning som måste styras.

Ledningen bör följa upp:

- hur länge dubbelheten ska vara acceptabel,
- vilka kostnader dubbelheten skapar,
- vilka personer som belastas av båda världarna,
- vilka risker som ökar under övergången,
- vilka system som står näst på tur,
- vilka beslut som behövs för att undvika permanent parallellitet.

Om dubbelheten inte följs upp kan hybrid bli ett permanent tillstånd där organisationen både behåller det gamla och finansierar det nya utan att få ut avsedd effekt.

### Undvik hybrid-fällorna

Vanliga hybrid-fällor är:

- **Fälla: Att använda hybrid som kompromiss utan prioritering.**
  - Motåtgärd: Ange tydligt vad som ska göras först, senare och inte alls.

- **Fälla: Att sakna avvecklingslogik.**
  - Motåtgärd: Beskriv vilka delar av befintlig miljö, arbetssätt eller undantag som ska fasas ut.

- **Fälla: Att underskatta styrningsbehovet.**
  - Motåtgärd: Skapa tydliga beslutspunkter och ägarskap för övergången.

- **Fälla: Att låta båda spåren konkurrera om samma personer.**
  - Motåtgärd: Planera bemanning utifrån verklig kapacitet, inte önskad tillgänglighet.

## Det chefen behöver äga

Chefen behöver inte äga varje teknisk detalj. Men chefen behöver äga de frågor som gör införandet möjligt.

Det gäller särskilt:

- mandat,
- prioritering,
- resurskonflikter,
- kompetensförsörjning,
- mottagande organisation,
- riskacceptans,
- uppföljning,
- beslutspunkter,
- förmågan att säga nej till orealistiska antaganden.

Ett vanligt problem är att chefen delegerar bort för mycket till projektet. Projektet kan driva aktiviteter, men det kan inte ensamt lösa linjeorganisationens kapacitet, otydligt ansvar eller konflikt mellan daglig drift och förändring.

Chefen behöver därför ställa praktiska styrfrågor:

- Har genomförandet ett tydligt uppdrag?
- Har rätt personer faktisk tid?
- Är säkerhet, drift och verksamhet med från början?
- Vet vi vad som ska vara sant efter 90 dagar?
- Vet vi vad som ska stoppas, pausas eller prioriteras ned?
- Finns beslutspunkter där vi kan ändra riktning?
- Minskar vi personberoenden eller flyttar vi dem?

## De första 90 dagarna

De första 90 dagarna bör inte försöka lösa allt. De bör skapa riktning, synliggöra risker och etablera arbetssätt som går att bygga vidare på.

En enkel 90-dagarsplan kan delas upp i tre delar.

### Dag 1–30: Gör beslutet genomförbart

Fokus:

- bekräfta beslut, villkor och mandat,
- utse ansvariga roller,
- säkra tid hos nyckelpersoner,
- etablera styrforum,
- bekräfta säkerhets- och driftmedverkan,
- välja pilot eller första system,
- identifiera de viktigaste riskerna.

Resultatet efter 30 dagar bör vara att organisationen vet vem som gör vad, varför och med vilka begränsningar.

### Dag 31–60: Pröva i kontrollerad skala

Fokus:

- starta pilot eller första brownfield-steg,
- dokumentera beroenden och beslut,
- pröva incident- och supportflöden,
- testa säkerhetsmönster,
- följa upp belastning på nyckelpersoner,
- justera standarder utifrån faktisk erfarenhet.

Resultatet efter 60 dagar bör vara att organisationen har verkligt lärande, inte bara planering.

### Dag 61–90: Besluta om nästa steg

Fokus:

- sammanfatta lärdomar,
- jämföra resultat med beslutets villkor,
- identifiera nya risker,
- besluta om fortsatt omfattning,
- justera bemanning och mandat,
- planera nästa våg,
- besluta om stopp, fortsättning eller ändrad riktning.

Resultatet efter 90 dagar bör vara ett medvetet nästa beslut, inte bara fortsatt aktivitet.

## Workshop: skapa första 90-dagarsplanen

Samla beslutsägare, plattformsteam, drift, säkerhet, verksamhetsrepresentant och representanter för berörda system eller applikationsteam.

Arbeta i fem steg:

1. Skriv vägvalet med en mening: greenfield, brownfield eller hybrid.
2. Lista beslutets viktigaste villkor.
3. Identifiera vad som måste vara sant efter 30, 60 och 90 dagar.
4. Markera vilka personer eller funktioner som har för lite tid.
5. Bestäm första beslutspunkt och vilka underlag som ska finnas där.

Använd gärna denna enkla mall:

| Tidpunkt | Vad ska vara uppnått? | Ansvarig | Viktigaste risk | Beslutsunderlag |
|---|---|---|---|---|
| Dag 30 | | | | |
| Dag 60 | | | | |
| Dag 90 | | | | |

Avsluta workshopen med tre frågor:

- Vilket antagande är mest osäkert?
- Vilken resurskonflikt måste lösas av chef eller styrgrupp?
- Vad ska vi inte göra under de första 90 dagarna?

Den sista frågan är viktig. Ett genomförande blir ofta mer realistiskt när organisationen tydligt anger vad som ska vänta.

## Vanliga misstag

- **Misstag: Att starta genomförandet utan tydliga villkor.**
  - Varför det händer: Beslutet uppfattas som tillräckligt tydligt.
  - Hur du undviker det: Översätt beslutet till mandat, ansvar, villkor och beslutspunkter.

- **Misstag: Att anta att ny teknik automatiskt minskar personberoende.**
  - Varför det händer: Plattformen uppfattas som standardiserande.
  - Hur du undviker det: Planera aktiv kompetensöverföring, dokumentation och teamförmåga.

- **Misstag: Att underskatta den dagliga driftens tyngd.**
  - Varför det händer: Införandet planeras som projekt, medan driftbelastningen ses som bakgrund.
  - Hur du undviker det: Följ upp faktisk tillgänglighet och prioritera bort annat arbete.

- **Misstag: Att låta pilot bli permanent undantag.**
  - Varför det händer: Piloten lyckas tekniskt men saknar övergång till ordinarie modell.
  - Hur du undviker det: Sätt överlämningskriterier och beslutspunkt redan från start.

- **Misstag: Att fortsätta trots att villkor inte är uppfyllda.**
  - Varför det händer: Organisationen vill visa framdrift.
  - Hur du undviker det: Använd stoppunkter som legitim styrning, inte som misslyckande.

## Snabb sammanfattning

- Ett beslut om vägval behöver översättas till mandat, ansvar, villkor och genomförandeplan.
- Greenfield kräver särskilt fokus på mottagande organisation, verklig pilot och undvikande av isolerad ö.
- Brownfield kräver särskilt fokus på första system, frigjorda nyckelpersoner, dokumentation och belastning på drift.
- Hybrid kräver särskilt fokus på övergångsplan, dubbel styrning och avvecklingslogik.
- Chefen behöver äga prioriteringar, resurskonflikter, riskacceptans och beslutspunkter.
- De första 90 dagarna bör skapa riktning, pröva verkligheten och ge underlag för nästa beslut.
- Genomförandet ska minska personberoenden, inte bara flytta dem till en ny teknisk miljö.

## Quiz/reflektionsfrågor

1. Vilka villkor i beslutet är viktigast för att genomförandet ska lyckas?
2. Vilka personer eller funktioner är mest belastade redan i dag?
3. Vilket pilotfall eller första system skulle ge mest relevant lärande med acceptabel risk?
4. Vilka gamla undantag riskerar att följa med in i den nya plattformen?
5. Vad behöver vara sant efter 90 dagar för att ni ska fortsätta med förtroende?

## Nästa steg

När genomförandet har startat behöver ledningen följa upp om införandet faktiskt skapar organisatorisk förmåga. Nästa kapitel visar hur styrgrupp och chefer kan följa upp effekter, riskindikatorer, kompetensspridning och lärande över tid.
