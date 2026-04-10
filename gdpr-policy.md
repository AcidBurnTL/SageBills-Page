# SageBills GDPR Data Processing Disclosure

**Last Updated:** April 10, 2026

This document provides the information required under **Articles 13 and 14** of the General Data Protection Regulation (EU) 2016/679 ("GDPR") regarding the processing of personal data through the SageBills application.

---

## Table of Contents

1. [Identity and Contact Details of the Data Controller](#1-identity-and-contact-details-of-the-data-controller)
2. [Data Protection Officer](#2-data-protection-officer)
3. [Categories of Personal Data](#3-categories-of-personal-data)
4. [Purposes of Processing](#4-purposes-of-processing)
5. [Lawful Basis for Processing](#5-lawful-basis-for-processing)
6. [Recipients of Personal Data](#6-recipients-of-personal-data)
7. [International Transfers](#7-international-transfers)
8. [Retention Periods](#8-retention-periods)
9. [Data Subject Rights](#9-data-subject-rights)
10. [Automated Decision-Making and Profiling](#10-automated-decision-making-and-profiling)
11. [Data Protection Measures](#11-data-protection-measures)
12. [Data Breach Notification](#12-data-breach-notification)
13. [Children's Data](#13-childrens-data)
14. [Source of Personal Data](#14-source-of-personal-data)
15. [Changes to This Disclosure](#15-changes-to-this-disclosure)
16. [Supervisory Authority](#16-supervisory-authority)
17. [Contact](#17-contact)

---

## 1. Identity and Contact Details of the Data Controller

**Controller:** SageBills (individual developer / sole proprietor)
**Location:** Romania, European Union
**Email:** privacy@sagebills.app

In accordance with **Article 13(1)(a)** and **Article 14(1)(a)** of the GDPR, the developer of SageBills is the data controller. However, due to the local-only architecture of SageBills, the controller does not receive, access, or store any personal data processed through the app. All processing occurs exclusively on the user's device.

## 2. Data Protection Officer

In accordance with **Article 37** of the GDPR, the appointment of a Data Protection Officer (DPO) is not required for SageBills. The controller is a small-scale operator that does not carry out:

- Regular and systematic monitoring of data subjects on a large scale; or
- Large-scale processing of special categories of data.

Furthermore, no personal data leaves the user's device, and the controller has no access to any user data.

For privacy-related inquiries, please contact: privacy@sagebills.app

## 3. Categories of Personal Data

Per **Article 13(1)(d)** and **Article 14(1)(d)**, the following categories of personal data may be processed locally on your device:

### 3.1 Data You Enter Directly

| Category | Examples | Special Category (Art. 9)? |
|---|---|---|
| Financial data | Bill amounts, currency, consumption costs | No |
| Utility provider data | Provider names, service categories | No |
| Temporal data | Bill dates, due dates, billing periods | No |
| Consumption data | kWh readings, cubic meters, usage quantities | No |
| Free-text data | Notes you add to bill records | No |
| Savings data | Savings goals, target amounts | No |

### 3.2 Data Extracted via OCR

When you scan an invoice, Apple's Vision framework (running locally) may extract:

| Category | Examples | Special Category (Art. 9)? |
|---|---|---|
| Account identifiers | Customer/account numbers | No |
| Address data | Service addresses on invoices | No |
| Financial details | Itemized charges, tax amounts | No |
| Provider details | Company names, registration numbers | No |

### 3.3 Technical Data

| Category | Purpose | Special Category (Art. 9)? |
|---|---|---|
| First-launch date | Grace period calculation (stored in Keychain) | No |
| Consent timestamp | GDPR consent integrity (stored in Keychain) | No |
| Spotlight index entries | Device search functionality | No |

**No special categories of personal data** (as defined in Article 9 of the GDPR) are processed by SageBills.

## 4. Purposes of Processing

Per **Article 13(1)(c)** and **Article 14(1)(c)**, personal data is processed for the following purposes:

| # | Purpose | Description |
|---|---|---|
| 1 | **Bill management** | Storing, displaying, organizing, and searching utility bill records |
| 2 | **Cost prediction** | Generating statistical forecasts of future utility costs based on historical data |
| 3 | **Anomaly detection** | Identifying bills that deviate significantly from established patterns |
| 4 | **Savings tracking** | Calculating and displaying progress toward user-defined savings goals |
| 5 | **Invoice digitization** | Extracting structured data from scanned invoice images via on-device OCR |
| 6 | **Due date reminders** | Scheduling local notifications for upcoming bill due dates |
| 7 | **Data export** | Generating CSV exports of bill data at the user's request |
| 8 | **Device search** | Indexing bill records in CoreSpotlight for Spotlight search |
| 9 | **Subscription management** | Reading subscription status from Apple StoreKit to enable features |
| 10 | **Anti-abuse** | Verifying grace period eligibility using the first-launch date |

## 5. Lawful Basis for Processing

Per **Article 13(1)(c)** and **Article 14(1)(c)**, in conjunction with **Article 6(1)**, the lawful basis for all processing is:

**Consent -- Article 6(1)(a) GDPR**

You provide explicit consent during the onboarding process before any data is collected or processed. Consent is:

- **Freely given:** The app cannot be used without consent, but you are free not to use the app.
- **Specific:** Consent covers the specific purposes listed in Section 4.
- **Informed:** Full information is provided during onboarding and in this disclosure.
- **Unambiguous:** Consent is given through a clear affirmative action (tapping the consent button).

### Withdrawal of Consent (Article 7(3))

You may withdraw consent at any time through the app's Settings screen. Withdrawal:

- Takes effect immediately.
- Results in the deletion of all personal data from the app.
- Does not affect the lawfulness of processing carried out before withdrawal.
- Is as easy as giving consent (single action in Settings).

## 6. Recipients of Personal Data

Per **Article 13(1)(e)** and **Article 14(1)(e)**:

**There are no recipients of your personal data.**

SageBills does not share, disclose, transmit, or make available any personal data to any third party, including:

- No data processors (Article 28)
- No joint controllers (Article 26)
- No third-party service providers
- No advertising networks
- No analytics providers
- No government authorities (we have no data to provide)

The only third-party involvement is Apple's App Store for subscription payment processing, which is governed by Apple's own privacy policy and does not involve SageBills receiving or accessing your payment data.

## 7. International Transfers

Per **Article 13(1)(f)** and **Article 14(1)(f)**:

**No international transfers of personal data occur.** All data is processed and stored exclusively on your local device. SageBills does not operate servers in any jurisdiction.

No transfer mechanisms under Chapter V of the GDPR (adequacy decisions, standard contractual clauses, binding corporate rules) are applicable.

## 8. Retention Periods

Per **Article 13(2)(a)** and **Article 14(2)(a)**:

| Data Category | Retention Period | Basis |
|---|---|---|
| Bill records | Until you delete them or uninstall the app | User control |
| OCR-extracted text | Until you delete the associated bill or uninstall the app | User control |
| App preferences | Until you reset them or uninstall the app | User control |
| First-launch date (Keychain) | Until app uninstallation | Anti-abuse |
| Consent timestamp (Keychain) | Until app uninstallation | Legal compliance |
| Spotlight index | Until you delete the bill or uninstall the app | User control |

**You control retention entirely.** You can delete individual records, all data, or uninstall the app at any time. The controller does not retain any data because it never receives any.

## 9. Data Subject Rights

Per **Article 13(2)(b)** and **Article 14(2)(c)**, you have the following rights under the GDPR:

### 9.1 Right of Access (Article 15)

You have the right to obtain confirmation of whether your personal data is being processed and access to that data. In SageBills, all your data is visible directly in the app at all times. You have complete and unrestricted access.

### 9.2 Right to Rectification (Article 16)

You have the right to correct inaccurate personal data. In SageBills, you can edit any bill record or data entry directly within the app.

### 9.3 Right to Erasure (Article 17)

You have the right to have your personal data deleted ("right to be forgotten"). In SageBills:

- Delete individual bill records at any time.
- Use "Delete All Data" in Settings to erase everything.
- Uninstall the app to remove all data from your device.

### 9.4 Right to Restriction of Processing (Article 18)

You have the right to restrict processing in certain circumstances. Contact privacy@sagebills.app if you wish to exercise this right. Alternatively, you may withdraw consent, which stops all processing.

### 9.5 Right to Data Portability (Article 20)

You have the right to receive your personal data in a structured, commonly used, machine-readable format. SageBills provides a **CSV export** feature that allows you to export all your bill data, with optional inclusion of OCR text.

### 9.6 Right to Object (Article 21)

You have the right to object to processing. Since processing is based on consent, you may withdraw consent at any time through Settings, which is equivalent to objecting to all processing.

### 9.7 Right to Withdraw Consent (Article 7(3))

You may withdraw your consent at any time via the Settings screen. See Section 5 above for details.

### 9.8 Right to Lodge a Complaint (Article 77)

You have the right to lodge a complaint with a supervisory authority. See Section 16 for details.

### How to Exercise Your Rights

Most rights can be exercised directly within the app without contacting us. For rights that require our involvement, email privacy@sagebills.app. We will respond within **30 days** in accordance with Article 12(3) of the GDPR.

## 10. Automated Decision-Making and Profiling

Per **Article 13(2)(f)** and **Article 14(2)(g)**:

SageBills includes features that use **statistical calculations** to predict future bill amounts and detect anomalies. These features:

- Use simple statistical methods (averaging, trend analysis) applied to your local bill history.
- Are **informational only** and do not produce any legal effects or similarly significant effects on you.
- Do not constitute **profiling** as defined in Article 4(4) of the GDPR, because they are not used to evaluate personal aspects or make decisions about you.
- Do not constitute **automated decision-making** under Article 22 of the GDPR, because no decisions with legal or significant effects are made based on them.

Predictions are displayed as estimates to help you plan your budget. You are free to disregard them.

## 11. Data Protection Measures

Per **Article 32** of the GDPR, the following technical and organizational measures protect your data:

### Technical Measures

- **Encryption at rest:** All data is stored using Apple's SwiftData framework with **NSFileProtectionComplete** encryption, meaning data is encrypted whenever the device is locked.
- **Keychain security:** First-launch date and consent timestamp are stored in the iOS/macOS Keychain, which provides hardware-backed encryption.
- **On-device processing:** All OCR, predictions, and data processing occur locally. No data is transmitted over any network by SageBills.
- **No network access for data:** SageBills does not make network calls to transmit user data. Network access is limited to Apple StoreKit for subscription verification.
- **No third-party code:** Zero external SDKs or libraries, eliminating supply-chain risk.

### Organizational Measures

- **Privacy by design** (Article 25(1)): The local-only architecture was a foundational design decision.
- **Privacy by default** (Article 25(2)): The app processes only the minimum data necessary for its functionality.
- **Data minimization** (Article 5(1)(c)): Only data directly relevant to bill tracking is collected.

## 12. Data Breach Notification

Per **Articles 33 and 34** of the GDPR:

Given that SageBills operates with a local-only architecture and the controller never receives or stores user data on any server, a traditional data breach involving controller-held data is not applicable.

However, should a vulnerability in the app be identified that could compromise data on a user's device:

- We will notify affected users through an app update and, where possible, through an in-app notification.
- We will report the breach to the competent supervisory authority (ANSPDCP) within **72 hours** of becoming aware, where required under Article 33.
- We will communicate the breach to affected data subjects without undue delay where it is likely to result in a high risk to rights and freedoms, per Article 34.

## 13. Children's Data

Per **Article 8** of the GDPR:

SageBills is not directed at children under the age of **16** (the age of consent for information society services in Romania under Article 8(1) GDPR, as implemented nationally).

Since all data is processed locally and we have no access to user data, we cannot verify or identify the age of users. If you believe a child under 16 is using SageBills without parental consent, please contact privacy@sagebills.app.

## 14. Source of Personal Data

Per **Article 14(2)(f)**:

All personal data processed by SageBills is obtained directly from the data subject through:

- Manual data entry within the app.
- OCR scanning of physical invoices initiated by the user.

No personal data is obtained from third-party sources.

## 15. Changes to This Disclosure

Per **Article 13(3)**:

If we intend to process personal data for purposes other than those described in this disclosure, we will provide you with updated information before such processing takes place, in accordance with Article 13(3) of the GDPR.

Any changes to this disclosure will be communicated through:

- An updated "Last Updated" date.
- An in-app notice for material changes.
- An updated version published within the app.

## 16. Supervisory Authority

Per **Article 13(2)(d)** and **Article 14(2)(e)**:

As the controller is based in Romania, the competent supervisory authority is:

**Autoritatea Nationala de Supraveghere a Prelucrarii Datelor cu Caracter Personal (ANSPDCP)**

- **Address:** B-dul G-ral. Gheorghe Magheru 28-30, Sector 1, cod postal 010336, Bucuresti, Romania
- **Phone:** +40.318.059.211 / +40.318.059.212
- **Website:** [www.dataprotection.ro](https://www.dataprotection.ro)
- **Email:** anspdcp@dataprotection.ro

You also have the right to lodge a complaint with the supervisory authority in the EU/EEA Member State of your habitual residence, place of work, or place of the alleged infringement, per **Article 77** of the GDPR.

## 17. Contact

For any questions, requests, or complaints regarding this GDPR disclosure or the processing of your personal data:

- **Email:** privacy@sagebills.app
- **General Support:** support@sagebills.app

We will acknowledge receipt of your inquiry and respond substantively within **30 days**, in accordance with Article 12(3) of the GDPR. If the complexity or volume of requests requires an extension, we will notify you within the initial 30-day period and may extend by a further two months, per Article 12(3).

---

*This disclosure is provided in compliance with Articles 13 and 14 of the General Data Protection Regulation (EU) 2016/679.*

*SageBills -- Your bills, your device, your privacy.*
