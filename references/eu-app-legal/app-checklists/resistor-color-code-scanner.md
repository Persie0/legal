# Resistor Color Code Scanner — legal documentation requirements

**Review snapshot:** 2026-10-16 · **Source:** [Persie0/resistor-scanner-android](https://github.com/Persie0/resistor-scanner-android) (`main`) · **Coverage:** source-backed where code is linked; otherwise explicitly provisional · **Not a published privacy policy or legal advice**.

## What the inspected source establishes

- Current native Kotlin Android app requests CAMERA and INTERNET; uses RevenueCat and self-hosted GlitchTip diagnostics.
- The inspected Kotlin Gradle configuration **does not list Appodeal**, unlike a legacy Flutter scanner branch. Do not copy obsolete ad clauses into this Android policy.
- Scans use camera frames, detected color bands and model-derived resistance estimates; separate original images from outputs/history.

**Source evidence:**
- [`app/src/main/AndroidManifest.xml`](https://github.com/Persie0/resistor-scanner-android/blob/main/app/src/main/AndroidManifest.xml)
- [`app/build.gradle.kts`](https://github.com/Persie0/resistor-scanner-android/blob/main/app/build.gradle.kts)
- [`app/src/main/java/at/austriao/resistorscanner/GlitchTipMonitoring.kt`](https://github.com/Persie0/resistor-scanner-android/blob/main/app/src/main/java/at/austriao/resistorscanner/GlitchTipMonitoring.kt)
- [`app/src/main/java/at/austriao/resistorscanner/billing/SubscriptionManager.kt`](https://github.com/Persie0/resistor-scanner-android/blob/main/app/src/main/java/at/austriao/resistorscanner/billing/SubscriptionManager.kt)
- [`app/src/main/java/at/austriao/resistorscanner/ui/EulaConsentScreen.kt`](https://github.com/Persie0/resistor-scanner-android/blob/main/app/src/main/java/at/austriao/resistorscanner/ui/EulaConsentScreen.kt)

## What the app-specific privacy policy must cover

### Data handled, origins and purposes
- Camera/gallery images, resistor crops, model predictions, color-band readings, scan counts and local history/settings.
- Purchase entitlement/customer ID and technical error events; any user-opt-in scan uploads must be independently confirmed.

For each category, distinguish **device-only** information, your own server transmissions, optional user-initiated exports, third-party collection and information accessible to other users. Set out the GDPR Article 6 legal basis for the actual purpose, and Article 9 conditions for special categories if relevant; specify real storage/deletion criteria and means to exercise rights.

### Third-party services and international transfers
- Google Play Billing and RevenueCat; self-hosted GlitchTip.
- Optional training data collection/remote image transfer **only if** enabled: record recipient, exact images, purpose, retention and withdrawal.

List each actual recipient (provider identity, purpose, data categories and controller/processor relationship), real retention duration/criteria and any transfer outside the EEA with applicable safeguards. SDK dependencies and ad adapters alone do **not** prove data is transmitted: verify the release artifact and runtime.

## Additional app-specific legal and product requirements
- Explain processing accuracy/lighting limits and that automated readings should be checked when safety-critical.
- Justify camera permission; describe whether scan photos are retained or only transient buffers.
- Use current native Android purchase/paywall model, restore path and pricing; do not assume Appodeal from old Flutter sources.
- For iOS app implementation, inspect Swift/Core ML, Apple App Privacy, subscriptions and any different recipients separately.

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

- https://help.yuka.io/l/en/article/jcejovibd3
- https://cryptomator.org/privacy/

References: [Austrian/EU requirements](../APP_LEGAL_REQUIREMENTS_AT_EU.md), [actual provider categories](../SERVICE_COVERAGE.md), [per-app portfolio guide](../PER_APP_LEGAL_REQUIREMENTS.md). The publisher must check all factual statements and cannot delegate those duties to Apple, Google, Appodeal or RevenueCat.
