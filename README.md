# HealthShield

**Exploratory Data Security & Responsible Data Handling**

**Scope Statement — Responsible Data Handling Exploration**  
HealthShield is an exploratory project that demonstrates foundational approaches to handling sensitive information in digital systems. It focuses on encryption, hashing, and audit-style techniques to illustrate how basic protective mechanisms can be applied responsibly in context. This repository is intended for learning and demonstration, not production deployment or compliance certification.


> **Live demo:** https://healthshield.streamlit.app/

Simple healthcare data security demo (hashing, encryption, audit log) built with **Streamlit and Python**.

**Goal:** 
Explore how hashing, encryption and audit logs could help protect health related data in a safe, synthetic environment.

---

## Versions

- v0.1 Basic Streamlit app, loads one synthetic patient record from JSON.
- v0.2 Added password hashing demo (SHA-256) to show how raw passwords should not be stored.
- v0.3 Added Fernet-based encryption/decryption demo for a synthetic patient summary.
- v0.4 Added simple in-memory audit log using Streamlit session_state.
- v0.5 Added minimal non-identifying view (data minimisation).
- v0.6 Added suspicious behaviour demo based on multiple decrypt attempts.
- v0.7 Added security warning banner and Security Notes section.

---

## What It Demonstrates

### 1. Password Hashing
- User types a **demo password**  
- App shows a **SHA-256 hash**  
- Explains why systems should store the hash, not the raw password  

### 2. Encryption / Decryption
- Builds a short summary from the fake patient record  
- Encrypts it with **Fernet**  
- Decrypts it back to plain text  
- Highlights that keys should be handled more safely in real systems  

### 3. Audit Logging
- Uses `st.session_state` to append log events  
- Shows a small JSON list of “events” for that session  
- Illustrates the idea of tracking access behaviour  

### 4. Data Minimisation
- Renders a **minimal view** of the record: age + diagnosis only  
- No name, no internal ID  
- This is closer to what some safer UIs might show by default  

### 5. Suspicious Behaviour Alert
- Tracks a counter for “decrypt attempts”  
- After 3 attempts, shows a warning: “Suspicious behaviour detected”  
- Demonstrates the idea of basic anomaly detection (rule-based)
---

## Security Notes

HealthShield is a **demo**, not a production security system.

- Uses synthetic, fake patient data only  
- Hashing and encryption are simplified for teaching purposes  
- Keys and secrets are not stored the way a real system would  
- Do NOT connect this to real hospital systems or patient records

---

## Limitations & Threat Model

This project is designed to **start conversations**, not replace real security work.

Some simplified assumptions:
- Single “demo user” that has no real authentication or identity management  
- Keys are generated in-memory for each demo run and are not persisted securely  
- No database, no network calls and all logic is in memory for teaching  
- No real logging infrastructure or SIEM connection  

Real healthcare systems would need:
- Strong authentication and authorisation  
- Key management (HSMs, key vaults)  
- Encrypted databases and backups  
- Regulatory and compliance reviews (e.g. NHS, GDPR)

---

## Installation & Run

```bash
pip install -r requirements.txt
streamlit run app.py







