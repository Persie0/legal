# VPN & Proxy Detector — legal documentation requirements

**Review snapshot:** 2026-10-16 · **Source:** **unverified source repository** · **Coverage:** source-backed where code is linked; otherwise explicitly provisional · **Not a published privacy policy or legal advice**.

## What the inspected source establishes

- Store inventory identifies package `at.persie0.vpn_proxy_detector`, but the authoritative application repository was **not found** via GitHub search.
- An app named VPN/Proxy Detector may inspect active network transport, routing, proxy settings, public IP or DNS; none of these are verified code findings.
- This is a **provisional checklist** pending a matching repository or release binary.

**Source evidence:**
- **Unavailable:** no authoritative application repository was located using name/package searches. Do **not** regard this file as a source-code audit.

## What the app-specific privacy policy must cover

### Data handled, origins and purposes
- Potential local network interface state, proxy/VPN status, IP addresses, DNS/routing checks and scan timestamp/history.
- Any contacted remote IP-check endpoint may see public IP, headers, time and other request metadata.

For each category, distinguish **device-only** information, your own server transmissions, optional user-initiated exports, third-party collection and information accessible to other users. Set out the GDPR Article 6 legal basis for the actual purpose, and Article 9 conditions for special categories if relevant; specify real storage/deletion criteria and means to exercise rights.

### Third-party services and international transfers
- Unknown without code; do not assert an IP lookup service, Google, VPN tunnel, analytics, ad network or backend.
- Identify each external endpoint and what is sent for IP/proxy detection.

List each actual recipient (provider identity, purpose, data categories and controller/processor relationship), real retention duration/criteria and any transfer outside the EEA with applicable safeguards. SDK dependencies and ad adapters alone do **not** prove data is transmitted: verify the release artifact and runtime.

## Additional app-specific legal and product requirements
- Explain that VPN detection is heuristic and not a guarantee of anonymity/security.
- If merely detecting VPN/proxy, do not claim the app actually supplies a VPN tunnel or claims encryption.
- If Android VpnService is used, apply Google's dedicated VPN service policy and prominent disclosure/consent rules.
- If advertising or in-app purchases exist, add partner, billing and consent details only after verification.

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

- https://www.bitpanda.com/de/legal/bitpanda-group-privacy-notice
- https://cryptomator.org/privacy/

References: [Austrian/EU requirements](../APP_LEGAL_REQUIREMENTS_AT_EU.md), [actual provider categories](../SERVICE_COVERAGE.md), [per-app portfolio guide](../PER_APP_LEGAL_REQUIREMENTS.md). The publisher must check all factual statements and cannot delegate those duties to Apple, Google, Appodeal or RevenueCat.
