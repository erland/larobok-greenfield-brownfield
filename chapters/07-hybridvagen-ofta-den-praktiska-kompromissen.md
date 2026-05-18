# Kapitel 7: Hybridvägen: ofta den praktiska kompromissen

## Varför detta kapitel finns

I större myndigheter blir valet mellan greenfield och brownfield sällan helt rent. Det kan vara lockande att tala om två tydliga alternativ: antingen bygger vi nytt vid sidan av, eller så förändrar vi det befintliga stegvis. I praktiken behöver många organisationer göra båda delarna samtidigt.

Det beror inte på brist på beslutsförmåga. Det beror på att myndigheter ofta har långlivade system, höga säkerhetskrav, begränsad förändringskapacitet, upptagna nyckelpersoner och verksamheter som inte kan pausa medan en ny plattform etableras.

Hybridvägen kan därför vara den mest realistiska vägen: en ny plattformsförmåga byggs upp med greenfield-liknande frihetsgrader, samtidigt som verkliga system och befintliga beroenden hanteras med brownfield-disciplin.

Men hybrid är inte automatiskt klokt. En otydlig hybrid kan bli det sämsta av båda världar: en ny plattform som inte får fäste, ett gammalt landskap som inte förändras, dubbla arbetssätt, dubbel styrning och ökande belastning på redan hårt pressade personer.

Kapitlet hjälper dig att skilja mellan en sund hybridstrategi och en hybrid som egentligen bara skjuter upp svåra beslut.

## Lärandemål

Efter kapitlet ska du kunna:

- förklara varför hybrid ofta blir det praktiska vägvalet i större myndigheter,
- skilja mellan sund hybrid och otydlig kompromiss,
- identifiera vanliga hybridmönster vid införande av en containerplattform,
- bedöma vilka risker hybrid skapar för styrning, drift, kompetens och prioritering,
- använda en enkel workshop för att avgöra om hybrid är ett verkligt vägval eller ett uppskjutet beslut.

## Innan vi börjar

Kapitel 5 visade att greenfield kan ge handlingsutrymme, men riskerar att skapa en isolerad ö. Kapitel 6 visade att brownfield kan vara verksamhetsnära, men riskerar att föra med sig gamla beroenden in i den nya miljön.

Hybridvägen uppstår när organisationen försöker hantera båda dessa sanningar samtidigt:

- Det behövs tillräckligt mycket frihet för att bygga en modern plattformsförmåga.
- Det behövs tillräckligt mycket koppling till befintlig verklighet för att plattformen ska bli användbar.
- Det behövs tillräckligt mycket styrning för att övergången inte ska bli permanent dubbelarbete.

Frågan är därför inte:

> Ska vi kompromissa?

Frågan är:

> Vilken kombination av greenfield och brownfield ger oss bäst chans att skapa faktisk organisatorisk förmåga?

## Vad hybrid betyder i denna bok

Hybrid betyder att organisationen kombinerar greenfield och brownfield som medveten förändringsstrategi.

Det kan till exempel innebära att:

- plattformen etableras som en ny miljö,
- styrning, säkerhet och driftmodell utvecklas parallellt,
- ett fåtal verkliga system väljs för stegvis migrering,
- befintliga beroenden kartläggs innan de flyttas,
- applikationsteam och driftfunktioner lär sig nya arbetssätt genom praktiskt arbete,
- äldre miljöer inte avvecklas direkt men får en tydlig övergångsplan.

Hybrid är alltså inte bara att göra lite av varje. En sund hybrid har en tydlig idé om vad som ska vara nytt, vad som ska förändras stegvis och vad som ska avvecklas eller lämnas utanför.

Det är skillnad på dessa två utsagor:

> Vi väljer hybrid eftersom olika delar av organisationen behöver olika förändringstakt.

och:

> Vi väljer hybrid eftersom vi inte kan enas om greenfield eller brownfield.

Den första kan vara en strategi. Den andra är ofta en varningssignal.

## Varför hybrid ofta passar myndighetsmiljöer

Hybrid passar ofta myndighetsmiljöer eftersom den tar höjd för att organisationen både behöver förändring och kontinuitet.

En större myndighet kan sällan säga:

> Vi börjar om helt från noll.

Det finns system som måste fungera, datakällor som måste skyddas, avtal som måste följas, säkerhetskrav som måste uppfyllas och verksamheter som är beroende av stabil drift.

Samtidigt kan myndigheten sällan säga:

> Vi förändrar bara det befintliga i befintlig takt.

Då finns risken att införandet blir så bundet av dagens arbetssätt att containerplattformen aldrig blir mer än ännu en driftmiljö.

Hybrid blir därför attraktivt när organisationen behöver:

- bygga ny förmåga utan att störa kritisk drift,
- minska personberoenden utan att tappa nyckelkompetens,
- införa standardisering utan att låtsas att alla system är lika,
- pröva nya arbetssätt utan att skapa en frikopplad experimentmiljö,
- skapa lärande i praktiken snarare än genom enbart utbildning,
- hantera säkerhetskrav stegvis men kontrollerat.

Hybridens styrka är att den kan skapa rörelse. Dess svaghet är att rörelsen lätt blir otydlig om styrningen är svag.

## Tre vanliga hybridmönster

Det finns många sätt att kombinera greenfield och brownfield. För en chef är det viktigare att förstå mönstren än att hitta perfekta etiketter.

### Mönster 1: Ny plattform, stegvis migrering

Organisationen etablerar en ny containerplattform med relativt rena principer, men låter befintliga system migreras stegvis utifrån risk, nytta och genomförbarhet.

Det är ofta det mest begripliga hybridmönstret.

Fördelar:

- plattformsteamet får möjlighet att etablera tydliga standarder,
- migrering kan prioriteras utifrån verkligt värde,
- kritiska system behöver inte flyttas först,
- organisationen kan lära sig innan de mest komplexa systemen berörs.

Risker:

- gamla miljöer kan bli kvar längre än planerat,
- samma personer kan behöva stödja både gamla och nya arbetssätt,
- plattformen kan byggas utan tillräcklig återkoppling från de svåra systemen,
- avvecklingsplanen kan bli för svag.

Detta mönstret kräver tydlig prioritering. Annars blir den nya plattformen en extra miljö, inte en väg till förändring.

### Mönster 2: Verkligt pilotsystem i ny miljö

Organisationen väljer ett verkligt system som pilot, men avgränsar omfattning och risk så att införandet kan ske kontrollerat.

Detta är ofta starkare än en helt konstgjord pilot. Ett verkligt system tvingar fram frågor om säkerhet, drift, integrationer, loggning, övervakning, support, livscykelhantering och ansvar.

Fördelar:

- piloten testar verkliga organisatoriska förmågor,
- beroenden blir synliga tidigt,
- lärandet blir konkret,
- plattformsteam och applikationsteam får arbeta tillsammans.

Risker:

- fel pilotsystem kan skapa för hög risk eller för låg relevans,
- nyckelpersoner kan bli ännu mer belastade,
- piloten kan tolkas som tekniskt projekt snarare än organisationsförändring,
- lärdomar kan stanna i projektet och inte spridas.

Detta mönstret kräver ett noggrant val av pilot. Systemet ska vara tillräckligt verkligt för att ge lärande, men inte så kritiskt eller komplext att det blockerar hela införandet.

### Mönster 3: Ny styrning för nya system, stegvis anpassning av gamla

Organisationen beslutar att nya system eller större förändringar ska använda den nya plattformen och nya arbetssätt, medan befintliga system anpassas stegvis.

Detta mönster kan fungera när myndigheten har en stor systemportfölj och inte kan migrera allt samtidigt.

Fördelar:

- nya initiativ kan börja med modernare standarder,
- äldre system tvingas inte in i en olämplig modell för snabbt,
- styrningen kan skapa riktning utan att stoppa verksamheten,
- prioritering kan göras vid naturliga förändringstillfällen.

Risker:

- två regelverk kan leva parallellt för länge,
- undantag kan bli norm,
- gamla system kan aldrig komma in i förändringen,
- otydlighet kan uppstå om vilka krav som gäller när.

Detta mönstret kräver tydliga beslut om när ett system ska omfattas av den nya modellen. Annars blir hybrid en permanent uppdelning mellan gammalt och nytt.

## När hybrid är klokt

Hybrid är ofta klokt när organisationen behöver både handlingsutrymme och verklighetsförankring.

Det kan vara ett bra vägval när:

- befintliga system är för viktiga för att hanteras som experiment,
- organisationen har teknisk skuld men också stark verksamhetskritisk kunskap,
- nyckelpersoner är hårt belastade men måste involveras,
- säkerhets- och driftkrav behöver utvecklas praktiskt,
- det finns behov av ny plattformsförmåga men låg tolerans för störningar,
- alla system inte har samma mognad, risknivå eller förändringsbehov,
- ledningen vill minska personberoenden utan att tappa kontroll över befintlig drift.

Hybrid är också klokt när organisationen inser att införandet är en resa i flera steg. Man behöver bygga förmåga, testa arbetssätt, skapa styrning, migrera system och avveckla gamla lösningar i en ordning som går att genomföra.

## När hybrid är riskabelt

Hybrid är riskabelt när det används som ett sätt att undvika prioritering.

Varningssignaler:

- Ingen kan säga vilka delar som är greenfield och vilka som är brownfield.
- Det finns ingen tydlig målbild för när övergångsperioden ska vara över.
- Både gammal och ny miljö finansieras, men ingen avveckling planeras.
- Samma nyckelpersoner förväntas bära både daglig drift och införande.
- Undantag hanteras informellt i stället för som medvetna beslut.
- Säkerhets-, drift- och arkitekturkrav skiljer sig mellan team utan tydlig motivering.
- Plattformen växer tekniskt men adoptionen i organisationen är låg.
- Ledningen följer upp projektaktiviteter men inte faktisk förmågeutveckling.

I dessa lägen kan hybrid bli ett ord som döljer brist på styrning. Då växer dubbel komplexitet: fler miljöer, fler arbetssätt, fler beroenden och fler oklara ansvar.

## Dubbel styrning: hybridens centrala chefsrisk

Hybrid kräver ofta dubbel styrning under en period. Organisationen behöver styra både den nya plattformsförmågan och den befintliga miljön.

Det är inte fel. Felet uppstår när dubbel styrning blir osynlig.

En chef behöver därför säkerställa att det finns svar på fem frågor:

1. Vem beslutar vilka system som får eller ska gå till den nya plattformen?
2. Vem beslutar vilka undantag som är tillåtna?
3. Vem finansierar övergången när både gammalt och nytt måste leva samtidigt?
4. Vem ansvarar för drift och incidenthantering under övergången?
5. Vem beslutar när gamla miljöer, arbetssätt eller beroenden ska avvecklas?

Utan dessa svar skapas lätt en miljö där alla förväntas vara positiva till förändringen, men ingen har mandat att göra den svåra prioriteringen.

Dubbel styrning bör därför vara tidsatt, bemannad och följd. Den ska inte vara ett naturligt tillstånd.

## Beslutsstöd: sund hybrid eller uppskjutet beslut?

Använd tabellen nedan för att bedöma om hybrid är ett medvetet vägval eller ett tecken på att organisationen undviker beslut.

| Fråga | Sund hybrid | Riskabel hybrid |
|---|---|---|
| Finns en tydlig målbild? | Ja, organisationen vet vilken förmåga som ska byggas | Nej, hybrid betyder mest att flera spår pågår |
| Finns prioriterade system eller områden? | Ja, ordningen är beslutad utifrån risk och nytta | Nej, varje del försöker hitta sin egen väg |
| Finns avvecklingslogik? | Ja, gamla arbetssätt och miljöer har en väg bort | Nej, nytt läggs ovanpå gammalt |
| Är nyckelpersoners tid säkrad? | Ja, deras insats är prioriterad och avlastad | Nej, de förväntas lösa införandet utöver daglig drift |
| Är undantag styrda? | Ja, undantag dokumenteras och tidsätts | Nej, undantag blir informell praxis |
| Följs förmåga upp? | Ja, ledningen följer upp adoption, kompetens och driftförmåga | Nej, uppföljningen handlar mest om teknikleveranser |

Om flera svar hamnar i den högra kolumnen är hybrid sannolikt inte tillräckligt styrd.

## Workshop: är hybrid rätt väg?

Den här workshopen kan genomföras med ledningsgrupp, styrgrupp, plattformsteam, driftrepresentanter, säkerhetsfunktion och representanter för några applikations- eller systemområden.

Syftet är att avgöra om hybrid är en genomtänkt strategi eller ett sätt att slippa välja.

### Steg 1: Rita upp de två världarna

Lista vad som i dag hör till befintlig miljö:

- system,
- driftmodeller,
- beroenden,
- nyckelpersoner,
- säkerhetsprocesser,
- incidentrutiner,
- dokumentation,
- avtal,
- verktyg.

Lista sedan vad som ska höra till den nya plattformsförmågan:

- plattformsteam,
- standarder,
- säkerhetsmönster,
- CI/CD-flöden,
- övervakning,
- loggning,
- supportmodell,
- livscykelhantering,
- krav på applikationsteam.

Fråga sedan:

> Vilka delar måste kopplas ihop tidigt för att den nya plattformen ska bli verklig för organisationen?

### Steg 2: Markera övergångsbryggor

Identifiera de delar som måste fungera mellan gammalt och nytt.

Exempel:

- identitet och åtkomst,
- nätverk och integrationer,
- loggning och spårbarhet,
- incident- och problemhantering,
- säkerhetsgranskning,
- release- och förändringsprocesser,
- bemanning och jour,
- dokumentation och kunskapsöverföring.

Dessa övergångsbryggor är ofta viktigare än själva installationsplanen. Om de saknas får organisationen en teknisk plattform utan fungerande verksamhetskoppling.

### Steg 3: Välj första verkliga förändringsobjekt

Välj ett system, en systemkategori eller ett initiativ som kan bära lärande.

Det bör vara:

- tillräckligt relevant för att testa verkliga krav,
- tillräckligt avgränsat för att inte skapa oacceptabel risk,
- tillräckligt prioriterat för att få resurser,
- tillräckligt representativt för att lärdomarna ska vara användbara.

Undvik två ytterligheter:

- ett så enkelt pilotfall att det inte säger något om verkligheten,
- ett så kritiskt och komplext system att införandet fastnar direkt.

### Steg 4: Besluta vad som inte ska göras ännu

Hybrid kräver inte att allt görs samtidigt. Tvärtom är en sund hybrid ofta tydlig med vad som får vänta.

Exempel:

- vissa system migreras inte i första vågen,
- vissa automatiseringar byggs inte innan driftmodellen är beslutad,
- vissa undantag accepteras bara under begränsad tid,
- vissa gamla miljöer hålls kvar men får ingen fortsatt nyutveckling.

Detta är chefsarbete. Att välja bort är lika viktigt som att välja väg.

### Steg 5: Sätt upp uppföljning

Bestäm hur hybridspåret ska följas upp.

Följ inte bara upp om plattformen finns. Följ upp om organisationen faktiskt utvecklar förmåga.

Exempel på uppföljningsfrågor:

- Har personberoendet minskat eller ökat?
- Har fler än nyckelpersonerna praktisk kompetens?
- Har pilotens lärdomar blivit standarder?
- Har gamla beroenden dokumenterats och minskats?
- Har incident- och driftansvar blivit tydligare?
- Har gamla miljöer fått en realistisk avvecklingsplan?
- Har applikationsteam förstått vad den nya modellen kräver?

## Vanliga misstag

- **Misstag: Att kalla allt hybrid.**
  - Varför det händer: Organisationen vill undvika ett binärt val.
  - Hur du undviker det: Beskriv exakt vad som är greenfield, vad som är brownfield och vad som är övergång.

- **Misstag: Att bygga nytt utan avvecklingsplan.**
  - Varför det händer: Den nya plattformen känns mer konkret än den svåra frågan om vad som ska bort.
  - Hur du undviker det: Kräv att varje nytt spår har en koppling till migrering, avveckling eller tydlig avgränsning.

- **Misstag: Att underskatta belastningen på nyckelpersoner.**
  - Varför det händer: Samma personer kan både det gamla och behövs i det nya.
  - Hur du undviker det: Frigör tid formellt och acceptera inte att införandet läggs ovanpå ordinarie drift.

- **Misstag: Att låta undantag bli standard.**
  - Varför det händer: Övergången kräver flexibilitet.
  - Hur du undviker det: Dokumentera undantag, ange ägare och sätt slutdatum eller omprövningsdatum.

- **Misstag: Att följa upp projektplanen men inte förmågan.**
  - Varför det händer: Tekniska leveranser är lättare att mäta än organisatoriskt lärande.
  - Hur du undviker det: Följ upp kompetensspridning, adoption, driftsäkerhet, standardisering och minskat personberoende.

## Tecken på att hybrid fungerar

Hybrid fungerar när den skapar kontrollerad rörelse.

Tecken på att ni är på rätt väg:

- Den nya plattformen används av verkliga system, inte bara demonstrationer.
- Befintlig driftkompetens är involverad men inte ensam bärare av förändringen.
- Plattformsteamet får återkoppling från verkliga migreringar.
- Säkerhets- och driftkrav blir tydligare genom arbetet.
- Undantag minskar över tid.
- Gamla miljöer får tydligare framtid: behållas, förändras eller avvecklas.
- Ledningen förstår vilka prioriteringar som krävs för nästa steg.

Det viktigaste tecknet är att organisationen lär sig. Hybrid är inte bara en arkitektur- eller migreringsmodell. Det är en praktisk lärandemodell för en organisation som måste förändras utan att tappa kontrollen.

## Övningar

### Övning 1: Skriv en hybriddefinition

Skriv tre meningar som beskriver vad hybrid skulle betyda i er organisation.

Använd gärna formen:

1. Vi bygger nytt inom följande områden: ...
2. Vi förändrar befintligt inom följande områden: ...
3. Vi accepterar en övergångsperiod för följande delar, men med dessa begränsningar: ...

Om ni inte kan fylla i alla tre meningar är hybridvägen troligen för otydlig.

### Övning 2: Identifiera dubbel styrning

Lista de områden där gammal och ny modell behöver styras samtidigt.

Exempel:

- finansiering,
- driftansvar,
- säkerhetsgranskning,
- arkitekturprinciper,
- incidenthantering,
- kompetensförsörjning,
- avveckling.

För varje område, svara på:

- Vem äger frågan?
- Vilka beslut måste fattas?
- Hur länge kan dubbel styrning accepteras?
- Vad händer om inget beslut fattas?

### Övning 3: Bedöm hybridens ärlighet

Samla styrgruppen och låt varje deltagare svara på frågan:

> Väljer vi hybrid därför att det är rätt förändringsstrategi, eller därför att vi inte vill välja?

Svaren behöver inte vara bekväma. Syftet är att synliggöra om hybrid är en strategi eller en kompromiss utan riktning.

## Snabb sammanfattning

- Hybrid betyder att greenfield och brownfield kombineras som medveten förändringsstrategi.
- Hybrid passar ofta större myndigheter eftersom de behöver både ny förmåga och stabil kontinuitet.
- En sund hybrid är tydlig med vad som byggs nytt, vad som förändras stegvis och vad som ska avvecklas.
- En riskabel hybrid döljer ofta brist på prioritering, avvecklingsplan eller mandat.
- Hybrid kräver styrning av övergången, inte bara etablering av ny teknik.
- Den största chefsrisken är dubbel komplexitet: gammalt och nytt lever parallellt utan tydlig riktning.
- Hybrid fungerar när organisationen lär sig, minskar personberoenden och omsätter plattformen i verklig driftförmåga.

## Quiz/reflektionsfrågor

1. Vad är skillnaden mellan en sund hybrid och en otydlig kompromiss?
2. Varför kan ett verkligt pilotsystem vara bättre än en helt konstgjord pilot?
3. Vilka risker uppstår om gamla miljöer inte får en avvecklingsplan?
4. Hur kan hybrid både minska och öka personberoenden?
5. Vilka tre styrningsfrågor behöver vara besvarade innan en hybridstrategi startar?

## Nästa steg

Nu har vi jämfört greenfield, brownfield och hybrid. Nästa steg är att göra vägvalet praktiskt beslutsbart.

I nästa kapitel samlar vi därför kriterierna i en konkret beslutsmodell. Där vägs förändringskapacitet, kompetensrisk, systemkritikalitet, säkerhetskrav, teknisk skuld och mandat mot varandra för att ge en strukturerad rekommendation: greenfield, brownfield eller hybrid.
