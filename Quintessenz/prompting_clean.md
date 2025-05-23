# Prompting für Anfänger: Wie man mit KI-Tools richtig kommuniziert

Ich sehe sehr häufig Menschen, die mit einem KI-System arbeiten wollen, aber nicht wissen wie sie Anfangen wollen. Ich sage immer, dass Prompten eine Fähigkeit wie googlen ist. Das klingt banal, aber auch eine effiktive Googlesuche ist manchmal "koplexer" als man denkt. Auch wenn uns die Arbeit gut zu prompten von den Tools und Systemem immer mehr abgenommen wird, sollten wir trotzdem nicht die Fähigkeit verlieren Fragestellungen ordentlich zu formulieren. Denn auch wenn je nach Applkation im Hintergrund unser Prompt vom System h umformuliert werden sollte, ist eine genaue Beschriebung von dem was wir als Ergebniss bekommen sollen besser als einfach nur zu schreiben: "Schreib mir was über Marketing."
Anders gesagt: Gute Kommunikation funktioniert bei KI-Systemem genauso wie zwischen Menschen, je klarer die Anweisung, desto besser das Ergebnis.

Entgegen der gänigen Ausdrucksweise werde ich hier "LM" statt "LLM" nutzen. Da sich diese Strategien auch auf kleine Instruction Tuned Modelle (SLM - small Language Models) anwenden lassen, die in 2025 mehr und mehr an Relevanz gewinnen werden. Mark my words!

## Was ist eigentlich ein Prompt?

Das Wort "Prompt" begegnet uns mittlerweile täglich, auch außerhalb der KI-Welt. Wenn der Computer nach einem Passwort fragt, promptet er uns. Wenn uns jemand dazu ermutigt, etwas zu tun, promptet er uns. Im Kontext von Sprachmodellen ist ein Prompt unsere Art, mit dem KI-System zu kommunizieren. Dabei ist es egal ob wir den Prompt schreiben oder sprechen. Ein Prompt soll als eine Anleitung oder Wegbeschreibung für das LM sein. Damit es an in der Richtigen Richtung im Latent Space nach Informationen suchen kann.

Abstrakter betrachtet ist ein Sprachmodell ist im Grunde eine Komprimierung aller Trainingsdaten. Wir nutzen unsere natürliche Sprache, um dieses riesige Wissensarchiv zu durchsuchen und die gelernten Informationen herauszukitzeln. Ich stelle mir das immer so vor, wir erkunden mit unserer Spreche den "Latent Space" des Modells. Der Latent Space ist dieser multidimensionaler Raum in dem das LM sein wissen speichert.

## Die technische Grundlage verstehen

Bevor wir tiefer einsteigen, sollten wir kurz klären, womit wir es eigentlich zu tun haben. Viele verwechseln die Begriffe (L/S)LM, KI-System und Interface. Das ist aber wie der Unterschied zwischen Motor, Auto und Lenkrad.

Das **Large Language Model** (wie GPT-4 oder Claude)also das eigentliche Sprachmodell mit all seinem Wissen, ist gewissermaßen der Motor. Das **KI-System** ist das komplette Auto. Es kann zusätzliche Funktionen haben wie Internetsuche, Bilderkennung oder spezialisierte Tools. Das **Interface** schließlich ist unser Lenkrad Die Oberfläche, über die wir mit dem System interagieren, wie ChatGPT, Claude oder spezialisierte Anwendungen.

Diese Unterscheidung ist wichtig, weil sich Prompting-Strategien je nach System unterscheiden können. Was bei einem einfachen Chat interface funktioniert, muss bei einem System mit zusätzlichen Funktionen noch lange nicht zum selben Ergbeniss führen.

Prompten ist generell ein itartiver Prozess, der auch nicht immer zu den selben Ergebinssen führt. LMs sind nicht-deterministisch. Sie Produzieren nie ein und den selben Output.
Häufig wird auch ein LM als Betriebssystem bezeichnet.
Wer mit ChatGPT und Claude redet interagiert man sozusagen mit dem Betreibssystem eines KI-Systems. Je nach System hat das Modell ganz unterschiedliche Zusatzfunktionen, bei denen das Modell selbst entscheidet, welche Aktion als nächstes aufgeführt wird. Wie dein Computer der Speicher und die Prozesse verwaltet.

Das erklärt auch, warum Prompting so wichtig ist. Wenn du schlecht formulierte "Befehle" an dein Betriebssystem sendest, passiert entweder nichts oder etwas Unerwartetes. Bei LMs ist es genauso: Ein unpräziser Prompt ist wie ein schlecht geschriebenes Programm. Es läuft vielleicht, aber das Ergebnis ist meist nicht das, was angedacht war.
Genau wie bei Betriebssystemen kommt es darauf an, die richtigen "Treiber" und "Anweisungen" zu verwenden, um das System effektiv zu nutzen. Deine Prompting-Fähigkeiten sind quasi deine Programmierkenntnisse für dieses Sprach-Betriebssystem.

## Die vier Säulen eines guten Prompts

Nach nun mehr als drei Jahren in denen ich mit Chatmodellen arbeite, haben sich vier Kernaspekte herauskristallisiert, die einen guten Prompt ausmachen:

**Kontext geben** bedeutet, dem Modell Hintergrundinformationen und die gewünschte Perspektive zu vermitteln. Statt einfach "Erkläre mir Datenschutz" zu schreiben, könnten wir formulieren: "Du bist eine Rechtsanwältin für IT- und Datenschutzrecht mit mehrjähriger Erfahrung. Erkläre mir die wichtigsten DSGVO-Aspekte für ein kleines Online-Unternehmen."

**Klarheit und Präzision** sorgen für konkrete Anweisungen und spezifische Fragen. Anstatt vage nach einem "Bericht" zu fragen, definieren wir genau: "Analysiere die beigefügten Vertragsbedingungen nach deutschem Recht und beantworte dabei folgende drei Fragen: Erstens..."

**Struktur** gibt dem gewünschten Output eine klare Gliederung. Wir können explizit um Tabellen, Schritt-für-Schritt-Anleitungen oder bestimmte Formate bitten. Das ist besonders hilfreich, wenn die Antwort weiterverarbeitet werden soll.

**Grenzen setzen** schließlich bedeutet, Längenangaben oder spezifische Einschränkungen zu definieren. "Fasse das in maximal drei Sätzen zusammen" oder "Gib eine kurze Gesamtbewertung ab" helfen dabei, brauchbare Ergebnisse zu erhalten.
ChatGPT z.B ist mir ohne Eingrenzung viel zu "chatty". Die Ausgaben sind mir nicht präzise.

## Prompt Patterns - Die Macht der Rollenspiele

Hier wird es richtig spannend. Prompt Patterns sind Strukturen oder Templates die als Startpunkt für einen Prompt genutzt werden können. Die zwei wichtigsten Patterns für Einsteiger sind meiner Meinung nach das **Persona Pattern** und das **Audience Persona Pattern**.

Beim Persona Pattern wird das KI-System angweisen eine bestimmte Rolle übernehmen: "Du bist ein Pirat, beantworte alle Fragen wie ein Pirat." Das funktioniert überraschend gut, nicht nur für lustige Experimente, sondern auch für fachliche Perspektiven wenn z.B mit einer bestimmten Persona "gechattet" wird um Fragestellugnen aus einem anderem Blickwinkel zu betrachten.

Das Audience Persona Pattern ist oft präziser. Hier bleibt das KI-System "es selbst", passt aber die Antwort an eine bestimmte Zielgruppe an: "Erkläre mir Transformer im Kontext von Machine Learning, gehe davon aus, dass ich sehr wenig technisches Verständnis habe."

Meiner Erfahrung nach liefert das Audience Pattern meist genauere Ergebnisse, weil das KI-System ihre "natürliche" Wissensbasis beibehält, aber die Kommunikation anpasst.

## Der 6-Schritte-Algorithmus für bessere Prompts

Wie auch beim Prgrammieren, kann auch das Formulieren eines Promptes algorithmisch angegangen werden.

**Schritt 1: Aufgabe definieren.** Was soll das Modell genau tun? Welche Unteraufgaben gibt es? Hier ein Tipp: Fragen Sie das Modell selbst, welche Teilbereiche wichtig sein könnten.

**Schritt 2: Kontext sammeln.** Welche Details sind relevant? Gibt es besondere Einschränkungen oder Anforderungen? Je mehr relevanten Kontext dem Modell an die Hand gegeben wird, desto passender wird die Antwort.

**Schritt 3: Persona wählen.** Welche Fachperson würde diese Aufgabe am besten lösen? Ein innovativer Koch, ein erfahrener Anwalt, ein geduldiger Lehrer? Nutz Personas die diese Fachperson beschreiben.

**Schritt 4: Beispiele hinzufügen.** Falls möglich, sollten ein oder mehrere Beispiele für das gewünschte Ergebnis mit beigefügt werden. Diese "Few-Shot-Prompts" verbessern die Qualität erheblich.

**Schritt 5: Output-Struktur definieren.** Wie soll die Antwort aussehen? Schritt-für-Schritt-Anleitung? Tabelle? Mit Kommentaren nach jedem Punkt?

**Schritt 6: Tonfall festlegen.** Soll die Antwort förmlich, freundlich, erklärend oder enthusiastisch sein? Der Tonfall beeinflusst nicht nur die Lesbarkeit, sondern oft auch die Qualität der Inhalte.

## Wichtige Zusatzkonzepte

Ein paar Konzepte sollte man außerdem kennen: **Zero-Shot-Prompting** bedeutet, eine Aufgabe ohne Beispiele zu stellen. **One-Shot** gibt ein Beispiel mit, **Few-Shot** mehrere Beispiele. In der Regel werden die Ergebnisse mit mehr Beispielen besser, weil dem Modell eine klarere Struktur vorgegeben wird.

**Introducing New Information** ist entscheidend, wenn mit spezifischen Daten gearbeitet. Das Modell kann nicht wissen, was im Kühlschrank steht oder welcher Vertrag analysiert werden soll. Diese Informationen müssen explizit mitgeliefert werden.

Beim **Prompt Chaining** werden komplexe Aufgaben in mehrere aufeinander aufbauende Prompts aufgeteilt, anstatt alles in einen überlangen Prompt zu packen. Das Konzept alles in einen riesen großen Prompt zu stopfen, nennt sich **Prompt Stuffing**. Ich persönlich arbeite mit sher häufig mit **Prompt Chaining**, da Chaining die Möglichkeit beitet, sich zwischen Ergebnisse zu speichern. Was fürher bei den ersten Modellen, auf Grund des kleinen Kontextfenster dringed notwendig war. Fast alle modernen LMs haben aber mittlerweile so große Kontextfenster, dass auch **Prompt Stuffing** betrieben werden kann. \* _Reasoning Modelle_ _ funktionieren am besten mit **Prompt Stuffing** da während _ _Test Time_ \* alle Informationen, die in den Kontext gegeben werden, berücksichtigt werden.
Tipp: Wer Resoning auch ohne fancy Modell nutzen möchte, sollte sich den MCP-Server **sequential Thinking** von Anthropic anschauen.

## Ein praktisches Beispiel

Abschließen möchte ich mit einem naiven Beispiel.

"Du bist eine Expertin für Mikrowellengerichte. Deine Aufgabe ist es, ein einzigartiges Apfelkuchenrezept zu kreieren, das mit einer Mikrowelle zubereitet werden kann. Das Rezept sollte Äpfel, Erdbeeren und Kirschen enthalten und vegan sein.

Folgende Schritte sollten berücksichtigt werden:

1. **Auswahl und Vorbereitung der Früchte**
2. **Herstellung des veganen Kuchenteigs**
3. **Zusammenstellen des Kuchens**
4. **Mikrowellen-Kochtechnik mit spezifischen Zeitangaben**
5. **Präsentation und Serviervorschläge**

Verwende einen professionellen, aber verständlichen Tonfall."

Dieser Prompt kombiniert alle wichtigen Elemente: klare Persona, spezifische Aufgabe, strukturierte Gliederung und Tonfall-Vorgabe.

## Praktische Tipps für den Alltag

Ein kleiner Trick am Rande: Modelle wie GPT verstehen Markdown-Formatierung sehr gut, weil sie auch auf Code-Daten trainiert wurden. Deshalb funktionieren **fette Überschriften** oder _kursive Hervorhebungen_ in Prompts oft erstaunlich gut.

Wenn Sie schönere Outputs möchten, können Sie auch um HTML-Ausgabe mit CSS-Styling bitten. Das mag zunächst übertrieben wirken, aber für Berichte oder Präsentationen ist das extrem nützlich.

Experimentieren Sie auch mit der Aufteilung komplexer Aufgaben. Statt einem riesigen Prompt für eine Vertragsanalyse könnten Sie beispielsweise erst nach einer strukturierten Übersicht fragen, dann nach spezifischen Risikobewertungen und schließlich nach Optimierungsvorschlägen.

## Ein persönlicher Ausblick

Ehrlich gesagt bin ich immer wieder überrascht, wie sehr sich die Qualität der KI-Antworten verbessert, wenn man diese Grundprinzipien beachtet. Es ist ein bisschen wie beim Kochen - die richtigen Zutaten in der richtigen Reihenfolge machen den Unterschied zwischen mittelmäßig und excellent aus.

Was mich besonders fasziniert: Je mehr ich mit einem KI-System interageiere, desto mehr lerne ich auch über meine eigene Kommunikation. Klarheit, Struktur und präzise Anweisungen helfen nicht nur bei Prompts, sondern auch im Umgang mit Kollegen, Freunden und Familie.

Vielleicht ist das der wahre Wert des Prompt-Lernens, es macht uns zu besseren Kommunikatoren, ganz unabhängig davon, ob unser Gegenüber aus Fleisch und Blut oder aus Code und Daten besteht.
