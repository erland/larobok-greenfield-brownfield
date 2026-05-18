# Kapitel 5: Greenfield: när det är klokt och när det är riskabelt

## Varför detta kapitel finns

Greenfield lockar ofta när en organisation vill ta ett tydligt steg bort från gamla beroenden. Det kan kännas rationellt att bygga nytt, rent och modernt i stället för att börja i en befintlig miljö där dokumentationen är ojämn, driftmönstren är personberoende och systemen har vuxit fram under lång tid.

I ett införande av en containerplattform, exempelvis OpenShift, kan greenfield därför framstå som den snabbaste vägen till framtiden. Organisationen kan etablera en ny plattform, nya arbetssätt, tydligare standarder och ett mer automatiserat driftsmönster utan att direkt behöva reda ut varje gammalt beroende.

Men greenfield är inte riskfritt. Den största risken är inte att den nya plattformen inte går att bygga. Den största risken är att den byggs på ett sätt som organisationen inte kan ta emot, bemanna, styra eller använda i verklig produktion.

Kapitlet hjälper dig att bedöma när greenfield är ett klokt vägval, när det är riskabelt och vilket beslutsunderlag som behövs innan du ger klartecken.

## Lärandemål

Efter kapitlet ska du kunna:

- förklara vad greenfield innebär som förändringsväg vid införande av en containerplattform,
- identifiera greenfields viktigaste fördelar, nackdelar och risker,
- bedöma om organisationen har rätt förutsättningar för ett greenfield-spår,
- känna igen varningssignaler som tyder på att greenfield kan bli en isolerad ö,
- använda en enkel riskbedömning för att pröva greenfield innan beslut.

## Innan vi börjar

I kapitel 4 betonades att vägvalet måste bygga på nuläget. Greenfield kan inte bedömas abstrakt. Det som är ett klokt greenfield-val i en organisation kan vara ett farligt sidospår i en annan.

Frågan är därför inte:

> Är greenfield modernt?

Frågan är:

> Har vi förutsättningar att bygga nytt på ett sätt som blir användbart, styrbart och förvaltningsbart i vår verkliga organisation?

För en chef är detta en avgörande skillnad. Greenfield kan skapa handlingsutrymme, men det kan också skapa en parallell verklighet där projektet går framåt medan linjen, driften och säkerhetsorganisationen inte hinner med.

## Vad greenfield betyder i praktiken

Greenfield betyder i denna bok att organisationen etablerar en ny miljö, plattform eller förmåga med begränsad direkt koppling till befintlig teknisk miljö.

Det innebär inte att organisationen saknar historik, regler eller ansvar. En myndighet kan aldrig vara helt “grön mark”. Den nya plattformen måste fortfarande passa in i säkerhetskrav, styrning, upphandling, driftansvar, budgetprocesser och kompetensförsörjning.

Greenfield i en myndighetsmiljö betyder därför oftast:

- en ny plattform etableras vid sidan av befintliga driftmiljöer,
- nya arbetssätt och standarder tas fram,
- ett begränsat antal applikationer eller tjänster väljs som första användningsfall,
- gamla system flyttas inte automatiskt från start,
- organisationen försöker skapa en modern målbild utan att först förändra hela befintliga miljön.

Det kan vara ett bra sätt att minska startfriktion. Samtidigt skapar det ett nytt ansvar: att tidigt planera hur den nya förmågan ska bli en del av organisationens ordinarie styrning och drift.

## Greenfields viktigaste fördelar

Greenfield kan vara värdefullt när organisationen behöver bryta med arbetssätt som inte längre fungerar. Fördelen ligger inte bara i ny teknik, utan i möjligheten att skapa tydligare principer från början.

### Renare arkitektur och tydligare standarder

När plattformen byggs från början kan organisationen sätta standarder innan undantagen hunnit ta över. Det kan handla om säkerhetszoner, åtkomstmodeller, loggning, övervakning, nätverksprinciper, deploymentflöden, livscykelhantering och ansvarsfördelning.

Detta är särskilt värdefullt om den befintliga miljön präglas av många speciallösningar. Greenfield ger möjlighet att fråga:

- Hur vill vi att en modern applikationsdrift ska fungera?
- Vilka standarder ska vara gemensamma?
- Vilka undantag ska inte längre accepteras?
- Vilka krav ska vara inbyggda från början?

Greenfield kan därmed fungera som en praktisk målbild, inte bara som en teknisk installation.

### Lägre initial belastning från gamla beroenden

Ett brownfield-spår börjar ofta med att reda ut befintliga beroenden. Det kan vara nödvändigt, men också tungt. Greenfield kan skapa en kontrollerad start där organisationen slipper börja med de mest komplexa systemen.

Det kan vara klokt om nuläget är otydligt och organisationen behöver lära sig hur containerplattformen ska styras, säkras och användas innan den tar sig an de tyngsta migreringarna.

Det betyder inte att gamla beroenden kan ignoreras. Det betyder att de inte behöver dominera de första stegen.

### Snabbare lärande om nya arbetssätt

Greenfield kan ge ett avgränsat utrymme för lärande. Plattformsteam, säkerhetsfunktion, drift, arkitektur och applikationsteam kan pröva nya arbetssätt utan att varje beslut direkt påverkar hela den befintliga produktionsmiljön.

Det kan till exempel handla om:

- hur applikationsteam beställer eller använder plattformsresurser,
- hur säkerhetsgranskning byggs in i leveransflöden,
- hur incidenter hanteras i den nya miljön,
- hur uppdateringar och patchning ska styras,
- hur dokumentation och standarder ska hållas levande.

Detta lärandet är en av greenfields stora styrkor. Men lärandet måste fångas upp, dokumenteras och översättas till ordinarie arbetssätt. Annars blir det bara kunskap hos en liten grupp.

### Tydligare förändringssignal

Greenfield kan ha ett kommunikativt värde. Det visar att organisationen menar allvar med att bygga en ny förmåga och kan samla energi, riktning och kompetensutveckling.

Signalen är bara positiv om den kopplas till verklig förankring. Om greenfield uppfattas som ett projekt vid sidan av linjen kan budskapet i stället bli att framtiden byggs någon annanstans än där dagens ansvar finns.

## Greenfields viktigaste nackdelar

Greenfield har ofta lägre teknisk friktion i starten, men kan ha hög organisatorisk friktion senare. Det är därför chefen behöver titta särskilt noga på mottagande, bemanning och övergång till ordinarie drift.

### Risk för parallella världar

Den vanligaste nackdelen är att greenfield skapar en ny värld bredvid den gamla. Den nya världen har moderna verktyg, nya principer och engagerade personer. Den gamla världen har kritiska system, incidenter, etablerade avtal och människor som redan är hårt belastade.

Om de två världarna inte kopplas ihop tidigt kan organisationen få dubbel komplexitet. Då behöver den både bära det gamla och förstå det nya, utan att något faktiskt har blivit enklare.

Tecken på parallella världar kan vara:

- plattformsteamet arbetar med andra prioriteringar än driftorganisationen,
- säkerhetskrav tolkas olika i ny och gammal miljö,
- applikationsteam vet inte hur de ska ansluta sig,
- styrgruppen får positiva projektbilder men få tecken på verklig adoption,
- linjeorganisationen saknar tid att delta i design, test och mottagande.

### Kompetensgapet kan underskattas

Greenfield kan ge intryck av att organisationen kan börja om med ny kompetens. I praktiken behövs både ny och gammal kompetens samtidigt.

Den nya plattformen kräver kunskap om containerplattform, automatisering, säkerhetsmodeller, nätverk, observability, livscykelhantering och plattformsdrift. Samtidigt behövs kunskap om befintliga system, verksamhetskrav, driftmönster, incidenthistorik och säkerhetsklassning.

Om de personer som kan den gamla miljön redan är hårt belastade kan de få svårt att bidra. Då riskerar greenfield-teamet att bygga en lösning som är tekniskt rimlig men dåligt anpassad till verkliga beroenden.

### Överlämningen till förvaltning skjuts upp

Ett greenfield-initiativ kan drivas som projekt. Det kan vara effektivt i början, men farligt om förvaltning, driftansvar och långsiktig finansiering kommer för sent.

Frågor som ofta skjuts upp är:

- Vem äger plattformen efter projektet?
- Vilka roller behövs i ordinarie organisation?
- Hur finansieras vidareutveckling och drift?
- Vem ansvarar för patchning, säkerhetsuppdateringar och incidenthantering?
- Hur ska applikationsteam få stöd?
- Vilka servicenivåer gäller?
- Hur ska undantag beslutas?

Om dessa frågor inte är besvarade innan plattformen börjar användas i skarpt läge flyttas risken från projektet till linjen.

### Greenfield kan ge falsk enkelhet

Eftersom greenfield börjar i en ny miljö kan arbetet se enklare ut än det är. De första demonstrationerna kan fungera väl. En pilotapplikation kan driftsättas snabbt. Automatiserade flöden kan visa imponerande resultat.

Men det säger inte automatiskt att organisationen har löst de svåra frågorna. Den verkliga prövningen kommer när fler system, fler team, högre säkerhetskrav, incidenter, revision, uppföljning och livscykelansvar ska hanteras.

Greenfield är därför riskabelt om beslutet baseras på vad som fungerar i en avgränsad teknisk demonstration snarare än vad som fungerar i myndighetens ordinarie ansvarsmiljö.

## När greenfield är ett klokt vägval

Greenfield är mest klokt när organisationen behöver etablera en ny förmåga och har möjlighet att skydda den från för mycket arv i början, utan att tappa kopplingen till verkliga behov.

Det talar för greenfield när flera av följande påståenden stämmer:

- den befintliga miljön är så komplex att ett direkt brownfield-spår skulle fastna,
- organisationen behöver en tydlig målbild för moderna arbetssätt,
- det finns mandat att etablera en ny plattformsförmåga,
- det finns resurser att bemanna både etablering och mottagande,
- säkerhets- och styrningsfunktioner kan delta tidigt,
- det finns lämpliga pilotfall med verkligt värde men hanterbar risk,
- ledningen accepterar att greenfield bara är början, inte hela transformationen,
- det finns en plan för hur lärdomar ska föras in i ordinarie organisation.

Greenfield är alltså inte ett sätt att slippa organisationens verklighet. Det är ett sätt att skapa en kontrollerad startpunkt för förändring.

## När greenfield är riskabelt

Greenfield blir riskabelt när det används för att undvika svåra frågor som egentligen måste hanteras.

Det talar emot greenfield när flera av följande påståenden stämmer:

- organisationen saknar tid att avsätta nyckelpersoner från drift och säkerhet,
- plattformen drivs av ett projekt utan tydlig mottagare,
- pilotfallen är valda för att vara enkla snarare än relevanta,
- befintliga applikationsteam är inte involverade,
- driftansvar och finansiering efter projektet är oklara,
- ledningen saknar gemensam bild av vad plattformen ska användas till,
- införandet motiveras främst av tekniktrend eller leverantörstryck,
- det finns ingen plan för hur gamla miljöer ska påverkas på sikt.

I sådana lägen kan greenfield skapa mer komplexitet än nytta. Organisationen får då en ny plattform, men inte nödvändigtvis en ny förmåga.

## De viktigaste riskerna att hantera

Greenfield-risker bör inte beskrivas allmänt. De bör kopplas till konkreta beslut och motåtgärder. Tabellen nedan kan användas som stöd i styrgrupp eller ledningsgrupp.

| Risk | Hur den märks | Möjlig motåtgärd |
|---|---|---|
| Isolerad ö | Plattformen fungerar tekniskt men används inte brett | Koppla greenfield till verkliga pilotfall och ordinarie styrning |
| Kompetensgap | Få personer förstår både ny plattform och befintlig drift | Planera kompetensöverföring och gemensamma team tidigt |
| Oklart mottagande | Projektet bygger, men linjen vet inte vad den ska ta över | Besluta mottagande organisation, roller och finansiering före skarp drift |
| Falsk pilotframgång | En enkel pilot lyckas men säger lite om verklig komplexitet | Välj pilotfall med faktisk verksamhetsrelevans och tydliga lärandemål |
| Dubbel komplexitet | Gammal och ny miljö behöver drivas utan avvecklingsplan | Skapa övergångsplan och kriterier för när äldre lösningar ska lämnas |
| Svag säkerhetsförankring | Säkerhetskrav kommer in sent och bromsar införandet | Involvera säkerhet, arkitektur och regelefterlevnad från start |
| Personberoende flyttas | Nya experter blir lika kritiska som gamla nyckelpersoner | Dokumentera, rotera ansvar och bygg teamförmåga i stället för hjältekultur |

Tabellen ska inte användas som en formell revisionsmall. Den ska användas för att få fram de samtal som annars ofta kommer för sent.

## Pilotfallet avgör vad ni lär er

I ett greenfield-spår blir valet av första pilotfall viktigt. En pilot är inte bara ett tekniskt test. Den är ett sätt att pröva om plattformen, styrningen, säkerheten, driften och organisationen fungerar tillsammans.

Ett bra pilotfall ska vara tillräckligt verkligt för att ge användbara lärdomar, men inte så kritiskt att en misslyckad start skapar oacceptabel verksamhetsrisk.

Ett svagt pilotfall är ofta valt för att vara enkelt. Det kan ge snabb framgång, men lär organisationen för lite. Ett alltför svårt pilotfall kan i stället göra att plattformen bedöms misslyckad innan organisationen hunnit lära sig.

Ett bra pilotfall kännetecknas av att det:

- har tydligt verksamhetsvärde,
- har en ägare som vill delta aktivt,
- har hanterbar säkerhets- och driftkritikalitet,
- kräver samverkan mellan flera funktioner,
- ger lärdomar som kan återanvändas,
- är möjligt att avgränsa i tid och omfattning,
- har tydliga kriterier för vad piloten ska bevisa.

Som chef bör du inte nöja dig med frågan om piloten “går att driftsätta”. Fråga i stället:

> Vilka organisatoriska antaganden ska piloten pröva?

Exempel på sådana antaganden är att applikationsteam kan använda plattformen med rimligt stöd, att säkerhetskrav kan integreras i leveransflödet, att driftorganisationen kan hantera incidenter och att styrningen kan fatta nödvändiga beslut i tid.

## Beslutsunderlag före greenfield-beslut

Innan ett greenfield-spår beslutas bör du kräva ett kort men tydligt beslutsunderlag. Det behöver inte vara omfattande, men det ska svara på rätt frågor.

Miniminivån bör omfatta:

- syftet med greenfield-spåret,
- vilka förmågor som ska etableras,
- vilka pilotfall som ska användas och varför,
- hur säkerhet och regelefterlevnad involveras,
- hur driftansvar och mottagande organisation ska se ut,
- vilka personer och roller som behöver avsättas,
- hur kompetensöverföring ska ske,
- vilka beroenden till befintlig miljö som ändå måste hanteras,
- hur framgång ska mätas,
- vilka beslutspunkter som avgör om spåret ska fortsätta, ändras eller stoppas.

Ett bra greenfield-beslut bör också innehålla tydliga gränser. Greenfield-spåret ska veta vad det får besluta själv, vad som kräver styrgruppsbeslut och när ordinarie linjeorganisation måste ta över ansvar.

## Greenfield och personberoenden

I den beskrivna myndighetssituationen är personberoenden en särskilt viktig fråga. Greenfield kan minska vissa gamla personberoenden, men det kan också skapa nya.

Ett vanligt mönster är att några få starka specialister driver den nya plattformen framåt. De blir snabbt oumbärliga eftersom de förstår både tekniken, beslutshistoriken och de praktiska undantagen. Då har organisationen inte minskat personberoendet. Den har bara flyttat det.

För att undvika detta behöver greenfield-spåret byggas med kompetensspridning från början.

Det innebär bland annat att:

- kritiska beslut dokumenteras kort och begripligt,
- drift- och säkerhetsrutiner inte bara finns hos projektgruppen,
- fler än en person kan felsöka centrala delar,
- plattformsteamet arbetar med gemensamma arbetssätt,
- applikationsteam lär sig använda plattformen stegvis,
- kunskap från befintlig drift tas in, inte rundas.

Greenfield är som mest värdefullt när det används för att bygga teamförmåga, inte nya hjältar.

## Workshop: greenfield-riskbedömning

Använd denna workshop när ledning, styrgrupp eller programledning behöver pröva om greenfield är rätt väg.

### Syfte

Att bedöma om ett greenfield-spår har tillräckliga organisatoriska förutsättningar för att lyckas.

### Deltagare

Lämpliga deltagare är:

- ansvarig chef eller beslutsfattare,
- representant för drift,
- representant för säkerhet,
- arkitektur- eller plattformsansvarig,
- representant för applikationsteam,
- verksamhetsrepresentant för tänkta pilotfall,
- eventuell upphandlings- eller leverantörsansvarig.

### Steg 1: Formulera greenfield-spårets uppdrag

Svara gemensamt på tre frågor:

1. Vilken förmåga ska greenfield-spåret etablera?
2. Vilka problem i dagens miljö ska det hjälpa oss att komma förbi?
3. Vad ska greenfield-spåret inte lösa i första steget?

Det tredje svaret är viktigt. Om allt ska lösas blir spåret otydligt.

### Steg 2: Bedöm mottagande organisation

Använd följande frågor:

- Vem tar emot plattformen efter projektet?
- Vilken funktion ansvarar för drift och vidareutveckling?
- Vilka roller saknas i dag?
- Vilka personer behöver avsättas från befintlig drift?
- Hur undviker vi att nyckelpersoner blir flaskhalsar?
- Vilka beslut måste vara fattade innan första skarpa produktionssättning?

Markera varje fråga som grön, gul eller röd.

- Grön betyder att svaret är tydligt och förankrat.
- Gul betyder att svaret finns men behöver preciseras.
- Röd betyder att svaret saknas eller är omstritt.

### Steg 3: Pröva pilotfallet

Bedöm det föreslagna pilotfallet med följande frågor:

- Är pilotfallet verksamhetsrelevant?
- Är risknivån hanterbar?
- Kommer piloten att pröva säkerhet, drift och styrning?
- Finns en aktiv system- eller tjänsteägare?
- Finns kriterier för vad piloten ska visa?
- Kan lärdomarna användas för nästa steg?

Om piloten bara visar att tekniken fungerar är den för svag som beslutsunderlag.

### Steg 4: Identifiera stoppunkter

Bestäm i förväg vilka signaler som ska leda till omprövning. Exempel:

- nyckelpersoner kan inte avsättas,
- säkerhetskrav visar sig vara mer omfattande än antaget,
- mottagande organisation saknar finansiering,
- pilotfallet saknar aktiv ägare,
- plattformen kräver fler undantag än förväntat,
- driftansvar blir oklart.

Stoppunkter är inte ett tecken på pessimism. De är ett sätt att styra med ansvar.

## Beslutsfrågor för chefen

Innan du rekommenderar greenfield bör du kunna svara på följande frågor:

1. Vilket problem löser greenfield bättre än brownfield i vårt fall?
2. Vilken organisatorisk förmåga ska vara etablerad när greenfield-spåret är klart?
3. Vilka personer behöver frigöras, och vad får de sluta göra under tiden?
4. Hur säkerställer vi att säkerhet, drift och förvaltning är med från början?
5. Vilket pilotfall ger verkliga lärdomar utan oacceptabel risk?
6. Hur undviker vi att skapa en isolerad ö?
7. Hur mäter vi att greenfield leder till minskat personberoende och ökad styrbarhet?
8. När ska vi byta riktning, bromsa eller gå över i ett hybrid- eller brownfield-spår?

Om dessa frågor inte kan besvaras bör beslutet inte vara ett ja till full greenfield. Det kan fortfarande vara rimligt att starta ett begränsat förberedande arbete, men då bör det beskrivas som lärande och förmågebyggande, inte som ett färdigt vägval.

## Vanliga misstag

- **Misstag: Att likställa greenfield med låg risk.**
  - Varför det händer: Den nya miljön saknar många av de gamla problemen.
  - Hur du undviker det: Bedöm även mottagande, driftansvar, säkerhet och kompetensöverföring.

- **Misstag: Att välja en för enkel pilot.**
  - Varför det händer: Organisationen vill visa snabb framgång.
  - Hur du undviker det: Välj ett pilotfall som prövar verkliga organisatoriska antaganden.

- **Misstag: Att låta projektet springa före linjen.**
  - Varför det händer: Projektet har fokus, energi och mandat medan linjen är upptagen.
  - Hur du undviker det: Avsätt linjeresurser och besluta mottagande organisation tidigt.

- **Misstag: Att skapa nya personberoenden.**
  - Varför det händer: Några få specialister driver den nya plattformen och blir snabbt oumbärliga.
  - Hur du undviker det: Bygg teamförmåga, dokumentera beslut och rotera ansvar.

- **Misstag: Att skjuta upp förvaltningsfrågorna.**
  - Varför det händer: Det känns effektivt att först få tekniken på plats.
  - Hur du undviker det: Kräv förvaltningsmodell, finansiering och driftansvar innan skarp produktionsanvändning.

## Övningar

### Övning 1: Greenfield som verkligt vägval

Skriv ner tre skäl till att greenfield skulle kunna vara rätt väg i din organisation. Skriv sedan ner tre skäl till att greenfield skulle kunna vara riskabelt.

Jämför svaren med nulägeskartan från kapitel 4. Markera vilka skäl som bygger på fakta och vilka som bygger på antaganden.

### Övning 2: Bedöm risken för isolerad ö

Gå igenom följande påståenden och markera varje som grön, gul eller röd:

- Det finns en tydlig mottagande organisation.
- Drift och säkerhet deltar aktivt från början.
- Minst ett verkligt pilotfall är identifierat.
- Applikationsteam har tid och mandat att delta.
- Förvaltningsansvar och finansiering är beskrivet.
- Kompetensöverföring är planerad.
- Det finns en plan för hur greenfield-spåret kopplas till befintlig systemportfölj.

Om två eller fler punkter är röda bör greenfield-beslutet omprövas eller avgränsas tydligare.

### Fördjupning: Formulera ett beslut med villkor

Skriv ett möjligt greenfield-beslut som innehåller villkor. Exempel:

> Organisationen får starta ett greenfield-spår för att etablera grundläggande plattformsförmåga, under förutsättning att mottagande organisation, pilotfall, säkerhetsmedverkan och kompetensöverföring är beslutade innan första produktionssättning.

Anpassa formuleringen till din egen organisation. Syftet är att undvika ett vagt ja som senare blir svårt att styra.

## Snabb sammanfattning

- Greenfield kan vara klokt när organisationen behöver skapa en ny plattformsförmåga utan att fastna i hela den befintliga komplexiteten från start.
- Den största greenfield-risken är ofta organisatorisk, inte teknisk.
- En greenfield-plattform som inte tas emot av linje, drift, säkerhet och applikationsteam riskerar att bli en isolerad ö.
- Pilotfallet ska pröva verkliga organisatoriska antaganden, inte bara visa att tekniken fungerar.
- Greenfield kan minska gamla personberoenden, men bara om kompetensspridning och teamförmåga byggs in från början.
- Ett bra greenfield-beslut innehåller uppdrag, gränser, mottagande organisation, pilotfall, risker och stoppunkter.

## Quiz/reflektionsfrågor

1. Vilken är den största skillnaden mellan att bygga en greenfield-plattform och att etablera en greenfield-förmåga?
2. Varför kan en lyckad teknisk pilot ändå vara ett svagt beslutsunderlag?
3. Vilka tecken tyder på att greenfield håller på att bli en isolerad ö?
4. Hur kan greenfield både minska och skapa personberoenden?
5. Vilka tre villkor skulle du kräva innan ett greenfield-spår får gå till skarp produktionsanvändning?

## Nästa steg

Nästa kapitel behandlar brownfield. Där vänder vi på perspektivet: i stället för att bygga nytt bredvid det befintliga prövar vi vad det innebär att förändra med utgångspunkt i dagens system, driftmönster, beroenden och kompetensläge.

Brownfield kan kännas långsammare och tyngre än greenfield. Men i en myndighet där verkliga system, ansvar och personberoenden redan finns kan det ibland vara den mest realistiska vägen till faktisk förändring.
