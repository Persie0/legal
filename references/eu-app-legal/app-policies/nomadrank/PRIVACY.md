---
layout: legal
legal_kind: privacy-en
app_name: "NomadRank: Rate Visited Places"
package_id: "at.persie0.nomadrank"
title: "Privacy Policy – NomadRank: Rate Visited Places (English)"
permalink: /privacy/nomadrank/en/
---

# Privacy Policy for NomadRank

**Last updated:** 5 November 2026

## 1. Scope

This privacy policy covers **NomadRank** and describes the processing related to the travel account, places, ratings and social sharing. The actually published app version is authoritative. The data described serves the function you trigger.

## 2. Controller

**Marvin Perzi (Persie0)**, Angerdorf 6, 3822 Karlstein an der Thaya, Austria. Email: [persie0@protonmail.com](mailto:persie0@protonmail.com). Further company details and contact options: [Imprint](https://persie0.github.io/translations_imprint/imprint-de.html).

## 3. At a glance

- NomadRank stores your travel account, places, ratings and social shares in a server backend operated by Persie0 in Frankfurt am Main; sign-in is via Firebase with Google or Apple.
- The core functions are ad-free; in the reviewed version no advertising service is integrated.
- Optional: travel suggestions from text imports via Gemini with your own API key, map views (CARTO) as well as country and currency data.
- Error reports go to a self-operated GlitchTip installation in Frankfurt am Main.
- You can delete your account in the app; a help page describes the process ([account deletion](https://github.com/Persie0/legal/blob/main/references/eu-app-legal/app-policies/KONTOLOESCHUNG_NOMADRANK.md)).

## 4. Processing by purpose

Processing is organised by function. A distinction must be drawn between purely local processing and data that arises on servers or with independent services. Where processes run exclusively on your device, Persie0 does not automatically gain access to their contents.

**Using the app on your device**

- Data: offline copies and queues of account, travel and social data; map/static datasets as well as cached country and currency data; settings and a Gemini API key stored in the secure operating-system storage.
- Legal basis: function you requested; where we process personal data ourselves, Art. 6(1)(b) GDPR.
- Recipients: none; the data remains on your device.
- Retention/deletion: until you delete the local data, reset it or uninstall the app.

**Creating, securing and signing in to a NomadRank account** *(optional, required for account functions)*

- Data: Firebase UID, email, display name, authentication provider, token and security/request logs including IP; Google or Apple additionally process the login data you authorised.
- Legal basis: Art. 6(1)(b) GDPR; security/abuse prevention additionally Art. 6(1)(f) GDPR.
- Recipients: Google Firebase and the sign-in provider you select (see section 6).
- Retention: for the lifetime of the account. After account deletion, deletion from live/backup systems follows provider cycles; for many deleted systems/backups Firebase states up to 180 days, subject to security/legal requirements.

**Providing the account, synchronisation, travel journal, leaderboard and requested social functions**

- Data: UID; user/display name; login email; avatar URL; home country; membership/rank/achievements; trips and planned trips (destination/city coordinates, dates, ratings, tags, notes, costs); bucket list; friends/invitations; groups; travel circles and members/stops; server/security logs including IP. Other users may see profile/social data depending on the function.
- Legal basis: Art. 6(1)(b) GDPR; service security/abuse prevention Art. 6(1)(f) GDPR. Social publication/sharing takes place at your request.
- Recipients: Persie0 backend on Oracle Cloud Infrastructure (Frankfurt) as well as the friends, invitees or group/circle members shown by the function (see section 6).
- Retention: account content until individual deletion or account deletion. Backups are purged according to the applicable retention rules; security logs only for abuse/claim purposes. A portable export is available in the app.

**Choosing regional defaults, currency, language or the consent flow**

- Data: public IP address, request metadata and a country/region derived from them; no GPS location.
- Legal basis: Art. 6(1)(f) GDPR (minimal regional configuration). Regional settings can be overridden where offered.
- Recipients: whichever country-lookup service is available first (see section 6).
- Retention: the response is used transiently or cached locally; Persie0 keeps no server log. Providers store request logs according to their policies.

**Extracting travel suggestions and resolving destinations for an import you start** *(optional)*

- Data: your Gemini API key, entered travel text, selected text/table attachments (up to the app limit), file names, prompts, possible destination lines and the generated travel extraction. The key is held in the secure operating-system storage; Persie0 does not receive it.
- Legal basis: Art. 6(1)(a)/(b) GDPR. Optional and started by you; Google acts under the API account/contract linked to your key.
- Recipients: Google AI (see section 6).
- Retention: Persie0 stores only the travel data you adopt. Google's retention/training depends on the paid service and account configuration; check the Gemini API terms before entering personal data.

**Displaying the map area you request**

- Data: IP, user agent, request time and the requested map tile coordinates/zoom level, from which the area viewed can be inferred. The map provider receives no NomadRank account password.
- Legal basis: Art. 6(1)(b) GDPR for the requested map and Art. 6(1)(f) for efficient delivery.
- Recipients: CARTO/CDN and, for direct queries, OpenStreetMap-related services (see section 6).
- Retention: Persie0 keeps no map tile request logs; provider periods apply. The local cache is deleted by the app/operating system or uninstallation.

**Displaying country information, notes/static facts and exchange rates**

- Data: IP, request metadata and the requested article, country or currency pair. No account password.
- Legal basis: Art. 6(1)(b) GDPR for requested content; Art. 6(1)(f) for cached, reliable delivery.
- Recipients: the content/API provider queried by the function (see section 6).
- Retention: responses may be cached locally; Persie0 keeps no server log. Provider periods apply.

**Technical error diagnosis**

- Data: app/system version, error message, stack trace and technical HTTP/device data.
- Legal basis: Art. 6(1)(f) GDPR, protection against errors and abuse.
- Recipients: self-operated GlitchTip installation (see section 6).
- Retention: 14 days for error events.

## 5. On-device processing and permissions

The device storage is used in particular for the following data for the functions you request: offline copies and queues of account, travel and social data, map/static datasets as well as cached country and currency data, settings and a Gemini API key stored in the secure operating-system storage. You can remove stored content via the app function offered for that purpose or reset local app data via the operating system. Exported copies may continue to exist outside the app.

- Exact/approximate location: suggest the nearest supported city; the matching is done against a local city database.
- Photos/files: select a profile/travel image or import/export travel files.
- Network: account synchronisation, social functions, maps, country/currency data, diagnostics and the optional Gemini import.

A system permission only covers the respective device access and is not consent to independent advertising or analytics purposes.

## 6. External services and recipients

### Sign-in (Firebase)

Account creation and sign-in take place via Google Firebase and the sign-in provider you select (Google or Apple). Section 4 describes which data is processed on which legal basis. [Provider privacy notice](https://firebase.google.com/support/privacy)

### NomadRank account and social functions (own backend, Oracle Frankfurt)

Account, travel, group and contact functions run on our backend at Oracle Cloud Infrastructure in Frankfurt am Main (Germany, region eu-frankfurt-1). Oracle acts as infrastructure processor; friends, invitees or group/circle members receive the fields shown by the respective function. Account deletion is described on the [separate help page](https://github.com/Persie0/legal/blob/main/references/eu-app-legal/app-policies/KONTOLOESCHUNG_NOMADRANK.md). [Provider privacy notice](https://www.oracle.com/legal/privacy/)

### Country lookup

For regional defaults, the first available of the services ipapi.co, FreeIPAPI or ip-api.com is queried. [Provider privacy notice](https://ipapi.co/privacy/)

### Optional Gemini travel import (with your own API key)

The import you start sends texts, attachments and prompts with your API key directly to Google AI; Persie0 is not an intermediate recipient of the API payload. [Provider terms of use](https://ai.google.dev/gemini-api/terms)

### Maps and geographic content

Map delivery is via CARTO/CDN and, for direct queries, OpenStreetMap-related services. [Provider privacy notice](https://carto.com/privacy/)

### Country, encyclopaedia and currency retrieval

For country information, notes and exchange rates, content/API providers are queried depending on the function, including Wikimedia services. [Provider privacy notice](https://foundation.wikimedia.org/wiki/Policy:Privacy_policy)

### Error reports (GlitchTip, self-operated)

To fix program errors we use our own GlitchTip installation on Oracle Cloud Infrastructure in Frankfurt am Main (Germany, region eu-frankfurt-1). Error descriptions, stack traces, app/system versions and technical connection data may be processed. Error events are stored for 14 days; rotated web-server access logs are purged after seven days and technical maintenance logs after 30 days.

## 7. Retention and deletion

Local records remain until you delete them; uninstalling removes the offline copies stored on the device. Account data remains until individual deletion or account deletion; you can initiate deletion via the app's account deletion function ([help page](https://github.com/Persie0/legal/blob/main/references/eu-app-legal/app-policies/KONTOLOESCHUNG_NOMADRANK.md)). Uninstalling alone does not delete the server account. Backups are purged according to the applicable retention rules. Where a function was set up with consent, withdrawal is possible for the future. We support the exercise of data-subject rights for data in our area of responsibility at [persie0@protonmail.com](mailto:persie0@protonmail.com).

## 8. Transfers to third countries

The NomadRank backend and the GlitchTip installation are located in Frankfurt am Main (Germany); for this data there is no transfer to a third country. Firebase (Google), Google AI (Gemini), the map provider CARTO and the country-lookup and content services may also process data outside the EEA. Insofar as the GDPR applies, such transfers are based on a permissible ground under Art. 44 et seq. GDPR, such as an applicable adequacy decision or suitable contractual safeguards.

## 9. Your rights

Under the GDPR you have the rights to information, rectification, erasure, restriction, where applicable data portability and objection. Consents given can be withdrawn for the future. You may lodge a complaint with a data-protection authority, in particular the [Austrian Data Protection Authority](https://dsb.gv.at/). For matters addressed to us, contact [persie0@protonmail.com](mailto:persie0@protonmail.com).

## 10. Children, security and updates

We align processing with the respective purpose and take appropriate security measures. The relevant protective provisions apply to minors. If the purposes, data types or recipients change materially, we will adapt this policy and, where necessary, obtain separate consent.
