# Reduce Image Size – Compressor — legal documentation requirements

**Review snapshot:** 2026-10-16 · **Source:** [Persie0/image_compressor](https://github.com/Persie0/image_compressor) (`master`) · **Coverage:** source-backed where code is linked; otherwise explicitly provisional · **Not a published privacy policy or legal advice**.

## What the inspected source establishes

- Flutter selects and compresses photos through image-picker and uses device storage/share APIs.
- Source includes native `in_app_purchase` and Sentry; technical inventory identifies self-hosted GlitchTip.
- Native store purchases are **not** RevenueCat subscriptions merely because other portfolio apps use RevenueCat.

**Source evidence:**
- [`pubspec.yaml`](https://github.com/Persie0/image_compressor/blob/master/pubspec.yaml)
- [`lib/main.dart`](https://github.com/Persie0/image_compressor/blob/master/lib/main.dart)
- [`android/app/src/main/AndroidManifest.xml`](https://github.com/Persie0/image_compressor/blob/master/android/app/src/main/AndroidManifest.xml)

## What the app-specific privacy policy must cover

### Data handled, origins and purposes
- Selected photos, thumbnails, crops, sizes/quality settings, metadata and compressed exports.
- Technical exception traces; store purchase-product and transaction data where purchases are available.

For each category, distinguish **device-only** information, your own server transmissions, optional user-initiated exports, third-party collection and information accessible to other users. Set out the GDPR Article 6 legal basis for the actual purpose, and Article 9 conditions for special categories if relevant; specify real storage/deletion criteria and means to exercise rights.

### Third-party services and international transfers
- Self-hosted GlitchTip and Google Play/Apple native billing as applicable.
- User-selected share sheets or file destinations; do not claim originals are uploaded without evidence.

List each actual recipient (provider identity, purpose, data categories and controller/processor relationship), real retention duration/criteria and any transfer outside the EEA with applicable safeguards. SDK dependencies and ad adapters alone do **not** prove data is transmitted: verify the release artifact and runtime.

## Additional app-specific legal and product requirements
- Explain whether EXIF/location metadata is preserved, stripped or modified in output.
- Identify originals vs compressed copies, working files, output destination and deletion.
- Disclose actual one-time/non-consumable purchases versus subscriptions; show restoration where applicable.
- Keep camera/library and processing permissions separate from diagnostics collection.

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

- https://www.photoroom.com/legal/privacy
- https://cryptomator.org/privacy/

References: [Austrian/EU requirements](../APP_LEGAL_REQUIREMENTS_AT_EU.md), [actual provider categories](../SERVICE_COVERAGE.md), [per-app portfolio guide](../PER_APP_LEGAL_REQUIREMENTS.md). The publisher must check all factual statements and cannot delegate those duties to Apple, Google, Appodeal or RevenueCat.
