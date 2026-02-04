import streamlit as st
import requests
import pandas as pd
import numpy as np

API_BASE = "http://127.0.0.1:8000"

st.set_page_config(page_title="DDoS Detection Dashboard", layout="wide")

st.title("DDoS Detection & Security Monitoring Dashboard")

# ===============================
# SINGLE FLOW DETECTION
# ===============================
st.header("🔍 Single Flow Detection")

features_input = st.text_area(
    "Enter flow features (comma separated numeric values only)",
    "0,0,0,0,0"
)

if st.button("Detect"):
    raw_values = features_input.split(",")

    features = []
    for val in raw_values:
        try:
            features.append(float(val.strip()))
        except:
            pass

    if len(features) == 0:
        st.error("No valid numeric features provided.")
    else:
        response = requests.post(
            f"{API_BASE}/predict",
            json={"features": features}
        )

        if response.status_code == 200:
            result = response.json()
            st.success(f"Prediction: {result['prediction']}")
            st.info(f"Confidence: {result['confidence']}")
        else:
            st.error("API error during prediction.")

# ===============================
# FILE UPLOAD (BATCH DETECTION)
# ===============================
st.divider()
st.header("📂 Upload Flow File for Batch DDoS Detection")

uploaded_file = st.file_uploader(
    "Upload CSV file with flow features",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip()

    st.subheader("Preview of uploaded data")
    st.dataframe(df.head())

    df_features = df.drop(
        columns=["Flow ID", "Source IP", "Destination IP", "Timestamp", "Label"],
        errors="ignore"
    )

    df_features = df_features.replace([np.inf, -np.inf], np.nan)
    df_features = df_features.fillna(0)

    if st.button("Run Batch Detection"):
        ddos_count = 0
        benign_count = 0

        for _, row in df_features.iterrows():
            features = row.astype(float).values.tolist()

            response = requests.post(
                f"{API_BASE}/predict",
                json={"features": features}
            )

            if response.status_code == 200:
                result = response.json()
                if result["prediction"] == "DDoS":
                    ddos_count += 1
                else:
                    benign_count += 1

        st.success("Batch detection completed")
        st.metric("DDoS Flows Detected", ddos_count)
        st.metric("Benign Flows", benign_count)

# ===============================
# LEDGER VIEW
# ===============================
st.divider()
st.header("📜 Security Event Ledger")

ledger_response = requests.get(f"{API_BASE}/ledger")

if ledger_response.status_code == 200:
    ledger = ledger_response.json()
    st.metric("Total Logged DDoS Events", ledger["total_events"])

    if ledger["events"]:
        st.dataframe(ledger["events"])
    else:
        st.info("No DDoS events logged yet.")
else:
    st.error("Unable to fetch ledger.")

# ===============================
# LEDGER INTEGRITY CHECK
# ===============================
st.divider()
st.header("🔐 Ledger Integrity Verification")

verify_response = requests.get(f"{API_BASE}/ledger/verify")

if verify_response.status_code == 200:
    verify = verify_response.json()
    if verify.get("valid"):
        st.success("Ledger integrity verified. No tampering detected.")
    else:
        st.error(f"Integrity violation: {verify.get('error')}")
else:
    st.error("Unable to verify ledger integrity.")
