# Kapitel 1: Vad är det som införs?

## Varför detta kapitel finns

Innan en organisation kan välja mellan greenfield, brownfield eller hybrid behöver den vara överens om vad införandet faktiskt innebär.

Det är lätt att beskriva ett införande av OpenShift eller annan containerplattform som ett teknikprojekt. Då blir frågan ungefär: “Vilken plattform ska vi installera, och var ska den köras?” För en större myndighet är det sällan tillräckligt. Den verkliga frågan är oftare: “Vilken ny förmåga behöver organisationen, och hur ska den förvaltas utan att skapa nya risker?”

Kapitlet ger en chefsnivåbild av containerplattformar. Målet är inte att göra läsaren till teknisk specialist, utan att skapa ett gemensamt språk inför vägvalet.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- beskriva containerplattformar som en organisatorisk och teknisk förmåga,
- skilja mellan att införa en produkt och att införa ett arbetssätt,
- identifiera vilka förmågor organisationen förväntar sig av plattformen,
- se varför införandet påverkar drift, säkerhet, kompetens, ansvar och styrning.

## Innan vi börjar

Bokens inledning beskrev greenfield, brownfield och hybrid som olika vägar för att införa eller förändra en förmåga. I detta kapitel backar vi ett steg och frågar vad förmågan består av.

När en myndighet diskuterar OpenShift handlar samtalet ofta om teknik: kluster, containrar, nätverk, säkerhet, lagring och integrationer. Dessa delar är viktiga, men för beslutet är de inte hela bilden. En containerplattform påverkar hur applikationer byggs, driftsätts, övervakas, uppdateras, säkras och avvecklas.

Det är därför mer användbart att se införandet som etablering av en plattformsförmåga.

## Containerplattform på chefsnivå

En containerplattform är en gemensam miljö för att köra och hantera applikationer som paketeras i containrar. OpenShift är ett exempel på en sådan plattform.

På chefsnivå är det viktigaste inte exakt hur containrar fungerar. Det viktiga är vad plattformen gör möjligt och vad den kräver av organisationen.

En containerplattform kan ge organisationen:

- mer standardiserad applikationsdrift,
- tydligare gränssnitt mellan utveckling och drift,
- högre grad av automatisering,
- bättre stöd för snabbare och mer kontrollerade leveranser,
- gemensamma säkerhets- och driftmönster,
- bättre spårbarhet kring versioner, beroenden och ändringar,
- möjlighet att minska variationen mellan olika systemmiljöer.

Men plattformen skapar inte dessa effekter av sig själv. Effekterna uppstår först när organisationen har arbetssätt, roller, mandat och kompetens som kan använda plattformen på ett konsekvent sätt.

Det är en central poäng för hela boken: containerplattformen är inte bara en teknisk komponent. Den är en del av en styrd leverans- och driftmodell.

## Från produkt till förmåga

Ett vanligt misstag är att behandla införandet som inköp och installation av en produkt. Då hamnar beslutet lätt i frågor som rör licenser, installation, hosting, teknisk design och leverantörsstöd. Dessa frågor är nödvändiga, men de räcker inte.

En myndighet behöver också avgöra vilken förmåga som ska byggas. Det kan exempelvis handla om att organisationen ska kunna:

- ta emot nya applikationer på ett standardiserat sätt,
- flytta utvalda befintliga system till en modernare driftmodell,
- minska manuella moment vid driftsättning,
- minska beroendet av enskilda driftspecialister,
- höja säkerhetsnivån genom gemensamma kontroller,
- skapa tydligare ansvar mellan applikationsteam, plattformsteam och drift,
- förvalta plattformen långsiktigt med rimlig bemanning.

Skillnaden är viktig. En installerad plattform utan förmåga blir lätt ännu en teknisk miljö att underhålla. En etablerad plattformsförmåga kan däremot förändra hur organisationen levererar och förvaltar IT.

## De fem förmågorna som beslutet bör omfatta

När en chef ska förstå vad som införs är det praktiskt att dela upp plattformsförmågan i fem delar.

### 1. Driftförmåga

Driftförmågan handlar om att plattformen ska kunna köras stabilt, övervakas, uppdateras och hanteras vid incidenter.

För en myndighet är detta särskilt viktigt eftersom många system kan ha höga krav på tillgänglighet, säkerhet och spårbarhet. Frågan är inte bara om plattformen fungerar i ett testläge. Frågan är om organisationen kan drifta den under vardag, förändring och störning.

En chef bör därför fråga:

- Vem ansvarar för plattformens drift?
- Hur ser jour, incidenthantering och eskalering ut?
- Vilka personer eller team kan felsöka när något går fel?
- Hur undviker vi att nyckelpersoner blir flaskhalsar?

### 2. Leveransförmåga

Leveransförmågan handlar om hur applikationer kommer in på plattformen och förändras över tid.

En containerplattform kan stödja snabbare och säkrare driftsättningar, men bara om det finns gemensamma arbetssätt. Annars riskerar varje applikationsteam att skapa sin egen variant, vilket leder till ny komplexitet.

En chef bör därför fråga:

- Vilka krav måste ett system uppfylla för att få använda plattformen?
- Hur ser processen ut från utveckling till produktion?
- Vilka delar är automatiserade och vilka är manuella?
- Hur säkerställs att applikationsteam och drift arbetar mot samma mål?

### 3. Säkerhetsförmåga

Säkerhetsförmågan handlar om hur plattformen skyddar applikationer, data, identiteter och infrastruktur.

I en större myndighet behöver säkerhet vara inbyggd i styrning och arbetssätt, inte bara hanteras som tekniska kontroller i efterhand. Plattformen kan bidra med gemensamma mönster, men den kan också skapa nya risker om ansvar, behörigheter och gränser är otydliga.

En chef bör därför fråga:

- Vilka säkerhetskrav gäller för de system som kan bli aktuella?
- Hur hanteras identiteter, behörigheter och åtkomst?
- Vem godkänner gemensamma säkerhetsmönster?
- Hur följs avvikelser upp?

### 4. Kompetensförmåga

Kompetensförmågan handlar om att organisationen kan förstå, använda och förvalta plattformen utan att bli beroende av ett fåtal personer.

Detta är ofta en av de mest underskattade delarna. Om organisationen redan är hårt belastad och personberoende kan en ny plattform både vara en lösning och en risk. Den kan minska gamla beroenden på sikt, men under införandet kan den öka belastningen på samma nyckelpersoner som redan är överbelastade.

En chef bör därför fråga:

- Vilken kompetens finns i dag?
- Vilken kompetens saknas?
- Vilka personer kommer att belastas mest under införandet?
- Hur sker kompetensöverföring från projekt till linje?
- Hur dokumenteras arbetssätt så att kunskap inte fastnar hos enskilda?

### 5. Styrningsförmåga

Styrningsförmågan handlar om beslut, prioriteringar, mandat och uppföljning.

Utan styrning kan plattformen bli en teknisk möjlighet som används ojämnt, eller ett prestigeprojekt som saknar verklig förankring. Med rätt styrning blir plattformen i stället en del av myndighetens samlade IT-förmåga.

En chef bör därför fråga:

- Vilka mål ska införandet uppnå?
- Vilka system eller verksamhetsbehov prioriteras först?
- Vem får besluta om undantag?
- Hur mäts om plattformen faktiskt ger önskad effekt?
- När ska beslutet omprövas?

## Varför detta påverkar greenfield och brownfield

När plattformen ses som en förmåga blir vägvalet tydligare.

Ett greenfield-tillvägagångssätt kan vara attraktivt om organisationen vill bygga förmågan rent, kontrollerat och utan att direkt bära med sig alla befintliga beroenden. Det kan ge tempo och tydlighet. Samtidigt finns risken att den nya förmågan etableras vid sidan av den verklighet där systemen, människorna och driftsansvaret redan finns.

Ett brownfield-tillvägagångssätt kan vara attraktivt om organisationen vill utgå från verkliga system, befintliga beroenden och faktisk drift. Det kan ge bättre förankring och mer realistiska prioriteringar. Samtidigt finns risken att den nya plattformen formas för mycket av gamla arbetssätt, gamla kompromisser och befintliga personberoenden.

Det är därför beslutet inte kan fattas enbart genom att fråga vilken teknisk väg som är modernast. Beslutet måste kopplas till vilken förmåga organisationen klarar att bygga, ta emot och förvalta.

## Exempel: teknikinförande eller förmågeinförande

Tänk på två sätt att formulera samma initiativ.

Den första formuleringen är teknikorienterad:

> Vi ska införa OpenShift som ny containerplattform.

Den andra formuleringen är förmågeorienterad:

> Vi ska etablera en gemensam plattformsförmåga för att driftsätta, säkra, övervaka och livscykelhantera utvalda applikationer på ett mer standardiserat och mindre personberoende sätt.

Den första formuleringen kan vara korrekt, men den är för smal. Den säger inget om varför plattformen behövs, vem som ska använda den, hur driftansvar ska fungera eller vilka effekter som ska uppnås.

Den andra formuleringen är mer användbar för ett chefsbeslut. Den visar att införandet kräver både teknik, arbetssätt, kompetens och styrning.

## Beslutsfråga för kapitlet

Innan organisationen väljer greenfield eller brownfield bör chefen säkerställa att ledning, IT, säkerhet, drift och berörda verksamheter kan svara på en gemensam fråga:

> Vilken plattformsförmåga ska vi bygga, och vilka organisatoriska förutsättningar krävs för att den ska fungera i praktiken?

Om svaret är otydligt är risken stor att greenfield och brownfield diskuteras på fel nivå. Då jämför man miljöer, inte förmågor.

## Vanliga misstag

- **Misstag: Att se plattformen som en produkt snarare än en förmåga.**
  - Varför det händer: Det är enklare att prata om installation, licenser och teknik än om ansvar, arbetssätt och kompetens.
  - Hur du undviker det: Beskriv alltid vilka organisatoriska förmågor plattformen ska skapa eller förstärka.

- **Misstag: Att anta att automatisering automatiskt minskar belastningen.**
  - Varför det händer: Automatisering förknippas ofta med effektivisering.
  - Hur du undviker det: Bedöm först vem som ska bygga, förvalta och felsöka automatiseringen.

- **Misstag: Att underskatta mottagande organisation.**
  - Varför det händer: Projekt fokuserar ofta på att etablera tekniken, inte på hur linjen ska ta över.
  - Hur du undviker det: Definiera tidigt driftmodell, supportansvar, kompetensöverföring och dokumentationskrav.

- **Misstag: Att låta plattformen bli ett expertområde för några få.**
  - Varför det händer: Ny teknik drivs ofta av engagerade specialister.
  - Hur du undviker det: Sätt krav på gemensamma arbetssätt, utbildning, pararbete, dokumentation och successiv breddning av kompetens.

## Workshop: lista förväntade plattformsförmågor

Syftet med övningen är att flytta samtalet från teknikval till förmågebehov.

### Steg 1: Lista förväntade effekter

Samla en mindre grupp med representanter från beslut, drift, säkerhet, arkitektur och berörda verksamheter. Be gruppen lista vilka effekter man förväntar sig av containerplattformen.

Använd gärna dessa startfrågor:

- Ska plattformen främst ge snabbare leveranser?
- Ska den minska driftvariation?
- Ska den förbättra säkerhet och spårbarhet?
- Ska den minska personberoende?
- Ska den möjliggöra modernisering av befintliga system?
- Ska den skapa en standardiserad väg för nya system?

### Steg 2: Översätt effekter till förmågor

För varje förväntad effekt, skriv vilken förmåga som krävs.

| Förväntad effekt | Förmåga som krävs | Vem påverkas? |
|---|---|---|
| Mindre personberoende | Dokumenterade arbetssätt och bredare plattformskompetens | Drift, plattformsteam, applikationsteam |
| Snabbare driftsättningar | Automatiserad leveransprocess och tydliga godkännanden | Utveckling, säkerhet, drift |
| Bättre säkerhetskontroll | Gemensamma säkerhetsmönster och uppföljning | Säkerhet, arkitektur, drift |
| Stabilare drift | Tydlig incident-, övervaknings- och uppdateringsmodell | Drift, support, leverantörer |

### Steg 3: Markera osäkerheter

Markera vilka förmågor som är oklara, saknar ägare eller är beroende av enskilda personer. Dessa punkter blir viktiga inför kommande beslut om greenfield, brownfield eller hybrid.

### Steg 4: Formulera en preliminär målbild

Avsluta med att formulera en mening som beskriver vad organisationen egentligen ska införa.

Exempel:

> Vi ska etablera en gemensam och långsiktigt förvaltad plattformsförmåga för utvalda applikationer, med tydlig driftmodell, säkerhetsstyrning och minskat personberoende.

## Snabb sammanfattning

- En containerplattform bör förstås som en teknisk och organisatorisk förmåga.
- OpenShift är inte bara en produkt att införa, utan en del av en ny drift- och leveransmodell.
- Beslutet påverkar drift, säkerhet, kompetens, ansvar, styrning och arbetssätt.
- Greenfield och brownfield bör jämföras utifrån vilken förmåga organisationen kan bygga och ta emot.
- Om målbilden är otydlig riskerar organisationen att fatta ett vägval på för smal teknisk grund.

## Quiz och reflektionsfrågor

1. Vilka tre förmågor är viktigast att stärka i er organisation genom en containerplattform?
2. Vilka delar av dagens drift är mest personberoende?
3. Vilka effekter förväntar sig ledningen, och är de formulerade som mätbara mål?
4. Finns det en tydlig mottagande organisation för plattformen efter införandet?
5. Är plattformen i första hand tänkt för nya system, befintliga system eller båda?

## Nästa steg

Nästa kapitel går vidare till själva vägvalet. Där definieras greenfield och brownfield som förändringsstrategier, inte bara som tekniska miljöer. Det gör det möjligt att senare jämföra dem utifrån nytta, risk, belastning och genomförbarhet.
