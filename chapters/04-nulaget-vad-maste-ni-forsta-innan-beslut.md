# Kapitel 4: Nuläget: vad måste ni förstå innan beslut?

## Varför detta kapitel finns

Ett beslut om greenfield, brownfield eller hybrid blir bara så bra som den nulägesbild det bygger på. Om organisationen överskattar sin förändringskapacitet, underskattar sina beroenden eller missar personberoenden i driften kan även ett till synes klokt vägval bli svårt att genomföra.

I en större myndighet är nuläget ofta mer komplext än det först ser ut. Det finns system som är gamla men verksamhetskritiska, beroenden som inte är dokumenterade, driftkunskap som sitter hos enskilda personer och styrningskrav som påverkar både tempo och handlingsutrymme. Det finns också ofta en formell vilja att modernisera, samtidigt som organisationen redan är hårt belastad av daglig drift, incidenter, förvaltning, upphandlingar och andra förändringsinitiativ.

Detta kapitlet hjälper dig som chef att samla rätt beslutsunderlag innan vägvalet görs. Syftet är inte att skapa en perfekt teknisk kartläggning. Syftet är att förstå tillräckligt mycket för att kunna bedöma vilken förändringsväg organisationen faktiskt kan genomföra.

## Lärandemål

Efter kapitlet ska du kunna:

- identifiera vilket nulägesunderlag som behövs före beslut om greenfield, brownfield eller hybrid,
- skilja mellan upplevd och faktisk förändringskapacitet,
- bedöma varför systemportfölj, teknisk skuld, driftmodell och kompetensläge hör ihop,
- ställa tydligare krav på beslutsunderlag från teknik, drift, säkerhet och verksamhet,
- använda en enkel nulägeskarta som stöd för lednings- eller styrgruppsdialog.

## Innan vi börjar

De tidigare kapitlen har visat att införande av containerplattform inte bara är en teknisk installation. Det är ett vägval som påverkas av styrning, säkerhet, drift, beroenden och personberoende kompetens.

Därför räcker det inte att fråga om organisationen “vill” välja greenfield eller brownfield. Den viktigare frågan är:

> Vad i vårt nuläge gör ett visst vägval klokt, riskabelt eller orealistiskt just nu?

Ett bra nulägesarbete gör tre saker. Det synliggör vad organisationen redan vet, vad den tror sig veta och vad den faktiskt behöver ta reda på innan beslut.

## Nulägesbilden som beslutsunderlag

Nulägesbilden ska inte vara en omfattande inventering som tar ett år att färdigställa. Då riskerar den att bli ett eget projekt som försenar beslutet utan att göra det tydligare. Den ska vara tillräckligt konkret för att besvara beslutets huvudfrågor.

De viktigaste frågorna är:

- Vilka system och tjänster påverkas direkt eller indirekt?
- Vilka beroenden finns mellan system, driftteam, säkerhetsfunktioner och leverantörer?
- Vilken kompetens krävs för dagens drift, och var finns den?
- Hur hårt belastad är organisationen redan?
- Vilka säkerhets-, upphandlings- och styrningskrav begränsar vägvalet?
- Vilka effekter förväntas införandet ge, och när behöver de synas?
- Vilka risker ökar om organisationen väljer fel tempo eller fel förändringsväg?

Ett vanligt misstag är att nulägesbilden blir för teknisk. Då kan den beskriva servrar, kluster, nätverk och applikationer, men missa de organisatoriska förutsättningarna. Ett annat vanligt misstag är att nulägesbilden blir för övergripande. Då låter allt möjligt i presentationen, men ingen vet vad det innebär för första systemet, första teamet eller första driftöverlämningen.

## Sex områden som måste förstås

Ett användbart beslutsunderlag bör minst täcka sex områden.

### 1. Systemportföljen

Systemportföljen beskriver vilka system organisationen har, hur viktiga de är, hur de används och vilka som kan vara aktuella för plattformen.

För beslutet behöver du inte veta varje teknisk detalj om varje system. Däremot behöver du förstå vilka kategorier av system som finns.

Exempel på kategorier:

- verksamhetskritiska system med höga tillgänglighetskrav,
- äldre system med svag dokumentation,
- system med många integrationer,
- nya eller planerade tjänster som kan passa för greenfield,
- system som redan är på väg att moderniseras,
- system som bör lämnas orörda tills vidare.

Om systemportföljen är oklar blir brownfield särskilt riskabelt, eftersom förändringen då sker direkt i en miljö som organisationen inte fullt ut förstår. Greenfield kan då framstå som enklare, men risken är att man bygger något nytt utan koppling till de system som faktiskt behöver förändras.

### 2. Beroenden och integrationer

Beroenden är ofta det som gör ett införande svårt. Ett system kan se avgränsat ut, men vara beroende av databaser, identitetstjänster, nätverksregler, loggning, batchflöden, filöverföringar, manuella rutiner eller externa leverantörer.

Beroenden påverkar vägvalet på flera sätt:

- Greenfield kräver att nya beroenden kan etableras utan att skapa en parallell och svårförvaltad struktur.
- Brownfield kräver att befintliga beroenden kan hanteras utan att förändringen fastnar i varje historiskt undantag.
- Hybrid kräver tydliga gränser mellan vad som moderniseras nu och vad som lämnas kvar under en övergångsperiod.

En chef behöver inte själv kartlägga alla integrationer, men bör kräva att de mest kritiska beroendena är kända innan beslutet tas.

### 3. Teknisk skuld

Teknisk skuld är inte bara gammal teknik. Det är kostnaden av tidigare val, genvägar, bristande dokumentation, undantag och lösningar som blivit svåra att ändra.

I beslutet om containerplattform är teknisk skuld viktig eftersom den kan följa med in i den nya miljön. Om organisationen containeriserar ett problem utan att förändra ansvar, byggsätt, driftmodell eller beroenden kan den nya plattformen ärva många av de gamla problemen.

Teknisk skuld påverkar också greenfield. Ett greenfield-spår kan skapa en ren startpunkt, men om den gamla miljön lämnas kvar utan avvecklingsplan har organisationen inte minskat skulden. Den har lagt till en ny miljö ovanpå den gamla.

### 4. Driftmodell och ansvar

Driftmodellen beskriver hur organisationen faktiskt tar ansvar för tjänster i produktion. Det handlar om mer än bemanning. Det handlar om incidenthantering, jour, övervakning, patchning, ändringshantering, säkerhetsuppföljning, releaseflöden och eskalering.

Vid införande av containerplattform behöver följande frågor vara tydliga:

- Vem ansvarar för plattformen?
- Vem ansvarar för applikationerna som körs på plattformen?
- Vem hanterar incidenter när felet ligger mellan plattform, applikation, nätverk och säkerhetskomponenter?
- Vem beslutar om uppgraderingar och standarder?
- Hur förs kunskap över från projekt till linjeorganisation?
- Vilket stöd får applikationsteam som ska använda plattformen?

Om driftmodellen är oklar är både greenfield och brownfield riskabla. Greenfield riskerar att skapa en tekniskt fungerande miljö utan tydlig mottagare. Brownfield riskerar att dra in den nya plattformen i gamla ansvarsglapp.

### 5. Kompetens och personberoenden

Personberoende är särskilt viktigt i en organisation där vissa typer av driftskompetens är knutna till få individer. Ett införande av containerplattform kan både minska och öka personberoenden.

Det kan minska personberoenden genom standardisering, dokumentation, automatisering och gemensamma arbetssätt. Men det kan också öka personberoenden om den nya plattformen bara förstås av ett fåtal specialister.

Nulägesbilden bör därför inte bara fråga vilken kompetens som finns. Den bör fråga hur robust kompetensen är.

En enkel kompetensbedömning kan skilja mellan fyra nivåer:

| Nivå | Beskrivning | Risk för beslutet |
|---|---|---|
| En person kan | Kunskapen finns hos en nyckelperson | Hög risk vid sjukdom, byte av roll eller överbelastning |
| Några kan | Flera personer kan lösa uppgiften, men inte alltid dokumenterat | Medelhög risk vid parallella initiativ |
| Teamet kan | Kunskapen finns i arbetssätt, dokumentation och gemensam praktik | Lägre risk |
| Organisationen kan | Det finns etablerade roller, utbildning, styrning och långsiktig förvaltning | Låg risk, men kräver fortsatt underhåll |

Den här bedömningen är central för vägvalet. Greenfield kan vara lämpligt om organisationen kan bygga ny gemensam förmåga utan att bero på samma få personer. Brownfield kan vara lämpligt om befintlig kompetens kan användas och spridas utan att nyckelpersoner blir flaskhalsar.

### 6. Förändringskapacitet

Förändringskapacitet är organisationens praktiska förmåga att genomföra förändring samtidigt som den dagliga verksamheten fortsätter. Den består av tid, kompetens, mandat, fokus, beslutsförmåga och uthållighet.

Det är vanligt att en ledningsgrupp bedömer förändringskapacitet utifrån ambition: “Det är viktigt, alltså prioriterar vi det.” Men faktisk förändringskapacitet avgörs av vad som händer när samma personer samtidigt ska hantera drift, incidenter, revisioner, upphandlingar, säkerhetsarbete, förvaltningsplaner och andra projekt.

Tecken på låg förändringskapacitet är till exempel:

- nyckelpersoner kan inte avsätta tid,
- beslut skjuts upp eftersom mandat är oklara,
- dokumentation prioriteras bort,
- workshops bemannas av ersättare utan beslutskraft,
- driftincidenter stoppar införandearbetet,
- säkerhets- eller arkitekturfrågor kommer in sent,
- projektet drivs framåt men linjeorganisationen hinner inte ta emot resultatet.

Om förändringskapaciteten är låg behöver vägvalet anpassas. Det betyder inte att förändringen ska stoppas, men det betyder att tempo, omfattning och första steg måste väljas med större försiktighet.

## Skillnaden mellan upplevd och faktisk förändringskapacitet

Upplevd förändringskapacitet är det organisationen säger sig kunna göra. Faktisk förändringskapacitet är det organisationen kan göra utan att skapa oacceptabel risk i drift, säkerhet eller verksamhet.

Skillnaden blir särskilt tydlig vid införande av en containerplattform. På strategisk nivå kan det finnas stark enighet. På praktisk nivå kan samma organisation sakna tillgängliga arkitekter, säkerhetsspecialister, driftresurser, produktägare eller applikationsteam.

Ett beslut som inte tar hänsyn till detta kan leda till två olika problem:

- Greenfield drivs av ett litet expertteam och blir svårt att skala till resten av organisationen.
- Brownfield startar i befintlig miljö men fastnar eftersom de personer som behövs redan är uppbundna.

Därför bör nulägesarbetet alltid innehålla en ärlig kapacitetsbedömning, inte bara en lista över önskade effekter.

## Workshop: nulägeskarta och kapacitetsbedömning

Den här workshopen kan genomföras med styrgrupp, ansvariga chefer, arkitektur, säkerhet, drift och representanter för berörda verksamhetsområden. Syftet är att skapa en gemensam bild, inte att lösa alla detaljer.

### Steg 1: Lista berörda systemkategorier

Skriv upp de systemkategorier som kan påverkas av införandet. Använd inte för mycket tid på detaljer. Målet är att se mönster.

Exempel:

- nya digitala tjänster,
- befintliga egenutvecklade system,
- system med höga säkerhetskrav,
- system med många integrationer,
- system som förvaltas av externa leverantörer,
- system med kända driftproblem,
- system som snart ska avvecklas.

### Steg 2: Markera beroenden

För varje kategori, markera de viktigaste beroendena.

Använd enkla frågor:

- Vilka andra system behöver detta system prata med?
- Vilka team eller leverantörer behövs för förändring?
- Vilka säkerhets- eller regelefterlevnadskrav påverkar?
- Vilka manuella rutiner finns runt systemet?
- Vilka personer brukar behövas när något går fel?

### Steg 3: Bedöm kompetensrobusthet

Bedöm om kompetensen ligger hos en person, några personer, ett team eller organisationen. Var särskilt uppmärksam på områden där svaret blir “det vet bara X”.

Det är inte ett misslyckande att hitta personberoenden. Det är ett misslyckande att fatta beslut som om de inte fanns.

### Steg 4: Bedöm faktisk kapacitet

Be varje deltagande funktion bedöma sin tillgängliga kapacitet för införandet under de kommande tre till sex månaderna.

Använd en enkel skala:

| Bedömning | Betydelse | Konsekvens |
|---|---|---|
| Grön | Kapacitet finns och är prioriterad | Vägval kan genomföras med normal styrning |
| Gul | Kapacitet finns delvis eller är osäker | Vägval kräver avgränsning, prioritering och tät uppföljning |
| Röd | Kapacitet saknas eller konkurrerar med kritisk drift | Vägval måste förenklas, skjutas upp eller förstärkas med tydligt mandat |

### Steg 5: Formulera beslutsimplikationer

Avsluta workshopen med att översätta nuläget till konsekvenser för vägvalet.

Exempel:

- “Greenfield är möjligt, men bara om vi redan nu utser mottagande organisation och verkliga pilotfall.”
- “Brownfield är för riskabelt innan vi har kartlagt beroenden för de tre första systemen.”
- “Hybrid är rimligt, men kräver tydlig gräns mellan ny plattformsförmåga och befintlig drift.”
- “Inget vägval är realistiskt utan att två nyckelpersoner frigörs från daglig drift.”

## Vanliga misstag

- **Misstag: Att låta nulägesanalysen bli en teknisk inventering.**
  - Varför det händer: Teknikfrågor är konkreta och lättare att lista än ansvar, mandat och kapacitet.
  - Hur du undviker det: Kräv att nulägesbilden alltid innehåller system, beroenden, driftmodell, kompetens och förändringskapacitet.

- **Misstag: Att underskatta personberoenden.**
  - Varför det händer: Organisationen är van vid att vissa personer “löser det”.
  - Hur du undviker det: Kartlägg vilka moment som bara en eller två personer kan utföra och behandla det som en beslutsrisk.

- **Misstag: Att utgå från att prioritering skapar kapacitet.**
  - Varför det händer: Ledningen kan besluta att något är viktigt, men inte automatiskt frigöra tid hos de personer som behövs.
  - Hur du undviker det: Koppla beslutet till faktisk bemanning, kalenderutrymme och bortprioritering av annat arbete.

- **Misstag: Att välja första pilot utifrån entusiasm i stället för lämplighet.**
  - Varför det händer: Ett engagerat team kan göra att införandet känns lättare att starta.
  - Hur du undviker det: Välj pilot utifrån risk, lärande, representativitet och mottagande förmåga.

- **Misstag: Att behandla nuläget som statiskt.**
  - Varför det händer: En nulägesbild presenteras ofta som en engångsrapport.
  - Hur du undviker det: Uppdatera nuläget när system, bemanning, incidentläge eller styrningsförutsättningar förändras.

## Övningar

### Övning 1: Skriv beslutets minsta nödvändiga nulägesbild

Formulera den minsta nulägesbild som måste finnas innan beslut kan fattas. Använd följande rubriker:

- system och tjänster som påverkas,
- viktigaste beroenden,
- teknisk skuld som påverkar vägvalet,
- driftmodell och ansvar,
- kompetens och personberoenden,
- förändringskapacitet,
- säkerhets- och styrningskrav,
- osäkerheter som måste utredas före beslut.

Målet är inte att skriva en lång rapport. Målet är att se om beslutet vilar på faktisk kunskap eller på antaganden.

### Övning 2: Identifiera tre röda risker

Välj tre områden där nuläget kan göra vägvalet riskabelt. För varje område, skriv:

1. Vad vet vi?
2. Vad tror vi?
3. Vad behöver vi ta reda på?
4. Vilket vägval påverkas mest?
5. Vilket beslut bör vi inte fatta förrän detta är tydligare?

### Fördjupning: Pröva vägvalet mot kapacitet

Ta ett preliminärt vägval: greenfield, brownfield eller hybrid. Pröva det mot faktisk kapacitet.

Besvara:

- Vilka personer eller team måste vara tillgängliga?
- Vilka andra uppgifter konkurrerar om samma personer?
- Vilken dokumentation saknas?
- Vilka beslut behöver tas snabbare än organisationen normalt arbetar?
- Vad händer om införandet måste pausas i tre månader på grund av drift eller säkerhetsarbete?

Om svaren visar att vägvalet kräver kapacitet som inte finns behöver beslutet justeras innan genomförandet startar.

## Snabb sammanfattning

- Ett beslut om greenfield, brownfield eller hybrid kräver en ärlig nulägesbild.
- Nulägesbilden behöver täcka systemportfölj, beroenden, teknisk skuld, driftmodell, kompetens och förändringskapacitet.
- Upplevd förändringsvilja är inte samma sak som faktisk förändringskapacitet.
- Personberoenden är inte bara en bemanningsfråga, utan en strategisk risk.
- Greenfield kan minska arv men skapa avstånd till verkliga system.
- Brownfield kan skapa närhet till verkligheten men kräver stark kontroll över beroenden och kapacitet.
- Hybrid kan vara klokt, men bara om gränser, ansvar och avvecklingsplan är tydliga.

## Quiz/reflektionsfrågor

1. Vilka tre delar av nulägesbilden är mest avgörande i din organisation?
2. Var är skillnaden störst mellan vad organisationen vill göra och vad den faktiskt har kapacitet att göra?
3. Vilka personberoenden behöver hanteras innan ett större införande kan bli robust?
4. Vilka system eller tjänster är olämpliga som första pilot, även om de är tekniskt intressanta?
5. Vilket vägval framstår som mest attraktivt just nu, och vilket nulägesfaktum skulle kunna ändra den bedömningen?

## Nästa steg

Nu finns grunden för att jämföra vägvalen mer konkret. Nästa kapitel går in på greenfield: när det är klokt, vilka fördelar det kan ge och vilka risker som särskilt behöver hanteras i en upptagen och personberoende myndighetsorganisation.
