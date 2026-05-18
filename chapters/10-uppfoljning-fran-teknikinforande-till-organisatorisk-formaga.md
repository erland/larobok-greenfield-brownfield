# Kapitel 10: Uppföljning: från teknikinförande till organisatorisk förmåga

## Varför detta kapitel finns

När beslutet är fattat och genomförandet har startat uppstår en ny risk: att organisationen börjar följa upp fel saker.

Det är lätt att mäta om plattformen är installerad, hur många miljöer som är skapade, hur många applikationer som har flyttats eller hur många team som har fått åtkomst. Sådana mått kan vara användbara, men de säger inte automatiskt om införandet har lyckats.

Ett införande av en containerplattform, exempelvis OpenShift, är inte färdigt när tekniken fungerar. Det är färdigt först när organisationen har byggt en stabil förmåga att använda, drifta, säkra, vidareutveckla och styra plattformen över tid.

Kapitlet visar hur chefen bör följa upp införandet efter beslutet. Fokus ligger på effekter, riskindikatorer, lärande och organisatorisk förmåga. Målet är att undvika att införandet blir ett teknikprojekt som avslutas innan organisationen faktiskt har förändrats.

## Lärandemål

Efter kapitlet ska du kunna:

- skilja mellan tekniska leveranser och organisatorisk förmåga,
- formulera effektmål som går att följa upp,
- identifiera tidiga riskindikatorer,
- följa upp om personberoenden faktiskt minskar,
- använda styrgruppen för lärande, inte bara rapportering,
- avgöra när vägvalet behöver justeras.

## Innan vi börjar

Föregående kapitel beskrev hur genomförandet kan läggas upp efter beslutet. Där betonades mandat, pilotval, mottagande organisation, driftmodell och kompetensöverföring.

Uppföljningen ska nu kontrollera om dessa saker faktiskt händer.

Det räcker inte att fråga om projektet följer plan. Chefen behöver också fråga om organisationen blir mer kapabel än tidigare.

Det är skillnad på två frågor:

- Levererar införandeprojektet enligt tidplan?
- Bygger organisationen den förmåga som beslutet syftade till?

Båda frågorna behövs. Men den andra är ofta viktigast.

## Vad betyder organisatorisk förmåga?

I den här boken betyder organisatorisk förmåga att organisationen inte bara har tillgång till teknik, utan också kan använda den på ett säkert, styrbart och hållbart sätt.

För en containerplattform kan organisatorisk förmåga handla om att:

- applikationsteam vet hur de ska använda plattformen,
- driftorganisationen vet hur incidenter och fel ska hanteras,
- säkerhetsfunktionen vet hur krav följs upp i den nya miljön,
- plattformsteamet har mandat att sätta standarder,
- dokumentation och arbetssätt finns och används,
- nyckelpersoner delar kunskap med fler,
- styrningen kan prioritera mellan nya behov, risker och teknisk skuld,
- ledningen förstår vilka effekter som faktiskt uppnås.

Om dessa delar saknas kan plattformen vara tekniskt modern men organisatoriskt svag.

Det är därför uppföljningen måste omfatta mer än teknikstatus.

## Följ upp effekter, inte bara aktiviteter

En vanlig fallgrop är att uppföljningen fylls med aktivitetsmått. Aktivitetsmått beskriver vad som görs. Effektmått beskriver vad som förändras.

Båda behövs, men de fyller olika funktioner.

| Typ av mått | Exempel | Vad det säger | Risk om det används ensamt |
|---|---|---|---|
| Aktivitet | Antal workshops genomförda | Att något har hänt | Säger inte om arbetssättet har förändrats |
| Leverans | Plattformsmiljö etablerad | Att en teknisk leverans finns | Säger inte om den kan användas hållbart |
| Adoption | Antal team som använder plattformen | Att användning har börjat | Säger inte om användningen är säker och effektiv |
| Effekt | Kortare ledtid för godkända driftsättningar | Att organisationen fått förbättrad förmåga | Kan vara svårt att mäta om nuläge saknas |
| Risk | Antal kritiska beroenden till enskilda personer | Om sårbarheter minskar eller ökar | Kräver ärlig rapportering |

Chefen bör kräva en balans mellan dessa typer av mått.

Ett bra uppföljningspaket visar inte bara vad som levererats, utan också om införandet minskar risk, ökar styrbarhet och skapar verklig nytta.

## Exempel på effektmål

Effektmål bör vara få, tydliga och kopplade till varför införandet gjordes.

Exempel på effektmål kan vara:

- minska personberoendet i utpekade driftmoment,
- skapa en gemensam och dokumenterad modell för applikationsdrift,
- korta tiden från godkänd ändring till produktionssättning för lämpliga system,
- förbättra spårbarhet och kontroll i driftsättningar,
- öka andelen standardiserade driftsättningsflöden,
- minska antalet manuella speciallösningar,
- förbättra förmågan att hantera sårbarheter och uppdateringar,
- skapa tydligare ansvar mellan plattformsteam, drift och applikationsteam.

Varje effektmål bör ha en ansvarig ägare och ett enkelt sätt att följas upp.

Det behöver inte alltid vara perfekt kvantitativt. I början kan en kombination av mätetal, självskattning, stickprov och styrgruppsdialog vara tillräcklig.

Det viktiga är att organisationen följer upp samma sak över tid.

## Riskindikatorer som chefen bör följa

Uppföljning handlar inte bara om att bekräfta framsteg. Den ska också fånga tidiga varningssignaler.

Här är riskindikatorer som är särskilt viktiga vid införande av containerplattform i en större myndighet.

### Personberoenden minskar inte

Om samma personer fortfarande måste lösa alla kritiska problem har införandet inte minskat sårbarheten. Det kan till och med ha ökat den, eftersom organisationen nu har både gamla och nya miljöer att hantera.

Frågor att ställa:

- Vilka moment kan bara en eller två personer utföra?
- Har fler personer fått praktisk erfarenhet, eller bara utbildning?
- Finns dokumenterade rutiner som används i verkligheten?
- Vad händer om en nyckelperson är borta i två veckor?

### Plattformen används men ägs inte tydligt

En plattform kan få användare innan ägarskapet är moget. Det skapar risk när incidenter, prioriteringar, kostnader eller säkerhetsfrågor uppstår.

Frågor att ställa:

- Vem äger plattformens roadmap?
- Vem prioriterar mellan nya behov och stabilitet?
- Vem beslutar om standarder och undantag?
- Vem ansvarar för livscykel, uppdateringar och avveckling?

### Gamla arbetssätt följer med in i den nya miljön

Om varje applikation får egna undantag, egna driftsättningsmönster och egna speciallösningar riskerar plattformen att bli en ny plats för gammal komplexitet.

Frågor att ställa:

- Vilka undantag har godkänts, och varför?
- Har undantagen slutdatum eller omprövningspunkt?
- Finns standardmönster som faktiskt används?
- Har plattformsteamet mandat att säga nej?

### Adoption sker utan mottagningsförmåga

Det kan se positivt ut att många team vill använda plattformen. Men om stöd, dokumentation, säkerhetsprocesser och driftmodell inte hinner med kan snabb adoption skapa ny risk.

Frågor att ställa:

- Hur många team kan plattformsteamet stödja samtidigt?
- Finns tydliga onboarding-kriterier?
- Vet teamen vad de själva ansvarar för?
- Finns supportmodell för både kontorstid och kritisk drift?

### Hybridläget blir permanent utan beslut

Hybrid kan vara en klok övergångsstrategi. Men om den saknar tydlig målbild, prioritering och avvecklingsplan kan den bli ett permanent tillstånd av dubbel komplexitet.

Frågor att ställa:

- Vilka delar av hybridläget är avsiktliga?
- Vilka delar är tillfälliga?
- Vad ska avvecklas, standardiseras eller flyttas?
- När ska vägvalet omprövas?

## Uppföljning i styrgrupp

Styrgruppen bör inte bara få en statusrapport. Den bör få ett beslutsunderlag.

En bra styrgruppsuppföljning bör innehålla:

- lägesbild för leveranser,
- lägesbild för effekter,
- aktuella risker och beroenden,
- beslut som behöver fattas,
- frågor där mandat saknas,
- lärdomar från pilot eller migrering,
- avvikelser från vägvalet,
- rekommendationer för nästa period.

Styrgruppen bör särskilt undvika att fastna i tekniska detaljfrågor. Den ska i stället fokusera på frågor som kräver ledningsbeslut.

Exempel:

- Behöver fler nyckelpersoner frigöras från linjearbete?
- Ska onboarding av nya team bromsas tills driftmodellen är tydligare?
- Ska vissa system undantas från första migreringsvågen?
- Ska ett greenfield-spår kopplas hårdare till befintlig styrning?
- Ska ett brownfield-spår få tydligare mandat att förenkla gamla arbetssätt?
- Ska hybridstrategin formaliseras med målbild och avvecklingsplan?

När styrgruppen används på detta sätt blir den ett forum för styrning och lärande, inte bara rapportering.

## Enkel uppföljningsmall

Följande mall kan användas månadsvis eller inför varje styrgruppsmöte.

| Område | Fråga | Status | Kommentar | Behöver beslut? |
|---|---|---|---|---|
| Effektmål | Ser vi mätbar eller observerbar effekt? | Grön/Gul/Röd | Kort beskrivning | Ja/Nej |
| Personberoende | Har beroenden till enskilda personer minskat? | Grön/Gul/Röd | Kort beskrivning | Ja/Nej |
| Driftmodell | Är ansvar för drift, incident och support tydligt? | Grön/Gul/Röd | Kort beskrivning | Ja/Nej |
| Säkerhet | Är säkerhetskrav integrerade i arbetssättet? | Grön/Gul/Röd | Kort beskrivning | Ja/Nej |
| Adoption | Använder rätt team och system plattformen i rätt takt? | Grön/Gul/Röd | Kort beskrivning | Ja/Nej |
| Standardisering | Följs gemensamma mönster och standarder? | Grön/Gul/Röd | Kort beskrivning | Ja/Nej |
| Kompetens | Sprids praktisk kunskap till fler? | Grön/Gul/Röd | Kort beskrivning | Ja/Nej |
| Vägval | Är valt vägval fortfarande rätt? | Grön/Gul/Röd | Kort beskrivning | Ja/Nej |

Mallen är enkel med avsikt. Den ska göra det lätt att se om införandet fortfarande rör sig mot rätt mål.

Om allt är grönt men inga svåra frågor lyfts bör chefen vara uppmärksam. I komplexa införanden är det normalt att vissa områden är gula. Det viktiga är att riskerna är synliga och hanteras.

## När vägvalet behöver justeras

Ett beslut om greenfield, brownfield eller hybrid ska inte ändras för lätt. Samtidigt får beslutet inte behandlas som heligt om verkligheten visar något annat.

Vägvalet kan behöva justeras när:

- förändringskapaciteten visar sig vara lägre än antaget,
- säkerhets- eller regelefterlevnadskrav kräver annan ordning,
- personberoenden blir större än väntat,
- pilotfall inte ger tillräckligt lärande,
- befintliga system visar sig vara mer beroende av varandra än kartläggningen visade,
- den mottagande organisationen inte hinner bygga förmåga,
- kostnadsbilden förändras,
- styrningen inte klarar av att prioritera mellan gammalt och nytt.

Justering betyder inte misslyckande. Det kan vara ett tecken på mogen styrning.

Exempel:

- Ett greenfield-spår kan behöva kompletteras med tidigare brownfield-migrering för att undvika isolering.
- Ett brownfield-spår kan behöva ett avgränsat greenfield-labb för att etablera standarder och arbetssätt snabbare.
- Ett hybridspår kan behöva tydligare beslut om vad som faktiskt ska avvecklas.
- Ett för snabbt införande kan behöva bromsas för att säkra driftmodell och kompetensöverföring.

Chefen bör skapa fasta omprövningspunkter där vägvalet granskas mot fakta, inte mot prestige.

## Workshop: skapa en uppföljningsmodell

Syftet med workshopen är att skapa en enkel modell för uppföljning som styrgruppen kan använda under införandet.

### Deltagare

- ansvarig chef eller sponsor,
- representant från plattformsteam,
- representant från drift,
- representant från säkerhet,
- representant från berörda applikationsteam,
- verksamhetsrepresentant om införandet påverkar kritiska tjänster.

### Tidsåtgång

Cirka 90 minuter.

### Steg 1: Bekräfta varför införandet görs

Skriv ned de tre viktigaste skälen till införandet.

Exempel:

- minska personberoende,
- skapa mer standardiserad applikationsdrift,
- förbättra spårbarhet och kontroll,
- öka förmågan att hantera förändring,
- minska manuell hantering.

Välj högst tre. Om allt är viktigt blir inget styrande.

### Steg 2: Välj effektmål

För varje skäl, formulera ett effektmål.

Exempel:

| Skäl | Effektmål |
|---|---|
| Minska personberoende | Minst tre personer ska kunna utföra och felsöka prioriterade driftmoment |
| Standardisera drift | Nya applikationer ska följa dokumenterad onboarding-process |
| Förbättra kontroll | Driftsättningar ska vara spårbara och följa godkänt flöde |

### Steg 3: Välj riskindikatorer

Välj två till fyra riskindikatorer som ska följas regelbundet.

Exempel:

- antal kritiska moment med enskilt personberoende,
- antal godkända undantag från standard,
- antal öppna frågor om driftansvar,
- antal team som väntar på stöd från samma nyckelperson,
- antal incidenter där ansvarsfördelning varit oklar.

### Steg 4: Bestäm rapporteringsrytm

Bestäm hur ofta uppföljningen ska göras och vem som ansvarar för att samla in underlag.

Rekommendation:

- kort operativ uppföljning varje eller varannan vecka,
- styrgruppsuppföljning varje månad,
- formell omprövning av vägvalet efter större pilot, första produktionssättning eller första migreringsvåg.

### Steg 5: Bestäm vad som kräver beslut

Markera vilka signaler som ska leda till styrgruppsbeslut.

Exempel:

- fler team vill in än plattformsteamet kan stödja,
- säkerhetskrav är otydliga för produktionssättning,
- personberoenden minskar inte efter två uppföljningsperioder,
- undantag från standard ökar,
- driftorganisationen saknar tid för nödvändig kompetensöverföring.

Resultatet av workshopen ska vara en uppföljningsmodell som ryms på en eller två sidor.

## Vanliga misstag

- **Misstag: Att mäta plattformsinstallation i stället för plattformsförmåga.**
  - Varför det händer: Tekniska leveranser är enklare att rapportera.
  - Hur du undviker det: Följ upp ansvar, användning, driftmodell, kompetens och effekter.

- **Misstag: Att tolka hög aktivitet som framgång.**
  - Varför det händer: Många möten, workshops och tekniska aktiviteter kan ge intryck av framdrift.
  - Hur du undviker det: Koppla aktiviteter till tydliga effekter och beslut.

- **Misstag: Att inte följa upp personberoenden.**
  - Varför det händer: Personberoenden är ofta känsliga och svåra att prata om.
  - Hur du undviker det: Gör beroendena sakliga, dokumenterade och kopplade till verksamhetsrisk.

- **Misstag: Att låta hybrid bli ett permanent undantagstillstånd.**
  - Varför det händer: Hybrid känns pragmatiskt och konfliktdämpande.
  - Hur du undviker det: Sätt målbild, avvecklingsplan och omprövningspunkter.

- **Misstag: Att styrgruppen bara tar emot rapporter.**
  - Varför det händer: Rapportering upplevs tryggare än beslut.
  - Hur du undviker det: Lyft fram beslutspunkter, mandatfrågor och prioriteringskonflikter.

## Övningar

### Övning 1: Skilj mellan aktivitet och effekt

Lista fem saker som införandeprojektet gör eller planerar att göra.

Markera sedan varje punkt som:

- aktivitet,
- leverans,
- adoption,
- effekt,
- riskindikator.

Fråga därefter:

- Har vi tillräckligt många effektmått?
- Har vi synliga riskindikatorer?
- Mäter vi något som faktiskt visar organisatorisk förmåga?

### Övning 2: Välj fem styrgruppsfrågor

Välj fem frågor som styrgruppen ska följa under de kommande tre månaderna.

Exempel:

1. Har personberoenden minskat i de prioriterade driftmomenten?
2. Har plattformsteamet tillräckligt mandat?
3. Är driftansvaret tydligt för första produktionssättningen?
4. Har säkerhetskraven integrerats i onboarding-processen?
5. Är valt vägval fortfarande rätt utifrån det vi lärt oss?

### Fördjupning: Ompröva vägvalet

Gå tillbaka till beslutsmatrisen från kapitel 8.

Uppdatera den med ny kunskap från genomförandet.

Fråga:

- Vilka antaganden var korrekta?
- Vilka antaganden var fel?
- Har riskbilden förändrats?
- Behöver vägvalet justeras?
- Behöver mandat, resurser eller tempo ändras?

## Snabb sammanfattning

- Införandet är inte färdigt när plattformen är installerad.
- Uppföljningen ska visa om organisationen bygger verklig förmåga.
- Effektmål är viktigare än enbart aktivitetsmått.
- Personberoenden, driftmodell, säkerhet, adoption och standardisering bör följas över tid.
- Styrgruppen ska fatta beslut, inte bara ta emot rapporter.
- Hybrid, greenfield och brownfield behöver alla följas upp mot sina egna risker.
- Ett justerat vägval kan vara ett tecken på mogen styrning, inte misslyckande.

## Quiz/reflektionsfrågor

1. Vilka tre effekter är viktigast att följa upp i din organisation?
2. Vilka mått använder ni i dag som mest visar aktivitet snarare än effekt?
3. Hur vet ni om personberoenden faktiskt minskar?
4. Vilka signaler skulle visa att valt vägval behöver justeras?
5. Vilka beslut bör styrgruppen vara beredd att fatta under de första sex månaderna?

## Avslutande steg

Boken har gått från förståelse av vägvalet till nulägesanalys, jämförelse, beslut, genomförande och uppföljning.

Som sista steg bör ledningen säkerställa att vägvalet inte bara är dokumenterat, utan också ägt. Det innebär att det finns ansvariga roller, tydliga beslutspunkter, en accepterad riskbild, bemannad förändringskapacitet och en uppföljningsmodell som visar om införandet stärker organisationens förmåga över tid.

Det viktigaste att ta med sig är att valet mellan greenfield, brownfield och hybrid inte avgörs av vilken väg som låter mest modern. Det avgörs av vilken väg organisationen kan genomföra, förvalta och lära av över tid.
