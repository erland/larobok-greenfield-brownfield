# Kapitel 2: Greenfield och brownfield som vägval

## Varför detta kapitel finns

När en organisation diskuterar införande av OpenShift eller annan containerplattform används ofta orden greenfield och brownfield som om de vore självklara. I praktiken betyder de olika saker för olika personer.

För någon betyder greenfield en helt ny teknisk miljö. För någon annan betyder det ett nytt arbetssätt, nya team och nya standarder. Brownfield kan på motsvarande sätt betyda allt från en försiktig migrering av befintliga system till en djup förändring av dagens driftmodell.

Detta kapitlet gör begreppen användbara som beslutsverktyg. Målet är inte att välja väg redan nu, utan att förstå vad valet faktiskt innebär.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- förklara greenfield och brownfield som förändringsstrategier,
- skilja mellan tekniskt vägval och organisatoriskt vägval,
- identifiera när ett införande i praktiken är en hybrid,
- formulera vad greenfield och brownfield skulle betyda i den egna organisationen,
- se vilka frågor som måste besvaras innan vägvalet kan göras ansvarsfullt.

## Innan vi börjar

Kapitel 1 beskrev införandet som etablering av en plattformsförmåga. Det är en viktig utgångspunkt. Om OpenShift bara ses som en teknisk produkt blir greenfield och brownfield lätt en fråga om var plattformen ska installeras. Om införandet ses som en ny förmåga blir vägvalet bredare.

Då handlar det om:

- hur snabbt organisationen kan förändra arbetssätt,
- vilka system som ska påverkas först,
- vilka personer och team som behöver delta,
- hur driftansvar ska fördelas,
- hur säkerhet och regelefterlevnad ska säkras,
- hur gammal och ny miljö ska leva tillsammans under övergången.

Greenfield och brownfield är därför inte bara arkitekturval. De är förändringsstrategier.

## Greenfield: att bygga nytt med begränsat arv

Greenfield betyder i denna bok att organisationen etablerar en ny lösning, miljö eller förmåga med begränsad direkt koppling till befintlig teknisk miljö.

I ett OpenShift-införande kan greenfield innebära att myndigheten bygger upp en ny containerplattform vid sidan av dagens driftmiljö. Plattformen får nya standarder, nya arbetssätt, ett nytt plattformsteam och tydliga principer för hur applikationer ska anslutas.

Det kan vara attraktivt eftersom organisationen får börja med en renare målbild. Gamla kompromisser, historiska beroenden och informella arbetssätt behöver inte följa med från första dagen.

Greenfield kan passa när organisationen behöver:

- skapa en tydlig målbild utan att omedelbart fastna i befintliga begränsningar,
- bygga upp ny kompetens och nya arbetssätt under kontrollerade former,
- testa plattformsförmågan med ett avgränsat användningsfall,
- undvika att den första versionen av plattformen tyngs av äldre systemkrav,
- visa vad ett modernare sätt att arbeta kan innebära.

Men greenfield har också en central risk: det som byggs nytt kan bli för frikopplat från den verkliga organisationen.

En ny plattform kan fungera väl i sig, men ändå misslyckas som myndighetsförmåga om den inte tas emot av applikationsteam, driftorganisation, säkerhetsfunktion, arkitektur, upphandling och styrning. Då uppstår en modern ö bredvid den befintliga verksamheten.

## Brownfield: att förändra med utgångspunkt i verkligheten

Brownfield betyder i denna bok att organisationen utgår från befintliga system, arbetssätt, beroenden och driftmodeller och förändrar dem stegvis.

I ett OpenShift-införande kan brownfield innebära att myndigheten börjar med befintliga system, befintliga driftflöden och verkliga beroenden. Plattformen införs genom att delar av dagens miljö moderniseras, migreras eller kompletteras.

Det kan vara attraktivt eftersom förändringen förankras i faktisk drift. Organisationen lär sig genom verkliga system, verkliga krav och verkliga begränsningar.

Brownfield kan passa när organisationen behöver:

- minska avståndet mellan ny plattform och befintlig drift,
- hantera system som redan är kritiska för verksamheten,
- använda befintlig kompetens och kunskap om systemportföljen,
- undvika att bygga en målmiljö som inte passar verkliga krav,
- skapa förändring utan att vänta på en perfekt ny startpunkt.

Men brownfield har också en central risk: arvet kan följa med in i det nya.

Om dagens driftmodell är personberoende, tungt manuell eller otydligt dokumenterad kan samma mönster återuppstå på den nya plattformen. Då får organisationen ny teknik men gamla svagheter.

## Hybrid: när verkligheten kräver både och

Många större myndigheter hamnar inte i ett rent greenfield- eller brownfield-val. De hamnar i en hybrid.

Hybrid betyder att organisationen kombinerar ett nytt etableringsspår med stegvis förändring av befintliga system och arbetssätt.

Ett vanligt mönster är:

- en ny plattformsförmåga etableras relativt greenfield,
- ett eller flera verkliga system används som kontrollerade pilotfall,
- migrering från befintlig miljö sker stegvis,
- driftmodell och ansvar förändras parallellt,
- gamla arbetssätt avvecklas först när nya fungerar i praktiken.

Hybrid kan vara klokt eftersom den kombinerar två behov. Organisationen behöver en tillräckligt ren målbild för att inte fastna i arvet, men den behöver också tillräcklig kontakt med verkligheten för att inte bygga fel förmåga.

Samtidigt kan hybrid bli en undanflykt. Om organisationen säger “vi gör både och” utan att tydliggöra mandat, ordning, kriterier och avvecklingsplan kan resultatet bli dubbel komplexitet. Då byggs nytt samtidigt som det gamla fortsätter utan tydlig riktning.

Hybrid är alltså inte automatiskt en balanserad lösning. Den måste styras.

## Vägvalet är bredare än teknik

En chef bör undvika att reducera vägvalet till frågan “ny miljö eller befintlig miljö?”. Det är en del av beslutet, men inte hela beslutet.

Vägvalet bör bedömas i minst fem dimensioner.

### 1. Teknisk startpunkt

Den tekniska startpunkten handlar om var införandet börjar.

Greenfield börjar oftare i en ny miljö. Brownfield börjar oftare i befintliga system, integrationer och driftflöden. Hybrid börjar ofta i en ny plattformsbas men med verkliga system tidigt i införandet.

Den tekniska startpunkten påverkar komplexitet, tempo och risk, men den säger inte ensam om vägvalet är klokt.

### 2. Organisatorisk förankring

Organisatorisk förankring handlar om vilka delar av organisationen som faktiskt är med.

Ett greenfield-spår kan gå snabbt om det drivs av ett fokuserat team, men riskerar svag förankring i linjeorganisationen. Ett brownfield-spår kan ha starkare koppling till dagens drift, men riskerar hög belastning på redan upptagna nyckelpersoner.

För en myndighet där många redan är upptagna med daglig drift är detta ofta en avgörande dimension.

### 3. Kompetensstrategi

Kompetensstrategin handlar om hur organisationen ska minska personberoende och bygga ny förmåga.

Greenfield kan skapa utrymme för ny kompetens och nya roller, men kan också bli beroende av en liten grupp specialister. Brownfield kan sprida lärande i befintlig organisation, men kan också förstärka beroendet av samma nyckelpersoner som redan bär dagens drift.

Frågan är inte bara vilken kompetens som finns. Frågan är vilken kompetensmodell organisationen vill ha efter förändringen.

### 4. Riskhantering

Riskhantering handlar om vilken typ av risk organisationen är beredd att ta.

Greenfield minskar vissa arvrelaterade risker men ökar risken för glapp mellan ny plattform och befintlig verksamhet. Brownfield minskar risken att bygga något verklighetsfrånvänt men ökar risken att förändringen blir långsam, tung och kompromissfylld.

Riskerna är olika. Därför kan de inte jämföras enbart med en generell känsla av att den ena vägen är tryggare.

### 5. Genomförbarhet

Genomförbarhet handlar om vad organisationen faktiskt kan göra med tillgänglig tid, kompetens, mandat och uppmärksamhet.

I en organisation där alla redan är hårt belastade kan ett stort brownfield-införande vara svårt eftersom det kräver deltagande från många nyckelpersoner. Samma organisation kan samtidigt få problem med greenfield om det nya spåret saknar mottagare, driftansvar och verksamhetskoppling.

Det viktiga är att bedöma genomförbarhet konkret, inte önsketänka.

## Tre möjliga vägval för samma myndighet

Tänk en större myndighet som vill införa OpenShift. Myndigheten har flera äldre system, komplexa integrationer, höga säkerhetskrav och ett antal erfarna driftpersoner som många är beroende av. Samtidigt är organisationen hårt belastad av den dagliga driften.

Samma myndighet kan välja tre olika vägar.

### Alternativ A: Greenfield-spår

Myndigheten etablerar en ny OpenShift-plattform med ett avgränsat plattformsteam. Ett nytt eller mindre kritiskt system väljs som första användningsfall. Fokus ligger på målbild, standarder, automatisering och nya arbetssätt.

Detta kan skapa fart och tydlighet. Det kan också minska risken att plattformen formas av gamla undantag från början.

Risken är att den nya plattformen inte blir relevant för de system och team som senare ska anslutas. Om driftorganisationen, säkerhetsfunktionen och applikationsägarna inte är med i rätt tid kan införandet skapa en parallell verklighet.

### Alternativ B: Brownfield-spår

Myndigheten väljer ett befintligt system eller en systemgrupp och använder detta som startpunkt för införandet. Man kartlägger beroenden, driftflöden, säkerhetskrav och kompetensbehov. Plattformen byggs och anpassas utifrån verkliga krav.

Detta kan ge stark förankring och tidig kontakt med faktiska problem. Det kan också skapa lärande i befintlig organisation.

Risken är att arbetet blir tungt från början. Nyckelpersoner kan behöva bära både daglig drift och förändring. Om systemet är komplext kan plattformsetableringen förväxlas med systemmodernisering, integrationsstädning och dokumentationsskuld på samma gång.

### Alternativ C: Hybridspår

Myndigheten etablerar en ny plattformsbas, men väljer tidigt ett verkligt pilotfall som prövar viktiga krav. Plattformsteamet byggs upp med tydligt mandat, samtidigt som linjeorganisationen involveras genom avgränsade beslutspunkter.

Detta kan kombinera målbild och verklighetskontakt. Det kan ge ett praktiskt införande utan att tappa riktning.

Risken är dubbel belastning och otydlighet. Om hybridspåret inte har tydliga kriterier för vad som ska göras nytt, vad som ska migreras, vad som ska avvecklas och vem som äger beslutet kan det bli det mest komplexa alternativet.

## Vanliga missförstånd

- **Missförstånd: Greenfield är alltid snabbast.**
  - Varför det händer: Det är lättare att börja utan att först lösa alla befintliga beroenden.
  - Hur du undviker det: Bedöm inte bara starttempo, utan även tid till verklig produktion, förankring och förvaltning.

- **Missförstånd: Brownfield är alltid tryggast.**
  - Varför det händer: Det utgår från kända system och kända personer.
  - Hur du undviker det: Granska om det kända faktiskt är stabilt, dokumenterat och skalbart, eller om tryggheten bygger på personberoende.

- **Missförstånd: Hybrid löser konflikten.**
  - Varför det händer: Hybrid låter balanserat och pragmatiskt.
  - Hur du undviker det: Kräv tydliga principer för vad som ska göras greenfield, vad som ska göras brownfield och när gamla lösningar ska avvecklas.

- **Missförstånd: Vägvalet kan delegeras till tekniken.**
  - Varför det händer: OpenShift och containerplattformar uppfattas som tekniska frågor.
  - Hur du undviker det: Se beslutet som en fråga om styrning, kapacitet, risk och organisatorisk förmåga.

## Beslutsfrågor före nästa steg

Innan organisationen börjar jämföra alternativen i detalj bör chefen kunna samla ledning, arkitektur, drift, säkerhet och berörda systemägare kring ett antal frågor.

- Vad betyder greenfield konkret hos oss?
- Vad betyder brownfield konkret hos oss?
- Vilka delar av dagens driftmodell vill vi behålla, förändra eller avveckla?
- Vilka personberoenden riskerar att följa med in i den nya plattformen?
- Vilka system är realistiska första kandidater?
- Vilka delar av organisationen måste vara med från början?
- Vilket mandat har plattformsteamet?
- Vilka effekter ska införandet ge som inte redan finns i dag?
- När vet vi att det nya arbetssättet fungerar?
- Vilka gamla arbetssätt ska inte längre accepteras när plattformen är införd?

Om dessa frågor inte kan besvaras behöver organisationen förmodligen mer nulägesarbete innan beslutet fattas.

## Övning: formulera vägvalet i den egna organisationen

Använd övningen i en ledningsgrupp, styrgrupp eller mindre förberedande workshop. Syftet är inte att fatta beslut direkt, utan att avslöja om deltagarna menar samma sak med orden.

### Steg 1: Skriv tre definitioner

Låt deltagarna formulera tre korta meningar:

1. Hos oss skulle greenfield betyda att ...
2. Hos oss skulle brownfield betyda att ...
3. Hos oss skulle hybrid betyda att ...

Jämför svaren. Om deltagarna beskriver helt olika saker är det för tidigt att välja väg.

### Steg 2: Markera viktigaste konsekvens

För varje vägval, skriv den viktigaste konsekvensen för:

- driftorganisation,
- säkerhetsarbete,
- applikationsteam,
- nyckelpersoner,
- styrning och mandat,
- kostnad och tid,
- befintliga system.

Syftet är att flytta samtalet från teknikord till faktiska förändringar.

### Steg 3: Identifiera det största okända

För varje vägval, skriv den största osäkerheten.

Exempel:

- För greenfield vet vi inte om mottagande organisation hinner byggas.
- För brownfield vet vi inte om nyckelpersoner kan frigöras.
- För hybrid vet vi inte om vi klarar dubbel styrning under övergången.

Det största okända visar ofta vilket beslutsunderlag som saknas.

## Snabb sammanfattning

- Greenfield innebär att bygga nytt med begränsad direkt koppling till befintlig miljö.
- Brownfield innebär att förändra med utgångspunkt i befintliga system, arbetssätt och beroenden.
- Hybrid innebär att kombinera en ny målbild med stegvis förändring av verkliga system.
- Vägvalet är inte bara tekniskt utan organisatoriskt.
- Greenfield riskerar att skapa en isolerad ö.
- Brownfield riskerar att föra med sig gamla beroenden.
- Hybrid riskerar dubbel komplexitet om den inte styrs tydligt.
- Chefen bör först säkerställa att organisationen menar samma sak med begreppen.

## Quiz och reflektionsfrågor

1. Vad är den viktigaste skillnaden mellan greenfield och brownfield som förändringsstrategier?
2. Varför kan greenfield vara snabbt i början men långsamt till verklig effekt?
3. Varför kan brownfield kännas tryggt men ändå vara riskabelt?
4. När är hybrid en genomtänkt strategi och när är den bara ett uppskjutet beslut?
5. Vilka tre delar av din organisation måste förstå vägvalet på samma sätt för att beslutet ska bli genomförbart?

## Nästa steg

Nu har vi definierat vägvalen. Nästa kapitel sätter dem i myndighetskontext. Där blir frågan varför styrning, säkerhet, upphandling, långlivade system och personberoenden gör valet mer krävande än i en mindre eller mer fristående IT-miljö.
