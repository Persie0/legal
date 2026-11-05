# Datenschutzerklärung für Toilet Compass: WC Finder

**Stand:** 5. November 2026

## 1. Geltungsbereich

Diese Datenschutzerklärung betrifft **Toilet Compass** und beschreibt die Verarbeitung im Zusammenhang mit der Suche nach WCs anhand von Standort und Kompass. Der Geräte-Standort, der Download des regionalen WC-Datensatzes und der Netzwerkzugriff auf eine Kartenkachel sind unterschiedliche technische Vorgänge. Maßgeblich ist die tatsächlich veröffentlichte App-Version.

## 2. Verantwortlicher

**Marvin Perzi (Persie0)**, Angerdorf 6, 3822 Karlstein an der Thaya, Österreich. E-Mail: [persie0@protonmail.com](mailto:persie0@protonmail.com). Weitere Unternehmensangaben und Kontaktmöglichkeiten: [Impressum](https://persie0.github.io/translations_imprint/imprint-de.html).

## 3. Kurzübersicht

- Toiletten, Standort und Kompassdaten bleiben auf Ihrem Gerät; ein Nutzerkonto ist nicht erforderlich.
- Regionale Offline-Datenbanken werden über GitHub geladen; die Download-URL enthält keine Live-GPS-Koordinate.
- Kartenkacheln werden von CARTO auf Basis von OpenStreetMap-Daten geladen.
- Auf Wunsch wird eine Route in der von Ihnen gewählten Karten-App geöffnet; dann ist deren Anbieter verantwortlich.
- Fehlerberichte gehen an eine selbst betriebene GlitchTip-Installation in Frankfurt am Main.

## 4. Datenverarbeitung nach Zwecken

Die Verarbeitung ist nach Funktion gegliedert. Dabei ist zwischen rein lokaler Verarbeitung und Daten, die auf Servern oder bei unabhängigen Diensten anfallen, zu unterscheiden. Bei ausschließlich lokal ausgeführten Vorgängen erhält Persie0 nicht automatisch Zugriff auf deren Inhalte.

**Verwendung der App auf Ihrem Gerät**

- Daten: heruntergeladene regionale Toilettendatenbanken; aktueller Standort und Kompassrichtung während der Nutzung; zwischengespeicherte Treffer und Einstellungen.
- Zweck: Bereitstellung der App-Funktion auf Ihrem Gerät.
- Rechtsgrundlage: von Ihnen angeforderte Funktion; soweit personenbezogene Daten durch uns verarbeitet werden, Art. 6 Abs. 1 lit. b DSGVO.
- Empfänger: keine; die Daten verbleiben auf Ihrem Gerät.
- Speicherdauer/Löschung: bis Sie die lokalen Daten löschen, zurücksetzen oder die App deinstallieren.

**Die ausgewählte Offline-Datenbank laden und ihre Integrität prüfen**

- Daten: IP, Anfragemetadaten und angeforderte Kontinentdatenbank; die Download-URL enthält keine Live-GPS-Koordinate.
- Rechtsgrundlage: Art. 6 Abs. 1 lit. b DSGVO und Art. 6 Abs. 1 lit. f für sichere Verteilung.
- Empfänger: GitHub (siehe Abschnitt 6).
- Speicherdauer: die Datenbank bleibt bis zur Entfernung/Deinstallation auf dem Gerät; GitHub speichert Downloadprotokolle nach dessen Richtlinie, Persie0 führt kein separates Protokoll.

**Den von Ihnen gewünschten Kartenbereich anzeigen**

- Daten: IP, User-Agent, Anfragezeit und angeforderte Kartenkachelkoordinaten/Zoomstufe, aus denen das betrachtete Gebiet hervorgehen kann. Der Kartenanbieter erhält kein Persie0-Kontopasswort.
- Rechtsgrundlage: Art. 6 Abs. 1 lit. b DSGVO für die gewünschte Karte und Art. 6 Abs. 1 lit. f für effiziente Auslieferung.
- Empfänger: CARTO/CartoCDN und bei direkter Abfrage OpenStreetMap-bezogene Dienste (siehe Abschnitt 6).
- Speicherdauer: Persie0 führt keine Kartenkachel-Anfrageprotokolle; es gelten Anbieterfristen. Der lokale Cache wird mit der App/dem Betriebssystem oder der Deinstallation gelöscht.

**Auf Ihre Anforderung eine Route öffnen** *(optional)*

- Daten: Ziel sowie aktueller Standort/Kontext, den die gewählte Karten-App nach Ihrem Öffnen hinzufügt; IP- und Geräte-/Kontodaten nach deren Einstellungen.
- Rechtsgrundlage: Art. 6 Abs. 1 lit. b DSGVO; der gewählte externe Anbieter ist eigenständig verantwortlich.
- Empfänger: die von Ihnen gewählte Karten-App/-Website (siehe Abschnitt 6).
- Speicherdauer: nach Konto-/Datenschutzeinstellungen des externen Anbieters; Persie0 erhält die Route nicht.

**Technische Fehlerdiagnose**

- Daten: App-/Systemversion, Fehlermeldung, Stacktrace und technische HTTP-/Gerätedaten.
- Rechtsgrundlage: Art. 6 Abs. 1 lit. f DSGVO, Schutz vor Fehlern und Missbrauch.
- Empfänger: selbst betriebene GlitchTip-Installation (siehe Abschnitt 6).
- Speicherdauer: 14 Tage für Fehlerereignisse.

## 5. Verarbeitung auf dem Gerät und Berechtigungen

Im Gerätespeicher werden für die angeforderten Funktionen insbesondere folgende Daten verwendet: heruntergeladene regionale Toilettendatenbanken, aktueller Standort und Kompassrichtung während der Nutzung, zwischengespeicherte Treffer und Einstellungen. Sie können gespeicherte Inhalte über die dafür angebotene App-Funktion entfernen beziehungsweise lokale App-Daten über das Betriebssystem zurücksetzen. Exportierte Kopien können außerhalb der App weiterbestehen.

- Genauer/ungefährer Standort: Toiletten in der Nähe finden und sortieren.
- Kompass-/Bewegungssensoren: in Richtung einer Toilette zeigen.
- Netzwerk: Toilettendatenbanken, Kartenkacheln und Diagnose laden.

Eine Systemberechtigung erlaubt nur den jeweiligen Gerätezugriff und stellt keine Zustimmung zu unabhängigen Werbe- oder Analysezwecken dar.

## 6. Externe Dienste und Empfänger

### Toiletten-Datenbanken (GitHub Releases)

Die regionalen Offline-Datenbanken werden über GitHub Releases bereitgestellt; dabei können IP-Adresse, Anfragezeit und User-Agent verarbeitet werden. [Datenschutzhinweise des Dienstes](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement)

### Kartenkacheln (CARTO/CartoCDN)

Für die Kartenanzeige werden Kacheln über CARTO auf Basis von OpenStreetMap-Daten geladen. [Datenschutzhinweise des Dienstes](https://carto.com/privacy/)

### Externe Routenführung

Auf Ihre Anforderung öffnet die App die Ziel-Toilette in der von Ihnen gewählten Karten-App oder Website (etwa Google Maps); deren Datennutzung regelt der jeweilige Anbieter. [Datenschutzhinweise von Google](https://policies.google.com/privacy)

### Fehlerberichte (GlitchTip, selbst betrieben)

Zur Behebung von Programmfehlern verwenden wir eine eigene GlitchTip-Installation auf der Oracle-Cloud-Infrastruktur in Frankfurt am Main (Deutschland, Region eu-frankfurt-1). Hierbei können die App- und Systemversion, Fehlermeldungen, Stacktraces sowie technische Verbindungsdaten verarbeitet werden. Fehlerereignisse werden 14 Tage gespeichert; rotierte Webserver-Zugriffsprotokolle werden nach sieben Tagen, technische Wartungsprotokolle nach 30 Tagen bereinigt.

## 7. Speicherdauer und Löschung

Lokale Datensätze bleiben bis zu Ihrer Löschung bestehen. Mit dem Zurücksetzen der App-Daten oder der Deinstallation werden die im Gerät gespeicherten Inhalte entfernt; selbst exportierte Kopien bleiben davon unberührt.

## 8. Übermittlung in Drittländer

Die selbst betriebene GlitchTip-Installation steht in Frankfurt am Main (Deutschland); für diese Fehlerdaten besteht keine Übermittlung in ein Drittland. GitHub und CARTO können Daten auch außerhalb des EWR verarbeiten, etwa bei Anbietern mit Sitz in den USA. Beim Öffnen einer Route in einer externen Karten-App gilt die Verarbeitung des jeweiligen Anbieters, die ebenfalls außerhalb des EWR erfolgen kann. Soweit die DSGVO anwendbar ist, beruhen solche Übermittlungen auf einer zulässigen Grundlage nach Art. 44 ff. DSGVO, etwa einem einschlägigen Angemessenheitsbeschluss oder geeigneten Vertragsgarantien.

## 9. Ihre Rechte

Ihnen stehen nach Maßgabe der DSGVO die Rechte auf Auskunft, Berichtigung, Löschung, Einschränkung, gegebenenfalls Datenübertragbarkeit und Widerspruch zu. Erteilte Einwilligungen können für die Zukunft widerrufen werden. Eine Beschwerde ist bei einer Datenschutzaufsichtsbehörde möglich, insbesondere der [österreichischen Datenschutzbehörde](https://dsb.gv.at/). Für an uns gerichtete Anliegen kontaktieren Sie [persie0@protonmail.com](mailto:persie0@protonmail.com).

## 10. Kinder, Sicherheit und Aktualisierung

Wir richten die Verarbeitung am jeweiligen Zweck aus und berücksichtigen angemessene Sicherheitsmaßnahmen. Für Minderjährige gelten die einschlägigen Schutzvorschriften. Bei wesentlichen Änderungen der Zwecke, Datenarten oder Empfänger werden wir diese Erklärung anpassen und erforderlichenfalls eine gesonderte Einwilligung einholen.
