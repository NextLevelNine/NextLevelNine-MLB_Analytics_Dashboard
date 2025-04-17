import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import base64

# This program imports the full html code for the project introduction used for the dashboard header
from doval_intro import project_intro

# This program sets the Streamlit page title
st.set_page_config(page_title='MLB Pitching Dashboard', page_icon='⚾', layout='wide')

# This program sets the main title of the dashboard
st.markdown(project_intro, unsafe_allow_html=True)
#st.title('📊 MLB Pitching Dashboard')

# This program displays the project overview and summary
st.markdown(project_intro, unsafe_allow_html=True)


# This program displays the author's name
st.markdown('**Created by Liza Osterdock**')
st.markdown('---')

# This program loads the Statcast dataset and prepares the data
file_path = 'camilo_doval_5yr_statcast.csv'
df = pd.read_csv(file_path)
df['game_date'] = pd.to_datetime(df['game_date'], errors='coerce')
df['year'] = df['game_date'].dt.year

# This program creates a section for Velocity & Spin Rate
st.header('Velocity & Spin Rate by Year')
st.markdown('* **Release Speed (MPH)**: The speed at which the ball leaves the pitcher’s hand.')
st.markdown('* **Spin Rate (RPM)**: How many times the ball spins per minute. A higher spin rate can lead to more movement and deception on pitches.')

velocity_spin = df.groupby('year')[['release_speed', 'release_spin_rate']].mean().round(2)
st.dataframe(velocity_spin)

fig1, ax1 = plt.subplots()
velocity_spin.plot(marker='o', ax=ax1)
plt.title('Velocity & Spin Rate by Year')
plt.xlabel('Year')
plt.ylabel('Average')
plt.grid(True)
st.pyplot(fig1)

# This program creates a section for Pitch Usage Percentages
st.header('Pitch Usage Percentages by Year')
st.markdown('This shows the percentage of each pitch type Camilo Doval threw per year.')
st.markdown(' **Pitch Types:**')
st.markdown('  - **FC**: Cutter')
st.markdown('  - **FF**: Four-Seam Fastball')
st.markdown('  - **SI**: Sinker')
st.markdown('  - **SL**: Slider')

pitch_counts = df.groupby(['year', 'pitch_type']).size().unstack(fill_value=0)
pitch_percent = pitch_counts.div(pitch_counts.sum(axis=1), axis=0).round(3) * 100

st.dataframe(pitch_percent)

fig2, ax2 = plt.subplots()
pitch_percent.plot(kind='bar', stacked=True, ax=ax2)
plt.title('Pitch Usage Percentages by Year')
plt.ylabel('Percentage (%)')
plt.xlabel('Year')
plt.legend(title='Pitch Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
st.pyplot(fig2)

# This program creates a section for Release Extension
st.header('Average Release Extension by Year')
st.markdown('* **Release Extension** measures how far in front of the pitching rubber the ball is released (in feet).')
st.markdown('* A longer extension means the pitcher is releasing the ball closer to the hitter, making pitches appear faster.')

extension_summary = df.groupby('year')['release_extension'].mean().round(2)
st.dataframe(extension_summary)

fig3, ax3 = plt.subplots()
extension_summary.plot(marker='o', color='green', ax=ax3)
plt.title('Release Extension by Year')
plt.ylabel('Feet')
plt.xlabel('Year')
plt.grid(True)
st.pyplot(fig3)

# This program creates a section for Whiff Rate
st.header('Whiff Rate by Year')
st.markdown('* A **whiff** is a swing-and-miss.')
st.markdown('* **Whiff Rate** = Swinging Strikes ÷ Total Swings.')
st.markdown('* High whiff rates indicate dominant “stuff” that hitters struggle to make contact with.')

df['description'] = df['description'].fillna('')
df['swinging'] = df['description'].str.contains('swing', case=False)
df['whiff'] = df['description'] == 'swinging_strike'

swing_data = df[df['swinging']]
whiff_rate = swing_data.groupby('year')['whiff'].mean().round(3)
st.dataframe(whiff_rate)

fig4, ax4 = plt.subplots()
whiff_rate.plot(marker='o', color='red', ax=ax4)
plt.title('Whiff Rate by Year')
plt.ylabel('Whiff Rate')
plt.xlabel('Year')
plt.grid(True)
st.pyplot(fig4)

# This program imports and encodes the logo image for display
logo_path = 'Next Level Nine Logo.png'
base64_logo = ''
if os.path.exists(logo_path):
    with open(logo_path, 'rb') as f:
        base64_logo = base64.b64encode(f.read()).decode()

# This program creates the footer with branding and logo
st.markdown('---')
st.markdown('<center>Designed by Liza Osterdock.</center>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<center>© 2025 Next Level Nine. All rights reserved.</center>', unsafe_allow_html=True)


if base64_logo:
    image_html = f"<div style='text-align: center;'><img src='data:image/png;base64,{base64_logo}' width='200'/></div>"
    st.markdown(image_html, unsafe_allow_html=True)
