# Offene technische Fakten für die Freigabe der App-Rechtstexte (INTERN)

**Prüfstand:** 16. Oktober 2026 · **Nicht in öffentliche Datenschutzerklärungen/AGB kopieren.**

Die 32 Datenschutzerklärungen und 32 Nutzungsbedingungen unter [app-policies](app-policies/README.md) sind Endnutzertexte. Ungeklärte Infrastrukturdetails und Nachweisaufgaben werden **ausschließlich hier** erfasst. Fehlende Beweise wurden nicht durch Vermutungen oder Fristen anderer Publisher ersetzt.

## Bereits geklärt / anhand GitHub überprüft

| Thema | Nachweis | Bewertung |
| --- | --- | --- |
| GlitchTip-Hauptserver | Nutzer bestätigt Oracle Cloud Frankfurt; [GlitchTip Compose](https://github.com/Persie0/glitchtip_setup/blob/main/docker-compose.yml) | Hauptinstanz auf OCI Frankfurt; das schließt weitere Datenkopien **nicht** aus |
| GlitchTip-Ereignisse/Transaktionen/Dateien | [Compose](https://github.com/Persie0/glitchtip_setup/blob/main/docker-compose.yml) | Jeweils `GLITCHTIP_*_RETENTION_DAYS=14`, Release-Daten `30`; **Konfiguration**, nicht garantierte erfolgreiche physische Löschung |
| Webserver-/Systemlogs | [cleanup.sh](https://github.com/Persie0/glitchtip_setup/blob/main/cleanup.sh) | Löscht Caddy-Logdateien älter als 7 Tage, GlitchTip-Protokolldateien älter als 30 Tage; System-Journal älter als 7 Tage/Größenlimit **sofern Skript ausgeführt wird** |
| GlitchTip-Sicherungsmechanismus | [backup.sh](https://github.com/Persie0/glitchtip_setup/blob/main/backup.sh) | Erstellt Datenbankdump, .env-Kopie und Upload-Archiv; löscht Backups im Script erst nach >14 Tagen **sofern es läuft** |
| GitHub-Sicherungen | [Private repository tree](https://github.com/Persie0/glitchtip_setup/tree/main/backups) | Commit enthält `backups/20260916_134525/glitchtip_db.dump` (~909 KB) und `.env.backup`; **keine Inhalte oder Zugangsdaten ausgelesen**. Git-Historie verlängert die Aufbewahrung unabhängig vom Backup-Prune. Sicherheit/Datenschutz klären! |
| NomadRank-Hauptserver | Nutzer bestätigt Oracle Frankfurt; [Oracle backend](https://github.com/Persie0/skratch_clone/tree/master/oracle_backend_server) | Oracle Cloud Frankfurt; kein pauschaler Retentionwert für Kontodaten/Backups nachgewiesen |
| NomadRank-Kontolösch-Client | [oracle_account_service.dart](https://github.com/Persie0/skratch_clone/blob/master/lib/services/oracle_account_service.dart) | App sendet `POST api/account/delete`. Nicht bewiesen ist damit eine vollständige Löschung in Oracle, Firebase und Backups |
| NomadRank API-Fehler | [ords_error_logging.sql](https://github.com/Persie0/skratch_clone/blob/master/oracle_backend_server/ords_error_logging.sql) | Beinhaltet `user_id_hash` (SHA-256) und Fehlertexte; Löschintervall aus Quellcode nicht belegt |
| Optionales Crash-SDK | Finger Chooser, Pareader, Recipe Price Calculator, Screenshot Detector | In Quellen wird SDK über `SENTRY_DSN` zur Buildzeit eingeschaltet; konkrete Release-Konfiguration unbekannt. **14-Tage-Frist für diese Apps nicht unterstellen.** |
| Selfie Diary und VPN & Proxy Detector | [App-Checklisten](app-checklists/README.md) | Zugehörige Quellrepos in GitHub-Installation nicht identifiziert; darf nicht als vollständiger Codeaudit gelten |

## Antworten benötigt – keine Passwörter oder Tokens zusenden

1. **GlitchTip GitHub-Backups:** Enthält der ältere DB-Dump echte Produktions-/Nutzerdaten? Wurden Backup-Dateien absichtlich in Git übernommen? Sind .env-Zugangsdaten aus diesem Commit noch gültig? Nur **ja/nein** antworten; keine Geheimnisse teilen. Falls echt: Repo/Git-Historie bereinigen, Credentials rotieren und Backups mit geeigneter Zugriffskontrolle außerhalb des regulären Git-Repositorys speichern. Vorher keine ausschließliche Frankfurt-Speicherung behaupten.
2. **Betriebsfristen:** Sind `cleanup.sh` und `backup.sh` auf dem laufenden Server zeitgesteuert aktiv? Welche zusätzlichen GlitchTip-Dumps/Backups sind vorhanden und wo liegen sie? Ein Repository-Skript allein beweist keine tatsächlich eingehaltene Löschfrist.
3. **NomadRank:** Wie lange werden Oracle-Autobackups, Oracle-/ORDS-/Reverse-Proxy-Logs und `NOMADRANK_API_ERRORS` aufbewahrt? Entfernt `api/account/delete` auch Firebase-Identität, Social/Trip-Daten und etwaige Backups (ggf. verzögert)? Wo sind NomadRank-Backups gespeichert?
4. **Bedingte Diagnostik:** Ist Fehlerdiagnose in den veröffentlichten Builds von **Finger Chooser, Pareader, Recipe Price Calculator und Screenshot Detector** eingeschaltet? Wenn ja, welcher Empfänger (eigener GlitchTip, Sentry.io oder anderer Dienst) und welche Löschfrist? Kein DSN-Token nötig.
5. **Fehlende Repositories:** Unter welchem Github-Repository/Branch liegen **Selfie Diary** (Paket `com.persie0.selfie_diary`) und **VPN & Proxy Detector** (Paket `at.persie0.vpn_proxy_detector`)? Wenn nicht auf GitHub, Quellarchiv bereitstellen. Ohne Source kann die Datenschutzerklärung keine belegten negativen Datenfluss-Aussagen treffen.
6. **Appodeal-Partner im tatsächlich veröffentlichten Build:** Gibt es ein Dashboard-/SDK-Protokoll oder Export der aktiven Netzwerke je App? SDK-Adapter allein belegen keine Datenübermittlung. Ein Screenshot der aktiven Partner ohne vertrauliche Werbe-IDs reicht.
7. **Zusätzliche Dienst- und Produktgrenzen:** Sind alle in der veröffentlichten Android/iOS/macOS-App aktiven Clouddienste, Datenspeicher und Bezahlmodelle identisch mit dem aktuell eingesehenen GitHub-Stand? Falls nicht: Version/Branch pro Ausnahme nennen.

## Verbindliche Regeln für die Endnutzertexte

- Keine **[OFFEN]**, `SENTRY_DSN`, Entwicklerhinweise, Codeaudit-Statements, internen Freigabevermerke oder technischen Arbeitsanweisungen in App-`DATENSCHUTZ.md`/`NUTZUNGSBEDINGUNGEN.md`.
- Frankfurt nur für die nachgewiesenen *primären* OCI-Dienste nennen, nicht pauschal für Drittanbieter oder etwaige ausgelagerte Backups.
- GlitchTip-**Fehlerereignisse 14 Tage** und **rotierte Webserver-Logs 7 Tage (bei Ausführung des Cleanup-Skripts)** differenzieren; GlitchTip-Dateilogs 30 Tage, Release-Metadaten 30 Tage, Backups 14 Tage im Skript — **Git-Historie ist keine 14-Tage-Löschung**.
- Nicht von lokalen Fotos oder Audiodaten auf Cloudübertragung schließen; umgekehrt keine vollständige Offline-Verarbeitung aller SDK-Verbindungsdaten behaupten.
- Für optionalen Crashreporting-Code ohne nachgewiesene Release-Konfiguration keine konkrete Anbieteradresse oder 14-Tage-Frist zusichern.
- Veröffentlichung erst, wenn tatsächliche Datenwege, DSGVO-Rechtsgrundlagen, Drittlandgarantien, Store-Datenlabels und die erforderlichen Kontakt-/Löschwege stimmen.

**Referenzen:** [App-Quellcodechecklisten](app-checklists/README.md), [alle Endnutzertexte](app-policies/README.md), [Serviceinventar](../../SERVICES_AND_DATA.md).
