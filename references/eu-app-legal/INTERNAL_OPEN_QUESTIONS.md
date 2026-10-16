# Interne Faktenprüfung der App-Rechtstexte

**Stand: 16. Oktober 2026. Nur für die Prüfung — nicht Bestandteil der App-Datenschutzerklärungen oder AGB.**

Die [Endnutzertexte](app-policies/README.md) enthalten keine Prüfanweisungen. Offen gebliebene Tatsachen werden hier geführt, statt eine unbelegte Pflichtangabe zu erfinden.

## Vom Betreiber beantwortet und anhand des Quellcodes eingeordnet

| Frage | Antwort / Nachweis | Konsequenz |
| --- | --- | --- |
| Hauptserver GlitchTip | Oracle Cloud Infrastructure Frankfurt, vom Betreiber bestätigt | Frankfurt für den Hauptserver angeben; andere Dienste/Backups getrennt |
| GlitchTip-Speicherfristen | [Compose](https://github.com/Persie0/glitchtip_setup/blob/main/docker-compose.yml): Fehlerereignisse 14 Tage; Releases 30 Tage; [cleanup.sh](https://github.com/Persie0/glitchtip_setup/blob/main/cleanup.sh): alte Caddy-Logs nach 7 Tagen, GlitchTip-Dateilogs nach 30 Tagen | Fristen als Konfiguration angeben; Betriebserfolg nicht aus Code allein ableiten |
| GlitchTip-Skripte | Betreiber bestätigt **ja**, sowohl `cleanup.sh` als auch `backup.sh` werden regelmäßig ausgeführt | Zeitgesteuerter Betrieb als bestätigt; tatsächliche Backup-Ziele/Logfristen bleiben teils offen |
| GitHub-GlitchTip-Sicherungen | Betreiber antwortet auf zwei separate Nachfragen gemeinsam **„nein“**; Aussage kann sich auf Echtdaten und/oder Gültigkeit früherer Zugangsdaten beziehen | Beides ohne getrennte Antwort nicht als sicher festgestellt behandeln. Das private Repo enthält weiterhin einen versionierten Dump und `.env.backup`; Git-Historie verlängert die Aufbewahrung |
| NomadRank | OCI Frankfurt, Betreiber antwortet auf Fragen zu Löschfunktion und Fristen pauschal **„ja“** | Existenz einer Löschfunktion bestätigt; **keine konkrete Zahl von Tagen** für Logs und Sicherungen genannt. Firebase-/Oracle-/Backup-Löschung getrennt prüfen |
| Sentry bei vier Apps | Betreiber: **„ja, sentry“** für Finger Chooser, Pareader, Recipe Price Calculator und Screenshot Detector | Alle vier Datenschutzerklärungen nennen Sentry statt eines rein hypothetischen Empfängers. Sentry-Datenschutzlink ergänzt; nicht die GlitchTip-14-Tage-Frist übernehmen |
| Appodeal-Partner | Betreiber: Android-Kotlin-Abhängigkeiten stellen die aktivierten Partner dar | Partner je tatsächlich geprüfter Android-Gradle-Konfiguration in zehn App-Datenschutzerklärungen aufgenommen |
| Quellcode Selfie Diary und VPN & Proxy Detector | Betreiber kennt derzeit kein dazugehöriges Repository | Weiterhin kein verbindlicher Audit der Datenflüsse möglich; keine erfundenen konkreten Drittdienste |

## Appodeal-Partner: Android-Konfiguration vom 16. Oktober 2026

Basiskette für die genannten Apps: Appodeal, AppLovin, BidMachine, Bidon, BIGO Ads, DT Exchange, Meta Audience Network, Mintegral, Unity Ads und Vungle. Die IAB-/Consent- und Sentry-Analytics-Adapter sind keine zusätzlichen Werbenetzwerke und werden nicht als solche gezählt.

| App | Quellnachweis | Abweichung von der Basiskette |
| --- | --- | --- |
| Background Noise Remover | [Gradle](https://github.com/Persie0/noise_remover/blob/master/android/app/build.gradle.kts) | Keine |
| Image Upscaler Offline | [Gradle](https://github.com/Persie0/image_enhancer/blob/main/android/app/build.gradle.kts) | **Mintegral ausgeschlossen** |
| 3D Face Model Maker | [Gradle](https://github.com/Persie0/face_scanner/blob/master/android/app/build.gradle) | Keine |
| Arbitrage Betting Calculator | [Gradle](https://github.com/Persie0/surebets_calculator/blob/master/android/app/build.gradle.kts) | Keine |
| PureMic | [Gradle](https://github.com/Persie0/recorder_noise_remove/blob/main/android/app/build.gradle.kts) | Keine |
| Memory Palace Training | [Gradle](https://github.com/Persie0/Memory_Palace_Builder/blob/main/android/app/build.gradle) | Keine |
| Resistor Finder | [Gradle](https://github.com/Persie0/resistor-calc/blob/master/android/app/build.gradle) | Keine |
| Live Noise Cancellation Demo | [Gradle](https://github.com/Persie0/live_noise_cancelling/blob/master/android/app/build.gradle) | Keine |
| Root & Phone Mods Detection | [Gradle](https://github.com/Persie0/root_detection_app/blob/master/app/build.gradle.kts) | **BIGO ausgeschlossen** |
| Fake Location Detector | [Gradle](https://github.com/Persie0/fake_gps_detector/blob/master/app/build.gradle.kts) | Keine |

**Wichtig:** Diese Feststellung betrifft die **Android-Einbindungen**. Eine im SDK vorhandene Verbindung muss nicht bei jeder Anzeigenauktion aktiv werden; die iOS-Mediation ist hiermit nicht nachgewiesen. Der aktuelle native Kotlin-[Resistor Scanner](https://github.com/Persie0/resistor-scanner-android/blob/main/app/build.gradle.kts) verfügt nicht über die frühere Flutter-Appodeal-Integration.

## Verbleibende Angaben, die nur der Betreiber bestätigen kann

1. **NomadRank-Löschfristen in Tagen:** Aufbewahrungsdauer von Oracle-Backups, ORDS-/Reverse-Proxy-Logs und `NOMADRANK_API_ERRORS`. Der [Client](https://github.com/Persie0/skratch_clone/blob/master/lib/services/oracle_account_service.dart) ruft `POST api/account/delete`; aus dem Client ist nicht bewiesen, ob auch Firebase-Identity, alle Datensätze und Sicherungen erfasst werden.
2. **Sentry-Datenaufbewahrung:** Welcher Sentry-Tarif bzw. in der Sentry-Organisation eingestellter Retention-Wert gilt für die vier benannten Apps? Nicht den eigenen GlitchTip-Retention-Wert verwenden.
3. **Historische GlitchTip-Backups:** Bei „nein“ bitte unterscheiden: *keine echten Nutzerdaten* **und** *keine mehr gültigen Zugangsdaten*, oder nur eines davon? Die Repo-Kopie wird trotz laufender Skript-Bereinigung nicht automatisch aus der Git-Historie gelöscht.
4. **Andere Backup-Ziele:** Existieren zusätzliche GlitchTip-/NomadRank-Kopien außerhalb der OCI-Frankfurt-Instanz, und welche Aufbewahrungsfrist gilt dort?
5. **Selfie Diary / VPN & Proxy Detector:** Exakte Quellrepos/Store-Builds oder ein Quellarchiv sind nötig für eine definitive Erklärung zu Netzwerkverbindungen, SDKs und Löschung.
6. **Andere Plattformen:** Die aktiven iOS-/macOS-Adapter und die veröffentlichten Release-Binaries können sich von den überprüften Android-Gradle-Dateien unterscheiden.

## Nachweise und Sicherheitsbefund

- [GlitchTip-backup.sh](https://github.com/Persie0/glitchtip_setup/blob/main/backup.sh) erstellt Dumps, eine `.env`-Kopie und Upload-Archiv und löscht Verzeichnisse älter als 14 Tage **bei Ausführung**. Ein `git`-Commit unter `backups/20260916_134525/` enthält historische Versionen solcher Dateien. Die Inhalte wurden nicht geöffnet und keine Zugangsdaten ausgelesen.
- Ein als privat gekennzeichnetes Repository vermindert die Zugänglichkeit, ersetzt aber keine sichere Geheimnis-/Backup-Verwaltung. Bei echten personenbezogenen Daten beziehungsweise noch gültigen Zugangsdaten müssen Schutzmaßnahmen und gegebenenfalls Git-Historienbereinigung/Rotation bewertet werden.
- Appodeal dokumentiert ausdrücklich die Verantwortung des App-Anbieters für eine eigene Datenschutzerklärung, Identifikatoren und transparente Partnerangaben: https://docs.appodeal.com/onboarding/data-protection/privacy-policy
- Die Datenschutz- und Aufbewahrungshinweise von Sentry sind unter https://sentry.io/privacy/ abrufbar. Spezifische Aufbewahrungswerte können von Tarif/Organisation abhängen; daher keine 14-Tage-Zusage.

**Endnutzertexte:** [alle 32 Apps](app-policies/README.md). **Quellcodebasierte App-Checklisten:** [App-Checklisten](app-checklists/README.md).
