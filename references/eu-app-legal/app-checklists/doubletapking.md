# DoubleTapKing – Clicking Game — legal documentation requirements

**Review snapshot:** 2026-10-16 · **Repository:** [Persie0/double_tap_king](https://github.com/Persie0/double_tap_king) (`master`) · **Coverage:** current source evidence + Austrian/EU/Google Play/Apple requirements; **not a certified privacy policy**.

## What the inspected source establishes

- Core source records elapsed touch timing and a locally managed high score; Android manifest requests vibration.
- The inspected pubspec does not declare a dedicated ad, analytics, billing, or crash-report SDK; this supports a short offline-oriented notice, not an assertion about release-binary behavior.

**Source evidence:**
- [`lib/main.dart`](https://github.com/Persie0/double_tap_king/blob/master/lib/main.dart)
- [`pubspec.yaml`](https://github.com/Persie0/double_tap_king/blob/master/pubspec.yaml)
- [`android/app/src/main/AndroidManifest.xml`](https://github.com/Persie0/double_tap_king/blob/master/android/app/src/main/AndroidManifest.xml)

## What the app-specific privacy policy must cover

### Data handled, origins and purposes
- Touch timing, high score and locally saved visual/preferences state.
- No external recipients identified from inspected manifests; if added later, update the privacy policy and stores.

For each category, specify whether it remains **only on device**, is transmitted to a backend/provider or shared by the user's deliberate export; name the legal basis under GDPR Article 6 (plus Article 9 where applicable), actual retention period/criteria, user control and deletion mechanism. Device-only computations must not be conflated with SDK network transfers.

### Third-party services, recipients and transfers
- Ordinary operating-system store infrastructure; third-party recipients cannot be asserted absent without checking the release binary.
- Any future ads, leaderboards or cloud accounts must be described separately.

For each **actually initialized** SDK or endpoint, include types of identifiers/data, purpose, independent-controller/processor status, third-country destination and lawful transfer safeguards; identify the real hosting/retention arrangements. The presence of a dependency alone does not prove that every adapter is actively collecting.

## Additional app-specific disclosures and actions
- Explain how the high score is stored and removed by clearing app data.
- State that vibration is optional device feedback, not collection of biometric fingerprints.
- Complete Play target-audience/age rating; children's/families rules only if actually targeted to children.
- No mandatory custom EULA, advertising consent or account deletion screen for an offline game without these features.

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
- https://help.yuka.io/l/en/article/jcejovibd3

Also see [EU app legal requirements](../APP_LEGAL_REQUIREMENTS_AT_EU.md), [provider-to-app coverage](../SERVICE_COVERAGE.md), and [official Apple/Google policies](../PER_APP_LEGAL_REQUIREMENTS.md). **These notes are a drafting brief, not finished legal advice.**
