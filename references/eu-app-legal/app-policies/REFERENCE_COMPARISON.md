# Reference comparison and redrafting decisions

**16 October 2026 · restructuring pass 5 November 2026** · Companion to the [32 policy/terms pairs](README.md)

The previous drafts were replaced after a closer reading of **real Austrian/EU publisher policies**, particularly:

| Real publisher document | Useful structural model | How this was adapted for Persie0 |
| --- | --- | --- |
| [ÖAMTC – privacy for its specific app](https://www.oeamtc.at/mitgliedschaft/leistungen/datenschutzerklaerung-oeamtc-app-28493389) | Specific app scope, local/location processing, purposes, legal grounds, retention, registration/deletion and complaints | Each draft names its **own** app and separates local processing and external data flows; location only appears in relevant apps |
| [Photoroom – privacy policy](https://www.photoroom.com/legal/privacy) | **Purpose / data / legal basis / retention** coverage and named recipient classes | Each `DATENSCHUTZ.md` presents every purpose as its own block with Daten, Zweck, Rechtsgrundlage, Empfänger and Speicherdauer bullets; the earlier table layout was replaced by these purpose blocks (list form preferred by the operator); external vendors also have dedicated descriptions |
| [Auphonic – privacy](https://eu1.auphonic.com/privacy) | Distinction among media content, account data, external service tokens, subscriptions and provider roles | Noise Remover and PureMic distinguish audio processed on-device from payments, advertising and diagnostics; media is not assumed uploaded merely because network SDKs exist |
| [willhaben – privacy](https://www.willhaben.at/iad/datenschutzerklaerung) | Specific account/social-processing disclosures, advertising and consent discussions | NomadRank has social sharing/account-specific language, and ad-supported apps explain that consent is a separate act from an EULA |
| [Bitpanda – Group Privacy Notice](https://www.bitpanda.com/de/legal/bitpanda-group-privacy-notice) | Structured explanations of the legal basis and the reason for requesting information | Avoids claiming that every app collects every kind of data; local calculators/games have much narrower drafts |
| [Photoroom – terms](https://www.photoroom.com/legal/terms-and-conditions) | Scope, paid service, cancellation, accounts, content/licensing and termination | Subscription clauses are limited to apps offering purchases; actual prices and trial terms belong to the current store purchase screen |
| [Auphonic – terms](https://auphonic.com/terms_of_service) | Account/content responsibilities, ownership, processing limitations and separate payment terms | Media/learning apps address rights to imported content and realistic processing limits without copying Auphonic's restrictions or disclaimers |

**Nothing from those third-party terms was reproduced word for word as a model clause.** Only conventional legal-document structure and coverage were used. Reusing another company's retention figures, liability exclusions, privacy claims, payment models, company address or DPO details would be both misleading and potentially unlawful.

## What materially changed

- The **32 Datenschutzerklärungen** follow one ten-section skeleton (1 Geltungsbereich, 2 Verantwortlicher, 3 Kurzübersicht, 4 Datenverarbeitung nach Zwecken, 5 Verarbeitung auf dem Gerät und Berechtigungen, 6 Externe Dienste und Empfänger, 7 Speicherdauer und Löschung, 8 Übermittlung in Drittländer, 9 Ihre Rechte, 10 Kinder, Sicherheit und Aktualisierung) aligned with the recommended structure in [APP_LEGAL_REQUIREMENTS_AT_EU.md](../APP_LEGAL_REQUIREMENTS_AT_EU.md) §2; each processing purpose is a bullet block instead of a table.
- The **32 Nutzungsbedingungen** were rewritten around actual app functions and the relevant payment/consent/account distinctions rather than assuming every app needs an oversized EULA.
- The **Austrian Impressum URL** in the new texts is the actual [published page](https://persie0.github.io/translations_imprint/imprint-de.html), not the broken shortcut path used in the previous drafts.
- The app-checklist index points directly to existing app files and to all Android Play listings.
- For **Resistor Scanner**, the native Kotlin code is the relevant source and old Flutter Appodeal wording was excluded.
- For **Photo Print Size Editor**, billing is marked disabled in the inspected build; it should not claim live paid subscriptions.
- For **NomadRank**, authentication and the app-operated Oracle backend are separate recipients; sharing and account deletion require their own treatment.
- For **Vitamin D Tracker**, health records, weather requests, and optional cloud backups require separate treatment; Article 9 must not be presented as a universal rule for purely private on-device computations.
- For **Selfie Diary** and **VPN & Proxy Detector**, the exact published source remains unidentified, so these cannot be truthfully finalized.

## Restructuring pass — 5 November 2026

All 32 `DATENSCHUTZ.md` drafts were restructured to the shared skeleton above. All wording is original German drafting; no reference-publisher text was copied.

- **Lists instead of tables:** the purpose/data/legal-basis/retention tables were replaced by one block per processing purpose with bullets (Daten, Zweck, Rechtsgrundlage, Empfänger, Speicherdauer). Device and permission notes are bullet lists as well.
- **New Kurzübersicht (§3):** each policy opens with a short at-a-glance list of what stays on-device, which optional services exist and where diagnostics go.
- **Deduplicated recipients (§6):** the old section combined an "Anzeigenanbieter" list with a second near-identical "Advertising (Appodeal)" block; these were merged into one service block that references §4 for data and legal basis instead of repeating it. Empty stub sections and per-vendor purpose/data/legal-basis repetitions were removed; service blocks now keep only recipient-specific facts (links, hosting location, retention details).
- **Concrete third-country statements (§8):** the generic "manche Dienstleister können Informationen außerhalb des EWR speichern" boilerplate was replaced with app-specific statements naming which recipients can process data outside the EEA (Appodeal partner networks, RevenueCat, Sentry.io, GitHub, Google/Apple, Microsoft, external websites) and stating that the self-operated GlitchTip installation in Frankfurt am Main involves no third-country transfer. Apps with no external services say so explicitly.
- **Diagnostics recipients now app-specific:** Sentry.io apps (Finger Chooser, Live Noise Cancellation Demo, MoWa, Pareader, Recipe Price Calculator, Screenshot Detector, UniMinder) reference Sentry's own agreed retention rules rather than the self-hosted 14-day GlitchTip figure; GlitchTip apps keep the Frankfurt 14-day statement.
- **Terms fixes:** numbering gaps in Neon Snake and Photo Print Size Editor (3 → 5 → 6) were corrected to sequential numbering; the irrelevant content-rights clause was removed from the Neon Snake game terms.
- **Conventions:** `**Stand:** 5. November 2026` under the title; §9 lists rights, revocation, the complaint route (DSB) and contact; §10 covers children, security and updates.

## English drafts — 5 November 2026

Each app folder additionally contains an English translation pair: `PRIVACY.md` (privacy policy, same ten-section skeleton) and `TERMS.md` (terms of service, `legal_kind: terms-en`, served at `/terms/<app-slug>/en/`). The English texts are original translations written for this project; no reference-publisher wording was copied. They mirror the restructured German drafts — per-purpose bullet blocks, Kurzübersicht, deduplicated recipients, concrete third-country statements — and remain unpublished working texts like the German drafts. The root index [APP_POLICY_LINKS.md](../../APP_POLICY_LINKS.md) links every app to its policy and terms drafts in this repository (privacy and terms, German and English).

## Publication blockers

These are **working legal texts** rather than production-approved policies. Their internal markers are an intentional warning, not an invitation to publish them unchanged.

1. Replace each `[OFFEN]`, `[ZU PRÜFEN]` and editorial note with substantiated facts or remove inapplicable processing.
2. Verify actual **release-binary** network traffic, ad mediation initialization, DSN, processor agreements and countries (not merely whether a dependency appears in source).
3. Determine real **server/diagnostics retention periods**, third-country safeguards and relevant independent controllers. Do not borrow any figures from a competitor.
4. Verify Android/iOS/macOS variants, actual purchase terms, free-function limits, the identity of the contractual seller and consumer withdrawal rules, including [§ 13a FAGG](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20008847&Paragraf=13a).
5. Have sensitive health, biometric, social-content and paid-contract clauses reviewed by a qualified Austrian legal professional before putting them into store listings.

The app operators' existing live GitHub Pages policies were **not modified** and these drafts should not be represented to users as replacing them until cleared.
