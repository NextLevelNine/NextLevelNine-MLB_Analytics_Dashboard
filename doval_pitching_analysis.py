import pandas as pd

# Step 1: Load the saved Statcast CSV
df = pd.read_csv("camilo_doval_5yr_statcast.csv")

# Step 2: Convert game_date to datetime and extract the year
df['game_date'] = pd.to_datetime(df['game_date'], errors='coerce')
df['year'] = df['game_date'].dt.year

# Step 3: Create swing-related columns for whiff rate analysis
df['description'] = df['description'].fillna('')
df['swinging'] = df['description'].str.contains('swing', case=False)
df['whiff'] = df['description'] == 'swinging_strike'

# =========================
# SUMMARY 1: Velocity & Spin
# =========================
print("\n--- Yearly Averages: Velocity & Spin Rate ---")
velocity_spin = df.groupby('year')[['release_speed', 'release_spin_rate']].mean().round(2)
print(velocity_spin)

# =========================
# SUMMARY 2: Pitch Usage
# =========================
print("\n--- Pitch Usage by Year ---")
pitch_counts = df.groupby(['year', 'pitch_type']).size().unstack(fill_value=0)
pitch_percent = pitch_counts.div(pitch_counts.sum(axis=1), axis=0).round(3) * 100

print("Pitch Counts:")
print(pitch_counts)
print("\nPitch Percentages (%):")
print(pitch_percent)

# =========================
# SUMMARY 3: Release Extension
# =========================
print("\n--- Average Release Extension by Year ---")
extension_summary = df.groupby('year')['release_extension'].mean().round(2)
print(extension_summary)

# =========================
# SUMMARY 4: Whiff Rate
# =========================
print("\n--- Whiff Rate by Year ---")
swing_data = df[df['swinging']].copy()

# Group by year
grouped = swing_data.groupby('year')

# Calculate whiff rate per year
whiff_rate_by_year = {}
for year, group in grouped:
    total_swings = len(group)
    total_whiffs = group['whiff'].sum()
    whiff_rate = round(total_whiffs / total_swings, 3)
    whiff_rate_by_year[year] = whiff_rate

# Create DataFrame from dictionary
whiff_rate_df = pd.DataFrame.from_dict(whiff_rate_by_year, orient='index', columns=['whiff_rate'])
print(whiff_rate_df)

# =========================
# OPTIONAL: Save results
# =========================
velocity_spin.to_csv("doval_velocity_spin_by_year.csv")
pitch_percent.to_csv("doval_pitch_usage_percent_by_year.csv")
extension_summary.to_csv("doval_release_extension_by_year.csv")
whiff_rate_df.to_csv("doval_whiff_rate_by_year.csv")

print("\n Analysis complete. Summary files saved.")
