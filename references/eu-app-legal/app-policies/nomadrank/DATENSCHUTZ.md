# Datenschutzerklärung für NomadRank

**Stand:** 5. November 2026

## 1. Geltungsbereich

Diese Datenschutzerklärung betrifft **NomadRank** und beschreibt die Verarbeitung im Zusammenhang mit Reisekonto, Orten, Bewertungen und sozialen Freigaben. Maßgeblich ist die tatsächlich veröffentlichte App-Version. Die genannten Daten dienen der von Ihnen ausgelösten Funktion.

## 2. Verantwortlicher

**Marvin Perzi (Persie0)**, Angerdorf 6, 3822 Karlstein an der Thaya, Österreich. E-Mail: [persie0@protonmail.com](mailto:persie0@protonmail.com). Weitere Unternehmensangaben und Kontaktmöglichkeiten: [Impressum](https://persie0.github.io/translations_imprint/imprint-de.html).

## 3. Kurzübersicht

- NomadRank speichert Ihr Reisekonto, Orte, Bewertungen und sozialen Freigaben in einem von Persie0 betriebenen Server-Backend in Frankfurt am Main; die Anmeldung erfolgt über Firebase mit Google oder Apple.
- Die Kernfunktionen sind ohne Werbung; in der überprüften Version ist kein Werbedienst eingebunden.
- Optional: Reisevorschläge aus Textimporten über Gemini mit Ihrem eigenen API-Schlüssel, Kartenansichten (CARTO) sowie Länder- und Währungsdaten.
- Fehlerberichte gehen an eine selbst betriebene GlitchTip-Installation in Frankfurt am Main.
- Ihr Konto können Sie in der App löschen; eine Hilfeseite beschreibt den Ablauf ([Kontolöschung](https://github.com/Persie0/legal/blob/main/references/eu-app-legal/app-policies/KONTOLOESCHUNG_NOMADRANK.md)).

## 4. Datenverarbeitung nach Zwecken

Die Verarbeitung ist nach Funktion gegliedert. Dabei ist zwischen rein lokaler Verarbeitung und Daten, die auf Servern oder bei unabhängigen Diensten anfallen, zu unterscheiden. Bei ausschließlich lokal ausgeführten Vorgängen erhält Persie0 nicht automatisch Zugriff auf deren Inhalte.

**Verwendung der App auf Ihrem Gerät**

- Daten: Offline-Kopien und Warteschlangen von Konto-, Reise- und Sozialdaten; Karten-/statische Datensätze sowie zwischengespeicherte Länder- und Währungsdaten; Einstellungen und ein im sicheren Betriebssystemspeicher abgelegter Gemini-API-Schlüssel.
- Rechtsgrundlage: angeforderte Funktion; soweit personenbezogene Daten durch uns verarbeitet werden, Art. 6 Abs. 1 lit. b DSGVO.
- Empfänger: keine; die Daten verbleiben auf Ihrem Gerät.
- Speicherdauer/Löschung: bis Sie die lokalen Daten löschen, zurücksetzen oder die App deinstallieren.

**NomadRank-Konto erstellen, absichern und anmelden** *(optional, für Konto­funktionen erforderlich)*

- Daten: Firebase-UID, E-Mail, Anzeigename, Authentifizierungsanbieter, Token und Sicherheits-/Anfrageprotokolle einschließlich IP; Google oder Apple verarbeiten zusätzlich die von Ihnen autorisierten Anmeldedaten.
- Rechtsgrundlage: Art. 6 Abs. 1 lit. b DSGVO; Sicherheit/Missbrauchsprävention zusätzlich Art. 6 Abs. 1 lit. f DSGVO.
- Empfänger: Google Firebase und der von Ihnen gewählte Anmeldeanbieter (siehe Abschnitt 6).
- Speicherdauer: für die Kontolaufzeit. Nach Kontolöschung erfolgt die Löschung aus Live-/Sicherungssystemen nach Anbieterzyklen; Firebase nennt für viele gelöschte Systeme/Sicherungen bis zu 180 Tage, vorbehaltlich Sicherheits-/Rechtsnachweisen.

**Konto, Synchronisierung, Reisetagebuch, Ranglisten- und gewünschte Sozialfunktionen bereitstellen**

- Daten: UID; Benutzer-/Anzeigename; Anmelde-E-Mail; Avatar-URL; Heimatland; Mitgliedschaft/Rang/Erfolge; Reisen und geplante Reisen (Ziel-/Stadtkoordinaten, Daten, Bewertungen, Tags, Notizen, Kosten); Bucket List; Freunde/Einladungen; Gruppen; Reisekreise und Mitglieder/Stopps; Server-/Sicherheitsprotokolle einschließlich IP. Andere Nutzer können Profil-/Sozialdaten funktionsabhängig sehen.
- Rechtsgrundlage: Art. 6 Abs. 1 lit. b DSGVO; Dienstsicherheit/Missbrauchsprävention Art. 6 Abs. 1 lit. f DSGVO. Soziale Veröffentlichung/Weitergabe erfolgt auf Ihre Anforderung.
- Empfänger: Persie0-Backend auf Oracle-Cloud-Infrastruktur (Frankfurt) sowie die von der Funktion angezeigten Freunde, Eingeladene oder Gruppen-/Kreismitglieder (siehe Abschnitt 6).
- Speicherdauer: Kontoinhalte bis zur Einzellöschung oder Kontolöschung. Sicherheitskopien werden nach den jeweils festgelegten Aufbewahrungsregeln bereinigt; Sicherheitsprotokolle nur für Missbrauchs-/Anspruchszwecke. Ein portabler Export ist in der App verfügbar.

**Regionale Voreinstellungen, Währung, Sprache oder Einwilligungsablauf wählen**

- Daten: öffentliche IP-Adresse, Anfragemetadaten und ein daraus abgeleitetes Land/eine Region; kein GPS-Standort.
- Rechtsgrundlage: Art. 6 Abs. 1 lit. f DSGVO (minimale regionale Konfiguration). Regionale Einstellungen können, soweit angeboten, überschrieben werden.
- Empfänger: der jeweils zuerst verfügbare Ländererkennungsdienst (siehe Abschnitt 6).
- Speicherdauer: die Antwort wird vorübergehend verwendet oder lokal zwischengespeichert; Persie0 führt kein Serverprotokoll. Anbieter speichern Anfrageprotokolle nach ihren Richtlinien.

**Bei von Ihnen gestartetem Import Reisevorschläge extrahieren und Ziele auflösen** *(optional)*

- Daten: Ihr Gemini-API-Schlüssel, eingegebener Reisetext, ausgewählte Text-/Tabellenanhänge (bis zum App-Limit), Dateinamen, Prompts, mögliche Zielortzeilen und die erzeugte Reiseextraktion. Der Schlüssel liegt im sicheren Betriebssystemspeicher; Persie0 erhält ihn nicht.
- Rechtsgrundlage: Art. 6 Abs. 1 lit. a/b DSGVO. Optional und von Ihnen gestartet; Google handelt nach dem mit Ihrem Schlüssel verbundenen API-Konto/-Vertrag.
- Empfänger: Google AI (siehe Abschnitt 6).
- Speicherdauer: Persie0 speichert nur die von Ihnen übernommenen Reisedaten. Googles Aufbewahrung/Training hängt von bezahltem Dienst und Kontokonfiguration ab; prüfen Sie vor der Eingabe personenbezogener Daten die Gemini-API-Bedingungen.

**Den von Ihnen gewünschten Kartenbereich anzeigen**

- Daten: IP, User-Agent, Anfragezeit und angeforderte Kartenkachelkoordinaten/Zoomstufe, aus denen das betrachtete Gebiet hervorgehen kann. Der Kartenanbieter erhält kein Persie0-Kontopasswort.
- Rechtsgrundlage: Art. 6 Abs. 1 lit. b DSGVO für die gewünschte Karte und Art. 6 Abs. 1 lit. f für effiziente Auslieferung.
- Empfänger: CARTO/CDN und bei direkter Abfrage OpenStreetMap-bezogene Dienste (siehe Abschnitt 6).
- Speicherdauer: Persie0 führt keine Kartenkachel-Anfrageprotokolle; es gelten Anbieterfristen. Der lokale Cache wird durch App/Betriebssystem oder Deinstallation gelöscht.

**Länderinformationen, Hinweise/statische Fakten und Wechselkurse anzeigen**

- Daten: IP, Anfragemetadaten und der angefragte Artikel, das Land oder das Währungspaar. Kein Kontopasswort.
- Rechtsgrundlage: Art. 6 Abs. 1 lit. b DSGVO für gewünschte Inhalte; Art. 6 Abs. 1 lit. f für zwischengespeicherte, zuverlässige Auslieferung.
- Empfänger: der von der Funktion abgefragte Inhalts-/API-Anbieter (siehe Abschnitt 6).
- Speicherdauer: Antworten werden bei Bedarf lokal zwischengespeichert; Persie0 führt kein Serverprotokoll. Anbieterfristen gelten.

**Technische Fehlerdiagnose**

- Daten: App-/Systemversion, Fehlermeldung, Stacktrace und technische HTTP-/Gerätedaten.
- Rechtsgrundlage: Art. 6 Abs. 1 lit. f DSGVO, Schutz vor Fehlern und Missbrauch.
- Empfänger: selbst betriebene GlitchTip-Installation (siehe Abschnitt 6).
- Speicherdauer: 14 Tage für Fehlerereignisse.

## 5. Verarbeitung auf dem Gerät und Berechtigungen

Im Gerätespeicher werden für die angeforderten Funktionen insbesondere folgende Daten verwendet: Offline-Kopien und Warteschlangen von Konto-, Reise- und Sozialdaten, Karten-/statische Datensätze sowie zwischengespeicherte Länder- und Währungsdaten, Einstellungen und ein im sicheren Betriebssystemspeicher abgelegter Gemini-API-Schlüssel. Sie können gespeicherte Inhalte über die dafür angebotene App-Funktion entfernen beziehungsweise lokale App-Daten über das Betriebssystem zurücksetzen. Exportierte Kopien können außerhalb der App weiterbestehen.

- Genauer/ungefährer Standort: die nächstgelegene unterstützte Stadt vorschlagen; der Abgleich erfolgt mit einer lokalen Städtedatenbank.
- Fotos/Dateien: Profil-/Reisebild auswählen oder Reisedateien importieren/exportieren.
- Netzwerk: Kontosynchronisierung, soziale Funktionen, Karten, Länder-/Währungsdaten, Diagnose und optionaler Gemini-Import.

Eine Systemberechtigung erfasst nur den jeweiligen Gerätezugriff und ist keine Zustimmung zu unabhängigen Werbe- oder Analysezwecken.

## 6. Externe Dienste und Empfänger

### Anmeldung (Firebase)

Kontoerstellung und Anmeldung erfolgen über Google Firebase und den von Ihnen gewählten Anmeldeanbieter (Google oder Apple). Welche Daten dabei mit welcher Rechtsgrundlage verarbeitet werden, beschreibt Abschnitt 4. [Datenschutz des Anbieters](https://firebase.google.com/support/privacy)

### NomadRank-Konto und Sozialfunktionen (eigenes Backend, Oracle Frankfurt)

Konto-, Reise-, Gruppen- und Kontaktfunktionen laufen auf unserem Backend bei Oracle Cloud Infrastructure in Frankfurt am Main (Deutschland, Region eu-frankfurt-1). Oracle ist als Infrastruktur-Auftragsverarbeiter tätig; Freunde, Eingeladene oder Gruppen-/Kreismitglieder erhalten die von der jeweiligen Funktion angezeigten Felder. Die Kontolöschung beschreibt die [gesonderte Hilfeseite](https://github.com/Persie0/legal/blob/main/references/eu-app-legal/app-policies/KONTOLOESCHUNG_NOMADRANK.md). [Datenschutz des Anbieters](https://www.oracle.com/legal/privacy/)

### Ländererkennung

Für regionale Voreinstellungen wird der zuerst verfügbare der Dienste ipapi.co, FreeIPAPI oder ip-api.com abgefragt. [Datenschutzhinweise des Dienstes](https://ipapi.co/privacy/)

### Optionaler Gemini-Reiseimport (mit eigenem API-Schlüssel)

Der von Ihnen gestartete Import sendet Texte, Anhänge und Prompts mit Ihrem API-Schlüssel direkt an Google AI; Persie0 ist kein Zwischenempfänger der API-Nutzlast. [Nutzungsbedingungen des Dienstes](https://ai.google.dev/gemini-api/terms)

### Karten und geografische Inhalte

Kartenauslieferung erfolgt über CARTO/CDN und bei direkter Abfrage über OpenStreetMap-bezogene Dienste. [Datenschutz des Anbieters](https://carto.com/privacy/)

### Länder-, Lexikon- und Währungsabrufe

Für Länderinformationen, Hinweise und Wechselkurse werden je nach Funktion Inhalts-/API-Anbieter abgefragt, unter anderem Wikimedia-Dienste. [Datenschutz des Anbieters](https://foundation.wikimedia.org/wiki/Policy:Privacy_policy)

### Fehlerberichte (GlitchTip, selbst betrieben)

Zur Behebung von Programmfehlern verwenden wir eine eigene GlitchTip-Installation auf der Oracle-Cloud-Infrastruktur in Frankfurt am Main (Deutschland, Region eu-frankfurt-1). Hierbei können Fehlerbeschreibungen, Stacktraces, App-/Systemversionen und technische Verbindungsdaten verarbeitet werden. Fehlerereignisse werden 14 Tage gespeichert; rotierte Webserver-Zugriffsprotokolle werden nach sieben Tagen, technische Wartungsprotokolle nach 30 Tagen bereinigt.

## 7. Speicherdauer und Löschung

Lokale Datensätze bleiben bis zu Ihrer Löschung bestehen; die Deinstallation entfernt die im Gerät gespeicherten Offline-Kopien. Kontodaten bleiben bis zur Einzellöschung oder Kontolöschung; die Löschung können Sie über die Kontolöschfunktion der App veranlassen ([Hilfeseite](https://github.com/Persie0/legal/blob/main/references/eu-app-legal/app-policies/KONTOLOESCHUNG_NOMADRANK.md)). Die Deinstallation allein löscht das Serverkonto nicht. Sicherheitskopien werden nach den festgelegten Aufbewahrungsregeln bereinigt. Wo eine Funktion mit Einwilligung eingerichtet wurde, ist ein Widerruf für die Zukunft möglich. Wir unterstützen die Ausübung von Betroffenenrechten für Daten in unserem Verantwortungsbereich unter [persie0@protonmail.com](mailto:persie0@protonmail.com).

## 8. Übermittlung in Drittländer

Das NomadRank-Backend und die GlitchTip-Installation stehen in Frankfurt am Main (Deutschland); für diese Daten besteht keine Übermittlung in ein Drittland. Firebase (Google), Google AI (Gemini), der Kartenanbieter CARTO sowie die Ländererkennungs- und Inhaltsdienste können Daten auch außerhalb des EWR verarbeiten. Soweit die DSGVO anwendbar ist, beruhen solche Übermittlungen auf einer zulässigen Grundlage nach Art. 44 ff. DSGVO, etwa einem einschlägigen Angemessenheitsbeschluss oder geeigneten Vertragsgarantien.

## 9. Ihre Rechte

Ihnen stehen nach Maßgabe der DSGVO die Rechte auf Auskunft, Berichtigung, Löschung, Einschränkung, gegebenenfalls Datenübertragbarkeit und Widerspruch zu. Erteilte Einwilligungen können für die Zukunft widerrufen werden. Eine Beschwerde ist bei einer Datenschutzaufsichtsbehörde möglich, insbesondere der [österreichischen Datenschutzbehörde](https://dsb.gv.at/). Für an uns gerichtete Anliegen kontaktieren Sie [persie0@protonmail.com](mailto:persie0@protonmail.com).

## 10. Kinder, Sicherheit und Aktualisierung

Wir richten die Verarbeitung am jeweiligen Zweck aus und berücksichtigen angemessene Sicherheitsmaßnahmen. Für Minderjährige gelten die einschlägigen Schutzvorschriften. Bei wesentlichen Änderungen der Zwecke, Datenarten oder Empfänger werden wir diese Erklärung anpassen und erforderlichenfalls eine gesonderte Einwilligung einholen.
