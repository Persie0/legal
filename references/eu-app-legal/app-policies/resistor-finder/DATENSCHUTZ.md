# Datenschutzerklärung – Resistor Finder

**Stand des Entwurfs:** 16. Oktober 2026 · **Geltungsbereich:** Resistor Finder (Quellcode: [Persie0/resistor-calc](https://github.com/Persie0/resistor-calc)) · **Redaktioneller Entwurf, noch nicht öffentlich freigegeben**

> **Veröffentlichungshinweis (nicht Bestandteil der Endfassung):** Dieser Text ist eine aus dem bekannten Codezustand verfasste Datenschutzerklärung, kein bloßer Maßnahmenkatalog. Die mit **[VOR VERÖFFENTLICHUNG]** markierten Tatsachen sind vor Nutzung in einer Store-Website zu klären. 

## 1. Verantwortlicher und Kontakt

Verantwortlich für die hier beschriebene Verarbeitung ist **Marvin Perzi (Persie0)**, Angerdorf 6, 3822 Karlstein an der Thaya, Österreich. Sie erreichen uns für Datenschutzanfragen unter **[persie0@protonmail.com](mailto:persie0@protonmail.com)**. Weitere Angaben zum Diensteanbieter (einschließlich UID, Kontakt und Gewerbe) enthält unser [Impressum](https://persie0.github.io/impressum.html).

Diese Erklärung erläutert die Nutzung der Anwendung **Resistor Finder**. Verweist die App auf externe Websites oder Dienste, gelten für deren eigenständige Verarbeitung auch die Datenschutzinformationen dieser Anbieter.

## 2. Welche Daten die App verarbeitet und wofür

Eingegebene Farbringe werden für die lokale Bestimmung von Widerstandswerten und Toleranzen verarbeitet.

Auf dem Gerät können für Ihre gewählten Funktionen insbesondere folgende Informationen anfallen:

- ausgewählte Farbringe und Berechnungswerte.
- Einstellungen und letzte Berechnungen.

Diese Angaben werden für die Nutzung der App, das Wiederherstellen Ihrer Einstellungen und das Erstellen der von Ihnen gewünschten Ergebnisse verwendet. Soweit es sich um eine personenbezogene Verarbeitung durch uns handelt, kommen insbesondere Art. 6 Abs. 1 lit. b DSGVO (Bereitstellung einer angeforderten vertraglichen Funktion) und bei technisch notwendigen Betriebsdaten Art. 6 Abs. 1 lit. f DSGVO in Betracht. Daten, die ausschließlich auf Ihrem eigenen Gerät verarbeitet werden und auf die wir keinen Zugriff haben, sind davon zu unterscheiden.

Die geprüfte Flutter-Version verwendet native App-Store-Kaufbibliotheken statt RevenueCat.

## 3. Zugriffe auf Gerätefunktionen

Bei Nutzung der entsprechenden Funktionen können folgende Berechtigungen verlangt werden:

- Netzwerk: Werbung, Diagnose und Käufe.
- E-Mail-App, nur bei gewähltem Bericht: eine Supportnachricht senden.

Berechtigungen werden über das Betriebssystem gesteuert. Sie können sie dort entziehen; die zugehörige Funktion ist anschließend unter Umständen nicht mehr nutzbar. Eine erteilte Betriebssystemberechtigung ersetzt keine gegebenenfalls zusätzlich erforderliche datenschutzrechtliche Einwilligung.

## 4. Externe Dienste, Diagnosen und Datenempfänger

Daten werden nicht allein deshalb an sämtliche nachstehend genannten Unternehmen übertragen, weil diese unter Umständen als Abhängigkeit im Projekt enthalten sind. Beschrieben werden die für die Anwendung identifizierten oder ausdrücklich bedingten Datenwege; welche Anbieter in einer veröffentlichten App-Version tatsächlich aktiv sind, muss mit deren finaler Konfiguration abgeglichen werden.

### Advertising (Appodeal)

Zur Bereitstellung von Werbung anzeigen und messen sowie Werbebetrug verhindern. Personalisierte Werbung erfolgt nur mit Einwilligung können Werbe-ID, soweit erlaubt, IP-Adresse, Geräte- und App-Informationen, Anzeigenaufrufe, Klicks und Betrugspräventionssignale sowie ein aus der IP-Adresse abgeleiteter ungefährer Standort verarbeitet werden. Empfänger: **Appodeal und dessen Werbepartner.**. Einwilligung nach Art. 6 Abs. 1 lit. a DSGVO und § 165 Abs. 3 TKG 2021 für nicht notwendige Endgerätezugriffe. Die Auswahl kann in den Datenschutzeinstellungen der App geändert werden. Hinsichtlich der Aufbewahrung gilt: Die Einwilligungsauswahl bleibt bis zur Änderung, zum Zurücksetzen oder Entfernen der App auf dem Gerät. Für Appodeal und dessen Partner gelten die in deren Datenschutzhinweisen genannten Fristen. [Datenschutzhinweise des Dienstes](https://www.appodeal.com/home/privacy-policy/).

### Optional support email

Zur Bereitstellung von Anfrage beantworten, Fehler untersuchen und Austausch dokumentieren können Absenderadresse, Nachricht, Anhänge und technische E-Mail-Header, nur wenn Sie Support kontaktieren verarbeitet werden. Empfänger: **E-Mail-Transportanbieter und Proton.**. Art. 6 Abs. 1 lit. b DSGVO; Art. 6 Abs. 1 lit. f für Supportqualität und Anspruchsabwehr. Hinsichtlich der Aufbewahrung gilt: Für den Supportaustausch und bei Bedarf für Rechtsansprüche bis zu drei Jahre danach; länger nur bei gesetzlicher Pflicht. [Datenschutzhinweise des Dienstes](https://proton.me/legal/privacy).

### Selbst betriebene Fehlerdiagnose (GlitchTip)

Zur Erkennung und Behebung von Programmfehlern nutzen wir eine selbst betriebene GlitchTip-Instanz unter `persie0.duckdns.org`. Im Fehlerfall können Fehlermeldungen, Stacktraces, App- und Systemversionen sowie weitere technische Umstände des Fehlers übertragen werden. Dabei kann auch die für den technischen Verbindungsaufbau erforderliche IP-Adresse in Serverprotokollen anfallen. Diese Verarbeitung beruht, soweit anwendbar, auf unserem berechtigten Interesse an Betriebssicherheit und Fehlerbehebung (Art. 6 Abs. 1 lit. f DSGVO); ein etwaiges gesondertes Einwilligungserfordernis bleibt unberührt. **Die Daten werden nicht allein durch die Verwendung eines Sentry-kompatiblen SDKs an den Dienst Sentry.io übermittelt.** [VOR VERÖFFENTLICHUNG: Serverstandort, HTTP-Logs, tatsächlich übertragene Felder und Fehlerbericht-Löschfrist eintragen.]

### Werbeanzeigen und Einwilligungsverwaltung

Sofern kostenlose Funktionen durch Werbung finanziert werden, wird **Appodeal** mit den im jeweiligen Store-Build tatsächlich aktivierten Vermarktungspartnern eingesetzt. Hierbei können technische Anfrage- und Gerätekennungen, IP-Adresse, gegebenenfalls Werbe-IDs sowie Informationen zu der angezeigten oder angeklickten Anzeige verarbeitet werden. Die Beteiligung einzelner Netzwerke richtet sich nach Konfiguration, Region und Werbeausspielung. Soweit für Gerätezugriffe oder personalisierte Werbung eine Einwilligung erforderlich ist, wird diese über eine geeignete Einwilligungsverwaltung (z. B. Appodeal Stack Consent Manager) eingeholt und eine Änderung/Widerruf ermöglicht. Unter iOS ist eine erforderliche ATT-Erlaubnis davon getrennt. Angaben der Anbieter: [Appodeal Datenschutz](https://appodeal.com/privacy-policy/). [VOR VERÖFFENTLICHUNG: konkrete aktive Mediation-Partner mit deren Datenschutzhinweisen, tatsächlichen Einwilligungsweg und Speicherdauer bestätigen.]

### Käufe über den App-Store

Bei der Freischaltung kostenpflichtiger Funktionen erfolgt die Zahlungsabwicklung über **Google Play Billing** beziehungsweise **Apple In-App Purchase**. Der Store verarbeitet Zahlungs- und Belegdaten nach seinen eigenen Bedingungen; die App verarbeitet den für die Berechtigungsprüfung benötigten Kaufstatus. Zahlungsmittel werden nicht unmittelbar in der App erfasst. [Google Datenschutz](https://policies.google.com/privacy) · [Apple Datenschutz](https://www.apple.com/legal/privacy/).


## 5. Dauer der Speicherung und Löschung

Daten im lokalen App-Speicher bleiben grundsätzlich bis zu Ihrer eigenen Löschung, bis zum Zurücksetzen der App-Daten oder bis zur Deinstallation vorhanden. Von Ihnen exportierte Dateien können außerhalb des App-Speichers weiter bestehen und müssen gegebenenfalls separat gelöscht werden. Daten in einem freiwillig verbundenen Cloudkonto oder bei einem externen Dienst unterliegen zusätzlich den dortigen Lösch- und Aufbewahrungsabläufen.

Für technische Server-, Absturz-, Kauf- und Werbedaten gelten gesonderte Fristen und Löschkriterien der jeweils verantwortlichen Stelle; diese sind in Abschnitt 4 sowie in den verlinkten Anbieterinformationen beschrieben. **[VOR VERÖFFENTLICHUNG: konkrete Entwickler-Hosting- und GlitchTip-Logfristen, Supportanfragen, Abrechnungsfristen und gegebenenfalls Löschung von Backups ergänzen; pauschales „sofort“ nicht behaupten.]**

Anfragen zur Berichtigung, Auskunft oder Löschung von Daten in unserem Verantwortungsbereich richten Sie an [persie0@protonmail.com](mailto:persie0@protonmail.com). Eine Deinstallation beendet nicht automatisch Store-Abonnements.

## 6. Rechtsgrundlagen, internationale Übermittlung und Einwilligung

Für die Verarbeitung zur Erfüllung einer angeforderten Funktion kommt – soweit die DSGVO anwendbar ist – Art. 6 Abs. 1 lit. b DSGVO in Betracht; die Verarbeitung technisch notwendiger Fehler- und Sicherheitsdaten kann auf Art. 6 Abs. 1 lit. f DSGVO beruhen. Wird eine Einwilligung benötigt, beruht die betreffende Verarbeitung auf Art. 6 Abs. 1 lit. a DSGVO und, bei Informationen auf Endgeräten, auf den dafür einschlägigen Bestimmungen des § 165 TKG 2021. Eine erforderliche Einwilligung kann für die Zukunft widerrufen werden. Für besondere Datenkategorien ist zusätzlich Art. 9 DSGVO zu prüfen.

Manche in Abschnitt 4 genannten Unternehmen können Daten außerhalb des Europäischen Wirtschaftsraums verarbeiten oder auf Daten von dort zugreifen. Bei solchen Übermittlungen werden – sofern erforderlich – Angemessenheitsbeschlüsse, Standarddatenschutzklauseln und geeignete weitere Garantien herangezogen. **[VOR VERÖFFENTLICHUNG: tatsächliche betroffene Länder und je Anbieter geltende Übermittlungsgrundlage prüfen; eine bloße Verlinkung der Anbieterpolitik reicht nicht als Nachweis.]**

## 7. Ihre Rechte

Unter den gesetzlichen Voraussetzungen haben Sie Rechte auf Auskunft (Art. 15 DSGVO), Berichtigung (Art. 16), Löschung (Art. 17), Einschränkung (Art. 18), Datenübertragbarkeit (Art. 20) und Widerspruch (Art. 21). Soweit wir uns auf Einwilligung stützen, können Sie diese mit Wirkung für die Zukunft widerrufen. Einzelfälle und gesetzliche Aufbewahrungspflichten können die Ausübung bestimmter Rechte einschränken. Wir beantworten entsprechende Anfragen über die oben genannte Kontaktadresse und können eine angemessene Identitätsprüfung verlangen.

Sie können sich außerdem bei einer Datenschutzaufsichtsbehörde beschweren, in Österreich insbesondere bei der **[Österreichischen Datenschutzbehörde](https://dsb.gv.at/)**. Datenschutzfragen können Sie auch unmittelbar an uns richten.

## 8. Sicherheit, Minderjährige und Änderungen

Wir verwenden nach Maßgabe der tatsächlichen Verarbeitung geeignete technische und organisatorische Schutzmaßnahmen. Keine Software und keine Internetübertragung kann eine absolute Sicherheit garantieren. Für Kinder angebotene Funktionen oder eine auf Kinder ausgerichtete Verbreitung erfordern gesonderte Prüfung der Alters- und Einwilligungsregeln. Ändern sich wesentliche Zwecke oder Empfänger, passen wir diese Datenschutzerklärung an und informieren, soweit rechtlich erforderlich, gesondert.

## 9. Weitere Informationen

- [Impressum Persie0](https://persie0.github.io/impressum.html)
- [Allgemeine Datenschutzinformationen Persie0](https://persie0.github.io/datenschutz.html)
- [Kontakt](mailto:persie0@protonmail.com)
- [Rechtsgrundlagen: Datenschutz-Grundverordnung](https://eur-lex.europa.eu/eli/reg/2016/679/oj)

---

### Interner Freigabevermerk – vor öffentlicher Nutzung entfernen

- Abgleich mit den installierten SDKs und dem zuletzt an Nutzer ausgelieferten Android-/Apple-Build erforderlich.
- Speicherdauern, Hostingland, tatsächlich aktive Mediation/Endpunkte, internationale Übermittlungen, Rechtsgrundlagen und sämtliche markierten Angaben vor rechtlicher Freigabe überprüfen.
- **Vorliegendes Markdown ist nicht die bereits live geschaltete App-Datenschutzerklärung.** Als redaktionelle Ausgangsbasis dient der eigene Code und die eigene App-Dateninventur; vergleichbare externe Beispiele: [Auphonic](https://eu1.auphonic.com/privacy), [ÖAMTC](https://www.oeamtc.at/mitgliedschaft/leistungen/datenschutzerklaerung-oeamtc-app-28493389), [Photoroom](https://www.photoroom.com/legal/privacy). Ihre Texte wurden nicht übernommen.
