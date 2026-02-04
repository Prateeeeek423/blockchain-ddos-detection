import pandas as pd
import requests
import time
import numpy as np

API_URL = "http://127.0.0.1:8000/predict"
CSV_FILE = "data/raw/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"

df = pd.read_csv(CSV_FILE)
df.columns = df.columns.str.strip()

# Drop non-numeric & label columns
features_df = df.drop(
    columns=["Flow ID", "Source IP", "Destination IP", "Timestamp", "Label"],
    errors="ignore"
)

# Replace inf, -inf, NaN with 0
features_df = features_df.replace([np.inf, -np.inf], np.nan)
features_df = features_df.fillna(0)

print("Starting offline flow replay...\n")

for index, row in features_df.iterrows():
    features = row.astype(float).values.tolist()

    response = requests.post(
        API_URL,
        json={"features": features}
    )

    if response.status_code == 200:
        result = response.json()

        if result["prediction"] == "DDoS":
            print(f"[ALERT] DDoS detected at flow {index} | Confidence: {result['confidence']}")
        else:
            print(f"[OK] Benign flow {index}")

    time.sleep(0.05)  # simulate near real-time ingestion
