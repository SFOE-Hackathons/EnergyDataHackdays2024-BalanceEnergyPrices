import os
import pandas as pd

os.chdir(r"D:\Github\EnergyDataHackdays2024-BalanceEnergyPrices")

os.listdir("data")

df = pd.read_csv("data/kalender_2024_ch.csv")



# Convert 'Datum' to datetime format
df['Datum'] = pd.to_datetime(df['Datum'], format='%d.%m.%Y')

# Expand the dataframe for each hour (24 hours per day)
df_expanded = df.loc[df.index.repeat(24)].copy()

# Create a new 'Hour' column (repeated for each hour in a day)
df_expanded['Hour'] = [f'{hour:02d}:00:00' for hour in range(24)] * len(df)

# Combine 'Datum' and 'Hour' to get a full hourly timestamp
df_expanded['Datetime'] = df_expanded['Datum'] + pd.to_timedelta(df_expanded['Hour'])

# Rearrange columns and drop the 'Hour' column if not needed
df_expanded = df_expanded[['Datetime', 'Tag', 'Feiertag']]

df_expanded.to_csv("data/clean_data/hourly_calendar_2024_ch.csv")
