import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from pybaseball import playerid_lookup, statcast_pitcher
import pandas as pd

# This program looks up Camilo Doval’s MLB player ID
player_info = playerid_lookup('Doval', 'Camilo')
print(player_info)

# This program uses the MLBAM ID (from the lookup table above)
# The ID is stored in the 'key_mlbam' column
doval_id = int(player_info.loc[0, 'key_mlbam'])

# This program initializes an empty DataFrame to collect all years
all_data = pd.DataFrame()

# This program loops over each year and pull pitch-level data from Statcast
for year in range(2020, 2026):  # Includes 2020–2025
    print(f"Fetching data for {year}...")
    season_data = statcast_pitcher(f"{year}-03-01", f"{year}-10-31", player_id=doval_id)
    all_data = pd.concat([all_data, season_data], ignore_index=True)

# This program saves the full dataset to CSV
all_data.to_csv("camilo_doval_5yr_statcast.csv", index=False)
print("Data saved to camilo_doval_5yr_statcast.csv")
