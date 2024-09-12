import os
import pandas as pd

os.chdir(r"D:\Github\EnergyDataHackdays2024-BalanceEnergyPrices")

os.listdir("data")

df = pd.read_csv("data/auction_spot_volumes_switzerland_2024.csv", skiprows=1)

# Summing the columns 'Hour 3A' and 'Hour 3B' in the wide DataFrame
df['Hour 3'] = df[['Hour 3A', 'Hour 3B']].sum(axis=1, skipna=True)

# List of columns to drop  (for prices)
columns_to_drop2 = ['Minimum', 'Maximum', 'Middle-Night', 'Early Morning', 'Late Morning', 
                   'Early Afternoon', 'Rush Hour', 'Off-Peak 2', 'Baseload', 'Peakload', 
                   'Night', 'Off-Peak 1', 'Business', 'Offpeak', 'Morning', 'High Noon', 
                   'Afternoon', 'Evening', 'Sunpeak', "Hour 3A", "Hour 3B"]

columns_to_drop = ["Hour 3A", "Hour 3B", "Total Volume"] ### for volumes


# Drop the columns from the dataframe
df = df.drop(columns=columns_to_drop)

# Function to convert "Hour X" to "XX:00"
def rename_hours(col):
    if col.startswith('Hour'):
        hour_num = int(col.split(' ')[1])
        return f'{hour_num:02d}:00'  # Format to "HH:00"
    return col  # Return other columns unchanged

# Rename columns using the function
df.columns = [rename_hours(col) for col in df.columns]

# Convert the 'Delivery day' column to datetime format
df['Delivery day'] = pd.to_datetime(df['Delivery day'], format='%d/%m/%Y')


df_long = df.melt(id_vars=['Delivery day'], var_name='Time', value_name='Value')


# Convert 'Delivery day' to datetime if not already
df_long['Delivery day'] = pd.to_datetime(df_long['Delivery day'])

# Convert 'Time' column to a timedelta (hours)
df_long['Time'] = pd.to_timedelta(df_long['Time'] + ':00')

# Add 'Time' (timedelta) to 'Delivery day'
df_long['DateTime'] = df_long['Delivery day'] + df_long['Time']

# Create a new dataframe with only 'DateTime' and 'Value' columns
df_final = df_long[['DateTime', 'Value']].copy()

# Rename the columns to 'datetime' and 'eur_mwh' for prices and mwh for volumes
df_final.columns = ['datetime', 'mwh']

# Sort the dataframe by the 'datetime' column
df_final = df_final.sort_values(by='datetime').reset_index(drop=True)

df_final.to_csv("data/clean_data/auction_spot_volumes_switzerland_2024.csv")


