# Sagelight Studio GDPR Data Processing Disclosure

**Last Updated:** April 11, 2026 | **GDPR (EU) 2016/679**

---

> **In brief:** Information required under Articles 13 and 14 of the General Data Protection Regulation regarding data processing through Sagelight Studio apps (SageBills and SageMeet). SageBills processing occurs entirely on your device. SageMeet optionally transmits data to OpenAI when AI features are used.

---

## Key Points

- **Controller in EU** — Sole proprietor based in Romania. Your data is never sent to Sagelight Studio servers.
- **Lawful Basis: Consent + Contract** — SageBills: Art. 6(1)(a) consent. SageMeet: consent and Art. 6(1)(b) contractual necessity.
- **iCloud Sync** — Data syncs via Apple CloudKit to your private iCloud account. Apple acts as a data processor under its own GDPR commitments.
- **SageMeet: OpenAI as Processor** — When AI features are used, OpenAI LLC receives audio/text data as a data processor (Art. 28). No data is shared when Private Mode is enabled.

---

## Table of Contents

1. [Data Controller](#1-data-controller)
2. [Data Protection Officer](#2-data-protection-officer)
3. [Categories of Personal Data](#3-categories-of-personal-data)
4. [Purposes of Processing](#4-purposes-of-processing)
5. [Lawful Basis](#5-lawful-basis)
6. [Recipients](#6-recipients)
7. [International Transfers](#7-international-transfers)
8. [Retention Periods](#8-retention-periods)
9. [Data Subject Rights](#9-data-subject-rights)
10. [Automated Decision-Making](#10-automated-decision-making)
11. [Data Protection Measures](#11-data-protection-measures)
12. [Breach Notification](#12-breach-notification)
13. [Children's Data](#13-childrens-data)
14. [Supervisory Authority](#14-supervisory-authority)
15. [Contact](#15-contact)

---

## 1. Data Controller

**Controller:** Sagelight Studio (individual developer / sole proprietor)
**Location:** Romania, European Union
**Email:** contact@sagelight-studio.com

Per **Article 13(1)(a)** and **Article 14(1)(a)**, the developer is the data controller for all Sagelight Studio apps. For SageBills, the controller does not receive, access, or store any personal data — all processing occurs on the user's device. For SageMeet, data is processed locally except when the user initiates AI features, which transmit data to OpenAI as a data processor (Art. 28).

## 2. Data Protection Officer

Per **Article 37**, a DPO is not required. The controller is a small-scale operator that does not carry out regular and systematic monitoring on a large scale, nor large-scale processing of special categories of data.

For privacy inquiries: contact@sagelight-studio.com

## 3. Categories of Personal Data

Per **Article 13(1)(d)** and **14(1)(d)**:

### SageBills

| Category | Examples | Special Category (Art. 9)? |
|---|---|---|
| **Financial data** | Bill amounts, currency, consumption costs | No |
| **Utility provider data** | Provider names, service categories | No |
| **Temporal data** | Bill dates, due dates, billing periods | No |
| **Consumption data** | kWh readings, cubic meters | No |
| **Free-text data** | Notes you add to bill records | No |
| **OCR-extracted data** | Account numbers, addresses from invoices | No |
| **Technical data** | Consent timestamp (Keychain) | No |

### SageMeet

| Category | Examples | Special Category (Art. 9)? |
|---|---|---|
| **Audio data** | Meeting recordings | No |
| **Transcript data** | Text generated from audio via Whisper API | No |
| **AI-generated content** | Meeting notes, summaries, action items | No |
| **Embedding vectors** | Semantic representations for search (local SQLite) | No |
| **Calendar metadata** | Event titles, times, participants (read-only) | No |
| **Speaker analytics** | Speaking time, participation metrics | No |
| **API credentials** | OpenAI API key (Keychain) | No |
| **Technical data** | Consent timestamp, app preferences | No |

**No special categories of personal data** (Article 9) are processed by any Sagelight Studio app.

## 4. Purposes of Processing

Per **Article 13(1)(c)** and **14(1)(c)**:

### SageBills

| # | Purpose | Description |
|---|---|---|
| 1 | **Bill management** | Storing, displaying, organizing, and searching bill records |
| 2 | **Cost prediction** | Statistical forecasts based on historical data |
| 3 | **Anomaly detection** | Identifying bills that deviate from patterns |
| 4 | **Savings tracking** | Tracking progress toward savings goals |
| 5 | **Invoice digitization** | OCR extraction from scanned invoices |
| 6 | **Due date reminders** | Local notifications for upcoming bills |
| 7 | **Data export** | CSV exports at the user's request |
| 8 | **Device search** | Indexing in CoreSpotlight |

### SageMeet

| # | Purpose | Description |
|---|---|---|
| 11 | **Meeting recording** | Capturing and storing audio recordings locally |
| 12 | **Transcription** | Converting audio to text via OpenAI Whisper API |
| 13 | **AI summarization** | Generating notes and action items via GPT-4o |
| 14 | **Semantic search** | Creating embeddings for content search |
| 15 | **Speaker analytics** | Analyzing participation patterns via GPT-4o-mini |
| 16 | **Calendar integration** | Reading calendar events for meeting context |
| 17 | **iCloud sync** | Syncing meeting data across your devices |
| 18 | **Device search** | Indexing meetings in CoreSpotlight |

## 5. Lawful Basis

**SageBills:** Per **Article 6(1)(a)**: **Consent.** You provide explicit consent during onboarding.

**SageMeet:** Per **Article 6(1)(a)** and **Article 6(1)(b)**:
- **Consent** (Art. 6(1)(a)) — for optional AI features and data processing during onboarding.
- **Contractual necessity** (Art. 6(1)(b)) — for core AI processing features (transcription, note generation) that are integral to the service.

Consent is freely given, specific, informed, and unambiguous. You may withdraw consent at any time via Settings, which takes effect immediately.

### Withdrawal of Consent (Article 7(3))

- Takes effect immediately
- Does not affect the lawfulness of processing carried out before withdrawal
- Is as easy as giving consent (single action in Settings)

## 6. Recipients

Per **Article 13(1)(e)**:

### SageBills

**There are no recipients of your SageBills personal data.** No data processors (Art. 28), no joint controllers (Art. 26), no third-party services, no advertising networks, no analytics providers.

### SageMeet

When AI features are used, the following recipients process your data:

| Recipient | Role | Data Received | Legal Basis |
|---|---|---|---|
| **OpenAI LLC** | Data processor (Art. 28) | Audio recordings, text for transcription, meeting content for summarization, text for embedding generation | DPA with Art. 28 safeguards |
| **Apple (iCloud)** | Storage provider | Meeting data when iCloud sync is enabled | Apple's GDPR commitments |

OpenAI does not use API data to train its models. No advertising networks, analytics providers, or other third parties receive your data. When Private Mode is enabled, no data is shared with OpenAI.

## 7. International Transfers

Per **Article 13(1)(f)**:

**SageBills:** No international transfers occur. All data is processed on your local device.

**SageMeet:** When AI features are used, data is transferred to the United States (OpenAI's servers). These transfers are lawful under the **EU-US Data Privacy Framework** (DPF, Chapter V), under which OpenAI is a certified participant. When Private Mode is enabled, no international transfers occur.

## 8. Retention Periods

Per **Article 13(2)(a)** and **14(2)(a)**:

| Data | Retention | Basis |
|---|---|---|
| **Bill records** | Until you delete them or uninstall | User control |
| **OCR-extracted text** | Until the associated bill is deleted | User control |
| **App preferences** | Until reset or uninstall | User control |
| **Consent timestamp** | Until uninstallation | Legal compliance |

> **You control retention entirely.** Delete individual records, all data, or uninstall the app at any time.

## 9. Data Subject Rights

Per **Article 13(2)(b)** and **14(2)(c)**:

| Right | Article | How to Exercise |
|---|---|---|
| **Access** | Art. 15 | All your data is visible in the app at all times |
| **Rectification** | Art. 16 | Edit any record directly within the app |
| **Erasure** | Art. 17 | Delete individual or all records; uninstall removes everything |
| **Restriction** | Art. 18 | Contact contact@sagelight-studio.com or withdraw consent |
| **Portability** | Art. 20 | Export all bill data as CSV from within the app |
| **Object** | Art. 21 | Withdraw consent in Settings to stop all processing |
| **Withdraw Consent** | Art. 7(3) | Single action in Settings; takes effect immediately |
| **Lodge Complaint** | Art. 77 | Contact your supervisory authority (ANSPDCP for Romania) |

Most rights can be exercised directly within the app. For other rights, email contact@sagelight-studio.com. We respond within **30 days** per Article 12(3).

## 10. Automated Decision-Making

**SageBills** uses statistical calculations (averaging, trend analysis) for predictions and anomaly detection. These are **informational only** and do not constitute profiling (Art. 4(4)) or automated decision-making (Art. 22) as they produce no legal or similarly significant effects.

**SageMeet** uses AI models (GPT-4o, GPT-4o-mini) to generate meeting notes, summaries, action items, and speaker analytics. These AI-generated outputs are **informational only** and are not used for decisions producing legal or similarly significant effects. Users should review AI outputs for accuracy and not rely on them for legal, medical, or financial decisions.

## 11. Data Protection Measures

Per **Article 32**:

- **Encryption at rest:** NSFileProtectionComplete (data encrypted when device is locked)
- **Keychain security:** Hardware-backed encryption for timestamps
- **On-device processing:** All OCR and predictions run locally
- **No third-party code:** Zero external SDKs eliminates supply-chain risk
- **Privacy by design** (Art. 25(1)) and **privacy by default** (Art. 25(2))

## 12. Breach Notification

Per **Articles 33 and 34**: Given the local-only architecture, traditional data breaches are not applicable. Should a vulnerability be identified:

- Users will be notified through an app update
- ANSPDCP will be notified within **72 hours** (Art. 33)
- Affected data subjects will be notified without undue delay (Art. 34)

## 13. Children's Data

Per **Article 8**: Our apps are not directed at children under 16 (Romania's national threshold under Art. 8(1)). We cannot verify user age due to the primarily local architecture.

## 14. Supervisory Authority

**ANSPDCP** (Autoritatea Nationala de Supraveghere a Prelucrarii Datelor cu Caracter Personal)

- **Address:** B-dul G-ral. Gheorghe Magheru 28-30, Sector 1, 010336, Bucuresti
- **Phone:** +40.318.059.211
- **Website:** [www.dataprotection.ro](https://www.dataprotection.ro)

You may also lodge a complaint with the authority in your EU/EEA Member State of residence (Art. 77).

## 15. Contact

- **Contact:** contact@sagelight-studio.com

We respond within **30 days** (Art. 12(3)), with a possible two-month extension for complex requests.

---

*This disclosure is provided in compliance with Articles 13 and 14 of the General Data Protection Regulation (EU) 2016/679.*

*Sagelight Studio — Built with care in Romania, EU*
