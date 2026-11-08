
import requests
import pandas as pd
from pathlib import Path

# Lucknow coordinates
LATITUDE = 26.8467
LONGITUDE = 80.9462

START_DATE = "20150101"
END_DATE = "20251231"

PARAMETERS = [
    "ALLSKY_SFC_SW_DWN",
    "T2M",
    "T2M_MAX",
    "T2M_MIN",
    "RH2M",
    "WS10M",
    "PRECTOTCORR"
]

url = "https://power.larc.nasa.gov/api/temporal/daily/point"

params = {
    "parameters": ",".join(PARAMETERS),
    "community": "RE",
    "longitude": LONGITUDE,
    "latitude": LATITUDE,
    "start": START_DATE,
    "end": END_DATE,
    "format": "JSON"
}

print("Downloading NASA POWER data...")

response = requests.get(url, params=params, timeout=60)
response.raise_for_status()

data = response.json()

solar_data = data["properties"]["parameter"]

df = pd.DataFrame(solar_data)

# Convert date index
df.index = pd.to_datetime(df.index, format="%Y%m%d")
df.index.name = "DATE"

df = df.reset_index()

# Add location information
df["CITY"] = "Lucknow"
df["STATE"] = "Uttar Pradesh"

# Handle NASA missing-value codes
df.replace(-999, pd.NA, inplace=True)

# Save dataset
Path("data/raw").mkdir(parents=True, exist_ok=True)

df.to_csv(
    "data/raw/lucknow_solar_data.csv",
    index=False
)

print("\nDownload successful!")
print(df.head())
print("\nDataset shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum())
