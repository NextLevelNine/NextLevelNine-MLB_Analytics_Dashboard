import pandas as pd
import os

# Set working directory to script's location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load datasets
statcast = pd.read_csv('camilo_doval_5yr_statcast.csv')
fangraphs = pd.read_csv('doval_advanced_stats.csv')

# Preprocess Statcast: Extract season from game_date
statcast['game_date'] = pd.to_datetime(statcast['game_date'], errors='coerce')
statcast['Season'] = statcast['game_date'].dt.year

# Aggregate Statcast to season level
statcast_summary = statcast.groupby('Season').agg({
    'release_speed': 'mean',
    'release_spin_rate': 'mean',
    'release_extension': 'mean'
}).reset_index()

# Round for readability
statcast_summary = statcast_summary.round(2)

# Merge with FanGraphs data on 'Season'
merged = pd.merge(fangraphs, statcast_summary, on='Season', how='left')

# Save merged dataset
merged.to_csv('doval_complete_profile.csv', index=False)
print('Merged dataset saved to doval_complete_profile.csv')
