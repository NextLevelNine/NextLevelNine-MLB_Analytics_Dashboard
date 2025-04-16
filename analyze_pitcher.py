import pandas as pd

def analyze_pitcher(csv_file):
    # Load Statcast CSV
    df = pd.read_csv(csv_file)

    # Convert game_date to datetime and extract year
    df['game_date'] = pd.to_datetime(df['game_date'], errors='coerce')
    df['year'] = df['game_date'].dt.year

    # 1. Velocity & Spin Rate
    velocity_spin = df.groupby('year')[['release_speed', 'release_spin_rate']].mean().round(2)

    # 2. Pitch Usage (% by year)
    pitch_counts = df.groupby(['year', 'pitch_type']).size().unstack(fill_value=0)
    pitch_percent = (pitch_counts.div(pitch_counts.sum(axis=1), axis=0) * 100).round(1)

    # 3. Release Extension
    release_extension = df.groupby('year')['release_extension'].mean().round(2)

    # 4. Whiff Rate
    df['description'] = df['description'].fillna('')
    df['swinging'] = df['description'].str.contains('swing', case=False)
    df['whiff'] = df['description'] == 'swinging_strike'
    whiff_data = df[df['swinging']]
    whiff_rate = whiff_data.groupby('year')['whiff'].mean().round(3)

    return {
        'velocity_spin': velocity_spin,
        'pitch_percent': pitch_percent,
        'release_extension': release_extension,
        'whiff_rate': whiff_rate
    }

# Example usage (test it in the terminal)
if __name__ == '__main__':
    results = analyze_pitcher('camilo_doval_5yr_statcast.csv')
    for name, df in results.items():
        print(f"\n--- {name.replace('_', ' ').title()} ---")
        print(df)

