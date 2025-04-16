import os
import pandas as pd
import matplotlib.pyplot as plt

# Make script always run from its own folder
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Load dataset from same folder
df = pd.read_csv("camilo_doval_5yr_statcast.csv")


# Make sure the script always runs from its own folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load the dataset
df = pd.read_csv("camilo_doval_5yr_statcast.csv")

# Convert game_date to datetime and extract the year
df['game_date'] = pd.to_datetime(df['game_date'], errors='coerce')
df['year'] = df['game_date'].dt.year

# Group and average velocity and spin rate
velocity_spin = df.groupby('year')[['release_speed', 'release_spin_rate']].mean()

# Pitch usage by count and percent
pitch_counts = df.groupby(['year', 'pitch_type']).size().unstack(fill_value=0)
pitch_percent = pitch_counts.div(pitch_counts.sum(axis=1), axis=0) * 100

# Average release extension per year
extension_summary = df.groupby('year')['release_extension'].mean()

# Whiff rate calculation
df['description'] = df['description'].fillna('')
df['swinging'] = df['description'].str.contains('swing', case=False)
df['whiff'] = df['description'] == 'swinging_strike'
swing_data = df[df['swinging']]
whiff_rate = swing_data.groupby('year')['whiff'].mean()

# Plot: Velocity and Spin Rate
velocity_spin.plot(marker='o', title="Camilo Doval - Avg Velocity & Spin Rate by Year")
plt.xlabel("Year")
plt.ylabel("Average")
plt.grid(True)
plt.tight_layout()
plt.savefig("velocity_spin.png")
plt.show()
plt.close()

# Plot: Pitch Usage Percentages
pitch_percent.plot(kind='bar', stacked=True, title="Camilo Doval - Pitch Usage % by Year")
plt.ylabel("Percentage (%)")
plt.xlabel("Year")
plt.legend(title="Pitch Type", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("pitch_usage_percent.png")
plt.show()
plt.close()

# Plot: Release Extension
extension_summary.plot(marker='o', color='green', title="Camilo Doval - Avg Release Extension by Year")
plt.ylabel("Release Extension (ft)")
plt.xlabel("Year")
plt.grid(True)
plt.tight_layout()
plt.savefig("release_extension.png")
plt.show()
plt.close()

# Plot: Whiff Rate
whiff_rate.plot(marker='o', color='red', title="Camilo Doval - Whiff Rate by Year")
plt.ylabel("Whiff Rate")
plt.xlabel("Year")
plt.grid(True)
plt.tight_layout()
plt.savefig("whiff_rate.png")
plt.show()
plt.close()

#This should be displayed when done
print ('We are done. Thank you!')


