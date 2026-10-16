# Austrian and EU mobile-app legal references

Curated **primary-source legal documents and store listings**, checked **16 October 2026**, for comparing privacy policies, EULAs, usage terms, subscriptions, advertising disclosures and related consumer information.

**Scope:** 5 Austria-based app publishers, 3 more EU-based publishers, plus Apple's standard App Store EULA. These are research references, **not legal templates** and not evidence that the same terms suit your apps. Publisher documents remain on the original sites; their copyrighted text is **not copied here**.

## Austria first

| App / publisher | Official store listing | Privacy policy | Terms / EULA | Useful for |
| --- | --- | --- | --- | --- |
| **ÖAMTC** · AT | [iOS](https://apps.apple.com/at/app/%C3%B6amtc/id329772634) · [Android](https://play.google.com/store/apps/details?id=at.oeamtc.android) | [ÖAMTC App privacy](https://www.oeamtc.at/mitgliedschaft/leistungen/datenschutzerklaerung-oeamtc-app-28493389) | [App terms](https://www.oeamtc.at/mitgliedschaft/leistungen/nutzungsbedingungen-oeamtc-app-28489530) | GPS/location, analytics, consumer rights, permissions |
| **bergfex: Wandern & Tracking** · AT | [iOS](https://apps.apple.com/at/app/bergfex-wandern-tracking/id912776148) · [Android](https://play.google.com/store/apps/details?id=com.bergfex.tour) | [bergfex privacy](https://www.bergfex.at/c/datenschutz/) | [bergfex AGB](https://www.bergfex.at/c/agb/) | Location tracking, advertising, subscriptions, fitness-related features |
| **willhaben** · AT | [iOS](https://apps.apple.com/at/app/willhaben/id660325616) · [Android](https://play.google.com/store/apps/details?id=at.willhaben) | [willhaben privacy](https://www.willhaben.at/iad/datenschutzerklaerung) | [willhaben AGB](https://www.willhaben.at/iad/agb) | Advertising, user-generated content, account deletion, payments |
| **Bitpanda** · AT | [iOS](https://apps.apple.com/at/app/bitpanda-krypto-aktien-etf/id1449018960) | [Group privacy notice](https://www.bitpanda.com/de/legal/bitpanda-group-privacy-notice) | [User-agreement versions](https://www.bitpanda.com/de/legal/user-agreement) | Complex processor/data-category notices, security, account and financial data |
| **wegfinder** · AT | [iOS](https://apps.apple.com/at/app/wegfinder/id680580267) | [wegfinder privacy](https://wegfinder.at/datenschutz/) | [wegfinder AGB](https://wegfinder.at/agb/) | Location, mobility data, external partners, payments, archived versions |

## Other EU publishers

| App / publisher | Official store listing | Privacy policy | Terms / EULA | Useful for |
| --- | --- | --- | --- | --- |
| **Photoroom** · France | [iOS](https://apps.apple.com/at/app/photoroom-ki-foto-editor/id1455009060) · [Android](https://play.google.com/store/apps/details?id=com.photoroom.app) | [Privacy](https://www.photoroom.com/legal/privacy) | [Terms and conditions](https://www.photoroom.com/legal/terms-and-conditions) | AI image processing, uploads, user content, subscriptions |
| **YAZIO** · Germany | [iOS](https://apps.apple.com/at/app/yazio-kalorien-z%C3%A4hler-di%C3%A4t/id946099227) · [Android](https://play.google.com/store/apps/details?id=com.yazio.android) | [Combined terms, withdrawal, privacy](https://help.yazio.com/hc/de/articles/203444951-Nutzungsbedingungen-Datenschutzerkl%C3%A4rung) | [Same document](https://help.yazio.com/hc/de/articles/203444951-Nutzungsbedingungen-Datenschutzerkl%C3%A4rung) | Health-related data, advertising, subscription/consumer rights |
| **Freeletics** · Germany | [iOS](https://apps.apple.com/at/app/freeletics-hiit-fitness-coach/id654810212) | [Freeletics privacy](https://www.freeletics.com/de/pages/privacy/) | Not added (unverified) | Workout data, analytics, behavioral tracking, health/fitness |

## Platform baseline (not an app publisher)

**[Apple standard Licensed Application EULA](https://www.apple.com/legal/internet-services/itunes/dev/stdeula/)** — compare with the requirements for a custom EULA. Apple's [developer help](https://developer.apple.com/help/app-store-connect/manage-app-information/provide-a-custom-license-agreement) explains that the standard EULA applies if a custom one is not supplied.

## Versions visible when checked

| Document | Version printed by publisher |
| --- | --- |
| willhaben privacy | September 2026 |
| willhaben AGB | 30 September 2026 |
| Bitpanda group privacy notice | July 2026 |
| wegfinder privacy | 2025 |
| wegfinder AGB | Effective 1 July 2025 for new users |
| Photoroom privacy | March 2026 |
| Photoroom terms | Effective 29 July 2026 |

No version is inferred when a document does not clearly print one. Source versions may change without the URL changing.

## Change monitoring

- [`sources.json`](sources.json) — registry of publisher, jurisdiction, store listings, document URL, subject, observed version and monitoring status.
- [`check.py`](check.py) — an **opt-in** Python 3 checker using only the standard library. It reads publisher legal pages into memory, hashes normalized visible text and stores **only hashes, sizes and change timestamps**, never the text.
- [`fingerprints.json`](fingerprints.json) — repository's current known hashes. **Empty until the first successful permitted check**; the initial fetch sets a baseline, not a claim that a change occurred.
- **Manual-only:** willhaben, due to published limitations on automated copying/crawling. It stays linked but is never fetched by the checker.
- The checker honors `robots.txt`; blocked/unavailable/JavaScript-only pages remain flagged for **manual review**. A skipped page is **not** treated as unchanged. Automatic checks are best-effort; look at workflow logs for errors.
- GitHub Actions, when configured, lives in the **public [Persie0/Playground](https://github.com/Persie0/Playground)** repository, not here. It runs at most weekly and proposes fingerprint changes for review. It uses the first available of `secrets.PRIVATE_REPO_TOKEN || secrets.GH_TOKEN || secrets.GH_RELEASE_TOKEN` and needs permission to create branches and pull requests in `Persie0/legal`.

Run locally to inspect:

```bash
python3 references/eu-app-legal/check.py
```

Run locally to update baseline/fingerprints:

```bash
python3 references/eu-app-legal/check.py --update
```

**Important limitations:** Web terms can change their layout without changing legal provisions (false positives); a stable hash cannot prove that there were no legally significant changes (false negatives), especially when sites are blocked. Store privacy nutrition labels and Google Play Data safety are **developer-supplied** disclosures and should be checked against your own real data flows, not copied. This catalog does not replace an Austrian/EU legal review.

## Questions to compare for each of your apps

Check the controller's identity/contact, legal bases and purposes per data category, processor/service recipients (including Appodeal mediation and RevenueCat), international transfers, storage/retention, rights and deletion instructions, advertising consent/ATT, sensitive location/health data, subscriptions/renewal/cancellation/refunds, consumer-law withdrawal clauses, accessibility and language requirements.

The audit of *your own* integrations is in [SERVICES_AND_DATA.md](../../SERVICES_AND_DATA.md); the released-app catalog is [README.md](../../README.md).
