# Kapitel 8: Beslutsmodellen: så väljer ni rätt väg

## Varför detta kapitel finns

När greenfield, brownfield och hybrid har analyserats var för sig återstår den svåraste delen: att fatta ett beslut som går att genomföra i den verkliga organisationen.

I många organisationer fattas den här typen av beslut för tidigt. Det kan ske för att tekniken upplevs brådskande, för att ett projekt redan är igång, för att en leverantör föreslår en väg eller för att en stark intern röst har en tydlig preferens. I en större myndighet är det riskabelt. Vägvalet påverkar drift, säkerhet, kompetens, styrning, kostnader, ansvarsfördelning och verksamhetens förändringstakt.

Beslutet bör därför inte formuleras som:

> Vill vi bygga nytt eller förändra det gamla?

Det bör formuleras som:

> Vilket vägval ger oss bäst chans att skapa en hållbar plattformsförmåga, med acceptabel risk, utifrån vår faktiska förändringskapacitet?

Kapitlet ger en praktisk beslutsmodell. Syftet är inte att skapa en perfekt matematisk sanning. Syftet är att göra antaganden synliga, jämföra alternativen på samma grunder och ge beslutsfattare ett gemensamt språk för varför ett vägval rekommenderas.

## Lärandemål

Efter kapitlet ska du kunna:

- skilja mellan beslutsunderlag, beslutskriterier och rekommendation,
- välja kriterier som passar en myndighetskontext,
- använda viktning för att visa vad som är viktigast i beslutet,
- jämföra greenfield, brownfield och hybrid på ett strukturerat sätt,
- identifiera när resultatet visar ett tydligt vägval och när mer underlag behövs,
- genomföra en enkel beslutsworkshop med ledning, styrgrupp eller berörda ansvariga.

## Innan vi börjar

Beslutsmodellen bygger på de tidigare kapitlen:

- Kapitel 1 förklarade att containerplattformen är en organisatorisk förmåga, inte bara teknik.
- Kapitel 2 definierade greenfield, brownfield och hybrid som vägval.
- Kapitel 3 visade varför myndighetskontexten ställer särskilda krav.
- Kapitel 4 visade vilket nuläge som måste förstås.
- Kapitel 5, 6 och 7 jämförde greenfield, brownfield och hybrid.

Om dessa delar saknas blir beslutsmodellen svag. Då riskerar den att ge ett prydligt resultat på osäker grund.

En bra beslutsmodell ersätter inte omdöme. Den hjälper omdömet att bli tydligt, jämförbart och möjligt att granska.

## Beslutets tre delar

Ett robust vägval består av tre delar:

1. Beslutsunderlag.
2. Beslutskriterier.
3. Rekommendation med villkor.

Beslutsunderlaget beskriver verkligheten. Det handlar om systemportfölj, driftmodell, kompetens, personberoenden, säkerhetskrav, teknisk skuld, pågående belastning och förändringskapacitet.

Beslutskriterierna beskriver vad organisationen värderar i vägvalet. Det kan vara låg genomföranderisk, snabb effekt, minskat personberoende, säkerhetskontroll, kostnadskontroll eller förmåga att förändra arbetssätt.

Rekommendationen beskriver vilket vägval som bör väljas och under vilka förutsättningar. En bra rekommendation säger inte bara “välj hybrid”. Den säger exempelvis:

> Välj hybrid, men endast om plattformsteamet får tydligt mandat, två nyckelpersoner frigörs från löpande drift och de första systemen väljs utifrån dokumenterade beroenden.

Det är ofta villkoren som avgör om rekommendationen är seriös.

## Vanliga misstag i beslutsfasen

Beslutsfasen misslyckas ofta av andra skäl än tekniken. Här är några vanliga misstag.

- **Misstag: Att låta teknikpreferens bli beslutsmodell.**
  - Varför det händer: Personer med stark erfarenhet av en viss väg kan uppleva den som självklart rätt.
  - Hur du undviker det: Kräv att varje alternativ bedöms mot samma kriterier.

- **Misstag: Att jämföra ett idealiserat greenfield med ett realistiskt brownfield.**
  - Varför det händer: Det nya beskrivs som rent och framtidssäkert, medan det befintliga beskrivs med alla sina problem.
  - Hur du undviker det: Bedöm även greenfield mot verklig mottagarkapacitet, driftansvar, säkerhetskrav och kompetensläge.

- **Misstag: Att jämföra ett idealiserat brownfield med ett orealistiskt greenfield.**
  - Varför det händer: Organisationen överskattar hur lätt det är att förändra befintliga miljöer stegvis.
  - Hur du undviker det: Bedöm hur hårt befintliga nyckelpersoner redan är belastade och vilka beroenden som faktiskt måste hanteras.

- **Misstag: Att välja hybrid utan att välja styrning.**
  - Varför det händer: Hybrid låter pragmatiskt och mindre konfliktfyllt.
  - Hur du undviker det: Kräv tydlig ansvarsfördelning, prioritering och avvecklingslogik.

- **Misstag: Att fatta beslut utan villkor.**
  - Varför det händer: Ledningen vill komma vidare.
  - Hur du undviker det: Formulera vilka förutsättningar som måste vara uppfyllda för att beslutet ska gälla.

## Välj rätt beslutskriterier

Beslutskriterierna ska vara få nog för att kunna användas, men breda nog för att fånga verkliga risker. För en större myndighet rekommenderas åtta kriterier.

| Kriterium | Fråga att besvara |
|---|---|
| Verksamhetsnytta | Hur väl stödjer vägvalet myndighetens uppdrag och prioriterade behov? |
| Genomförbarhet | Kan organisationen genomföra vägvalet med nuvarande tid, mandat och kapacitet? |
| Drift- och stabilitetsrisk | Hur påverkas kritisk drift under införandet och efteråt? |
| Säkerhet och regelefterlevnad | Ger vägvalet tillräcklig kontroll över säkerhet, spårbarhet och kravuppfyllnad? |
| Kompetens och personberoende | Minskar vägvalet sårbar kompetensbindning över tid? |
| Förändringstakt | Ger vägvalet en rimlig takt utan att överbelasta organisationen? |
| Kostnads- och resurskontroll | Är kostnader, resurser och dubbelarbete möjliga att styra? |
| Långsiktig plattformsförmåga | Leder vägvalet till en hållbar förmåga, inte bara ett införandeprojekt? |

Kriterierna bör inte väljas i enbart IT-gruppen. De bör ägas av beslutssammanhanget: styrgrupp, ledning eller annan beslutsfunktion. Teknikspecialister kan bidra med fakta, men kriterierna uttrycker organisationens prioriteringar.

## Viktning: visa vad som faktiskt är viktigast

Alla kriterier är inte lika viktiga. En myndighet med mycket kritisk drift kan behöva väga stabilitet och säkerhet högre än snabb effekt. En organisation med allvarligt personberoende kan behöva väga kompetensrobusthet högre än kortsiktig enkelhet.

Viktning gör detta synligt.

Använd en enkel skala från 1 till 5:

| Vikt | Betydelse |
|---|---|
| 1 | Låg betydelse i detta beslut |
| 2 | Viss betydelse |
| 3 | Tydlig betydelse |
| 4 | Mycket stor betydelse |
| 5 | Avgörande betydelse |

Viktning ska göras innan alternativen poängsätts. Annars finns risk att viktningen justeras för att bekräfta ett redan önskat vägval.

En enkel kontrollfråga är:

> Om vi bara fick optimera tre saker i detta beslut, vilka skulle de vara?

Svaret bör påverka viktningen.

## Poängsättning av alternativen

När kriterierna är viktade bedöms varje alternativ: greenfield, brownfield och hybrid.

Använd en enkel skala från 1 till 5:

| Poäng | Tolkning |
|---|---|
| 1 | Svagt stöd eller hög risk |
| 2 | Betydande brister |
| 3 | Acceptabelt men med tydliga villkor |
| 4 | Starkt alternativ |
| 5 | Mycket starkt alternativ |

Poängen ska inte sättas som magkänsla. För varje poäng bör gruppen kunna ange en kort motivering. Om motiveringen saknas är poängen svag.

Exempel:

| Kriterium | Vikt | Greenfield | Brownfield | Hybrid |
|---|---|---|---|---|
| Genomförbarhet | 5 | 3 | 2 | 4 |
| Drift- och stabilitetsrisk | 5 | 3 | 3 | 4 |
| Kompetens och personberoende | 4 | 4 | 2 | 4 |
| Förändringstakt | 3 | 4 | 2 | 3 |
| Långsiktig plattformsförmåga | 5 | 4 | 3 | 4 |

I en enkel modell multipliceras vikt med poäng. Det ger inte ett slutgiltigt svar, men det hjälper gruppen att se mönster.

Exempel: om genomförbarhet har vikt 5 och hybrid får poäng 4 blir delresultatet 20.

Det viktigaste är inte totalpoängen i sig. Det viktigaste är samtalet som visar varför ett alternativ får höga eller låga poäng.

## Tolkning av resultatet

När matrisen är ifylld behöver resultatet tolkas. Undvik att automatiskt välja högsta totalpoäng utan granskning.

Ställ tre frågor:

1. Är skillnaden mellan alternativen tydlig?
2. Beror resultatet på fakta eller antaganden?
3. Finns det något kriterium där ett alternativ får så låg poäng att det blir olämpligt trots hög totalpoäng?

Den tredje frågan är särskilt viktig. Ett vägval kan få hög totalpoäng men ändå vara olämpligt om det faller på ett avgörande kriterium.

Exempel:

- Greenfield kan se attraktivt ut men vara olämpligt om mottagande organisation saknas.
- Brownfield kan se tryggt ut men vara olämpligt om personberoendet är extremt.
- Hybrid kan se balanserat ut men vara olämpligt om styrningen inte klarar dubbel komplexitet.

Beslutsmodellen bör därför innehålla spärrfrågor.

## Spärrfrågor innan beslut

Spärrfrågor är frågor där ett negativt svar kräver åtgärd innan beslutet genomförs.

För greenfield:

- Finns ett tydligt mandat för plattformsteamet?
- Finns en mottagande organisation som kan ta över förmågan?
- Finns verkliga pilotfall som kopplar plattformen till myndighetens behov?
- Finns en plan för drift, säkerhet och förvaltning efter etableringen?

För brownfield:

- Finns tillräcklig nulägesbild av system, beroenden och teknisk skuld?
- Kan nyckelpersoner frigöras från daglig drift för att delta i förändringen?
- Finns prioritering för vilka system som ska moderniseras först?
- Finns acceptans för att införandet kan gå långsammare men bli mer verksamhetsnära?

För hybrid:

- Är det tydligt vilka delar som är greenfield och vilka som är brownfield?
- Finns styrning för parallella miljöer och arbetssätt?
- Finns en plan för att undvika permanent dubbelarbete?
- Finns tydliga beslutspunkter där hybridvägen kan justeras eller avbrytas?

Om flera spärrfrågor inte kan besvaras bör beslutet inte döljas i en positiv rekommendation. Då bör rekommendationen vara att först stärka förutsättningarna.

## Beslutsrekommendation med villkor

En beslutsrekommendation bör ha följande struktur:

- Rekommenderat vägval.
- Skäl för rekommendationen.
- Viktigaste risker.
- Villkor som måste vara uppfyllda.
- Första beslutspunkter.
- Vad som inte ingår i beslutet.

Exempel:

> Rekommendationen är att välja en hybridväg. Skälet är att organisationen behöver etablera en ny plattformsförmåga men samtidigt hantera befintliga system, driftberoenden och personberoenden stegvis. De största riskerna är dubbel styrning, överbelastning av nyckelpersoner och otydlig mottagande organisation. Beslutet bör därför villkoras med att plattformsteamets mandat fastställs, att två pilotfall väljs utifrån dokumenterade beroenden och att nyckelpersoner frigörs minst deltid under de första sex månaderna.

Detta är starkare än en rekommendation som bara säger:

> Vi bör välja hybrid.

En chef behöver kunna fatta beslut på en rekommendation som visar både riktning och genomförbarhet.

## Workshop: fyll i beslutsmatrisen

Den här workshopen kan genomföras i styrgrupp, ledningsgrupp eller med en mindre beslutsberedande grupp.

### Syfte

Att skapa en gemensam, spårbar och diskuterbar rekommendation om greenfield, brownfield eller hybrid.

### Deltagare

Bjud in personer som tillsammans kan bedöma verksamhet, teknik, säkerhet, drift, ekonomi, styrning och kompetens.

Undvik två ytterligheter:

- en grupp med bara tekniska specialister,
- en grupp med bara chefer utan tillgång till konkret nulägeskunskap.

### Förberedelser

Samla följande underlag:

- nulägeskarta från kapitel 4,
- sammanfattad systemportfölj,
- kompetens- och personberoendematris,
- riskbedömningar från kapitel 5, 6 och 7,
- kända säkerhets- och regelefterlevnadskrav,
- pågående större initiativ som konkurrerar om samma personer.

### Genomförande

1. Bekräfta beslutets formulering.
2. Välj eller justera kriterierna.
3. Vikta kriterierna från 1 till 5.
4. Poängsätt greenfield, brownfield och hybrid.
5. Skriv kort motivering för varje låg eller hög poäng.
6. Gå igenom spärrfrågorna.
7. Formulera rekommendation med villkor.
8. Identifiera vilket underlag som fortfarande saknas.

### Tidsram

En första beslutsworkshop kan ofta genomföras på två till tre timmar om underlaget är förberett. Om gruppen behöver skapa nulägesbilden under mötet är det inte en beslutsworkshop, utan en kartläggningsworkshop.

## Mall: enkel beslutsmatris

Använd denna mall som utgångspunkt.

| Kriterium | Vikt 1–5 | Greenfield 1–5 | Brownfield 1–5 | Hybrid 1–5 | Viktig motivering |
|---|---|---|---|---|---|
| Verksamhetsnytta | | | | | |
| Genomförbarhet | | | | | |
| Drift- och stabilitetsrisk | | | | | |
| Säkerhet och regelefterlevnad | | | | | |
| Kompetens och personberoende | | | | | |
| Förändringstakt | | | | | |
| Kostnads- och resurskontroll | | | | | |
| Långsiktig plattformsförmåga | | | | | |

Efter matrisen bör gruppen skriva en kort slutsats:

- Alternativ med högst stöd:
- Största osäkerhet:
- Viktigaste spärrfråga:
- Rekommenderat vägval:
- Villkor för beslut:
- Första beslutspunkt för uppföljning:

## När modellen visar att ni inte är redo

Ibland ger modellen inte ett tydligt svar. Det är inte ett misslyckande. Det kan vara ett viktigt resultat.

Organisationen är kanske inte redo att välja väg om:

- nulägesbilden är för svag,
- systemportföljen är okänd eller för grovt beskriven,
- kompetensberoenden är större än ledningen trodde,
- säkerhetskraven inte är tillräckligt tolkade,
- mandatet för plattformsteamet är oklart,
- driftorganisationen inte har utrymme att delta,
- finansiering bara täcker teknik men inte förändringsarbete.

I ett sådant läge bör beslutet inte pressas fram. Ett bättre beslut kan vara:

> Vi beslutar inte om införandeväg än. Vi beslutar om en begränsad förberedelsefas med tydliga leverabler: nulägeskarta, kompetensmatris, riskbedömning och förslag till styrning.

Det kan upplevas långsamt, men det är ofta snabbare än att fatta ett vägval som senare måste göras om.

## Tecken på ett moget beslut

Ett moget beslut har flera kännetecken.

- Det är tydligt vilket problem beslutet ska lösa.
- Alternativen har jämförts på samma grunder.
- Både teknik, styrning, drift, säkerhet och kompetens har vägts in.
- Personberoenden är synliga.
- Organisationens faktiska förändringskapacitet har prövats.
- Rekommendationen innehåller villkor.
- Det finns beslutspunkter för uppföljning.
- Det är tydligt vem som äger genomförandet efter beslutet.

Ett moget beslut betyder inte att risken är låg. Det betyder att risken är känd, accepterad och styrbar.

## Övning: skapa er första rekommendation

Använd underlaget från tidigare kapitel och fyll i beslutsmatrisen.

Gör sedan följande:

1. Skriv en rekommendation på högst tio meningar.
2. Ange tre skäl till rekommendationen.
3. Ange tre risker som måste följas upp.
4. Ange tre villkor som måste vara uppfyllda.
5. Ange första beslutspunkt efter genomförandestart.

Avsluta med att pröva rekommendationen mot denna fråga:

> Skulle en ny chef kunna förstå varför beslutet fattades och vilka förutsättningar som gällde?

Om svaret är nej behöver rekommendationen förtydligas.

## Snabb sammanfattning

- Vägvalet bör fattas med en tydlig beslutsmodell, inte utifrån teknikpreferens eller organisatorisk vana.
- Beslutsunderlag beskriver verkligheten, beslutskriterier beskriver vad organisationen värderar och rekommendationen beskriver valt vägval med villkor.
- Viktning hjälper organisationen att visa vad som faktiskt är viktigast.
- Poängsättning ska alltid motiveras, särskilt vid mycket höga eller låga poäng.
- Hög totalpoäng räcker inte om ett alternativ faller på en avgörande spärrfråga.
- En bra rekommendation innehåller villkor, risker och beslutspunkter.
- Om modellen visar att underlaget är för svagt är det ett legitimt resultat, inte ett misslyckande.

## Quiz/reflektionsfrågor

1. Vilka tre kriterier skulle väga tyngst i din organisation?
2. Vilket alternativ tror du spontant att organisationen föredrar, och varför?
3. Vilket alternativ skulle kunna få hög totalpoäng men ändå vara olämpligt?
4. Vilka spärrfrågor är mest kritiska hos er?
5. Vilket underlag saknas för att kunna ge en seriös rekommendation?

## Nästa steg

När beslutet är fattat behöver vägvalet omsättas i praktisk förändring. Nästa kapitel visar hur genomförandet bör läggas upp efter beslutet, med fokus på vad som skiljer greenfield, brownfield och hybrid i de första konkreta stegen.
