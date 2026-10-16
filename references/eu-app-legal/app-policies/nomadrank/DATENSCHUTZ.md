# Datenschutzerklärung – NomadRank

**Stand des Entwurfs:** 16. Oktober 2026 · **Geltungsbereich:** NomadRank (Quellcode: [Persie0/skratch_clone](https://github.com/Persie0/skratch_clone)) · **Redaktioneller Entwurf, noch nicht öffentlich freigegeben**

> **Veröffentlichungshinweis (nicht Bestandteil der Endfassung):** Dieser Text ist eine aus dem bekannten Codezustand verfasste Datenschutzerklärung, kein bloßer Maßnahmenkatalog. Die mit **[VOR VERÖFFENTLICHUNG]** markierten Tatsachen sind vor Nutzung in einer Store-Website zu klären. 

## 1. Verantwortlicher und Kontakt

Verantwortlich für die hier beschriebene Verarbeitung ist **Marvin Perzi (Persie0)**, Angerdorf 6, 3822 Karlstein an der Thaya, Österreich. Sie erreichen uns für Datenschutzanfragen unter **[persie0@protonmail.com](mailto:persie0@protonmail.com)**. Weitere Angaben zum Diensteanbieter (einschließlich UID, Kontakt und Gewerbe) enthält unser [Impressum](https://persie0.github.io/impressum.html).

Diese Erklärung erläutert die Nutzung der Anwendung **NomadRank**. Verweist die App auf externe Websites oder Dienste, gelten für deren eigenständige Verarbeitung auch die Datenschutzinformationen dieser Anbieter.

## 2. Welche Daten die App verarbeitet und wofür

Reiseziele, Bewertungen, Listen, Profilangaben und soziale Funktionen werden über eine Nutzerkonto-Verbindung mit dem App-Backend synchronisiert. Informationen, die aktiv mit Kontakten oder Gruppen geteilt werden, sind anderen berechtigten Nutzern sichtbar.

Auf dem Gerät können für Ihre gewählten Funktionen insbesondere folgende Informationen anfallen:

- Offline-Kopien und Warteschlangen von Konto-, Reise- und Sozialdaten.
- Karten-/statische Datensätze sowie zwischengespeicherte Länder- und Währungsdaten.
- Einstellungen und ein im sicheren Betriebssystemspeicher abgelegter Gemini-API-Schlüssel.

Diese Angaben werden für die Nutzung der App, das Wiederherstellen Ihrer Einstellungen und das Erstellen der von Ihnen gewünschten Ergebnisse verwendet. Soweit es sich um eine personenbezogene Verarbeitung durch uns handelt, kommen insbesondere Art. 6 Abs. 1 lit. b DSGVO (Bereitstellung einer angeforderten vertraglichen Funktion) und bei technisch notwendigen Betriebsdaten Art. 6 Abs. 1 lit. f DSGVO in Betracht. Daten, die ausschließlich auf Ihrem eigenen Gerät verarbeitet werden und auf die wir keinen Zugriff haben, sind davon zu unterscheiden.

Eine Standortberechtigung dient der angeforderten Funktion und kann über die Systemeinstellungen entzogen werden. Bei einer Verarbeitung am Gerät ist sie von der Übertragung von Koordinaten an Wetter-, Karten- oder sonstige Netzwerkdienste zu unterscheiden.

Profildaten und freiwillig für Freunde oder Gruppen freigegebene Inhalte sind für die jeweils ausgewählten Kontakte zugänglich. Werden Inhalte öffentlich bereitgestellt, legen die entsprechenden App-Einstellungen den Empfängerkreis fest.

Bei einer ausdrücklich gestarteten KI-Funktion werden die dafür ausgewählten Texte, Anweisungen oder Anlagen an den eingestellten KI-Anbieter gesendet. Die Anbieter sehen dabei Verbindungsdaten und erhalten den von Ihnen gewählten Inhalt. Ein selbst bereitgestellter API-Schlüssel ändert nichts an deren eigenen Datenschutzbedingungen.

Öffentlich oder für Kontakte freigegebene Reiseinformationen müssen vor dem Teilen erkennbar sein. Eine Kontolöschung umfasst grundsätzlich Daten aus dem eigenen Backend, soweit keine gesetzlichen Aufbewahrungspflichten oder berechtigten Gründe entgegenstehen; Daten in bereits selbstständig geteilten Inhalten erfordern eine gesonderte Beurteilung.

Die GPS-Position für den Vorschlag einer nahegelegenen Stadt verbleibt auf dem Gerät. Gespeicherte Reisekoordinaten stellen die von Ihnen gewählte Stadt oder das Ziel dar und keine fortlaufende Live-Ortung. Der optionale Gemini-Import sendet eingegebenen Text und ausgewählte Text- oder Tabellenanhänge mit Ihrem API-Schlüssel an Google.

## 3. Zugriffe auf Gerätefunktionen

Bei Nutzung der entsprechenden Funktionen können folgende Berechtigungen verlangt werden:

- Genauer/ungefährer Standort: die nächstgelegene unterstützte Stadt vorschlagen; der Abgleich erfolgt mit einer lokalen Städtedatenbank.
- Fotos/Dateien: Profil-/Reisebild auswählen oder Reisedateien importieren/exportieren.
- Netzwerk: Kontosynchronisierung, soziale Funktionen, Karten, Länder-/Währungsdaten, Diagnose und optionaler Gemini-Import.

Berechtigungen werden über das Betriebssystem gesteuert. Sie können sie dort entziehen; die zugehörige Funktion ist anschließend unter Umständen nicht mehr nutzbar. Eine erteilte Betriebssystemberechtigung ersetzt keine gegebenenfalls zusätzlich erforderliche datenschutzrechtliche Einwilligung.

## 4. Externe Dienste, Diagnosen und Datenempfänger

Daten werden nicht allein deshalb an sämtliche nachstehend genannten Unternehmen übertragen, weil diese unter Umständen als Abhängigkeit im Projekt enthalten sind. Beschrieben werden die für die Anwendung identifizierten oder ausdrücklich bedingten Datenwege; welche Anbieter in einer veröffentlichten App-Version tatsächlich aktiv sind, muss mit deren finaler Konfiguration abgeglichen werden.

### NomadRank authentication

Zur Bereitstellung von NomadRank-Konto erstellen, absichern und anmelden können Firebase-UID, E-Mail, Anzeigename, Authentifizierungsanbieter, Token und Sicherheits-/Anfrageprotokolle einschließlich IP; Google oder Apple verarbeiten zusätzlich die von Ihnen autorisierten Anmeldedaten verarbeitet werden. Empfänger: **Google Firebase und der von Ihnen gewählte Anmeldeanbieter (Google oder Apple).**. Art. 6 Abs. 1 lit. b DSGVO; Sicherheit/Missbrauchsprävention zusätzlich Art. 6 Abs. 1 lit. f. Hinsichtlich der Aufbewahrung gilt: Für die Kontolaufzeit. Nach Kontolöschung erfolgt Löschung aus Live-/Sicherungssystemen nach Anbieterzyklen; Firebase nennt für viele gelöschte Systeme/Sicherungen bis zu 180 Tage, vorbehaltlich Sicherheits-/Rechtsnachweisen. [Datenschutzhinweise des Dienstes](https://firebase.google.com/support/privacy).

### NomadRank account and social backend

Zur Bereitstellung von Konto, Synchronisierung, Reisetagebuch, Ranglisten- und gewünschte Sozialfunktionen bereitstellen können UID; Benutzer-/Anzeigename; Anmelde-E-Mail; Avatar-URL; Heimatland; Mitgliedschaft/Rang/Erfolge; Reisen und geplante Reisen (Ziel-/Stadtkoordinaten, Daten, Bewertungen, Tags, Notizen, Kosten); Bucket List; Freunde/Einladungen; Gruppen; Reisekreise und Mitglieder/Stopps; Server-/Sicherheitsprotokolle einschließlich IP. Andere Nutzer können Profil-/Sozialdaten funktionsabhängig sehen verarbeitet werden. Empfänger: **Persie0 und Oracle als Infrastruktur-Auftragsverarbeiter; Freunde, Eingeladene oder Gruppen-/Kreismitglieder erhalten die von der Funktion angezeigten Felder.**. Art. 6 Abs. 1 lit. b DSGVO; Dienstsicherheit/Missbrauchsprävention Art. 6 Abs. 1 lit. f. Soziale Veröffentlichung/Weitergabe erfolgt auf Ihre Anforderung. Hinsichtlich der Aufbewahrung gilt: Kontoinhalte bis zur Einzellöschung oder Kontolöschung. Betriebssicherungen rotieren nach Anbieterplan; Sicherheitsprotokolle nur für Missbrauchs-/Anspruchszwecke. Portabler Export ist in der App verfügbar. [Datenschutzhinweise des Dienstes](https://www.oracle.com/legal/privacy/).

### Country/region detection

Zur Bereitstellung von Regionale Voreinstellungen, Währung, Sprache oder den passenden Einwilligungsablauf wählen können Öffentliche IP-Adresse, Anfragemetadaten und aus der IP abgeleitetes Land/Region; kein GPS-Standort verarbeitet werden. Empfänger: **Der jeweils zuerst verfügbare oben genannte Ländererkennungsdienst.**. Art. 6 Abs. 1 lit. f DSGVO (minimale regionale Konfiguration). Regionale Einstellungen können, soweit angeboten, überschrieben werden. Hinsichtlich der Aufbewahrung gilt: Die Antwort wird vorübergehend verwendet oder lokal zwischengespeichert; Persie0 führt kein Serverprotokoll. Anbieter speichern Anfrageprotokolle nach ihren Richtlinien. [Datenschutzhinweise des Dienstes](https://ipapi.co/privacy/).

### Optional Gemini trip import (bring your own key)

Zur Bereitstellung von Bei von Ihnen gestartetem Import Reisevorschläge extrahieren und Ziele auflösen können Ihr Gemini-API-Schlüssel, eingegebener Reisetext, ausgewählte Text-/Tabellenanhänge (bis zum App-Limit), Dateinamen, Prompts, mögliche Zielortzeilen und erzeugte Reiseextraktion. Der Schlüssel liegt im sicheren Betriebssystemspeicher; Persie0 erhält ihn nicht verarbeitet werden. Empfänger: **Google AI. Persie0 ist kein Zwischenempfänger der API-Nutzlast.**. Art. 6 Abs. 1 lit. a/b DSGVO. Optional und von Ihnen gestartet. Google handelt nach dem mit Ihrem Schlüssel verbundenen API-Konto/-Vertrag. Hinsichtlich der Aufbewahrung gilt: Persie0 speichert nur von Ihnen übernommene Reisedaten. Googles Aufbewahrung/Training hängt von bezahltem Dienst und Kontokonfiguration ab; prüfen Sie vor personenbezogenen Daten die Gemini-API-Bedingungen. [Datenschutzhinweise des Dienstes](https://ai.google.dev/gemini-api/terms).

### Map tiles and geographic content

Zur Bereitstellung von Den von Ihnen gewünschten Kartenbereich anzeigen können IP, User-Agent, Anfragezeit und angeforderte Kartenkachelkoordinaten/Zoomstufe, aus denen das betrachtete Gebiet hervorgehen kann. Der Kartenanbieter erhält kein Persie0-Kontopasswort verarbeitet werden. Empfänger: **CARTO/CDN und bei direkter Abfrage OpenStreetMap-bezogene Dienste.**. Art. 6 Abs. 1 lit. b DSGVO für die gewünschte Karte und Art. 6 Abs. 1 lit. f für effiziente Auslieferung. Hinsichtlich der Aufbewahrung gilt: Persie0 führt keine Kartenkachel-Anfrageprotokolle; es gelten Anbieterfristen. Lokaler Cache wird durch App/Betriebssystem oder Deinstallation gelöscht. [Datenschutzhinweise des Dienstes](https://carto.com/privacy/).

### Country, encyclopedia and currency lookups

Zur Bereitstellung von Länderinformationen, Hinweise/statische Fakten und Wechselkurse anzeigen können IP, Anfragemetadaten und angefragter Artikel/Land/Währungspaar. Kein Kontopasswort verarbeitet werden. Empfänger: **Der von der Funktion abgefragte Inhalts-/API-Anbieter.**. Art. 6 Abs. 1 lit. b DSGVO für gewünschte Inhalte; Art. 6 Abs. 1 lit. f für zwischengespeicherte, zuverlässige Auslieferung. Hinsichtlich der Aufbewahrung gilt: Antwort wird bei Bedarf lokal zwischengespeichert; kein Serverprotokoll bei Persie0. Anbieterfristen gelten. [Datenschutzhinweise des Dienstes](https://foundation.wikimedia.org/wiki/Policy:Privacy_policy).

### Selbst betriebene Fehlerdiagnose (GlitchTip)

Zur Erkennung und Behebung von Programmfehlern nutzen wir eine selbst betriebene GlitchTip-Instanz unter `persie0.duckdns.org`. Im Fehlerfall können Fehlermeldungen, Stacktraces, App- und Systemversionen sowie weitere technische Umstände des Fehlers übertragen werden. Dabei kann auch die für den technischen Verbindungsaufbau erforderliche IP-Adresse in Serverprotokollen anfallen. Diese Verarbeitung beruht, soweit anwendbar, auf unserem berechtigten Interesse an Betriebssicherheit und Fehlerbehebung (Art. 6 Abs. 1 lit. f DSGVO); ein etwaiges gesondertes Einwilligungserfordernis bleibt unberührt. **Die Daten werden nicht allein durch die Verwendung eines Sentry-kompatiblen SDKs an den Dienst Sentry.io übermittelt.** [VOR VERÖFFENTLICHUNG: Serverstandort, HTTP-Logs, tatsächlich übertragene Felder und Fehlerbericht-Löschfrist eintragen.]


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
