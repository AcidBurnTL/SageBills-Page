# SageBills Privacy Policy

**Last Updated:** April 10, 2026
**Effective Date:** April 1, 2026

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Who We Are](#2-who-we-are)
3. [Our Privacy-First Architecture](#3-our-privacy-first-architecture)
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

Welcome to SageBills. We built this app with a fundamental belief: your financial data belongs to you, stays with you, and is controlled by you. This Privacy Policy explains how SageBills handles your information when you use our utility bill tracking application on iOS and macOS.

We encourage you to read this policy carefully. It complies with the General Data Protection Regulation (GDPR), the ePrivacy Directive, and Apple App Store Guidelines (sections 5.1.1 and 5.1.2).

## 2. Who We Are

SageBills is developed and maintained by an individual developer / sole proprietor based in Romania, European Union.

- **Contact Email (Privacy):** privacy@sagebills.app
- **Contact Email (General):** support@sagebills.app

For the purposes of the GDPR, the developer of SageBills acts as the data controller. However, because all data processing occurs locally on your device, your data never reaches us.

## 3. Our Privacy-First Architecture

SageBills is designed with a **local-only, zero-server architecture**. This means:

- **No servers.** We do not operate any backend servers that receive, store, or process your data.
- **No cloud sync.** Your data is not uploaded to any cloud service by SageBills.
- **No analytics.** We do not collect usage analytics, crash reports, or telemetry of any kind.
- **No tracking.** We do not track your behavior, location, or activity.
- **No third-party SDKs.** The app is built entirely with Apple frameworks. There are zero external dependencies.

All data you enter into SageBills remains on your device unless you explicitly choose to export it.

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

When you use the invoice scanning feature, SageBills uses Apple's Vision framework to extract text from photos of your bills. This processing happens **entirely on your device**. Scanned text may include:

- Bill amounts and dates
- Provider names and details
- Account numbers
- Service addresses
- Other text present on the invoice

Scanned text is stored locally on your device alongside the corresponding bill record. The original image is not retained after scanning unless you choose otherwise.

### 4.3 App Preferences and Settings

- Your chosen currency and display preferences
- Notification preferences (due date reminders)
- Savings goals configuration
- Onboarding and consent status

### 4.4 Subscription Status

Subscription purchase and status information is managed entirely by Apple through StoreKit and the App Store. SageBills reads your subscription status from StoreKit to unlock features but does not store payment details.

### 4.5 Keychain Data

SageBills stores two non-personal items in the device Keychain:

- **First-launch date:** Used to calculate the 90-day free grace period and prevent abuse.
- **GDPR consent date:** Stored for tamper detection to ensure the integrity of your consent record.

No personal data is stored in the Keychain.

### 4.6 Spotlight Index

Bill records are indexed in Apple's CoreSpotlight so you can find them using device search. This index is local to your device and managed by the operating system.

## 5. How We Use Your Data

Because all data stays on your device, "use" means local processing within the app. SageBills processes your data for the following purposes:

| Purpose | Description |
|---|---|
| **Bill tracking** | Displaying, organizing, and managing your utility bills |
| **Cost prediction** | Generating statistical predictions of future bills based on your history |
| **Anomaly detection** | Identifying unusual bills that deviate from your typical patterns |
| **Savings tracking** | Calculating progress toward your savings goals |
| **Invoice scanning** | Extracting bill data from photos using on-device OCR |
| **Reminders** | Sending local notifications for upcoming bill due dates |
| **Data export** | Generating CSV files of your bill data when you request it |
| **Device search** | Making your bills findable through Spotlight search |

## 6. Legal Basis for Processing

Under Article 6(1)(a) of the GDPR, our legal basis for processing your data is **your explicit consent**, which you provide during the app's onboarding process.

You may withdraw your consent at any time through the app's Settings. Withdrawing consent will result in the deletion of all your data from the app. Withdrawal of consent does not affect the lawfulness of processing carried out before the withdrawal.

## 7. Data Storage and Security

### 7.1 Local Storage

All data is stored on your device using Apple's **SwiftData** framework. Data files are protected with **NSFileProtectionComplete**, which means:

- Data is encrypted when your device is locked.
- Data is only accessible when your device is unlocked and authenticated.
- Encryption keys are tied to your device passcode/biometrics.

### 7.2 No Remote Storage

SageBills does not transmit your data to any remote server, database, or cloud service. We have no ability to access, read, or recover your data.

### 7.3 Your Responsibility

Because data is stored only on your device, **you are responsible for maintaining backups** through your device's backup mechanisms (e.g., iCloud device backup, local Mac backup). If you delete the app or lose your device, your SageBills data cannot be recovered by us.

## 8. Data Retention

Your data is retained on your device for as long as you keep the app installed and choose to retain it. You have full control:

- **Delete individual bills** at any time within the app.
- **Delete all data** using the "Delete All Data" option in Settings.
- **Uninstall the app** to remove all associated data from your device.

We do not retain any copy of your data because we never receive it.

## 9. Third-Party Services

### 9.1 Apple App Store and StoreKit

SageBills offers optional subscriptions managed through Apple's App Store. When you make a purchase:

- Payment processing is handled entirely by Apple.
- SageBills does not receive or store your payment information, billing address, or Apple ID.
- SageBills only receives subscription status information (active, expired, etc.) through Apple's StoreKit framework.
- Apple's handling of your payment data is governed by [Apple's Privacy Policy](https://www.apple.com/legal/privacy/).

### 9.2 No Other Third Parties

SageBills contains **no third-party SDKs, frameworks, libraries, or services**. The app is built entirely with Apple-provided frameworks. We do not share, sell, or disclose your data to any third party because we never have access to it.

## 10. International Data Transfers

SageBills does not transfer your data internationally or across borders. Your data remains on your device at all times. The only exception is if you personally move your device to a different country, which is outside our control and responsibility.

## 11. Cookies and Tracking

SageBills does not use cookies, web beacons, pixels, device fingerprinting, advertising identifiers, or any other tracking technology. The app does not contain any advertising.

## 12. Your Rights Under GDPR

As a resident of the European Union or European Economic Area, you have the following rights regarding your personal data:

| Right | How to Exercise in SageBills |
|---|---|
| **Right of access** (Art. 15) | View all your data directly in the app at any time |
| **Right to rectification** (Art. 16) | Edit any bill or data entry within the app |
| **Right to erasure** (Art. 17) | Delete individual bills or all data via Settings |
| **Right to restriction** (Art. 18) | Contact us at privacy@sagebills.app |
| **Right to data portability** (Art. 20) | Export your data as CSV from within the app |
| **Right to object** (Art. 21) | Withdraw consent in Settings, which deletes all data |
| **Right to withdraw consent** (Art. 7(3)) | Withdraw consent at any time in Settings |
| **Right to lodge a complaint** | Contact your national data protection authority |

Because all data is stored locally on your device, you can exercise most of these rights directly within the app without needing to contact us. For any rights you cannot exercise through the app, please contact us at privacy@sagebills.app.

### Supervisory Authority

If you are in Romania, the competent supervisory authority is:

**ANSPDCP** (Autoritatea Nationala de Supraveghere a Prelucrarii Datelor cu Caracter Personal)
Website: [www.dataprotection.ro](https://www.dataprotection.ro)

You may also contact the supervisory authority in your country of residence.

## 13. Children's Privacy

SageBills is not directed at children under the age of 16. We do not knowingly process data from children under 16. Since all data is stored locally and we never receive any user data, we have no means to identify or verify the age of users. If you believe a child under 16 is using SageBills, please contact us at privacy@sagebills.app.

## 14. Changes to This Policy

We may update this Privacy Policy from time to time. When we make changes:

- The "Last Updated" date at the top of this policy will be revised.
- For material changes, we will notify you through an in-app notice.
- Continued use of SageBills after changes take effect constitutes acceptance of the revised policy.

We encourage you to review this policy periodically.

## 15. Contact Us

If you have questions, concerns, or requests regarding this Privacy Policy or your personal data, please contact us:

- **Privacy inquiries:** privacy@sagebills.app
- **General support:** support@sagebills.app

We aim to respond to all privacy-related inquiries within 30 days, as required by the GDPR.

---

*SageBills -- Your bills, your device, your privacy.*
