import streamlit as st
import json
import hashlib
from cryptography.fernet import Fernet



st.set_page_config(page_title="HealthShield • v0.1", layout="centered")

st.title("HealthShield: Healthcare Data Security Demo (v0.1)")
st.caption("Synthetic demo • Not for clinical use")

st.subheader("Welcome")
st.write(
    "HealthShield is a tiny demo app that explores how we might protect "
    "health data using hashing, encryption and audit logs."
)

st.subheader("Demo patient record (raw JSON)")
try:
    with open("data/test_patient.json", "r") as f:
        patient = json.load(f)
    st.json(patient)
except FileNotFoundError:
    st.error("test_patient.json not found. Please check the data/ folder.")
st.subheader("Password Hashing Demo (v0.2)")

st.write(
    "This simple demo shows how we never store raw passwords. "
    "Instead, we store a hash."
)

password_input = st.text_input("Enter a demo password", type="password")

if password_input:
    hash_obj = hashlib.sha256(password_input.encode())
    hex_digest = hash_obj.hexdigest()
    st.write("Hashed password (SHA-256, hex):")
    st.code(hex_digest)
    st.info("In a real system, only the hash is stored, not the password itself.")
else:
    st.caption("Type a demo password above to see its hash.")

st.subheader("Encryption Demo (v0.3)")

st.write(
    "Here we show how a simple symmetric key can encrypt and decrypt a small record. "
    "This is a demo, not production crypto."
)

# In a real system the key would be stored securely (e.g. environment variable or key vault)
key = Fernet.generate_key()
cipher = Fernet(key)

# Build a small string from our fake test patient record
try:
    patient_summary = f"ID={patient['patient_id']}, Dx={patient['diagnosis']}, Age={patient['age']}"
except Exception:
    patient_summary = "ID=P-001, Dx=Hypertension, Age=45"

st.write("Original (plaintext) summary:")
st.code(patient_summary)

encrypted = cipher.encrypt(patient_summary.encode())
st.write("Encrypted:")
st.code(encrypted)

decrypted = cipher.decrypt(encrypted).decode()
st.write("Decrypted again:")
st.code(decrypted)

st.info("In reality, the key would not be regenerated on each run and would never be exposed in the app.")

st.subheader("Minimal Info View (v0.5)")

st.write(
    "Real systems often use data minimisation: show only what is necessary. "
    "Here we show a minimal, non-identifying view of the record."
)

try:
    minimal_view = {
        "age": patient["age"],
        "diagnosis": patient["diagnosis"]
    }
except Exception:
    minimal_view = {"age": 45, "diagnosis": "Hypertension"}

st.json(minimal_view)
st.caption("No name or internal ID: this is safer to show in some contexts.")

st.subheader("Audit Log (v0.4)")

if "audit_log" not in st.session_state:
    st.session_state.audit_log = []

# Log that the user has visited the page
st.session_state.audit_log.append(
    {"event": "view_page", "section": "main", "user": "demo-user"}
)

st.write(f"Audit log entries this session: {len(st.session_state.audit_log)}")
st.json(st.session_state.audit_log[-5:])
