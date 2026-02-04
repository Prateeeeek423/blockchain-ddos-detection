import pandas as pd

df = pd.read_csv("data/raw/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")

df.columns = df.columns.str.strip()

print("Rows:", df.shape[0])
print("Label counts:")
print(df["Label"].value_counts())
