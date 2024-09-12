import os
import pandas as pd

os.chdir(r"D:\Github\EnergyDataHackdays2024-BalanceEnergyPrices")

os.listdir("data")

df = pd.read_csv("data/balancing_prices_2024.csv")

# Convert the 'Datum' column to datetime format
df['Datum'] = pd.to_datetime(df['Datum'], format='%d.%m.%Y %H:%M')

# Convert the 'Datum' column to datetime format if not already done
df['Datum'] = pd.to_datetime(df['Datum'], format='%d.%m.%Y %H:%M')

# Set 'Datum' as the index to use resampling
df.set_index('Datum', inplace=True)

# Resample the data by hour and apply aggregation (mean in this case)
df_hourly = df.resample('H').mean().reset_index()

df_hourly.to_csv("data/clean_data/hourly_balancing_prices_2024.csv")
