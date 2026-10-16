# EarnMeter: Work Motivator — legal documentation requirements

**Review snapshot:** 2026-10-16 · **Repository:** [Persie0/paymeter](https://github.com/Persie0/paymeter) (`master`) · **Coverage:** current source evidence + Austrian/EU/Google Play/Apple requirements; **not a certified privacy policy**.

## What the inspected source establishes

- The Kotlin main activity uses SharedPreferences and working-time/pay calculations; the manifest does not declare broad sensitive permissions.
- No major ad, account, cloud, or billing SDK is apparent from the inspected Gradle source.

**Source evidence:**
- [`app/src/main/java/at/persie0/paymeter/MainActivity.kt`](https://github.com/Persie0/paymeter/blob/master/app/src/main/java/at/persie0/paymeter/MainActivity.kt)
- [`app/src/main/AndroidManifest.xml`](https://github.com/Persie0/paymeter/blob/master/app/src/main/AndroidManifest.xml)
- [`app/build.gradle.kts`](https://github.com/Persie0/paymeter/blob/master/app/build.gradle.kts)

## What the app-specific privacy policy must cover

### Data handled, origins and purposes
- Entered hourly pay, working time, breaks or sessions and saved UI preferences if stored.
- Time-based estimated earnings are calculations, not necessarily payroll records transmitted to a backend.

For each category, specify whether it remains **only on device**, is transmitted to a backend/provider or shared by the user's deliberate export; name the legal basis under GDPR Article 6 (plus Article 9 where applicable), actual retention period/criteria, user control and deletion mechanism. Device-only computations must not be conflated with SDK network transfers.

### Third-party services, recipients and transfers
- No app backend recipient identified in selected files; verify final dependencies and any optional external links.
- Platform support emails, if user-initiated, are handled by the email provider chosen by the user.

For each **actually initialized** SDK or endpoint, include types of identifiers/data, purpose, independent-controller/processor status, third-country destination and lawful transfer safeguards; identify the real hosting/retention arrangements. The presence of a dependency alone does not prove that every adapter is actively collecting.

## Additional app-specific disclosures and actions
- Explain formulas, taxes/break assumptions and whether amounts are gross or net; avoid presenting results as authoritative payroll calculations.
- Describe on-device data retention and how to clear/reset history.
- Use a short explicit privacy policy rather than boilerplate ad/account terms for features that do not exist.
- Verify whether the final Play artifact remains free of SDK data collection before selecting 'no data collected'.

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
- https://www.bitpanda.com/de/legal/bitpanda-group-privacy-notice

Also see [EU app legal requirements](../APP_LEGAL_REQUIREMENTS_AT_EU.md), [provider-to-app coverage](../SERVICE_COVERAGE.md), and [official Apple/Google policies](../PER_APP_LEGAL_REQUIREMENTS.md). **These notes are a drafting brief, not finished legal advice.**
