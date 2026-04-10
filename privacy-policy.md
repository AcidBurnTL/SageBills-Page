# Sagelight Studio Privacy Policy

**Last Updated:** April 11, 2026 | **Effective:** April 1, 2026

---

> **In brief:** This policy covers all apps published by Sagelight Studio, including **SageBills** and **SageMeet**. Your data belongs to you. SageBills uses a fully local architecture; SageMeet optionally sends data to OpenAI when you use AI features.

---

## Key Points

- **SageBills: 100% Local Data** — All your data stays on your device. No servers, no cloud, no exceptions.
- **SageMeet: Local + Optional AI** — Data is stored locally. When you use AI features, audio and text are sent to OpenAI APIs. A Private Mode disables all external transmission.
- **Zero Tracking** — No analytics, no advertising IDs, no telemetry in any of our apps.
- **Encrypted at Rest** — Data is protected by Apple's NSFileProtectionComplete when your device is locked.

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Who We Are](#2-who-we-are)
3. [Privacy-First Architecture](#3-privacy-first-architecture)
4. [Data We Process](#4-data-we-process)
5. [How We Use Your Data](#5-how-we-use-your-data)
6. [Legal Basis for Processing](#6-legal-basis-for-processing)
7. [Data Storage and Security](#7-data-storage-and-security)
8. [Data Retention](#8-data-retention)
9. [Third-Party Services](#9-third-party-services)
10. [International Data Transfers](#10-international-data-transfers)
11. [Cookies and Tracking](#11-cookies-and-tracking)
12. [Your Rights Under GDPR](#12-your-rights-under-gdpr)
13. [Children's Privacy](#13-childrens-privacy)
14. [Changes to This Policy](#14-changes-to-this-policy)
15. [Contact Us](#15-contact-us)

---

## 1. Introduction

Welcome to Sagelight Studio. This Privacy Policy explains how we handle your information when you use our applications — **SageBills** (utility bill tracking) and **SageMeet** (meeting recording and AI transcription) — on iOS and macOS.

This policy complies with the General Data Protection Regulation (GDPR), the ePrivacy Directive, and Apple App Store Guidelines (sections 5.1.1 and 5.1.2).

## 2. Who We Are

Sagelight Studio apps are developed and maintained by a sole proprietor based in Romania, European Union.

- **Contact:** contact@sagelight-studio.com

For the purposes of the GDPR, the developer acts as the data controller. For SageBills, all data processing occurs locally on your device and your data never reaches us. For SageMeet, data is processed locally except when you explicitly use AI features, which transmit data to OpenAI (see Sections 9 and 10).

## 3. Privacy-First Architecture

### SageBills

SageBills is designed with a **local-only, zero-server architecture**:

- **No servers.** We do not operate any backend servers that receive, store, or process your data.
- **No cloud sync.** Your data is not uploaded to any cloud service by SageBills.
- **No analytics.** We do not collect usage analytics, crash reports, or telemetry of any kind.
- **No tracking.** We do not track your behavior, location, or activity.
- **No third-party SDKs.** The app is built entirely with Apple frameworks. Zero external dependencies.

> All data you enter into SageBills is stored on your device and synced securely to your private iCloud account. It is never sent to our servers or shared with third parties.

### SageMeet

SageMeet stores all data locally on your device and optionally syncs via iCloud. However, when you use AI-powered features:

- **Audio and text are sent to OpenAI APIs** (Whisper for transcription, GPT-4o for notes and analytics, embedding APIs for semantic search) when you explicitly request AI processing.
- **Private Mode** disables all external data transmission. When enabled, no data leaves your device.
- **No analytics or tracking.** SageMeet does not collect usage analytics, crash reports, or telemetry.
- **Your OpenAI API key** is stored securely in the device Keychain and is only used to authenticate requests you initiate.

> When AI features are disabled or Private Mode is on, SageMeet behaves identically to SageBills — fully local, zero external transmission.

## 4. Data We Process

### 4.1 SageBills Data

All of the following data is stored **on your device and in your private iCloud account**:

- **Bill Data:** Bill amounts and currency, provider/utility company names, bill categories, bill dates, notes, consumption readings (kWh, cubic meters, etc.)
- **OCR-Scanned Data:** When you scan an invoice, Apple's Vision framework extracts text **entirely on your device**. The original image is not retained after scanning unless you choose otherwise.
- **App Preferences:** Currency and display preferences, notification preferences, savings goals configuration, onboarding and consent status.
- **Keychain Data:** GDPR consent date (for tamper detection). No personal data is stored in the Keychain.
- **Spotlight Index:** Bill records are indexed in Apple's CoreSpotlight for device search. This index is local to your device.

### 4.2 SageMeet Data

The following data is stored **on your device and optionally in your private iCloud account**:

- **Audio Recordings:** Meeting recordings stored locally and optionally in iCloud Drive.
- **Transcripts:** Text generated from audio via OpenAI's Whisper API (when AI features are used) or stored locally.
- **AI-Generated Notes:** Meeting summaries, action items, and analytics generated by GPT-4o.
- **Semantic Embeddings:** Vector representations of your meeting content stored in a local SQLite database for search.
- **Calendar Data:** Read-only access to your calendar for meeting context. SageMeet does not modify your calendar.
- **Speaker Analytics:** AI-generated speaking time and participation data (processed via GPT-4o-mini).
- **OpenAI API Key:** Stored securely in the device Keychain. Used only to authenticate your requests to OpenAI.
- **App Preferences:** Display settings, recording preferences, AI feature toggles, Private Mode status.
- **Spotlight Index:** Meeting records are indexed in Apple's CoreSpotlight for device search.

## 5. How We Use Your Data

### SageBills

Because all data stays on your device, "use" means local processing within the app:

| Purpose | Description |
|---|---|
| **Bill tracking** | Displaying, organizing, and managing your utility bills |
| **Cost prediction** | Generating statistical predictions based on your history |
| **Anomaly detection** | Identifying unusual bills that deviate from patterns |
| **Savings tracking** | Calculating progress toward your savings goals |
| **Invoice scanning** | Extracting bill data from photos via on-device OCR |
| **Reminders** | Sending local notifications for upcoming due dates |
| **Data export** | Generating CSV files when you request it |
| **Device search** | Making bills findable through Spotlight search |

### SageMeet

| Purpose | Description | Involves External Service? |
|---|---|---|
| **Meeting recording** | Capturing audio on your device | No |
| **Transcription** | Converting audio to text via OpenAI Whisper API | Yes (OpenAI) |
| **AI note generation** | Generating summaries and action items via GPT-4o | Yes (OpenAI) |
| **Semantic search** | Creating embeddings for content search via OpenAI API | Yes (OpenAI) |
| **Speaker analytics** | Analyzing participation patterns via GPT-4o-mini | Yes (OpenAI) |
| **Calendar integration** | Reading calendar events for meeting context | No |
| **Spotlight indexing** | Making meetings findable through device search | No |
| **iCloud sync** | Syncing meeting data across your devices | No (Apple infrastructure) |

## 6. Legal Basis for Processing

**SageBills:** Under Article 6(1)(a) of the GDPR, our legal basis is **your explicit consent**, which you provide during the app's onboarding process.

**SageMeet:** Our legal bases are:
- **Consent** (Art. 6(1)(a)) — for optional AI features and data processing during onboarding.
- **Contractual necessity** (Art. 6(1)(b)) — for core AI processing features that are integral to the service you requested (transcription, note generation).

You may withdraw your consent at any time through either app's Settings. Withdrawal does not affect the lawfulness of processing carried out before the withdrawal.

## 7. Data Storage and Security

### 7.1 Local Storage

All data is stored using Apple's SwiftData framework with **NSFileProtectionComplete** encryption:

- Data is encrypted when your device is locked
- Data is only accessible when your device is unlocked and authenticated
- Encryption keys are tied to your device passcode/biometrics

### 7.2 No Remote Storage

SageBills does not transmit data to any remote server. We have no ability to access, read, or recover your data.

### 7.3 Your Responsibility

> **Important:** Because data is stored only on your device, you are responsible for maintaining backups through your device's backup mechanisms (e.g., iCloud device backup, Time Machine).

## 8. Data Retention

Your data is retained on your device for as long as you keep the app installed and choose to retain it. You have full control:

- **Delete individual bills** at any time within the app
- **Delete all data** using the option in Settings
- **Uninstall the app** to remove all associated data

We do not retain any copy of your data because we never receive it.

## 9. Third-Party Services

### 9.1 Apple iCloud (SageMeet)

SageMeet optionally syncs meeting data via Apple's iCloud (CloudKit). Apple acts as a data processor under its own GDPR commitments. iCloud data is encrypted in transit and at rest.

### 9.2 OpenAI (SageMeet)

When you use AI features in SageMeet, audio and text data are sent to **OpenAI LLC** for processing. OpenAI acts as a **data processor** under Article 28 GDPR. The following OpenAI services are used:

- **Whisper API** — audio-to-text transcription
- **GPT-4o** — meeting note generation and summarization
- **GPT-4o-mini** — speaker analytics processing
- **Embedding API** — semantic vector generation for search

OpenAI's data handling is governed by their [API Data Usage Policy](https://openai.com/policies/api-data-usage-policies). OpenAI does not use API data to train their models. OpenAI is certified under the **EU-US Data Privacy Framework** (DPF).

You authenticate with OpenAI using your own API key. We do not have access to your OpenAI account.

### 9.3 SageBills: No Other Third Parties

SageBills contains **no third-party SDKs, frameworks, libraries, or services** beyond Apple's own frameworks. We do not share, sell, or disclose your SageBills data to any third party.

## 10. International Data Transfers

**SageBills** does not transfer your data internationally. Your data remains on your device at all times.

**SageMeet** transfers data to the United States when you use AI features, as OpenAI's API servers are located in the US. These transfers are lawful under the **EU-US Data Privacy Framework** (DPF), under which OpenAI is a certified participant. When Private Mode is enabled, no international transfers occur.

## 11. Cookies and Tracking

Neither SageBills nor SageMeet uses cookies, web beacons, pixels, device fingerprinting, advertising identifiers, or any other tracking technology. Neither app contains any advertising.

## 12. Your Rights Under GDPR

As a resident of the EU or EEA, you have the following rights:

| Right | How to Exercise |
|---|---|
| **Right of access** (Art. 15) | View all your data directly in the app |
| **Right to rectification** (Art. 16) | Edit any bill or data entry within the app |
| **Right to erasure** (Art. 17) | Delete individual bills or all data via Settings |
| **Right to restriction** (Art. 18) | Contact contact@sagelight-studio.com |
| **Right to portability** (Art. 20) | Export your data as CSV from within the app |
| **Right to object** (Art. 21) | Withdraw consent in Settings |
| **Withdraw consent** (Art. 7(3)) | Single action in Settings, takes effect immediately |
| **Lodge a complaint** (Art. 77) | Contact your national data protection authority |

Most rights can be exercised directly within the app. For other rights, email contact@sagelight-studio.com.

### Supervisory Authority

If you are in Romania, the competent authority is **ANSPDCP** ([www.dataprotection.ro](https://www.dataprotection.ro)). You may also contact the authority in your country of residence.

## 13. Children's Privacy

Our apps are not directed at children under 16. We do not knowingly process data from children. Since data is stored locally, we have no means to identify or verify user age.

## 14. Changes to This Policy

We may update this Privacy Policy from time to time. The "Last Updated" date will be revised, and material changes will be communicated through an in-app notice.

## 15. Contact Us

- **Contact:** contact@sagelight-studio.com

We aim to respond to all privacy-related inquiries within 30 days, as required by the GDPR.

---

*Sagelight Studio — Built with care in Romania, EU*
