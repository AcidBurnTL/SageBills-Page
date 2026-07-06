# Sagelight Studio Terms of Service

**Last Updated:** June 14, 2026 | **Effective:** May 21, 2026

---

> **In brief:** The agreement between you and Sagelight Studio, covering **SageBills**, **SageMeet**, and **SageDocs**. Clear, fair, and respectful of your rights as a European consumer.

---

## Key Points

- **Your Data, Your Control** — SageBills data stays local. SageMeet data is local except when you use AI features. SageDocs data is encrypted and synced via your private iCloud.
- **Transparent Pricing** — SageBills and SageMeet are free. SageDocs is offered as a subscription at $2.99/month or $24.99/year.
- **EU Consumer Rights** — Romanian law, with full EU consumer protection preserved.

---

## Table of Contents

1. [Acceptance of Terms](#1-acceptance-of-terms)
2. [Description of Service](#2-description-of-service)
3. [System Requirements](#3-system-requirements)
4. [Pricing](#4-pricing)
5. [Data Storage Model](#5-data-storage-model)
6. [Data Ownership](#6-data-ownership)
7. [Intellectual Property](#7-intellectual-property)
8. [Prohibited Uses](#8-prohibited-uses)
9. [Warranties and Liability](#9-warranties-and-liability)
10. [Governing Law](#10-governing-law)
11. [Dispute Resolution](#11-dispute-resolution)
12. [Termination](#12-termination)
13. [Contact](#13-contact)

---

## 1. Acceptance of Terms

By downloading, installing, or using any Sagelight Studio app ("the App"), you agree to these Terms. If you do not agree, do not use the App.

These Terms constitute a legal agreement between you and **Florin Nica**, an independent individual developer trading as Sagelight Studio, based in Romania, EU. Your use is also governed by our [Privacy Policy](privacy-policy.html) and [GDPR Disclosure](gdpr.html).

## 2. Description of Service

### SageBills

SageBills is a utility bill tracking application for iOS and macOS. Features include bill recording, invoice scanning (OCR), cost predictions, anomaly detection, savings goals, due date reminders, and CSV data export.

> SageBills is a personal finance **tracking** tool. It does not provide financial advice, nor does it process payments to utility providers.

### SageMeet

SageMeet is a meeting recording and AI transcription application for iOS and macOS. Features include audio recording, AI-powered transcription (via OpenAI Whisper), meeting note generation (via GPT-4o), semantic search, speaker analytics, calendar integration, and iCloud sync.

> SageMeet is a **productivity** tool. AI-generated outputs (transcripts, notes, analytics) may be inaccurate and should not be relied upon for legal, medical, or financial decisions.

### SageDocs

SageDocs is a personal document vault application for iOS and macOS. Features include secure document storage, document scanning via camera, AES-256-GCM encryption for all attachments, biometric authentication (Face ID/Touch ID) and master PIN protection, document categorization (identity cards, insurance, loans, contracts, medical records, etc.), expiry tracking with reminders, secure sharing, and iCloud sync of encrypted data.

> SageDocs is a **personal document management** tool. It is not a certified digital safe, legal archive, or replacement for official document repositories. You should maintain independent copies of important documents.

## 3. System Requirements

### SageBills
- **iOS:** iPhone or iPad running iOS 17.0 or later (iOS 26+ recommended)
- **macOS:** Mac running macOS 14.0 (Sonoma) or later (macOS 26+ recommended)
- An Apple ID for downloading
- Internet is only required for downloading the app. Core functionality works entirely offline.

### SageMeet
- **iOS:** iPhone or iPad running iOS 17.0 or later (iOS 26+ recommended)
- **macOS:** Mac running macOS 14.0 (Sonoma) or later (macOS 26+ recommended)
- An Apple ID for downloading
- SageMeet requires an internet connection for AI features and a user-provided OpenAI API key. Recording and local playback work offline.

### SageDocs
- **iOS:** iPhone or iPad running iOS 17.0 or later (iOS 26+ recommended)
- **macOS:** Mac running macOS 14.0 (Sonoma) or later (macOS 26+ recommended)
- An Apple ID for downloading
- An iCloud account for document sync across devices
- Face ID, Touch ID, or a device passcode for biometric authentication (a master PIN is always required)

## 4. Pricing

### SageBills

SageBills is free to download. No subscription, no in-app purchases, and no account required. Monetization may be introduced in a future release and will be communicated clearly in advance; existing free functionality will not be removed without adequate notice.

### SageMeet

SageMeet is free to download. No subscription is required. AI features (transcription, summarization, semantic search, speaker analytics) require a user-provided OpenAI API key; usage costs are billed directly by OpenAI under your own account. Sagelight Studio does not receive any portion of OpenAI charges.

### SageDocs

SageDocs is offered as an auto-renewing subscription via the App Store:

- **Monthly:** $2.99 per month
- **Yearly:** $24.99 per year

Payment is charged to your Apple ID account at confirmation of purchase. The subscription automatically renews unless cancelled at least 24 hours before the end of the current period. Your account is charged for renewal within 24 hours prior to the end of the current period. You may manage and cancel your subscription in **Settings → [your Apple ID] → Subscriptions** at any time; cancellation takes effect at the end of the current billing period. Local taxes (VAT) may apply.

> **EU 14-day right of withdrawal:** Under Directive 2011/83/EU, EU consumers have 14 days to withdraw from a digital service purchase. By starting to use SageDocs Pro features immediately upon purchase, you expressly request immediate performance and acknowledge that you lose the 14-day withdrawal right (Art. 16(m) of the Directive). The App Store handles refund requests in line with Apple's refund policy.

### Future pricing

We reserve the right to revise pricing or introduce new tiers. Any pricing changes will be communicated in advance and will not affect already-purchased lifetime upgrades. Free features in current versions will not be removed without adequate notice.

## 5. Data Storage Model

### SageBills

> **Important:** SageBills does not provide cloud backup. You are solely responsible for backing up your data using iCloud device backup, Time Machine, or similar mechanisms.

We are not liable for data loss from device loss, app deletion, OS updates, or any other circumstance, as we have no access to your data.

The app provides a CSV export feature for maintaining independent copies of your records.

### SageMeet

SageMeet stores data locally and optionally syncs via iCloud. Audio recordings and AI-generated content may be stored in iCloud Drive when sync is enabled. When AI features are used, data is transmitted to OpenAI for processing (see our [Privacy Policy](privacy-policy.html) for details).

> **Important:** You are responsible for backing up your recordings. We do not have access to your meeting data.

### SageDocs

SageDocs stores all document metadata locally using SwiftData and syncs via Apple CloudKit. All document attachments (scans, photos, PDFs) are encrypted with AES-256-GCM before storage.

> **Important:** You must remember your master PIN. If you lose your PIN and cannot authenticate via biometrics, your encrypted documents cannot be recovered. Sagelight Studio does not have access to your encryption keys and cannot reset your PIN.

## 6. Data Ownership

All data you enter remains **your property**. We do not claim any ownership, license, or rights to your data. You are responsible for the accuracy of data you enter, including reviewing OCR-extracted results.

**SageMeet AI outputs:** AI-generated outputs (transcripts, notes, summaries, analytics) are derived content. You own your recordings and input data. AI-generated outputs are subject to [OpenAI's usage policies](https://openai.com/policies/terms-of-use).

**SageDocs documents:** All documents, scans, and metadata you store in SageDocs remain entirely your property. Encrypted data synced to iCloud is protected by your personal encryption key.

## 7. Intellectual Property

The apps' design, code, UI, graphics, and icons are owned by Sagelight Studio and protected by intellectual property laws. You receive a limited, non-exclusive, non-transferable license for personal use.

You may not copy, modify, distribute, reverse-engineer, or use any app to develop a competing product.

If you provide feedback or suggestions, you grant us a non-exclusive, royalty-free right to incorporate that feedback without obligation.

## 8. Prohibited Uses

You agree not to:

- Violate any applicable law or third-party rights
- Circumvent any access controls or security measures
- Reverse-engineer or tamper with the app's source code
- Use the app in ways that could damage or impair its functionality
- Attempt to extract encryption keys, bypass PIN/biometric protection, or access other users' encrypted data (SageDocs)

## 9. Warranties and Liability

THE APPS ARE PROVIDED "AS IS" WITHOUT WARRANTIES OF ANY KIND, EXPRESS OR IMPLIED. WE DO NOT WARRANT THAT THE APPS WILL BE UNINTERRUPTED, ERROR-FREE, OR THAT PREDICTIONS WILL BE ACCURATE. TO THE MAXIMUM EXTENT PERMITTED BY LAW, OUR TOTAL LIABILITY IS LIMITED TO THE AMOUNT, IF ANY, YOU HAVE PAID US IN THE PRECEDING TWELVE MONTHS.

**AI accuracy disclaimer (SageMeet):** AI-generated transcriptions, summaries, and analytics may be inaccurate. SageMeet does not guarantee the accuracy of AI outputs. Do not rely on them for legal, medical, or financial decisions. You are responsible for reviewing all AI-generated content.

**Encryption disclaimer (SageDocs):** While SageDocs uses industry-standard encryption (AES-256-GCM), no security system is infallible. SageDocs is not a certified digital safe or legally recognized secure archive. We do not guarantee that encryption cannot be compromised under all circumstances.

> **EU consumers:** This does not affect your statutory rights under the EU Digital Content Directive (2019/770). Liability cannot be excluded for intentional misconduct or gross negligence.

## 10. Governing Law

These Terms are governed by **Romanian law**. EU consumers also benefit from mandatory consumer protections of their country of residence, including:

- Directive 2011/83/EU (Consumer Rights)
- Directive 2019/770/EU (Digital Content)
- National consumer protection laws of your Member State

## 11. Dispute Resolution

We encourage informal resolution first via contact@sagelight-studio.com. We aim to respond to all complaints within 30 days.

If a dispute cannot be resolved informally, EU consumers may seek recourse through **Alternative Dispute Resolution (ADR)** pursuant to Directive 2013/11/EU. In Romania, the National Authority for Consumer Protection (ANPC) offers a conciliation service ([anpc.ro](https://anpc.ro)). Sagelight Studio does not currently participate in a specific ADR scheme.

> **Note:** The EU Online Dispute Resolution (ODR) platform established under Regulation (EU) 524/2013 was discontinued by the European Commission in July 2025 and is no longer available. The right to ADR under Directive 2013/11/EU remains in force.

Disputes that cannot be resolved otherwise are resolved by competent **Romanian courts**. EU consumers resident in another Member State may also use the courts of their habitual residence (Regulation (EU) 1215/2012, Brussels I recast).

## 12. Termination

You may stop using any Sagelight Studio app at any time by uninstalling. Upon termination, your data remains on your device.

We may update these Terms from time to time. Material changes will have at least **30 days' notice**. These Terms, together with the Privacy Policy and GDPR Disclosure, constitute the entire agreement.

Our apps are also subject to Apple's [Licensed Application EULA](https://www.apple.com/legal/internet-services/itunes/dev/stdeula/).

## 13. Contact

- **Contact:** contact@sagelight-studio.com

---

*Sagelight Studio — Built with care in Romania, EU*
