# SageBills Privacy Policy

**Last Updated:** April 10, 2026 | **Effective:** April 1, 2026

---

> **In brief:** Your financial data belongs to you, stays with you, and is controlled by you. SageBills is built with a local-only, zero-server architecture. We never see your data.

---

## Key Points

- **100% Local Data** — All your data stays on your device. No servers, no cloud, no exceptions.
- **Zero Tracking** — No analytics, no advertising IDs, no telemetry. We cannot see what you do.
- **No Third Parties** — Built entirely with Apple frameworks. Zero external SDKs or dependencies.
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

Welcome to SageBills. This Privacy Policy explains how SageBills handles your information when you use our utility bill tracking application on iOS and macOS.

This policy complies with the General Data Protection Regulation (GDPR), the ePrivacy Directive, and Apple App Store Guidelines (sections 5.1.1 and 5.1.2).

## 2. Who We Are

SageBills is developed and maintained by a sole proprietor based in Romania, European Union.

- **Privacy inquiries:** privacy@sagebills.app
- **General support:** support@sagebills.app

For the purposes of the GDPR, the developer acts as the data controller. However, because all data processing occurs locally on your device, your data never reaches us.

## 3. Privacy-First Architecture

SageBills is designed with a **local-only, zero-server architecture**:

- **No servers.** We do not operate any backend servers that receive, store, or process your data.
- **No cloud sync.** Your data is not uploaded to any cloud service by SageBills.
- **No analytics.** We do not collect usage analytics, crash reports, or telemetry of any kind.
- **No tracking.** We do not track your behavior, location, or activity.
- **No third-party SDKs.** The app is built entirely with Apple frameworks. Zero external dependencies.

> All data you enter into SageBills remains on your device unless you explicitly choose to export it.

## 4. Data We Process

All of the following data is stored **exclusively on your device**:

### 4.1 Bill Data (User-Entered)

- Bill amounts and currency
- Provider/utility company names
- Bill categories (electricity, gas, water, internet, etc.)
- Bill dates (issue date, due date)
- Notes you add to bills
- Consumption readings (kWh, cubic meters, etc.)

### 4.2 OCR-Scanned Data

When you scan an invoice, Apple's Vision framework extracts text **entirely on your device**. This may include bill amounts, provider names, account numbers, and service addresses. The original image is not retained after scanning unless you choose otherwise.

### 4.3 App Preferences and Settings

- Currency and display preferences
- Notification preferences
- Savings goals configuration
- Onboarding and consent status

### 4.4 Subscription Status

Managed entirely by Apple through StoreKit. SageBills reads your subscription status to unlock features but does not store payment details.

### 4.5 Keychain Data

SageBills stores two non-personal items in the device Keychain:

- **First-launch date:** Used to calculate the 90-day free grace period.
- **GDPR consent date:** Stored for tamper detection to ensure consent integrity.

No personal data is stored in the Keychain.

### 4.6 Spotlight Index

Bill records are indexed in Apple's CoreSpotlight for device search. This index is local to your device and managed by the operating system.

## 5. How We Use Your Data

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

## 6. Legal Basis for Processing

Under Article 6(1)(a) of the GDPR, our legal basis for processing your data is **your explicit consent**, which you provide during the app's onboarding process.

You may withdraw your consent at any time through the app's Settings. Withdrawal does not affect the lawfulness of processing carried out before the withdrawal.

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

### 9.1 Apple App Store and StoreKit

SageBills offers optional subscriptions managed through Apple's App Store. Payment processing is handled entirely by Apple. SageBills does not receive or store your payment information.

Apple's handling of your payment data is governed by [Apple's Privacy Policy](https://www.apple.com/legal/privacy/).

### 9.2 No Other Third Parties

SageBills contains **no third-party SDKs, frameworks, libraries, or services**. We do not share, sell, or disclose your data to any third party.

## 10. International Data Transfers

SageBills does not transfer your data internationally. Your data remains on your device at all times.

## 11. Cookies and Tracking

SageBills does not use cookies, web beacons, pixels, device fingerprinting, advertising identifiers, or any other tracking technology. The app does not contain any advertising.

## 12. Your Rights Under GDPR

As a resident of the EU or EEA, you have the following rights:

| Right | How to Exercise |
|---|---|
| **Right of access** (Art. 15) | View all your data directly in the app |
| **Right to rectification** (Art. 16) | Edit any bill or data entry within the app |
| **Right to erasure** (Art. 17) | Delete individual bills or all data via Settings |
| **Right to restriction** (Art. 18) | Contact privacy@sagebills.app |
| **Right to portability** (Art. 20) | Export your data as CSV from within the app |
| **Right to object** (Art. 21) | Withdraw consent in Settings |
| **Withdraw consent** (Art. 7(3)) | Single action in Settings, takes effect immediately |
| **Lodge a complaint** (Art. 77) | Contact your national data protection authority |

Most rights can be exercised directly within the app. For other rights, email privacy@sagebills.app.

### Supervisory Authority

If you are in Romania, the competent authority is **ANSPDCP** ([www.dataprotection.ro](https://www.dataprotection.ro)). You may also contact the authority in your country of residence.

## 13. Children's Privacy

SageBills is not directed at children under 16. We do not knowingly process data from children. Since all data is stored locally, we have no means to identify or verify user age.

## 14. Changes to This Policy

We may update this Privacy Policy from time to time. The "Last Updated" date will be revised, and material changes will be communicated through an in-app notice.

## 15. Contact Us

- **Privacy inquiries:** privacy@sagebills.app
- **General support:** support@sagebills.app

We aim to respond to all privacy-related inquiries within 30 days, as required by the GDPR.

---

*Sage**Bills** — Your bills, your device, your privacy.*

*Built with care in Romania, EU*
