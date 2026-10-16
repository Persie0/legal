# Reference comparison and redrafting decisions

**16 October 2026** · Companion to the [32 policy/terms pairs](README.md)

The previous drafts were replaced after a closer reading of **real Austrian/EU publisher policies**, particularly:

| Real publisher document | Useful structural model | How this was adapted for Persie0 |
| --- | --- | --- |
| [ÖAMTC – privacy for its specific app](https://www.oeamtc.at/mitgliedschaft/leistungen/datenschutzerklaerung-oeamtc-app-28493389) | Specific app scope, local/location processing, purposes, legal grounds, retention, registration/deletion and complaints | Each draft names its **own** app and separates local processing and external data flows; location only appears in relevant apps |
| [Photoroom – privacy policy](https://www.photoroom.com/legal/privacy) | **Purpose / data / legal basis / retention** table and named recipient classes | Each new `DATENSCHUTZ.md` contains a purpose-by-purpose table populated from relevant source/service inventory; external vendors also have dedicated descriptions |
| [Auphonic – privacy](https://eu1.auphonic.com/privacy) | Distinction among media content, account data, external service tokens, subscriptions and provider roles | Noise Remover and PureMic distinguish audio processed on-device from payments, advertising and diagnostics; media is not assumed uploaded merely because network SDKs exist |
| [willhaben – privacy](https://www.willhaben.at/iad/datenschutzerklaerung) | Specific account/social-processing disclosures, advertising and consent discussions | NomadRank has social sharing/account-specific language, and ad-supported apps explain that consent is a separate act from an EULA |
| [Bitpanda – Group Privacy Notice](https://www.bitpanda.com/de/legal/bitpanda-group-privacy-notice) | Structured explanations of the legal basis and the reason for requesting information | Avoids claiming that every app collects every kind of data; local calculators/games have much narrower drafts |
| [Photoroom – terms](https://www.photoroom.com/legal/terms-and-conditions) | Scope, paid service, cancellation, accounts, content/licensing and termination | Subscription clauses are limited to apps offering purchases; actual prices and trial terms belong to the current store purchase screen |
| [Auphonic – terms](https://auphonic.com/terms_of_service) | Account/content responsibilities, ownership, processing limitations and separate payment terms | Media/learning apps address rights to imported content and realistic processing limits without copying Auphonic's restrictions or disclaimers |

**Nothing from those third-party terms was reproduced word for word as a model clause.** Only conventional legal-document structure and coverage were used. Reusing another company's retention figures, liability exclusions, privacy claims, payment models, company address or DPO details would be both misleading and potentially unlawful.

## What materially changed

- The **32 Datenschutzerklärungen** now have purpose/data/legal-basis/retention tables, relevant provider-level subsections, and distinct descriptions of local data and internet requests.
- The **32 Nutzungsbedingungen** were rewritten around actual app functions and the relevant payment/consent/account distinctions rather than assuming every app needs an oversized EULA.
- The **Austrian Impressum URL** in the new texts is the actual [published page](https://persie0.github.io/translations_imprint/imprint-de.html), not the broken shortcut path used in the previous drafts.
- The app-checklist index points directly to existing app files and to all Android Play listings.
- For **Resistor Scanner**, the native Kotlin code is the relevant source and old Flutter Appodeal wording was excluded.
- For **Photo Print Size Editor**, billing is marked disabled in the inspected build; it should not claim live paid subscriptions.
- For **NomadRank**, authentication and the app-operated Oracle backend are separate recipients; sharing and account deletion require their own treatment.
- For **Vitamin D Tracker**, health records, weather requests, and optional cloud backups require separate treatment; Article 9 must not be presented as a universal rule for purely private on-device computations.
- For **Selfie Diary** and **VPN & Proxy Detector**, the exact published source remains unidentified, so these cannot be truthfully finalized.

## Publication blockers

These are **working legal texts** rather than production-approved policies. Their internal markers are an intentional warning, not an invitation to publish them unchanged.

1. Replace each `[OFFEN]`, `[ZU PRÜFEN]` and editorial note with substantiated facts or remove inapplicable processing.
2. Verify actual **release-binary** network traffic, ad mediation initialization, DSN, processor agreements and countries (not merely whether a dependency appears in source).
3. Determine real **server/diagnostics retention periods**, third-country safeguards and relevant independent controllers. Do not borrow any figures from a competitor.
4. Verify Android/iOS/macOS variants, actual purchase terms, free-function limits, the identity of the contractual seller and consumer withdrawal rules, including [§ 13a FAGG](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20008847&Paragraf=13a).
5. Have sensitive health, biometric, social-content and paid-contract clauses reviewed by a qualified Austrian legal professional before putting them into store listings.

The app operators' existing live GitHub Pages policies were **not modified** and these drafts should not be represented to users as replacing them until cleared.
