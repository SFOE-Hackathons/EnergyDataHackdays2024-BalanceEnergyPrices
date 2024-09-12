import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates

# Get Generation per type data
gpt = pd.read_csv('data/generation_per_type.csv')


gpt['datetime'] = pd.to_datetime(gpt['datetime'])
gpt['datetime'] = gpt['datetime'].apply(lambda x: x.tz_localize(None)) # Remove UCT

gpt['datetime'] = gpt['datetime'].dt.floor('H')
gpt = gpt[~(gpt['datetime'] < '2024-01-01')]

# Get Balancing prices
sl = pd.read_csv('data/balancing_prices_2024.csv')

sl['Datum'] = pd.to_datetime(sl['Datum'], dayfirst=True)

# Resample by hour and calculate medians
sl = sl.resample('h', on='Datum').mean()

# Create plot

fig, ax = plt.subplots()
ax2 = ax.twinx()

ax.stackplot(gpt['datetime'], [gpt["Nuclear"],gpt["Hydro_Run_of_river_and_poundage"],gpt["Solar"],gpt["Hydro_Pumped_Storage"],gpt["Hydro_Water_Reservoir"]], alpha=0.5)

# If we want to display each generator type individually
# for parameter in ["Hydro_Run_of_river_and_poundage", "Hydro_Water_Reservoir", "Nuclear", "Solar"]:
#     ax.plot(gpt['datetime'], gpt[parameter], label=parameter, alpha=0.6)



ax2.plot(sl.index, sl['short_ct/kWh'], color='red', label="short_ct/kWh")
ax2.plot(sl.index, sl['long_ct/kWh'], color='green', label="long_ct/kWh")

ax.legend(["Nuclear", "Hydro_Run_of_river_and_poundage", "Solar", "Hydro_Pumped_Storage", "Hydro_Water_Reservoir"])
ax2.legend()
# This is required to see the full date when hovering over with the mouse
ax.fmt_xdata = matplotlib.dates.DateFormatter("%H:00-%d-%b-%Y")
ax2.fmt_xdata = matplotlib.dates.DateFormatter("%H:00-%d-%b-%Y")


plt.grid()

plt.show()
