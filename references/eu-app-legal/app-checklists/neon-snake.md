# Neon Snake — legal documentation requirements

**Review snapshot:** 2026-10-16 · **Repository:** [Persie0/neon_snake_matrix](https://github.com/Persie0/neon_snake_matrix) (`main`) · **Coverage:** current source evidence + Austrian/EU/Google Play/Apple requirements; **not a certified privacy policy**.

## What the inspected source establishes

- The Flutter game stores high score and audio volume in SharedPreferences and plays locally bundled audio.
- Inspected dependencies do not declare advertising, crash SDK or purchases; review final build before claiming absolute offline behavior.

**Source evidence:**
- [`lib/main.dart`](https://github.com/Persie0/neon_snake_matrix/blob/main/lib/main.dart)
- [`pubspec.yaml`](https://github.com/Persie0/neon_snake_matrix/blob/main/pubspec.yaml)
- [`android/app/src/main/AndroidManifest.xml`](https://github.com/Persie0/neon_snake_matrix/blob/main/android/app/src/main/AndroidManifest.xml)

## What the app-specific privacy policy must cover

### Data handled, origins and purposes
- High score, score, volume settings, gameplay choices and local preferences.
- No third-party data recipient identified from this source subset.

For each category, specify whether it remains **only on device**, is transmitted to a backend/provider or shared by the user's deliberate export; name the legal basis under GDPR Article 6 (plus Article 9 where applicable), actual retention period/criteria, user control and deletion mechanism. Device-only computations must not be conflated with SDK network transfers.

### Third-party services, recipients and transfers
- Platform distribution infrastructure; conditional external links only if the final game offers them.
- Do not invent user accounts, ad partners or purchase processors.

For each **actually initialized** SDK or endpoint, include types of identifiers/data, purpose, independent-controller/processor status, third-country destination and lawful transfer safeguards; identify the real hosting/retention arrangements. The presence of a dependency alone does not prove that every adapter is actively collecting.

## Additional app-specific disclosures and actions
- Explain local high-score retention and reset/app uninstall behavior.
- Clarify game play does not require a user profile if that is true of the release.
- Complete target age/audience and content rating; apply Families/child-directed ads only if targeted at children.
- Short privacy policy + shared Austrian imprint are enough if genuinely free/offline.

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

Also see [EU app legal requirements](../APP_LEGAL_REQUIREMENTS_AT_EU.md), [provider-to-app coverage](../SERVICE_COVERAGE.md), and [official Apple/Google policies](../PER_APP_LEGAL_REQUIREMENTS.md). **These notes are a drafting brief, not finished legal advice.**
