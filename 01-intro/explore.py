import pandas as pd

url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"
df = pd.read_parquet(url)

print("Rows, Columns:", df.shape)
print("Columns:", df.columns.tolist())

df['duration'] = df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']
df['duration'] = df['duration'].dt.total_seconds() / 60

print("Std of duration (minutes):", df['duration'].std())