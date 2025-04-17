# This program defines the project summary and introduction for the Streamlit dashboard

project_intro = """
<h3>MLB Pitching Dashboard</h3>

<h4>🎯 Project Purpose</h4>
<p>This project was created to explore how advanced baseball analytics can be transformed into an interactive visual tool to evaluate MLB pitchers' performance over time. The goal was to build a clean, engaging, and accessible dashboard that showcases Camilo Doval’s five-year pitching trends using Python, real MLB data, and Streamlit.</p>

<p>The core challenge I set out to solve was this: <i>How can we simplify advanced metrics for decision-makers, fans, or player development teams by presenting them visually—while maintaining depth and accuracy?</i></p>

<p>As an aspiring <b>MLB Player Development</b> and <b>R&D Analyst</b>, I built this MLB Pitching Dashboard to demonstrate the skills I’ve developed over the past 6 months while earning my MLB Front Office Advanced Certificate. My work blends <b>baseball wisdom</b>, <b>analytical rigor</b>, and <b>emotional intelligence</b>—qualities cultivated through my 20+ years in high-tech and my recent certifications. This project is more than just code; it's a strategic representation of how I think, lead, and communicate performance insights that can support long-term athlete growth and team success.</p>

<h4>📋 Development Process</h4>
<p>To bring this project to life, I built a custom Python pipeline and visualization layer from scratch:</p>
<ul>
  <li><b>pull_doval_data.py:</b> Used PyBaseball to pull Camilo Doval’s Statcast data (2020–2025), creating <code>camilo_doval_5yr_statcast.csv</code>.</li>
  <li><b>doval_pitching_analysis.py:</b> Analyzed raw data to calculate year-over-year trends for: velocity, spin rate, pitch usage, release extension, and whiff rate.</li>
  <li><b>doval_charts.py:</b> Generated clear, labeled PNG charts using Matplotlib.</li>
  <li><b>pull_doval_advanced.py:</b> Explored FanGraphs integration (WAR, FIP, K/9), creating a placeholder <code>doval_advanced_stats.csv</code>.</li>
  <li><b>merge_doval_data.py:</b> Combined datasets into a unified <code>doval_complete_profile.csv</code>.</li>
</ul>

<h4>📊 What the Dashboard Displays</h4>
<p>The app presents <b>four key pitching metrics</b> to evaluate Camilo Doval (2021–2025). Each is accompanied by a table and visualization, making the data intuitive for analysts, coaches, and scouts:</p>

<p><b>1. Velocity & Spin Rate</b><br>
<b>What it shows:</b> Yearly averages of pitch velocity and spin rate.<br>
<b>Why it matters:</b> These metrics indicate raw power and movement quality. Doval peaked in 2023 (95.26 mph), with spin rate rebounding in 2025—showing he maintains elite pitch characteristics even as velocity slightly tapers.</p>

<p><b>2. Pitch Usage Breakdown</b><br>
<b>What it shows:</b> Proportions of pitch types thrown each season (e.g., SL, FC, SI).<br>
<b>Why it matters:</b> Shows strategic evolution. Doval's slider usage increased (51.2% → 58.1%), while his sinker declined—suggesting mechanical or tactical adjustments to improve effectiveness.</p>

<p><b>3. Release Extension</b><br>
<b>What it shows:</b> Average distance from the mound where the ball is released.<br>
<b>Why it matters:</b> Longer release extension creates deception and perceived velocity. Doval remained consistent (~6.3–6.6 ft), reflecting stable mechanics with minor year-to-year variation.</p>

<p><b>4. Whiff Rate</b><br>
<b>What it shows:</b> Proportion of swings resulting in misses.<br>
<b>Why it matters:</b> Indicates ability to miss bats—a core trait of elite relievers. Doval’s whiff rates (0.928–0.978) remain elite every year, even amid slight dips in velocity, showing that his movement and deception remain highly effective.</p>

<h4>📄 Project Overview</h4>
<ul>
  <li><b>Specific:</b> Build an interactive dashboard analyzing Camilo Doval’s past 5 seasons using Statcast data.</li>
  <li><b>Measurable:</b> Pull, clean, and visualize four key pitching metrics with trend summaries.</li>
  <li><b>Achievable:</b> Python (PyBaseball, Pandas, Matplotlib) + Streamlit deployment.</li>
  <li><b>Relevant:</b> Matches modern MLB evaluation methods in scouting and development.</li>
  <li><b>Time-bound:</b> Built over 3 focused days—data, scripting, visualizations, and deployment.</li>
</ul>

<h4>📈 Technical Stack</h4>
<ul>
  <li><b>Data:</b> Statcast via PyBaseball, FanGraphs (CSV)</li>
  <li><b>Processing:</b> Python (Pandas, Matplotlib)</li>
  <li><b>Dashboard:</b> Streamlit</li>
  <li><b>Hosting:</b> Streamlit Community Cloud (Free)</li>
</ul>

<h4>✅ Version 1 – MVP Scope</h4>
<p>This version delivers:</p>
<ul>
  <li>Raw data pulled from Statcast using PyBaseball</li>
  <li>Cleaned and grouped data by season</li>
  <li>Matplotlib visualizations and data tables</li>
  <li>Interactive dashboard with summaries and branding</li>
</ul>

<h4>🔮 Version 2 – Future Enhancements</h4>
<ul>
  <li>Compare pitchers side-by-side</li>
  <li>Integrate WAR, FIP, K/9, xFIP, WPA (FanGraphs/Savant)</li>
  <li>Dropdown filters by year, team, pitch type</li>
  <li>Downloadable PDF reports</li>
  <li>Mobile-friendly layout + pitch movement charts</li>
</ul>

<h4>👤 Author</h4>
<p><b>Liza Osterdock</b><br>
Bilingual (English/Spanish) | 20+ years in high-tech | Transitioning into MLB player development & analytics<br>
📅 Created: April 2025<br>
🌐 <a href='https://nextlevelnine-mlbanalyticsdashboard-camilo-doval.streamlit.app/' target='_blank'>Live App</a><br>
📁 <a href='https://github.com/NextLevelNine/MLB_Analytics_Dashboard' target='_blank'>GitHub Repo</a><br>
🔗 <a href='https://www.linkedin.com/in/lizaosterdock/' target='_blank'>LinkedIn</a><br>
📧 liza@allysixconsulting.com</p>
"""
