import pandas as pd
import warnings
from pybaseball import fangraphs_pitcher_leaders

# Silence warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Camilo Doval's FanGraphs ID
doval_id = 21992

# Pull 2023 pitching leaderboard from FanGraphs
print('✅ Checking if Camilo Doval appears in FanGraphs 2023 data...')
df = fangraphs_pitcher_leaders(2023, 2023)

# Preview to confirm
print(df[df['Name'].str.contains('Doval', case=False)])

# Filter by his ID
doval_stats = df[df['IDfg'] == doval_id]

# Print and save
print('\n✅ Camilo Doval - Season Stats (FanGraphs style)')
print(doval_stats)

doval_stats.to_csv('doval_advanced_stats.csv', index=False)
print('\n💾 Saved to doval_advanced_stats.csv')
