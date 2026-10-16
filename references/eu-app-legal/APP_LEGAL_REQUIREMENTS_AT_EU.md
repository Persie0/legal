# Austrian & EU legal requirements for published mobile and desktop apps

**Research date:** 16 October 2026 · **Scope:** Austrian commercial app developer distributing to users in Austria/EU via Google Play and Apple App Store.  
**Status:** Legal implementation guide, **not legal advice** or a certification of any individual app. Source material is linked below. Check the laws and contracts for the actual publisher and transaction model.

This document distinguishes **Austrian/EU legal obligations**, **platform policies**, and **recommended contract/document structure**. A published app does not need a separately authored EULA merely because it is an app, but it needs truthful store privacy disclosures and the legally applicable operator information, and it may need additional notices/consent and consumer-law disclosures.

## 1. Minimum document and action matrix

| Component | All apps? | Why and implementation |
| --- | --- | --- |
| **Privacy policy / Datenschutzerklärung** | **Yes under Google Play and Apple App Store rules**, including offline apps | Public, working, non-PDF and non-geofenced URL for Google Play, also discoverable inside app. Apple requires privacy policy URL and access within app. Actual GDPR scope depends on personal-data processing. [Google](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en-GB) · [Apple](https://developer.apple.com/app-store/review/guidelines/de/). |
| **Impressum / provider identification (ECG §5 + GewO/UGB where applicable)** | **Generally yes for a commercial Austrian app/information-society service** | Easily/directly accessible legal page; sole-trader fields depend on legal status, registered address, UID, chamber and trade. [WKO](https://www.wko.at/internetrecht/informationspflichten-nach-dem-e-commerce-gesetz--dem-unte). |
| **MedienG §25 Offenlegung** | When the app/site qualifies as a periodic electronic medium | Assess each associated website/content service. The requirements are not the same as ECG provider identification. [Austrian government](https://www.usp.gv.at/themen/brancheninformationen/information-und-kommunikation/offenlegungspflicht-gemaess-para-25-mediengesetz.html). |
| **Terms of service / AGB** | **No general obligation to create AGB** | Strongly advisable for accounts, user uploads, subscriptions and hosted services. If you use them, make them accessible, downloadable/storable and incorporate them validly before contract conclusion. [WKO ECG](https://www.wko.at/internetrecht/informationspflichten-nach-dem-e-commerce-gesetz--dem-unte). |
| **Custom EULA** | **Optional** in many cases | Apple automatically supplies its [standard EULA](https://www.apple.com/legal/internet-services/itunes/dev/stdeula/) if none is filed; other platforms/contexts may be different. A custom EULA must respect mandatory consumer protection. [Apple App Store Connect](https://developer.apple.com/help/app-store-connect/manage-app-information/provide-a-custom-license-agreement). |
| **Consumer contract, price, subscription/trial information** | **Where a covered paid/digital service or consumer contract is offered** | Features, tax-inclusive charges, trial length, renewal price, duration, cancellation, withdrawal/refund/guarantee rights and support must be made clear **before commitment**. [WKO 2026 FAGG](https://www.wko.at/internetrecht/webshops-die-wesentlichen-bestimmungen-verbraucherrechte). |
| **§13a FAGG online withdrawal function** | **Where the Austrian rule applies to a covered distance contract and a withdrawal right exists** | Effective **1 October 2026** for contracts entered after 30 September 2026; accessible labelled **“Vertrag widerrufen”** online function during the withdrawal period. Apple/Google IAP merchant/contracting-party responsibility must be legally checked; don't assume a store's cancel-subscription feature fulfils this automatically. [RIS §13a](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20008847&Paragraf=13a). |
| **Advertising consent / device access notices** | **If applicable** | Nonessential device storage/access and tracking/advertising may require consent under **§165(3) TKG 2021**, GDPR and store policy; provide applicable granular choice/withdrawal, and ATT on iOS where required. No bundled “EULA accepted = tracking consent”. [WKO](https://www.wko.at/noe/e-commerce/faq-19-cookies) · [Apple ATT](https://developer.apple.com/app-store/user-privacy-and-data-use/). |
| **Data safety (Google) and App Privacy (Apple)** | **Yes for distributed apps** | Describe direct and **SDK** data flows accurately. Google's declarations aggregate currently distributed versions per package; Apple captures data collected via third parties. [Google](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en) · [Apple](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy). |
| **Account deletion** | **Apps that offer account creation** | Apple: easy initiation in-app; Google: in-app deletion pathway **and** a functional deletion-request web URL. Delete associated data subject to lawful retention; distinguish deletion from deactivation. [Apple](https://developer.apple.com/support/offering-account-deletion-in-your-app/) · [Google](https://support.google.com/googleplay/android-developer/answer/13327111?hl=en). |
| **EU trader identification (DSA/App Store)** | **If acting as a trader on Apple's EU store** | Apple requires trader status and verification; displayable address/phone/email. Paid, ad-supported and business apps generally warrant reviewing trader classification; do not claim a hobby exemption without assessment. [Apple](https://developer.apple.com/help/app-store-connect/manage-compliance-information/manage-european-union-digital-services-act-trader-requirements). |
| **Barrierefreiheit / BaFG** | **For certain services; exemption may apply** | From 28 June 2025, applies to covered consumer e-commerce services and some mobile applications; **microenterprise service providers** can be exempt, but other accessibility/discrimination law may still apply. [WKO](https://www.wko.at/internetrecht/barrierefreiheitsgesetz-e-commerce). |

**Important 2026 correction for old Austrian templates:** EU Online Dispute Resolution (OS-/ODR-) platform shut down and its regulation was repealed effective **20 July 2025**. **Remove the obsolete mandatory ODR platform link.** Some Austrian AStG dispute-resolution notices continue to apply where relevant. [WKO](https://www.wko.at/internetrecht/alternative-streitbeilegung).

## 2. Recommended structure: privacy policy for *each app*

A separate URL per app (or a clearly segmented per-app page) is strongly recommended, even if many portions come from a shared verified base. Do **not** copy a competitor's policy, use generic SDK text without auditing your app, or claim *“no data collected”* when SDKs send identifiers, diagnostics or network requests.

Use these headings **in a straightforward, understandable language**:

1. **Title, app names and version/date.** Identify exact supported Android/iOS/macOS app or package IDs, last updated date, and country/language coverage.
2. **Controller and contact.** Legal name of responsible Austrian operator, business/service address and actual privacy contact. List a DPO **only if appointed/required**.
3. **At a glance.** Explain core local processing, if files/photos/audio remain on device, optional clouds, ad/diagnostic services, and whether an account is needed. Avoid unverified zero-data assertions.
4. **Data processing table** — **each purpose separately**. Columns: data category/source; purpose; lawful basis under GDPR Art 6 (and Art 9 exception where needed); recipients/processor; retention/deletion; whether optional; cross-border transfer.
5. **Local processing and device permissions.** File picker, photo library, camera/face mesh, microphone, precise/background location, notifications, app-list scanning, storage, clipboard and accessibility access **only when actually used**.
6. **Cloud login/sync.** Google Sign-In, Google Drive appData, iCloud, Microsoft, Firebase Auth, your Oracle backend, and whether backups are encrypted. Explain user-controlled enable/disable and erasure.
7. **Purchases and subscriptions.** RevenueCat/customer identifiers, App Store/Play billing, receipts and subscription status. Clarify who is responsible for billing/receipts.
8. **Ads, tracking, consent.** Appodeal, each actively included mediation partner, IAB/consent mechanism, ATT, identifiers, consent revocation, and how non-personalized ads differ. **The mediation adapter tree alone is not proof a network receives data.**
9. **Crash reports and diagnostics.** State whether the actual build sends events to **self-hosted GlitchTip, hosted Sentry.io or neither**, with data categories, event scrubbing, retention and actual hosting; logs may have IP-level transport metadata regardless of event scrubbing.
10. **Optional AI and external APIs.** Which prompts/media reach Gemini/OpenAI, whether BYOK, provider country, metadata and data retention; OpenWeather coordinate queries; map tiles and RSS sources.
11. **Retention and deletion.** Give **real retention durations or meaningful criteria**, not invented “30 days”; include local app removal, cloud account deletion, hosted logs, backups and legal retention exceptions.
12. **Recipients and third-country transfers.** Countries, safeguards and contacts; do not treat a US provider's privacy-policy link alone as a lawful transfer mechanism.
13. **User rights.** Access, rectification, deletion, restriction, portability (where relevant), objection, consent withdrawal; request/contact channels and the right to complain to the [Austrian Data Protection Authority](https://dsb.gv.at/) or another competent supervisory authority.
14. **Automated decisions and children, if relevant.** If GDPR Article 22 decisions occur, include the required information. Explain applicable age limitations where relevant rather than using arbitrary age rules.
15. **Policy changes.** How material changes will be communicated, revision date and archival/version process.

**Legal foundation:** [GDPR Articles 12–14](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679), the [EDPB guidance on privacy by design and transparency](https://www.edpb.europa.eu/sites/default/files/files/file1/edpb_guidelines_201904_dataprotection_by_design_and_by_default_v2.0_en.pdf), [Google policy](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en-GB), [Apple Guideline 5.1.1](https://developer.apple.com/app-store/review/guidelines/de/).

### How to write data-flow paragraphs (examples, adapt only after verification)

**On-device photo/audio processing:**  
> Die von Ihnen zur Bearbeitung ausgewählten Bilder bzw. Audioaufnahmen werden grundsätzlich auf Ihrem Gerät verarbeitet. Eine Übermittlung der Originaldateien an unsere Server findet für diese Funktion nicht statt. Von Ihnen ausdrücklich gewählte Teilen-, Cloud- oder Exportfunktionen sowie getrennte Diagnose-/Werbedienste können andere Datenübermittlungen auslösen; diese werden nachstehend beschrieben.

Use this language **only if runtime evidence confirms no media upload**. Note that an encrypted model file downloaded by the app is not equivalent to uploading a user image.

**Self-hosted error diagnostics:**  
> Zur Erkennung von Programmfehlern nutzen wir eine selbst betriebene GlitchTip-Installation. Dabei können je nach Fehler und App-Version technische Informationen wie App-Version, Fehlerart, Stacktrace und Geräte-/Systemmerkmale übertragen werden. Informationen zum Hosting, zu den konkreten Feldern und zu den Löschfristen finden Sie unten.

Fill in and validate the hosting destination, network/HTTP logs, scrubber behavior, lawful basis and durations before use.

**Subscriptions:**  
> Beim Kauf einer Pro-Version verarbeitet der jeweilige App-Store Ihre Zahlung. Zur Prüfung des erworbenen Zugangs verwenden wir RevenueCat, das hierfür kaufbezogene Kennungen, Produkt- und Berechtigungsinformationen erhalten kann. Die konkreten Empfänger, Zwecke, Aufbewahrungsfristen und Rechtsgrundlagen erläutern wir in der folgenden Tabelle.

**Location/weather:**  
> Nach Ihrer Standortfreigabe verwenden wir Ihren Standort für die ausgewählte Standortfunktion. Wenn Sie Wetter- oder UV-Daten abrufen, können Koordinaten und technische Anfrageinformationen an den Wetterdienst übermittelt werden.

State actual OpenWeather endpoint and whether position history is saved for Vitamin D Tracker; do not use this generic paragraph when the app also uploads location to other services.

These are **illustrative drafting examples**, **not automatically compliant final clauses**.

## 3. Recommended structure: Impressum for an Austrian sole trader

For a **non-registered sole trader** operating an Austrian commercial app, use a single central webpage and link it prominently from every app. Confirm mandatory items against your legal status; do not invent business registration numbers or a fake office:

```text
Impressum / Anbieterkennzeichnung

Diensteanbieter:
[Vollständiger Vor- und Nachname]

Geschäftsanschrift / ladungsfähige Anschrift:
[Tatsächliche rechtlich geeignete Anschrift]
[PLZ, Ort, Österreich]

Kontakt:
E-Mail: [aktive E-Mail-Adresse]
Telefon: [erreichbare Telefonnummer]  [ggf. weitere Kontaktmöglichkeit]

Unternehmensgegenstand / Tätigkeit:
[etwa Entwicklung und Vertrieb von Software und mobilen Anwendungen]

UID-Nummer: [ATU..., sofern vorhanden]

Mitglied der Wirtschaftskammer: [zutreffende Landeskammer und ggf. Fachgruppe]
Gewerbebehörde / Aufsichtsbehörde: [zutreffende Behörde, falls einschlägig]
Gewerberechtliche Vorschriften: [zutreffende Normen, z.B. GewO und RIS-Link]

Medieninhaber / Offenlegung nach § 25 MedienG, soweit anwendbar:
[Name, Wohnort, Unternehmensgegenstand, ggf. zusätzliche Angaben]
```

**Do not assume a PO box alone fulfills the ECG requirement for a physically serviceable address.** Consider a legitimate business/service address for privacy, but confirm it is legally accepted. Existing UID, chamber and trade details must be correct. If entered into Firmenbuch, the §14 UGB items also differ.

Sources: [WKO §5 ECG detail including fields](https://www.wko.at/internetrecht/informationspflichten-nach-dem-e-commerce-gesetz--dem-unte); [WKO non-Firmenbuch sole-trader example](https://www.wko.at/internetrecht/website-impressum-nicht-im-firmenbuch); [Austrian media disclosure](https://www.usp.gv.at/themen/brancheninformationen/information-und-kommunikation/offenlegungspflicht-gemaess-para-25-mediengesetz.html).

## 4. Recommended structure: terms / EULA / subscriptions

**Terms / Nutzungsbedingungen** (only the applicable provisions, not an oversized universal document):

1. Operator, apps covered and contract formation/platform billing parties.
2. Scope of service, free/Pro restrictions, device/platform compatibility and updates.
3. Account creation, data export, account deletion and optional cloud sync if supported.
4. Licence for software, third-party/open-source credits, ownership of the user's own media and content.
5. User responsibilities (especially uploaded/social/public content), content rules and any lawful moderation/removal processes.
6. Subscription: actual period, trial eligibility/length, **price after trial**, auto-renewal, cancellation path, refund/withdrawal rights, restoration and purchases across platforms.
7. Availability and reasonable discontinuation/update provisions. Do not disclaim mandatory statutory quality/consumer rights.
8. Liability only within lawful limits; never blanket-exclude gross negligence, mandatory product liability or consumer guarantees.
9. Contract duration, termination, complaint/support contact, mandatory applicable consumer law and dispute mechanisms.
10. Date/version, changes and notification procedure.

**Custom Apple EULA:** Unless you need additional licensing terms, using the standard Apple agreement may be simpler; do not create a bespoke EULA solely for the sake of showing an acceptance checkbox.

**Pre-purchase UI:** Put the price, renewal rate, interval and trial length near the buy button. Links to full terms, privacy, manage subscription and restore purchase are good UX, but are not substitutes for mandatory pre-contract information or a covered §13a withdrawal mechanism.

**No blanket “no refunds” clauses:** Austrian/EU statutory withdrawal and warranty rules cannot simply be eliminated by an EULA. For directly supplied digital content, the circumstances in which a withdrawal right is lost have specific conditions, including explicit agreement and confirmation. Apple/Google may act as merchants of record for particular store transactions; assess who owes which disclosure before writing the clause.

Sources: [WKO FAGG 2026](https://www.wko.at/internetrecht/webshops-die-wesentlichen-bestimmungen-verbraucherrechte); [WKO digital downloads](https://www.wko.at/internetrecht/ruecktrittsrecht-bei-downloads-b2c); [RIS §13a](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20008847&Paragraf=13a); [Apple standard EULA](https://developer.apple.com/help/app-store-connect/manage-app-information/provide-a-custom-license-agreement).

## 5. Feature-based requirements for the current app inventory

| Your app group | Priority additions beyond common legal pages |
| --- | --- |
| **Apps using Appodeal** — Noise Remover, Image Upscaler, Fake Location, Root Detection, Memory Palace, Surebets, 3D Face and others | Ad identifiers, consent/withdrawal, precise active network list, international transfer, iOS ATT, Google Data safety + Apple App Privacy, SDK disclosures. Do not combine consent with mandatory EULA acceptance or demand ATT approval for core features. |
| **Apps using RevenueCat / Pro subscriptions** — same plus Audiobooster, Vitamin D Tracker, HanziHero, Photo Print Size Editor, Resistor Scanner and others | Store purchases, RevenueCat entitlement data, trial → recurring price, cancellation, restore, statutory consumer rights, assess **new §13a FAGG**. |
| **GlitchTip / hosted Sentry diagnostic apps** | Use per-app **actual DSN destination**, collected event types, scrubbing, IP/network metadata, storage duration, hosted vs self-hosted explanation; never label Memory Palace “Sentry.io” if its latest build uses GlitchTip. |
| **Camera/media/ML** — 3D Face Model Maker, Resistor Scanner, Noise Remover, PureMic, Photo Print Size Editor, image/video upscalers | Local file access vs upload, face geometry handling, permission explanations, temporary/cache/export storage and media deletion. Biometric Art 9 category applies **if processed to uniquely identify** someone, not automatically to every face mesh. |
| **Health/wellness** — Vitamin D Tracker | Health-data processing can require an **Article 9(2) exception** (often explicit consent) **in addition** to Article 6; location/open-weather requests, optional Drive backups and retention. [DSB](https://dsb.gv.at/faqs/besondere-datenkategorien). |
| **Location/maps** — Toilet Compass, Fake Location Detector, NomadRank, Vitamin D Tracker | GPS accuracy/foreground-background distinction, map-tile service/coordinates, user choice, location history/cloud account; extra Play forms if background location used. |
| **Accounts/social** — NomadRank, optional sync accounts | Clearly explain identity provider, server-side data, sharing with friends, user-generated posts, download/export and both Apple/Google account-deletion paths. Any public/community content may create additional DSA content-moderation obligations depending on service role. |
| **AI/text/RSS/translation** — Pareader, NomadRank, MoWa | User-entered prompts, article content, external websites/providers, optional user API key and third-party data handling, copyright. |
| **University/calendar** — UniMinder | Microsoft/TU authentication/refresh tokens, events/appointments, secure credential retention and data exports. |
| **Mostly offline apps** — Neon Snake, QR Code Tools, DoubleTapKing, Secret Audio Messages | Still publish a clear app-specific store privacy policy and ECG operator identification. Avoid fake claims of *“no data collected”* when the final binary reports crash data, uses platform payments or contacts a server. |

## 6. In-app information architecture

Use a simple **Settings → Legal & Privacy** section:

- **Privacy policy** — always reachable, including before login/paywall; open a publicly hosted page with app-specific sections.
- **Impressum** — common central publisher page, clearly accessible from the app and website.
- **Terms of use** — show if used; app-specific sections and effective date; make contract terms savable/printable.
- **Open-source licences** — provide credit/notices where dependency licences require them.
- **Privacy choices / advertising consent** — show when relevant; re-open consent/withdrawal flow and honor ATT/device preferences.
- **Manage subscription / Restore purchases** — only for subscription/purchase apps.
- **Delete account and data / Export data** — for account apps; Google also needs a functional external deletion-request URL.
- **Contact support** — operational email plus app-specific context.

**Onboarding:** Showing legal links is not the same as lawful opt-in. Do not demand consent to *optional* analytics/ads as an inseparable condition of accepting the licence. Provide just-in-time permission rationale before camera/location/microphone access. For users under 18 or children-targeted apps, review relevant age/parental requirements.

**Language:** GDPR requires clear and intelligible wording; for Austria, German is the safest default for Austrian consumer-facing legal pages. Offer accurate translations where marketing/contracting with consumers in other languages/markets requires intelligibility. Do not publish machine translations that reverse material legal meaning.

## 7. What is still not established from code/reference links alone

- Actual **release-binary** network traffic, permission declarations and which Appodeal mediation partners initialize.
- GlitchTip/Sentry retention, hosting, IP logging, data-processing agreements and cross-border transfers.
- Your actual Austrian business address, formal Gewerbe/WKO category, registered status and complete required Impressum fields.
- Which Apple/Google IAP flows have you as the contractual party for **§13a FAGG** and what the platform already handles.
- Real per-app publication state: privacy URL entered in store, correctly linked in app, Google Data safety/Apple labels, account deletion, accessibility/trader status.
- Specific legal status of health, biometric, and social/user-content features.

## 8. Primary legal and platform sources (read before final publication)

1. [GDPR / DSGVO (EU Regulation 2016/679)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679).
2. [WKO: §5 ECG general information duties for apps](https://www.wko.at/internetrecht/informationspflichten-nach-dem-e-commerce-gesetz--dem-unte).
3. [WKO: Austrian sole-trader Impressum](https://www.wko.at/internetrecht/website-impressum-nicht-im-firmenbuch).
4. [Austrian government: MedienG §25](https://www.usp.gv.at/themen/brancheninformationen/information-und-kommunikation/offenlegungspflicht-gemaess-para-25-mediengesetz.html).
5. [WKO: FAGG 2026 paid online contracts](https://www.wko.at/internetrecht/webshops-die-wesentlichen-bestimmungen-verbraucherrechte).
6. [RIS: §13a FAGG (effective 1 October 2026)](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20008847&Paragraf=13a).
7. [WKO: §165(3) TKG 2021 and cookie/device access](https://www.wko.at/noe/e-commerce/faq-19-cookies).
8. [Austrian DSB: Article 9 special data](https://dsb.gv.at/faqs/besondere-datenkategorien).
9. [WKO: BaFG accessibility](https://www.wko.at/internetrecht/barrierefreiheitsgesetz-e-commerce).
10. [WKO: ODR platform abolished](https://www.wko.at/internetrecht/alternative-streitbeilegung).
11. [Google Play user data + privacy](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en-GB).
12. [Google Play data safety](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en).
13. [Google Play account deletion](https://support.google.com/googleplay/android-developer/answer/13327111?hl=en).
14. [Apple App Review Guidelines §5.1.1](https://developer.apple.com/app-store/review/guidelines/de/).
15. [Apple App Privacy](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy).
16. [Apple default EULA vs custom](https://developer.apple.com/help/app-store-connect/manage-app-information/provide-a-custom-license-agreement).
17. [Apple EU DSA trader declarations](https://developer.apple.com/help/app-store-connect/manage-compliance-information/manage-european-union-digital-services-act-trader-requirements).

For **examples of actual Austrian/EU publisher documents**, see [README.md](README.md). For the exact integrations found in the latest app repositories, see [SERVICE_COVERAGE.md](SERVICE_COVERAGE.md) and [SERVICES_AND_DATA.md](../../SERVICES_AND_DATA.md).
