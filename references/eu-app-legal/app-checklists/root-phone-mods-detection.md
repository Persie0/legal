# Root & Phone Mods Detection — legal documentation requirements

**Review snapshot:** 2026-10-16 · **Source:** [Persie0/root_detection_app](https://github.com/Persie0/root_detection_app) (`master`) · **Coverage:** source-backed where code is linked; otherwise explicitly provisional · **Not a published privacy policy or legal advice**.

## What the inspected source establishes

- Native Kotlin app has INTERNET/ACCESS_NETWORK_STATE and root/system integrity tests.
- Gradle integrates Appodeal with multiple mediation adapters, RevenueCat purchases and Sentry-protocol self-hosted diagnostics.
- In the checked Gradle, BIGO and duplicate Sentry ad analytics are intentionally omitted; verify actual resolved build output.

**Source evidence:**
- [`app/build.gradle.kts`](https://github.com/Persie0/root_detection_app/blob/master/app/build.gradle.kts)
- [`app/src/main/AndroidManifest.xml`](https://github.com/Persie0/root_detection_app/blob/master/app/src/main/AndroidManifest.xml)
- [`app/src/main/kotlin/at/persie0/root_detection_app/MainActivity.kt`](https://github.com/Persie0/root_detection_app/blob/master/app/src/main/kotlin/at/persie0/root_detection_app/MainActivity.kt)

## What the app-specific privacy policy must cover

### Data handled, origins and purposes
- Root/system properties, installed indicators (only as technically used), integrity scan results/history and app settings.
- Ad IDs and SDK network data, consent and rewarded/interstitial events; Pro entitlement/customer info and crash events.

For each category, distinguish **device-only** information, your own server transmissions, optional user-initiated exports, third-party collection and information accessible to other users. Set out the GDPR Article 6 legal basis for the actual purpose, and Article 9 conditions for special categories if relevant; specify real storage/deletion criteria and means to exercise rights.

### Third-party services and international transfers
- Appodeal plus active BidMachine, Bidon, AppLovin, Meta, Mintegral, Unity, DT Exchange, Vungle or other resolved adapters.
- RevenueCat and Play Billing; self-hosted GlitchTip.

List each actual recipient (provider identity, purpose, data categories and controller/processor relationship), real retention duration/criteria and any transfer outside the EEA with applicable safeguards. SDK dependencies and ad adapters alone do **not** prove data is transmitted: verify the release artifact and runtime.

## Additional app-specific legal and product requirements
- Explain what is inspected and whether installed app names/packages are transmitted; do not overclaim that a device is secure/unrooted.
- Tell users whether a network connection is needed for ad-funded extra checks and when a rewarded ad unlock is granted.
- Treat ad consent separately from device scanning; document fallback when ads cannot load.
- Check advertising mediation and target audience; comply with Play policies against misleading security claims.

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

- https://www.willhaben.at/iad/datenschutzerklaerung
- https://www.oeamtc.at/mitgliedschaft/leistungen/datenschutzerklaerung-oeamtc-app-28493389

References: [Austrian/EU requirements](../APP_LEGAL_REQUIREMENTS_AT_EU.md), [actual provider categories](../SERVICE_COVERAGE.md), [per-app portfolio guide](../PER_APP_LEGAL_REQUIREMENTS.md). The publisher must check all factual statements and cannot delegate those duties to Apple, Google, Appodeal or RevenueCat.
