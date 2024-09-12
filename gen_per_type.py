import os
import pandas as pd

os.chdir(r"D:\Github\EnergyDataHackdays2024-BalanceEnergyPrices")

os.listdir("data")

df = pd.read_csv("data/generation_per_type_staging.csv")

# Convert the 'datetime' column to a datetime object
df['datetime'] = pd.to_datetime(df['datetime'], utc=True)

# Convert the 'datetime' column back to UTC+1 (e.g., 'Europe/Berlin' timezone)
df['datetime'] = df['datetime'].dt.tz_convert('Europe/Berlin')

# Filter the dataframe for rows where the year is 2024
df_2024 = df[df['datetime'].dt.year == 2024]

# rename for staging data
# Add '_staged' suffix to all columns except 'datetime'
df_2024.columns = ['datetime'] + [col + '_staged' for col in df.columns if col != 'datetime']

df_2024.to_csv("data/clean_data/2024_staged_generation_per_type.csv")





