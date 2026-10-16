# Legal documents needed per app — requirements-only matrix

**Scope date:** 16 October 2026  
**Basis:** app names and apparent product purposes from [released-app inventory](../../README.md) (31 Android production titles + 1 additional macOS title).  
**Method:** **NO audit of current app implementation, privacy screens, GitHub source code or store metadata.** Every row says what the app **should have if it performs the named feature**, not what is currently installed, compliant or missing. iOS releases of the same titles use the corresponding Apple rules as well.

**Interpretation:** This is a practical Austrian/EU publisher checklist, not individual legal advice. “If” and “where applicable” are important: feature names alone cannot determine active SDKs, processors, medical-device status, licensing or merchant-of-record arrangements.

## A. Minimum legal package for every published app

| Item | Who supplies it? | Minimum practical action |
| --- | --- | --- |
| **App-specific privacy policy** | **You** | Public, readable, stable webpage (each app named); links in app + store listing; accurate processing/recipients, legal bases where GDPR applies, retention, rights, contact, deletion. Still required by **both stores even for offline/no-data apps**. [Google User Data](https://support.google.com/googleplay/android-developer/answer/10144311), [Apple 5.1.1](https://developer.apple.com/app-store/review/guidelines/). |
| **Austrian provider identification (Impressum, § 5 ECG)** | **You** | One legally correct central page can be reused by all apps; clear in-app/web link. Name, serviceable business address, email/direct contact, UID if held, chamber/trade/supervision details where applicable. Apple's DSA trader contact display is not a complete substitute. [WKO ECG](https://www.wko.at/internetrecht/informationspflichten-nach-dem-e-commerce-gesetz--dem-unte). |
| **Google Play Data safety** | **You complete; Google displays** | For every Android app, including offline apps: data collection/sharing, SDK data, encryption in transit, retention/deletion and any account deletion URL. [Google](https://support.google.com/googleplay/android-developer/answer/10787469). |
| **Google Play Health apps declaration** | **You complete; Google records** | Every published Play app completes it; apps without health features select **no health features**. A real health app declares its categories and meets further requirements. [Google](https://support.google.com/googleplay/android-developer/answer/14738291). |
| **Apple App Privacy labels and privacy URL** | **You complete; Apple displays** | For all iOS/macOS App Store apps, account for collection by you **and third-party SDKs**; publish privacy URL. [Apple](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy). |
| **App Store EULA** | **Apple provides its standard EULA** | Custom EULA is optional if standard terms suffice. On Google Play there is no equivalent requirement to author a custom EULA for every app. [Apple](https://developer.apple.com/help/app-store-connect/manage-app-information/provide-a-custom-license-agreement). |
| **App content / age declarations; required permission explanations** | **You** | Accurately complete target audience, age rating and feature-related forms. Clear just-in-time reason for permissions, and privacy notice describing access. |
| **Support contact & privacy-rights contact** | **You** | Valid support/privacy contact (can be the same responsible inbox), user deletion/access requests where GDPR applies and applicable statutory complaint information. |
| **DSA trader information for App Store EU distribution** | **You submit; Apple verifies/displays** | If a trader (including commercial sole trader), verify public contact details. This does not replace your Austrian ECG notice. [Apple](https://developer.apple.com/help/app-store-connect/manage-compliance-information/manage-european-union-digital-services-act-trader-requirements). |

**No blanket requirement to show a first-launch "accept the EULA" screen.** Privacy-policy access is required by the stores; consent is required only for processing that legally requires it. A privacy notice or EULA acceptance is not consent to personalized advertising or sensitive data processing.

## B. What the platforms and SDKs cover versus what you must do

| Area | Already handled by store / Appodeal / RevenueCat | Still the app publisher's task |
| --- | --- | --- |
| **EULA** | Apple automatically applies [standard licence](https://www.apple.com/legal/internet-services/itunes/dev/stdeula/) in App Store unless replaced. | Extra terms **only if actually needed** (accounts, community, service limitations, recurring online services). Clear contract incorporation; don't override mandatory consumer rights. |
| **App/store privacy information** | App Store and Play display your privacy URL and supplied privacy/data-safety summaries. | Author a truthful **app-specific** policy, update store declarations, list processors and permissions, retention and actual data flows. Neither store writes your GDPR notice. |
| **Advertising consent** | Appodeal's [Stack Consent Manager](https://docs.appodeal.com/android/data-protection/gdpr-and-ccpa) can display IAB TCF advertising consent and communicate the ad signal; Google lists **Appodeal Inc CMP (ID 432)** as certified for apps. | Configure/show CMP before nonessential advertising processing, provide a persistent way to revisit/withdraw, respect refusal, monitor enabled mediation partners. Handle Apple's **ATT** where tracking occurs; a CMP is not a substitute for ATT or your privacy policy. [Google CMP listing](https://support.google.com/admob/answer/13554116), [Appodeal iOS ATT](https://docs.appodeal.com/ios/data-protection/app-tracking-transparency). |
| **What Appodeal discloses** | Appodeal supplies its **own SDK** data-safety and App Privacy tables. | Assess **every active mediation/ad-network partner** and any non-ad SDKs; Apple and Google hold **you** responsible for the aggregate app declarations. [Android](https://docs.appodeal.com/android/data-protection/app-privacy-details), [iOS](https://docs.appodeal.com/ios/data-protection/app-privacy-details). |
| **Store purchases/renewals** | Apple StoreKit & Play Billing process native store checkout, recurring charges, store purchase histories and usual store cancellation/refund paths. RevenueCat (if used) verifies receipts and reports entitlement status. | Truthful paywall: plan name, duration, full renewal price and currency, trial duration, renewal/cancellation, upgrade/restore path and availability of free features. Link relevant privacy/terms. **RevenueCat is not the merchant of record for native App Store/Play purchases.** [RevenueCat responsibilities](https://www.revenuecat.com/docs/platform-resources/implementation-responsibilities). |
| **Subscription-management link** | Apple/Google provide pages for users to cancel **store-billed** subscriptions. | Surface an appropriate in-app link/access; Google explicitly requires an easy online cancellation method. Deleting an account **does not automatically cancel** a store subscription. [Google](https://support.google.com/googleplay/android-developer/answer/9900533), [Apple](https://developer.apple.com/support/offering-account-deletion-in-your-app/). |
| **Consumer withdrawal (Austria)** | Stores may handle withdrawal/refund for contracts **where they are the actual contractual counterparty**. | **§ 13a FAGG has applied in Austria since 1 October 2026** for covered contracts concluded via an online interface. Determine the actual seller/contractual structure and whether *you* must provide a visible withdrawal function; this is **not identical** to cancelling a recurring subscription. [RIS](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20008847&Paragraf=13a). |
| **Account sign-in** | Identity providers can authenticate users; Google/Apple account settings cover their own identity accounts. | Delete **your app's account and associated backend/user content** where required. Apple requires in-app initiation if app account creation exists; Google requires in-app **plus a functional web-based deletion request** for account-creating apps. [Apple](https://developer.apple.com/support/offering-account-deletion-in-your-app/), [Google](https://support.google.com/googleplay/android-developer/answer/13327111). |
| **Austrian ECG Impressum** | Apple may display DSA trader contact info; Play displays developer contacts. | Maintain the required operator imprint accessible for your own commercial service; do not assume store metadata contains all ECG mandatory fields. |
| **Privacy rights, records, cross-border transfers, sensitive data** | Each provider handles its own obligations and may offer contracts/documents. | You assess your processing legal bases, Art. 9 where relevant, user rights, retention, security, transfer safeguards, subprocessor oversight and breach response. |

## C. Trigger-based additional requirements

**Only add the relevant module(s):**

- **Advertising / rewarded ads**: GDPR/ePrivacy/TKG consent as applicable; functional Appodeal CMP and ad-partner information; ATT for iOS tracking; store ad declarations, child-directed restrictions; explain the effect of declining and any paywall/ad-based unlock mechanism.
- **Paid Pro / free trial / auto-renewable subscription**: localized price & interval, trial end and renewal price, cancellation and restoration, privacy/terms links, consumer rights/withdrawal analysis; use actual store product information rather than hardcoding invented fees.
- **Camera/photos/video/file import**: describe local vs server processing, temporary files, permission prompts, output retention and optional uploads; separate consent for optional training submissions where needed.
- **Microphone/background audio**: user-initiated recording, actual audio transfer/storage, background recording notice, export and cleanup; microphone purpose text.
- **Location/maps/network**: precise vs approximate location, permission necessity, retention/history, providers receiving coordinates, online maps and weather calls; extra rules if background location is used.
- **Health/biometric**: possible GDPR Art. 9 conditions, appropriate explicit consent when relied upon, data minimization and security, medical claims and Play Health declaration. A photo/face mesh is **not automatically** Article 9 biometric data unless it is processed to uniquely identify a person.
- **Accounts/cloud sharing/social**: identity/account data, security, backups, cloud-provider recipient, export and deletion, shared/public visibility; account deletion in-app (Apple), in-app + web (Play); consider DSA moderation if operating a hosting/community service.
- **AI/translations/RSS/website content**: destination and actual data sent (prompts, photos, URLs, articles), subprocessors, retention, user API keys and copyright/third-party notices; explain when an otherwise local feature calls the network.
- **Kids/teen-oriented games**: target-audience policies, ad SDK restrictions, age rating, data minimization.
- **Security/VPN-style functions**: permissions, device/network identifiers transmitted, claims and limitations; Android's VpnService-specific Play rules only if actually offering/using a VPN service.

## D. Per-app checklist: released Android titles

**Every row inherits section A** (app-specific public privacy policy + Austrian legal notice + Play Data safety + Health declaration + support/contact + accurate permissions/audience). The table covers obligations **by potential feature**, not claims that the app contains any particular SDK.

| App | What the app-specific legal notice needs to explain | Additional conditions |
| --- | --- | --- |
| **3D Face Model Maker** | Camera/face photos; 3D landmarks and meshes; where photos/models are stored, exported or uploaded; deletion; safety/accuracy of output. | If paid: purchase/trial terms. If ad-supported: CMP and ad disclosures. If face data is processed for **unique identification**, assess GDPR biometric Article 9; a face mesh is not automatically biometric identification. |
| **Arbitrage Betting Calculator** | Inputs such as odds/stakes and history; explain that results are mathematical calculations, not guaranteed profits or a betting service. | If linking to or promoting betting providers, assess gambling advertising, age and country restrictions; if paid/ads, apply those requirements. A calculator alone is not automatically a bookmaker. |
| **Background Noise Remover** | Microphone and file permissions; recording background behavior; whether source audio/video is processed locally or uploaded; temporary files, saved exports and deletion. | If Pro/trial, show precise free-feature restrictions and paid terms; if advertising, CMP/consent. Explain permissions needed for long processing/foreground notifications. |
| **Boost Phone Audio Volume** | Audio settings, microphone/system/audio permissions if used, whether audio content leaves the device; effects on hearing/device safety. | Prominent safety warning for excessive volume and limits; clear Pro/trial renewal terms if monetized; diagnostics disclosed if used. |
| **DoubleTapKing – Clicking Game** | Local touch/game scores, preferences and save state; say whether anything is transmitted or shared. | If aimed at children, comply with age-rating/families/child advertising rules; if truly offline/no data transferred, the privacy policy can say so accurately. |
| **EarnMeter: Work Motivator** | Time, pay/wage estimates and possibly employment records; distinguish local-only entries from cloud analytics or backups. | Explain that estimates are illustrative rather than payroll/tax advice; optional Pro/advertising rules only if such features are offered. |
| **Fake Location Detector** | Device/mock-location and GPS diagnostics; why location permission is needed; precision, local storage and transmission; device scanning. | For ads: consent and mediation-provider disclosures, especially if SDKs can access location. If paid/Pro, trial/purchase terms. |
| **Finger Chooser (+cheat mode)** | Multi-touch/finger selection rules, stored settings; whether fingers are merely touch points (not biometric fingerprint templates). | Child-directed audiences and age rating if applicable; if ads or telemetry are used, add separate disclosures rather than asserting no data. |
| **Image Upscaler Offline** | Selected images, on-device vs remote upscaling, model downloads, outputs/history, caches/cleanup, photo/camera permissions. | Ad-to-unlock/free-quota mechanics, rewarded-video choices and Pro terms **if offered**. Advertising consent is separate from photo access. |
| **Live Noise Cancellation Demo** | Real-time microphone audio processing, whether raw sound is transmitted/recorded, audio permissions and retention. | Avoid promises of hearing protection or guaranteed safety/noise isolation; if ads, provide ad/CMP and store disclosures. |
| **Memory Palace Training** | Learning/memory-palace progress; attached images; local database; optional account, export, synchronization and external learning integrations. | If Google Drive/cloud sync is offered: scopes, data classes, disable/delete. If ads/purchases: add CMP and subscription terms. Account deletion only if an actual app account is created. |
| **MoWa: Language Learning** | Text/words sent to external translation providers (if used), recipients, locale/content, retained translations/history. | Links to translator privacy terms and user notice at point of remote translation; if a text-only offline version is offered, distinguish it. |
| **Neon Snake** | Game state, local high scores and preferences; state whether network transfers exist. | Child-directed game category and suitable store audience declarations; ads/purchases only if enabled. |
| **NomadRank: Rate Visited Places** | Travel places, dates, coordinates, ratings, photos, profile, friends/groups and social visibility; account/server retention, exports and deletion. | Both stores' account-deletion routes if users create accounts. Sharing/audience defaults, content reporting/moderation and applicable DSA duties for hosted user content; AI import details if offered. |
| **Pareader: News & Languages** | RSS/article URL requests, third-party website cookies/IP, saved articles, reading/learning progress and any user-entered AI prompts. | Identify AI/translation providers and external-content/Anki flows when present; check content licensing/copyright and microphone permissions if spoken-word recording exists. |
| **Photo Print Size Editor** | Imported photos, print/PDF layout projects, filesystem/gallery permissions, autosave/history and exported files; local vs cloud processing. | If paid: in-app purchase/subscription cancellation or restoration. No special photo-consent banner purely for locally chosen file access. |
| **PureMic: Remove Recorder Noise** | Recording/microphone access, audio and imported files, local/noise-removal processing, playback/export/cache/deletion. | If Pro or ads: subscription/free-export limits, CMP and disclosures. Explain background recording and foreground-service notices if present. |
| **QR Code Tools (Offline)** | Camera scanning, decoded URLs/text, QR creation and local history; distinguish reading a code from opening its external URL. | If it claims offline: state exceptions for user-initiated website links/shares accurately. If storing scanned sensitive codes, describe retention. |
| **Recipe Price Calculator** | Ingredient recipes, quantities and prices, photo access if used, local history/export; no need to characterize non-uploaded recipes as a server collection. | If it gives cost estimates, explain assumptions/limitations; ads, accounts or purchases only if such functions are offered. |
| **Reduce Image Size – Compressor** | Photos, compress/crop results, local media permissions, saved outputs, image metadata handling and temporary files. | If one-time paid features or subscriptions, disclose product/renewal accurately; update privacy policy for any cloud compression if offered. |
| **Resistor Color Code Scanner** | Camera/photos, extracted color bands/scans and results; local model inference versus remote services. | If users can submit scan images for training/improvement, provide a **separate, specific optional upload choice** with retention/withdrawal explanation. Ads and Pro terms only where enabled. |
| **Resistor Finder** | Entered resistor colors/values, calculation history; whether any data is sent online. | Ads/consent and one-time purchases/Pro only if included; no camera/biometric disclosures when it is just a calculator. |
| **Root & Phone Mods Detection** | Device/root/integrity indicators examined, permissions, what results are stored or transmitted and security limitations. | Do not overstate security guarantees; if ads use identifier/device signals, disclose partners/CMP. Pro/paywall information if offered. |
| **Screenshot Detector** | Screenshot or screen-capture **events** versus screenshot image contents; system permissions and whether events/images are logged or transmitted. | If only detecting events, avoid falsely claiming screenshot images are uploaded. Separate disclosure if actual screen capture/recording is possible. |
| **Secret Audio Messages** | Recorded/imported audio, encoding/decoding, saved/temporary content, recipient/sharing flow and microphone permission. | If the app claims secrecy/encryption, precisely explain whether encryption is real and who can decode; external sharing is user-initiated where applicable. |
| **Selfie Diary** | Selfie photos, dates, journal notes, photo permissions, storage, backups/exports and deletion. | If automatic cloud backup or face analysis is added, give corresponding disclosures. If public sharing/account creation, add content visibility and account deletion. |
| **Toilet Compass: WC Finder** | Precise/approximate location, nearby toilet queries, map requests/tiles, downloaded datasets, history and external navigation. | Explain if coordinates stay local or reach map/weather/POI providers; location-permission rationale; optional offline mode and background location only if used. |
| **UniMinder – Uni Companion** | University logins/tokens, timetable/course data, calendar event import/export, notifications and external university pages. | Provider-specific authentication scope and secure session handling; if Outlook/calendar syncing exists, recipients and deletion. Do not imply TU Wien endorsement without authorization. |
| **Vitamin D Tracker** | Sun exposure, supplement/history, UV estimates, skin information, possible lab/blood-test records and location/weather requests. | **Highest sensitivity:** assess Art. 9 GDPR if health data is processed, explicit consent where relied on, optional Drive backup/security, in-app medical warnings, Play Health declaration; EU MDR if the intended use is medical. |
| **VPN & Proxy Detector** | IP/proxy/VPN detection information, network diagnostics, DNS/remote endpoint requests and any retained network identifiers. | If only a detector, do not claim it provides a VPN. If it creates a VPN tunnel or uses Android VpnService, apply the separate Google VpnService policy and prominent disclosures. |
| **Yoyillo: Learn Chinese Offline** | Vocabulary progress, repetition scores/settings and local/offline lessons; distinguish optional Google Drive/iCloud backup. | If Pro/subscription: actual billing/trial language. If sync enabled: account scope and deletion; avoid 'fully offline' if online purchases or optional backups still exist. |

## E. Additional Mac App Store release

A macOS app follows the **Apple App Privacy/URL, Apple standard EULA, DSA trader and Austrian provider rules** from sections A/B; it does not need Google Play declarations unless there is also an Android build.

| App | What its policy should explain | Additional conditions |
| --- | --- | --- |
| **Video Upscaler Offline (macOS)** | Input videos, audio tracks, thumbnail caches, saved output, access to selected files and whether media is ever uploaded. | Mac App Store App Privacy URL and accurate labels. StoreKit purchase/subscription terms and restoration if monetized; optional error reports and model download data if used. |

The corresponding iOS versions (when published) of the Android titles in section D additionally follow **Apple App Privacy labels, standard/custom EULA, subscription requirements and ATT if tracking occurs**. A single accurate **app-specific** privacy webpage may be reused across Android/iOS/macOS if platform-specific differences are clearly described.

## F. Smallest maintainable structure for your portfolio

**Shared across all apps:**
- `/impressum/`: one Austrian provider-identification page, linked from every app.
- `/privacy/<app-slug>/`: one accurate policy for each app, ideally built from shared factual modules and app-specific data tables.
- `/support/`: one accessible support and GDPR requests contact route.
- `/terms/`: a reusable *optional* terms page **only where you actually need terms**, with features/subscription details matched to each app.

**As-needed pages and in-app controls:**
- `/delete-account/`: only for apps creating an app account; ensure it genuinely handles the right app/backends and meets Google Play's web-path requirement.
- `/withdrawal/` or legally appropriate store route: only for covered contracts when you are responsible for the § 13a FAGG mechanism.
- Ad privacy preferences/CMP re-entry: only for apps with advertising.
- Pro subscription management/restoration: only for paid apps; add Apple/Play native store link depending on purchase platform.
- Open-source licence notices: for dependencies imposing attribution/notices; these are **licence-specific**, not dependent on a custom EULA.
- Medical/fitness warning/health consent: only when functionality/legal basis actually needs it.

**Avoid unnecessary paperwork:** A purely offline, free, non-ad-funded app does **not** need a home-grown “GDPR consent form”, a paid-subscription agreement, an account deletion page or a mandatory custom EULA. Its store policy URL, truthful no-off-device-data explanation, standard legal notice and required console disclosures still matter.

## G. Platform form checklist and common misconceptions

1. **Google Play:** privacy link (public non-PDF), Data safety (all apps including no collection), Health apps declaration (also 'no health features' for ordinary apps), age/content and any applicable ads/data deletion/permissions declarations.
2. **Apple:** privacy policy URL and App Privacy answers (including integrated SDKs), any ATT prompt where tracking occurs, permission-specific purpose strings, required EU trader status and correct purchase/terms links.
3. **Appodeal CMP:** **advertising consent only**. Its presence does not cover medical consent, cloud sync, GPS disclosure, publisher imprint, data deletion, EULA, all partner SDKs or store Data safety/App Privacy.
4. **RevenueCat:** receipt validation and entitlement state; not equivalent to user consent, account deletion, legal terms or an official refund/withdrawal mechanism for every possible contractual scenario.
5. **Store subscriptions:** subscription cancellation after renewal != statutory withdrawal of a new covered contract during the withdrawal window; seller allocation must be assessed.

## H. High-authority sources checked for this guide

- [Austrian WKO: §5 ECG information duties expressly applying to apps](https://www.wko.at/internetrecht/informationspflichten-nach-dem-e-commerce-gesetz--dem-unte)
- [Austria RIS: §13a FAGG in effect from 1 October 2026](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20008847&Paragraf=13a)
- [GDPR full regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679)
- [Apple: Privacy under App Review 5.1.1](https://developer.apple.com/app-store/review/guidelines/)
- [Apple: standard EULA unless custom](https://developer.apple.com/help/app-store-connect/manage-app-information/provide-a-custom-license-agreement)
- [Apple: App Privacy questionnaire](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy)
- [Apple: EU trader status](https://developer.apple.com/help/app-store-connect/manage-compliance-information/manage-european-union-digital-services-act-trader-requirements)
- [Apple: account deletion](https://developer.apple.com/support/offering-account-deletion-in-your-app/)
- [Apple: subscription signup requirements](https://developer.apple.com/app-store/subscriptions/)
- [Apple: ATT / tracking](https://developer.apple.com/app-store/user-privacy-and-data-use/)
- [Google Play: User Data / privacy policy](https://support.google.com/googleplay/android-developer/answer/10144311)
- [Google Play: Data safety](https://support.google.com/googleplay/android-developer/answer/10787469)
- [Google Play: Health declaration for all apps](https://support.google.com/googleplay/android-developer/answer/14738291)
- [Google Play: health/medical additional requirements](https://support.google.com/googleplay/android-developer/answer/16679511)
- [Google Play: account deletion](https://support.google.com/googleplay/android-developer/answer/13327111)
- [Google Play: subscription policy](https://support.google.com/googleplay/android-developer/answer/9900533)
- [Appodeal: consent manager](https://docs.appodeal.com/android/data-protection/gdpr-and-ccpa)
- [Appodeal: Google Play SDK Data safety table](https://docs.appodeal.com/android/data-protection/app-privacy-details)
- [Appodeal: Apple App Privacy table](https://docs.appodeal.com/ios/data-protection/app-privacy-details)
- [Google: certified CMPs (includes Appodeal)](https://support.google.com/admob/answer/13554116)
- [RevenueCat: division of store/SDK/developer responsibilities](https://www.revenuecat.com/docs/platform-resources/implementation-responsibilities)

**No implementation verification was performed or implied.** This guide is a list of possible obligations based on app purpose and monetization choices only, not a report on what is already deployed, what is missing in any specific repository or which app is currently compliant.
