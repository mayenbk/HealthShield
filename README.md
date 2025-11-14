# HealthShield

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







