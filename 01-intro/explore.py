import pandas as pd

# --- Load ---
url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"
df = pd.read_parquet(url)

print("Rows, Columns:", df.shape)
print("Columns:", df.columns.tolist())

# --- Compute duration in minutes ---
df['duration'] = df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']
df['duration'] = df['duration'].dt.total_seconds() / 60

print("Std of duration (minutes):", df['duration'].std())

# --- Filter outliers ---
original_count = len(df)

df_filtered = df[(df['duration'] >= 1) & (df['duration'] <= 60)]

filtered_count = len(df_filtered)
fraction_kept = filtered_count / original_count

print(f"Rows before filtering: {original_count}")
print(f"Rows after filtering: {filtered_count}")
print(f"Fraction kept: {fraction_kept:.4f} ({fraction_kept * 100:.2f}%)")