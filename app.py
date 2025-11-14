import streamlit as st
import json

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
