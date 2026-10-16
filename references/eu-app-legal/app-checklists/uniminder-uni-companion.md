# UniMinder – Uni Companion — legal documentation requirements

**Review snapshot:** 2026-10-16 · **Source:** [Persie0/student](https://github.com/Persie0/student) (`master`) · **Coverage:** source-backed where code is linked; otherwise explicitly provisional · **Not a published privacy policy or legal advice**.

## What the inspected source establishes

- Integrates university calendar/course services through TU Wien portals; repo includes MSAL authentication library and Outlook-related login UI (some inspected Outlook UI is commented, so verify activation).
- Android requests exact-alarm/full-screen/foreground-media-playback and notification permissions for time-sensitive alarms.
- Hosted Sentry.io is configured in main source; distinguish auth/browser traffic from error reporting.

**Source evidence:**
- [`lib/main.dart`](https://github.com/Persie0/student/blob/master/lib/main.dart)
- [`pubspec.yaml`](https://github.com/Persie0/student/blob/master/pubspec.yaml)
- [`android/app/src/main/AndroidManifest.xml`](https://github.com/Persie0/student/blob/master/android/app/src/main/AndroidManifest.xml)
- [`lib/screens/university/tuwel_login_screen.dart`](https://github.com/Persie0/student/blob/master/lib/screens/university/tuwel_login_screen.dart)
- [`lib/screens/email/outlook_login_screen.dart`](https://github.com/Persie0/student/blob/master/lib/screens/email/outlook_login_screen.dart)

## What the app-specific privacy policy must cover

### Data handled, origins and purposes
- University identity/session cookies or tokens, timetable, courses, exams, ICS/calendar entries, custom alarms/reminders and downloaded materials.
- Optional Microsoft/Outlook OAuth tokens if connected; diagnostic errors to hosted Sentry.io.

For each category, distinguish **device-only** information, your own server transmissions, optional user-initiated exports, third-party collection and information accessible to other users. Set out the GDPR Article 6 legal basis for the actual purpose, and Article 9 conditions for special categories if relevant; specify real storage/deletion criteria and means to exercise rights.

### Third-party services and international transfers
- TU Wien TISS/TUWEL and any actual identity endpoints; Microsoft/Outlook where active; hosted Sentry.io.
- System calendars and notification services if import/export is user-initiated.

List each actual recipient (provider identity, purpose, data categories and controller/processor relationship), real retention duration/criteria and any transfer outside the EEA with applicable safeguards. SDK dependencies and ad adapters alone do **not** prove data is transmitted: verify the release artifact and runtime.

## Additional app-specific legal and product requirements
- State credential handling, token storage, automatic sync frequency and deletion/revocation on logout.
- Explain exact alarms, wake-lock, full-screen notifications and other powerful Android permissions.
- Distinguish university service's own privacy notice and app operator; do not imply official TU Wien endorsement.
- Avoid claiming Outlook account data are connected unless the current release offers that integration.

## Mandatory baseline and conditional legal documents

- **App-specific privacy policy:** publicly readable URL usable by Play and App Store, with controller/address/contact; all actual purposes, data categories, GDPR legal bases, recipients, retention, location of processing, children where applicable, rights, withdrawal, supervisory-authority complaints and changes. Provide permanent access in the app and in the store listing.
- **Austrian Impressum / provider identification:** a shared operator website page is generally adequate for the Austrian commercial publisher if directly accessible from the app; check true business name, serviceable address, UID, WKO/trade and other legally applicable mandatory facts.
- **AGB / EULA:** Apple's standard licence is ordinarily supplied without a bespoke EULA. Separate terms only for useful licensing/account/community/purchase rules. Make applicable terms available before contractual commitment; do not treat terms acceptance as advertising, health or optional upload consent.
- **Google Play (Android versions):** Data safety including transitive SDK data, privacy URL, Health apps declaration (choose no health features if true), age-rating and Ads declaration, sensitive permissions/foreground-service declaration where used. If app account creation is offered, in-app and functional web deletion routes.
- **App Store (iOS/macOS versions):** App Privacy labels, public privacy URL, EU trader information, usage-purpose strings for protected system resources, ATT if Apple-defined tracking occurs, account-deletion feature where a user can create an app account.
- **Optional advertising:** correctly configured Appodeal Stack CMP/consent choices and revocation, truthful active mediation partner list, nonessential tracking safeguards and ATT where relevant. Appodeal's CMP does not write your GDPR privacy policy or cover SDKs unrelated to ads.
- **Optional subscriptions and IAP:** accurately show actual current price/currency, trial length, charge after trial, renewal/cancellation, manage/restore and refund/withdrawal rights. Identify the merchant/contractual party and whether Austria's §13a FAGG online withdrawal mechanism applies to a covered contract.
- **Accessibility / open-source / other law:** licenses/attribution for bundled code, datasets and models; assess Austrian consumer accessibility duties, contract rules and content- or health-specific regulation where applicable.

## Verification before publishing a definitive legal statement

- [ ] Confirm correct store release version and compare it with the inspected source branch.
- [ ] Identify all outbound hosts and actual transmitted personal data, active mediation SDKs, legal bases, storage periods and server location.
- [ ] Validate permission requests, user consent screens, consent withdrawal, local/cloud data erasure and account deletion where relevant.
- [ ] Check store privacy/Data safety labels and subscription screenshots against **the shipped binary**.
- [ ] Review all German and other language versions and the actual Austrian operator information; obtain specialist review for health, security/biometric, gambling and withdrawal questions if relevant.

## Comparable original EU/Austrian notices (do not copy clauses)

- https://nextcloud.com/privacy/
- https://www.inoreader.com/privacy_policy

References: [Austrian/EU requirements](../APP_LEGAL_REQUIREMENTS_AT_EU.md), [actual provider categories](../SERVICE_COVERAGE.md), [per-app portfolio guide](../PER_APP_LEGAL_REQUIREMENTS.md). The publisher must check all factual statements and cannot delegate those duties to Apple, Google, Appodeal or RevenueCat.
