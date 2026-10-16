# Memory Palace Training — legal documentation requirements

**Review snapshot:** 2026-10-16 · **Repository:** [Persie0/Memory_Palace_Builder](https://github.com/Persie0/Memory_Palace_Builder) (`main`) · **Coverage:** current source evidence + Austrian/EU/Google Play/Apple requirements; **not a certified privacy policy**.

## What the inspected source establishes

- App stores memory-palace rooms, objects, images and learning history, and offers Google Drive and Anki/AnkiConnect flows.
- Main code configures self-hosted GlitchTip (not Sentry.io), RevenueCat and Appodeal advertising.
- Manifest includes ACCESS_FINE_LOCATION; disclose the exact feature using this permission if enabled and avoid claiming it is essential to memorization.

**Source evidence:**
- [`lib/main.dart`](https://github.com/Persie0/Memory_Palace_Builder/blob/main/lib/main.dart)
- [`lib/gdrive/drive_helper.dart`](https://github.com/Persie0/Memory_Palace_Builder/blob/main/lib/gdrive/drive_helper.dart)
- [`lib/pages/anki/anki_connect_sync_client.dart`](https://github.com/Persie0/Memory_Palace_Builder/blob/main/lib/pages/anki/anki_connect_sync_client.dart)
- [`android/app/src/main/AndroidManifest.xml`](https://github.com/Persie0/Memory_Palace_Builder/blob/main/android/app/src/main/AndroidManifest.xml)

## What the app-specific privacy policy must cover

### Data handled, origins and purposes
- Mnemonics, locations/rooms *inside* palaces (not necessarily GPS), attached images, imported lists, training progress, history, preferences.
- Optional Google Drive sync payloads and OAuth tokens/scopes, optional local/network Anki data, ads/purchases/error telemetry.

For each category, specify whether it remains **only on device**, is transmitted to a backend/provider or shared by the user's deliberate export; name the legal basis under GDPR Article 6 (plus Article 9 where applicable), actual retention period/criteria, user control and deletion mechanism. Device-only computations must not be conflated with SDK network transfers.

### Third-party services, recipients and transfers
- Google Drive (user-authorized backup), local AnkiDroid or selected AnkiConnect host, potential feedback portal, self-hosted GlitchTip.
- Appodeal/mediators, RevenueCat and relevant store; external IP/country check if the final build actually uses it.

For each **actually initialized** SDK or endpoint, include types of identifiers/data, purpose, independent-controller/processor status, third-country destination and lawful transfer safeguards; identify the real hosting/retention arrangements. The presence of a dependency alone does not prove that every adapter is actively collecting.

## Additional app-specific disclosures and actions
- Distinguish app-internal virtual memory-palace 'locations' from actual GPS location.
- List exactly which data is in Drive appData, whether images are included/encrypted, retention and disconnect/deletion.
- Clarify AnkiConnect local-network transmissions versus independent AnkiWeb synchronization.
- Describe feedback submissions, ads, optional purchases and feature access; do not treat Firebase config alone as Firebase Analytics.

## Documents and store submissions to prepare

- **Privacy policy / Datenschutzerklärung:** a public HTML URL clearly identifying this app, operator/contact, all data categories/purposes/legal bases, recipients, retention, overseas transfers, rights, Austrian DSB complaint channel, security and changes. Link it in the app and every published store listing.
- **Austrian Impressum / Anbieterkennzeichnung:** a shared legally correct operator page is normally sufficient for commercial apps. Include business name, serviceable address, direct contact, UID/chamber/authority/MedienG items as applicable; link visibly from app and legal site.
- **AGB/EULA:** Apple normally provides a standard EULA; custom conditions are needed only where licensing, online accounts, user content, subscriptions or app-specific limitations merit them. Never use acceptance of terms to imply optional tracking consent.
- **Android Google Play:** complete truthful Data safety, app privacy URL, Health apps declaration (choose no health features if applicable), target-audience/ads questions, and all permission/foreground-service declarations triggered by the actual AAB. If an app account can be created, supply in-app and web deletion paths.
- **iOS/macOS where distributed:** supply App Privacy labels and accessible privacy URL; explain every protected-resource permission. If tracking as Apple defines it occurs, apply ATT; fill in EU DSA trader details and account-deletion requirements as applicable.
- **Payments and ads, only where used:** show exact current free/Pro constraints, product price, trial/renewal/cancellation and restoration; check statutory withdrawal rights and the contracting party. Appodeal's CMP may handle **ad consent**, but not health consent, optional uploads, your app policy, SDK inventory or Play/App privacy labels. Maintain a way to revisit consent where required.
- **Rights and operations:** reachable privacy/support contact, correction/access/deletion handling, local and server-side data-removal instructions, open-source licence notices where licences require them, and lawful security/incident-response processes.

## Checks before publishing text as a factual privacy statement

- [ ] Confirm app-store build/platform/SDK mediation **versus** the current default branch; record release version.
- [ ] For every third-party tool named above, identify what it sends **at runtime**, privacy-policy URL and retention/transfer agreements.
- [ ] Verify whether account creation, health, ads/ATT, subscriptions, uploads and background access are *active*; do not invent unavailable features.
- [ ] Verify all privacy and consumer statements in both German and any marketed languages against real behavior, including deletion and consent withdrawal.
- [ ] Ensure store Data safety/App Privacy answers match the actual shipped app and transitive SDKs.

## Independent Austrian/EU examples (structure only — do not copy)

- https://cryptomator.org/privacy/
- https://nextcloud.com/privacy/

Also see [EU app legal requirements](../APP_LEGAL_REQUIREMENTS_AT_EU.md), [provider-to-app coverage](../SERVICE_COVERAGE.md), and [official Apple/Google policies](../PER_APP_LEGAL_REQUIREMENTS.md). **These notes are a drafting brief, not finished legal advice.**
