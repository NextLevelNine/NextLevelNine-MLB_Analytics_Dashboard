import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Import visual header, body content, and footer
from doval_intro import project_intro, main_content, footer_content

# Set up page config
st.set_page_config(page_title='📊 MLB Pitching Dashboard', page_icon='⚾', layout='wide')

# Header + Title
st.markdown(project_intro, unsafe_allow_html=True)

# Divider
st.markdown('---')

# Project Summary: Purpose & Overview
st.markdown(main_content, unsafe_allow_html=True)

# Divider
st.markdown('---')

# Load data
file_path = 'camilo_doval_5yr_statcast.csv'
df = pd.read_csv(file_path)
df['game_date'] = pd.to_datetime(df['game_date'], errors='coerce')
df['year'] = df['game_date'].dt.year

# -----------------------------
# Velocity & Spin Rate
# -----------------------------
st.header('Velocity & Spin Rate by Year')
st.markdown('* **Release Speed (MPH):** Pitch speed out of the hand')
st.markdown('* **Spin Rate (RPM):** Rotations per minute. Higher spin increases pitch movement.')

velocity_spin = df.groupby('year')[['release_speed', 'release_spin_rate']].mean().round(2)
st.dataframe(velocity_spin)

fig1, ax1 = plt.subplots(figsize=(6, 3))
velocity_spin.plot(marker='o', ax=ax1)
plt.title('Velocity & Spin Rate by Year')
plt.xlabel('Year')
plt.ylabel('Average')
plt.grid(True)
st.pyplot(fig1)

# -----------------------------
# Pitch Usage
# -----------------------------
st.header('Pitch Usage Percentages by Year')
st.markdown('Pitch Mix by Type: SL (Slider), FC (Cutter), FF (4-Seamer), SI (Sinker)')

pitch_counts = df.groupby(['year', 'pitch_type']).size().unstack(fill_value=0)
pitch_percent = pitch_counts.div(pitch_counts.sum(axis=1), axis=0).round(3) * 100
st.dataframe(pitch_percent)

fig2, ax2 = plt.subplots(figsize=(6, 3))
pitch_percent.plot(kind='bar', stacked=True, ax=ax2)
plt.title('Pitch Usage Percentages by Year')
plt.ylabel('Percentage (%)')
plt.xlabel('Year')
plt.legend(title='Pitch Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
st.pyplot(fig2)

# -----------------------------
# Release Extension
# -----------------------------
st.header('Average Release Extension by Year')
st.markdown('* Measures how far in front of the mound Doval releases the ball.')

extension_summary = df.groupby('year')['release_extension'].mean().round(2)
st.dataframe(extension_summary)

fig3, ax3 = plt.subplots(figsize=(6, 3))
extension_summary.plot(marker='o', color='green', ax=ax3)
plt.title('Release Extension by Year')
plt.ylabel('Feet')
plt.xlabel('Year')
plt.grid(True)
st.pyplot(fig3)

# -----------------------------
# Whiff Rate
# -----------------------------
st.header('Whiff Rate by Year')
st.markdown('* A **whiff** is a swing-and-miss.')
st.markdown('* **Whiff Rate = Swinging Strikes ÷ Total Swings**')

df['description'] = df['description'].fillna('')
df['swinging'] = df['description'].str.contains('swing', case=False)
df['whiff'] = df['description'] == 'swinging_strike'

swing_data = df[df['swinging']]
whiff_rate = swing_data.groupby('year')['whiff'].mean().round(3)
st.dataframe(whiff_rate)

fig4, ax4 = plt.subplots(figsize=(6, 3))
whiff_rate.plot(marker='o', color='red', ax=ax4)
plt.title('Whiff Rate by Year')
plt.ylabel('Whiff Rate')
plt.xlabel('Year')
plt.grid(True)
st.pyplot(fig4)

# Divider
st.markdown('---')

# Footer
st.markdown(footer_content, unsafe_allow_html=True)
