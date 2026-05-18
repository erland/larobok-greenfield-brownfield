# Kapitel 3: Myndighetskontexten: styrning, säkerhet och beroenden

## Varför detta kapitel finns

Ett införande av OpenShift eller annan containerplattform sker aldrig i ett tomrum. I en större statlig myndighet påverkas beslutet av styrning, säkerhet, upphandling, regelverk, befintliga system, driftansvar och tillgänglig kompetens.

Det gör valet mellan greenfield och brownfield mer krävande än i en mindre eller mer fristående organisation. Ett vägval som ser rationellt ut tekniskt kan bli svårt att genomföra om det krockar med befintliga beslutsvägar, säkerhetskrav eller den faktiska belastningen i linjen.

Kapitlet hjälper dig att se vilka villkor som måste tas på allvar innan organisationen väljer väg.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- beskriva varför myndighetsmiljöer ställer särskilda krav på införande av containerplattformar,
- identifiera styrnings-, säkerhets- och driftberoenden som påverkar vägvalet,
- se hur personberoende och hög arbetsbelastning kan förändra riskbilden,
- skilja mellan formell förändringsvilja och faktisk genomförandeförmåga,
- formulera vilka begränsande villkor som måste vara synliga i beslutsunderlaget.

## Innan vi börjar

Kapitel 2 beskrev greenfield, brownfield och hybrid som förändringsstrategier. I praktiken avgörs valet inte bara av vilken strategi som verkar mest modern eller mest försiktig. Valet avgörs av vilken strategi organisationen kan genomföra utan att tappa kontroll över verksamhetskritiska system, säkerhet och ansvar.

I en myndighet finns ofta flera parallella verkligheter:

- den formella styrningen,
- den tekniska arkitekturen,
- den dagliga driften,
- säkerhets- och regelefterlevnadsarbetet,
- upphandlade avtal och leverantörsrelationer,
- informella beroenden till nyckelpersoner,
- verksamhetens behov av stabilitet.

Ett beslut om införande behöver fungera i alla dessa verkligheter samtidigt.

## Myndighetsmiljön är inte bara en större version av en vanlig organisation

Det är lätt att tänka att en större myndighet bara är en större IT-organisation. Det är missvisande. Storlek är bara en del av komplexiteten.

En myndighet verkar ofta under villkor som gör förändring mer styrd, mer spårbar och mer beroende av förankring än i många andra miljöer. Beslut behöver kunna motiveras. Risker behöver kunna beskrivas. Ansvar behöver kunna följas. Säkerhetskrav behöver hanteras systematiskt. Upphandling och avtal kan sätta ramar för vad som är praktiskt möjligt.

Det betyder inte att myndigheter inte kan arbeta modernt. Det betyder att moderna arbetssätt måste införas på ett sätt som fungerar tillsammans med offentlig styrning, rättssäkerhet, informationssäkerhet och långsiktigt ansvar.

För chefen innebär det att frågan inte bara är:

> Vilket tillvägagångssätt ger bäst teknisk målbild?

Den viktigare frågan är:

> Vilket tillvägagångssätt kan vi genomföra med kontroll, ansvar och uthållighet i vår faktiska myndighetsmiljö?

## Styrning: vem har mandat att förändra vad?

Containerplattformar påverkar ofta flera organisatoriska nivåer. De berör arkitektur, drift, utveckling, säkerhet, budget, sourcing, förvaltning och verksamhetsprioriteringar. Därför räcker det sällan med ett tekniskt projektmandat.

Ett greenfield-spår kan behöva mandat att etablera nya standarder, nya arbetssätt och nya ansvarsförhållanden. Utan det finns risken att plattformen byggs som en teknisk miljö, men aldrig blir en accepterad del av myndighetens ordinarie styrning.

Ett brownfield-spår kan behöva mandat att ändra befintliga driftmönster, dokumentera beroenden, prioritera migrering och frigöra nyckelpersoner. Utan det finns risken att arbetet fastnar i den dagliga driften och att förändringen blir en serie lokala kompromisser.

Ställ därför tidigt följande frågor:

- Vem äger beslutet om målbild?
- Vem äger beslutet om prioritering mellan daglig drift och förändringsarbete?
- Vem kan besluta om gemensamma standarder?
- Vem kan avveckla gamla arbetssätt när nya införs?
- Vem ansvarar när plattformen går från projekt till förvaltning?
- Vilka beslut kräver förankring i säkerhet, arkitektur, ekonomi eller verksamhetsledning?

Om dessa frågor saknar tydliga svar är vägvalet ännu inte moget.

## Säkerhet: inte ett efterhandsvillkor

Säkerhet får inte behandlas som en kontrollpunkt i slutet av införandet. I en myndighetsmiljö påverkar säkerhetskraven själva vägvalet.

En containerplattform kan ge bättre förutsättningar för standardisering, spårbarhet, automatiserade kontroller och konsekvent livscykelhantering. Samtidigt kan den införa nya beroenden, nya behörighetsmodeller och nya angreppsytor om ansvar och styrning är otydliga.

För greenfield är en vanlig risk att säkerhetsmodellen designas för den nya plattformen men inte tillräckligt kopplas till myndighetens befintliga säkerhetsstyrning. Plattformen kan då bli tekniskt välordnad men organisatoriskt svår att godkänna eller använda brett.

För brownfield är en vanlig risk att befintliga undantag, informella lösningar och otydliga ansvar följer med in i den nya miljön. Då kan organisationen tro att den moderniserar, men i praktiken flyttas gamla säkerhetsproblem till en ny plattform.

Ett tillräckligt beslutsunderlag bör därför beskriva:

- vilka informationsklasser och skyddsvärden som berörs,
- vilka säkerhetskrav som är styrande,
- hur identitet, behörighet och åtkomst ska hanteras,
- hur loggning, övervakning och spårbarhet ska fungera,
- hur sårbarheter och uppdateringar ska hanteras,
- vem som godkänner säkerhetsmodellen,
- vilka undantag som finns i dagens miljö och hur de ska hanteras.

Det viktiga är inte att alla detaljer är lösta före vägvalet. Det viktiga är att säkerhetsfrågorna är synliga nog för att påverka valet.

## Beroenden: det osynliga som styr genomförandet

Beroenden är ofta den del av nuläget som underskattas mest. De finns mellan system, team, avtal, miljöer, processer och personer.

Ett system kan se möjligt ut att flytta till en containerplattform tills organisationen upptäcker att det har beroenden till äldre databaser, nätverksregler, batchflöden, särskilda driftfönster, manuella rutiner eller en leverantörsmodell som inte passar den nya plattformen.

Beroenden påverkar greenfield och brownfield på olika sätt.

Vid greenfield finns risken att beroendena underskattas därför att den nya miljön byggs vid sidan av. Plattformen kan fungera väl med nya eller enkla applikationer, men få svårt att bära verkliga myndighetssystem när beroendena väl kommer in.

Vid brownfield finns risken att beroendena blir så styrande att den nya plattformen formas efter det gamla. Då kan organisationen få en containerplattform som tekniskt sett är ny, men som fortfarande styrs av samma begränsningar som tidigare.

Ett användbart sätt att hantera beroenden är att skilja på fyra typer:

| Typ av beroende | Exempel | Varför det påverkar vägvalet |
|---|---|---|
| Tekniskt beroende | Databaser, integrationer, nätverk, identitet | Avgör hur lätt system kan anslutas eller flyttas |
| Operativt beroende | Driftfönster, incidentrutiner, övervakning | Avgör hur förändring påverkar daglig stabilitet |
| Organisatoriskt beroende | Team, mandat, prioriteringar, budget | Avgör om beslut kan genomföras i praktiken |
| Personberoende | Enskilda specialister, informell kunskap | Avgör sårbarhet, tempo och risk vid förändring |

Tabellen är enkel, men den brukar avslöja en viktig sak: valet mellan greenfield och brownfield påverkas lika mycket av organisatoriska och personliga beroenden som av tekniska beroenden.

## Personberoende: när kompetens är både styrka och risk

I många myndigheter finns mycket hög kompetens hos enskilda personer eller små grupper. Det är en styrka. Det är ofta dessa personer som har hållit komplexa system stabila under lång tid.

Samtidigt kan samma kompetens bli en risk när organisationen ska förändras. Om drift, felsökning och beslut är beroende av ett fåtal personer blir införandet av en containerplattform sårbart.

Personberoende påverkar vägvalet på flera sätt.

Greenfield kan minska personberoenden på sikt genom nya standarder, dokumenterade arbetssätt och teamförmåga. Men i början kräver greenfield ofta ännu mer av nyckelpersonerna: de ska bidra med nulägeskunskap, bedöma risker, stödja nya team och samtidigt fortsätta hantera daglig drift.

Brownfield kan dra nytta av befintlig kompetens och verksamhetsnära kunskap. Men om förändringen inte frigör tid och dokumenterar arbetssätt riskerar brownfield att förstärka personberoendet. Då blir den nya plattformen bara ytterligare en miljö som samma få personer måste förstå.

Som chef bör du därför inte bara fråga om organisationen har kompetens. Fråga i stället:

- Är kompetensen spridd eller koncentrerad?
- Är kritisk kunskap dokumenterad?
- Finns det team som kan ta gemensamt ansvar?
- Kan nyckelpersoner frigöras utan att driften blir för sårbar?
- Finns tid för kunskapsöverföring?
- Finns det en plan för att minska personberoenden under införandet?

Ett vägval som förutsätter att redan överbelastade nyckelpersoner ska bära både drift och transformation är inte ett robust vägval.

## Hög arbetsbelastning förändrar riskbilden

En vanlig utgångspunkt i större organisationer är att alla redan är upptagna. Den dagliga driften, incidenter, förvaltning, säkerhetsarbete, upphandlingar, projekt och verksamhetsstöd fyller kalendern.

Detta är inte en detalj. Det är en av de viktigaste faktorerna i beslutet.

Greenfield kan se lockande ut när linjen är hårt belastad, eftersom det verkar möjligt att bygga nytt vid sidan av utan att störa det befintliga. Men om plattformen senare ska tas emot av samma organisation kommer belastningen tillbaka. Det som skjutits upp blir då ett mottagandeproblem.

Brownfield kan se realistiskt ut eftersom det utgår från befintliga system och team. Men om de teamen redan saknar tid kan förändringen bli för långsam, fragmenterad eller beroende av kvälls- och undantagsinsatser.

I båda fallen behöver beslutet innehålla en ärlig bedömning av kapacitet:

- Vilka personer behöver delta?
- Hur mycket tid kan de faktiskt avsätta?
- Vilka arbetsuppgifter ska prioriteras ned?
- Vilka risker uppstår om de inte kan frigöras?
- Vem skyddar förändringsarbetet från att alltid förlora mot akuta driftbehov?

Om svaret är att ingen kan frigöras, men införandet ändå ska lyckas, bygger beslutet på önsketänkande.

## När formella krav och driftverklighet pekar åt olika håll

I myndighetsmiljöer finns ofta en spänning mellan formell målbild och faktisk driftverklighet. På papperet kan organisationen vilja standardisera, automatisera och minska personberoenden. I vardagen kan den samtidigt behöva hantera gamla system, otydliga beroenden och akuta problem.

Detta skapar ett särskilt chefsansvar. Beslutet behöver hålla ihop två perspektiv:

- den önskade framtida förmågan,
- den faktiska vägen dit.

Ett beslut som bara utgår från målbilden kan bli för abstrakt. Ett beslut som bara utgår från nuläget kan bli för försiktigt. Den svåra men nödvändiga uppgiften är att välja en väg som rör organisationen mot målbilden utan att tappa kontroll över nuläget.

Det är därför hybrid ofta blir aktuellt i större myndigheter. Inte för att hybrid alltid är bäst, utan för att den kan vara ett sätt att skilja mellan två behov:

- att bygga en renare och mer styrbar plattformsförmåga,
- att förändra verkliga system och driftmönster stegvis.

Men hybrid kräver tydlighet. Utan tydlig styrning kan hybrid bli ett namn på obeslutsamhet.

## Miniworkshop: identifiera tre begränsande villkor

Använd den här övningen i ledningsgrupp, styrgrupp eller inför ett beslutsmöte. Syftet är att göra myndighetskontexten konkret innan vägvalet diskuteras.

### Steg 1: Lista villkor

Be deltagarna skriva ned de viktigaste villkoren som påverkar införandet. Använd fem kategorier:

- styrning och mandat,
- säkerhet och regelefterlevnad,
- system- och integrationsberoenden,
- personberoenden och kompetens,
- arbetsbelastning och förändringskapacitet.

### Steg 2: Välj de tre mest begränsande

Diskutera vilka tre villkor som mest begränsar organisationens handlingsutrymme. Det kan till exempel vara:

- att säkerhetsmodellen ännu inte är förankrad,
- att kritisk driftkompetens finns hos två personer,
- att de första systemen har fler integrationer än förväntat,
- att ingen linjeorganisation har tid att ta emot plattformen,
- att mandatet bara täcker teknik men inte arbetssätt.

### Steg 3: Bedöm påverkan på vägvalet

För varje villkor, diskutera hur det påverkar greenfield, brownfield och hybrid.

| Begränsande villkor | Påverkan på greenfield | Påverkan på brownfield | Påverkan på hybrid |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

Målet är inte att fatta beslut direkt. Målet är att undvika att beslutet fattas utan att de verkliga begränsningarna är synliga.

## Vanliga misstag

- **Misstag: Att se myndighetskrav som bromsklossar i stället för designvillkor.**
  - Varför det händer: Förändringsarbete drivs ofta av frustration över tröghet.
  - Hur du undviker det: Behandla styrning, säkerhet och spårbarhet som krav som måste byggas in i införandet.

- **Misstag: Att underskatta informella beroenden.**
  - Varför det händer: Formella systemkartor visar sällan vem som faktiskt löser problemen.
  - Hur du undviker det: Kartlägg personberoenden, driftkunskap och informella rutiner tidigt.

- **Misstag: Att tro att greenfield undviker belastning i linjen.**
  - Varför det händer: Ny miljö vid sidan av ser ut att kräva mindre av befintliga team.
  - Hur du undviker det: Planera redan från början för mottagande, driftansvar och övergång till ordinarie verksamhet.

- **Misstag: Att tro att brownfield automatiskt är tryggare.**
  - Varför det händer: Det känns säkrare att utgå från det befintliga.
  - Hur du undviker det: Synliggör risken att gamla beroenden, undantag och personberoenden följer med in i den nya plattformen.

## Snabb sammanfattning

- Myndighetsmiljöer kräver särskilt tydligt beslutsunderlag eftersom styrning, säkerhet, ansvar och beroenden påverkar genomförbarheten.
- Greenfield kan skapa en renare målbild men riskerar att bli frikopplat från ordinarie styrning och drift.
- Brownfield kan ligga närmare verkliga system men riskerar att bära med sig gamla beroenden och personberoenden.
- Personberoende är både en kompetensresurs och en förändringsrisk.
- Hög arbetsbelastning är inte ett praktiskt sidoproblem, utan en central del av riskbilden.
- Ett vägval är inte moget förrän organisationens viktigaste begränsande villkor är synliga.

## Quiz/reflektionsfrågor

1. Vilka delar av er myndighets styrning påverkar ett införande av containerplattform mest?
2. Vilka säkerhetsfrågor behöver vara synliga innan vägvalet görs?
3. Vilka system- eller integrationsberoenden riskerar att underskattas?
4. Var finns de största personberoendena i dagens drift?
5. Vilka personer eller team behöver frigöras för att införandet ska bli realistiskt?
6. Vilket är ert tydligaste tecken på att organisationen inte har tillräcklig förändringskapacitet just nu?

## Nästa steg

Nästa kapitel går från kontext till nuläge. Där samlar vi det beslutsunderlag som behövs innan greenfield, brownfield eller hybrid kan bedömas på allvar: systemportfölj, teknisk skuld, driftmodell, kompetensläge och förändringskapacitet.
