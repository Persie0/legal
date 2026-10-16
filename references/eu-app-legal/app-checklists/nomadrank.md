# NomadRank: Rate Visited Places — legal documentation requirements

**Review snapshot:** 2026-10-16 · **Repository:** [Persie0/skratch_clone](https://github.com/Persie0/skratch_clone) (`master`) · **Coverage:** current source evidence + Austrian/EU/Google Play/Apple requirements; **not a certified privacy policy**.

## What the inspected source establishes

- Firebase Authentication sign-in and a separate Oracle-backed app account/social backend handle profiles, travel histories, friends/groups and ratings.
- Account service exposes an app-data deletion API; document server-side content deletion, friends/shared copies, retention and any lawful exceptions.
- The app uses map/static content and optional Gemini trip import; developer-hosted GlitchTip handles diagnostics according to service inventory.

**Source evidence:**
- [`lib/services/oracle_account_service.dart`](https://github.com/Persie0/skratch_clone/blob/master/lib/services/oracle_account_service.dart)
- [`lib/screens/login_screen.dart`](https://github.com/Persie0/skratch_clone/blob/master/lib/screens/login_screen.dart)
- [`lib/main.dart`](https://github.com/Persie0/skratch_clone/blob/master/lib/main.dart)
- [`pubspec.yaml`](https://github.com/Persie0/skratch_clone/blob/master/pubspec.yaml)

## What the app-specific privacy policy must cover

### Data handled, origins and purposes
- Identity/email and login identifiers; visited countries/cities, dates, reviews, ratings, social graph, images, group memberships.
- Profile and trip information stored server-side, user-selected AI import text and documents, local queued changes, map/other request metadata.

For each category, specify whether it remains **only on device**, is transmitted to a backend/provider or shared by the user's deliberate export; name the legal basis under GDPR Article 6 (plus Article 9 where applicable), actual retention period/criteria, user control and deletion mechanism. Device-only computations must not be conflated with SDK network transfers.

### Third-party services, recipients and transfers
- Firebase Authentication, developer Oracle/ORDS/proxy infrastructure and hosting providers; optional Google Gemini via user's API key.
- Map tile/content services, Wiki/currency sources and self-hosted GlitchTip diagnostics.

For each **actually initialized** SDK or endpoint, include types of identifiers/data, purpose, independent-controller/processor status, third-country destination and lawful transfer safeguards; identify the real hosting/retention arrangements. The presence of a dependency alone does not prove that every adapter is actively collecting.

## Additional app-specific disclosures and actions
- Mandatory account deletion initiation in iOS and in-app plus web deletion request for Google Play; separately explain deletion of visible/social content.
- Define sharing defaults, public/private travel history, reporting, blocking/moderation, and possible DSA content-hosting obligations.
- Document what GPS coordinates are on-device vs saved destination coordinates; explain optional AI submissions.
- Declare access to Google/Apple login, Oracle backend, retention, account closure and data portability; avoid overpromising instant permanent backup erasure.

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

- https://www.willhaben.at/iad/datenschutzerklaerung
- https://www.bitpanda.com/de/legal/bitpanda-group-privacy-notice

Also see [EU app legal requirements](../APP_LEGAL_REQUIREMENTS_AT_EU.md), [provider-to-app coverage](../SERVICE_COVERAGE.md), and [official Apple/Google policies](../PER_APP_LEGAL_REQUIREMENTS.md). **These notes are a drafting brief, not finished legal advice.**
