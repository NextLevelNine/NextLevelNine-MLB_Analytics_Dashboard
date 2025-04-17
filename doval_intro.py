# This program defines the visual title, summary content, and footer for the Streamlit dashboard

# Header: Visual title, image, and tagline
project_intro = """
<div style='text-align: center;'>
    <h3 style='margin-bottom: 5px;'>MLB Pitching Analysis Dashboard</h3>
    <img src='https://raw.githubusercontent.com/NextLevelNine/NextLevelNine-MLB_Analytics_Dashboard/main/Pink%20Baseball.jpeg' alt='Pink Baseball' width='400' style='margin: 10px 0;'>
    <p style='font-style: italic; font-size: 16px;'>Scouting & Player Development Insights Through a Woman’s Lens</p>
</div>
"""

# Main summary content (HTML format)
main_content = """
<h4>Project Purpose</h4>
<p>As a bilingual, purpose-driven professional aspiring to transition into a Major League Baseball position, I built this dashboard to merge scouting instincts with modern analytics—through the lens of leadership, player development, and human performance. This project reflects my unique ability to translate data into meaningful, player-focused insight, shaped by over 20 years in business strategy, technology, and mental performance.</p>
<p>My goal was to design a tool that not only visualizes performance metrics, but also mirrors the decision-making needs of today’s MLB front offices. With a strong foundation in baseball analytics, scouting, and player development, this project demonstrates my ability to communicate insights clearly, build scalable systems, and align data storytelling with long-term athlete growth.</p>

<h4>Project Overview</h4>
<p>I created this dashboard using Python to evaluate the past five seasons of an MLB pitcher’s performance. For this case study, I selected San Francisco Giants reliever Camilo Doval and pulled Statcast data covering 2020–2025.</p>
<p>Before scripting, I reviewed Doval’s pitch arsenal, usage trends, and public scouting reports to ensure alignment between raw data and real-world insights. I then used tools like pybaseball, pandas, and matplotlib to extract, clean, and visualize performance patterns. The final result is a public-facing, interactive dashboard hosted via Streamlit Cloud.</p>

<h4>What the Dashboard Displays</h4>
<ol>
  <li><b>Velocity & Spin Rate:</b> Shows Doval’s power and pitch movement quality. His velocity peaked in 2023 (95.26 mph), and spin rebounded to 2555.13 rpm in 2025.</li>
  <li><b>Pitch Usage Breakdown:</b> Visualizes pitch mix evolution. Slider usage grew to 58.1% in 2025; sinker use declined.</li>
  <li><b>Release Extension:</b> Tracks release point distance. Remained consistent around 6.3–6.6 feet across years.</li>
  <li><b>Whiff Rate:</b> Measures swing-and-miss dominance. Maintained elite whiff rates above 0.92 in all five seasons.</li>
</ol>

<h4>Project Framework Using S.M.A.R.T.</h4>
<ul>
  <li><b>Specific:</b> Analyze Doval’s pitching trends (2020–2025)</li>
  <li><b>Measurable:</b> Four core metrics across five seasons</li>
  <li><b>Achievable:</b> Built using Python, PyBaseball, Pandas, Matplotlib, and Streamlit</li>
  <li><b>Relevant:</b> Supports player development, scouting, and front office decision-making</li>
  <li><b>Time-bound:</b> Completed in one week as a capstone MVP</li>
</ul>

<h4>Development Process</h4>
<ul>
  <li><b>pull_doval_data.py</b>: Pulled Statcast data (2020–2025) → <code>camilo_doval_5yr_statcast.csv</code></li>
  <li><b>doval_pitching_analysis.py</b>: Generated four key metric summaries into CSVs</li>
  <li><b>doval_charts.py</b>: Created PNG visualizations using Matplotlib</li>
  <li><b>pull_doval_advanced.py</b>: Placeholder FanGraphs metrics → <code>doval_advanced_stats.csv</code></li>
  <li><b>merge_doval_data.py</b>: Combined files into <code>doval_complete_profile.csv</code></li>
</ul>

<h4>Technical Stack</h4>
<ul>
  <li><b>Data Sources:</b> Statcast (PyBaseball), FanGraphs (CSV)</li>
  <li><b>Libraries:</b> pandas, matplotlib, pybaseball</li>
  <li><b>App Framework:</b> Streamlit</li>
  <li><b>Hosting:</b> Streamlit Community Cloud</li>
</ul>

<h4>Version 1: MVP Scope</h4>
<ul>
  <li>Pulls, cleans, and analyzes 5-year Statcast data</li>
  <li>Interactive charts and tables for 4 metrics</li>
  <li>Scalable for multi-pitcher or team use</li>
</ul>

<h4>Version 2: Future Enhancements</h4>
<ul>
  <li>Pitcher comparison view and dropdown selection</li>
  <li>FanGraphs integration: WAR, K/9, FIP, WPA, etc.</li>
  <li>PDF/CSV export for scouts and coaches</li>
  <li>Mobile optimization and layout refinement</li>
</ul>

<h4>About the Creator – Liza Osterdock</h4>
<p>Hi, I’m <b>Liza Osterdock</b>—a bilingual (English/Spanish), purpose-driven professional pivoting into Major League Baseball after 20+ years in tech, data analysis, and business strategy. I blend leadership, player development, and mental skills coaching to create high-performance environments.</p>
<p>I believe in connecting data and heart—building systems that empower athletes to succeed on and off the field through intentional, development-first practices.</p>

<h4>🎓 Baseball & Analytics Certifications</h4>
<ul>
  <li><b>Baseball GM & Scouting</b> – SMWW, Dec. 2024</li>
  <li><b>Baseball Player Development</b> – SMWW, Mar. 2025</li>
  <li><b>Baseball Analytics</b> – SMWW, Mar. 2025</li>
  <li><b>Analytics & Critical Thinking in Baseball (Level I)</b> – SABR, Apr. 2025</li>
</ul>
<p><b>Currently enrolled (expected completion by July 2025):</b></p>
<ul>
  <li>Advanced Analytics in Baseball (Level II) – SABR</li>
  <li>Python Programming – Stanford Continuing Education</li>
  <li>Baseball Agent Certification – SMWW</li>
</ul>

<h4>📬 Let’s Connect</h4>
<ul>
  <li><b>LinkedIn:</b> <a href="https://www.linkedin.com/in/lizaosterdock/" target="_blank">linkedin.com/in/lizaosterdock</a></li>
  <li><b>Email:</b> liza@allysixconsulting.com</li>
  <li><b>Website:</b> <a href="https://nextlevelnine.com" target="_blank">nextlevelnine.com</a> <i>(Coming Soon)</i></li>
</ul>
"""

# Footer section
footer_content = """
<hr>
<p style='text-align: center; font-size: 14px;'>
    © 2025 Next Level Nine. All rights reserved.<br>
    Designed & built by <b>Liza Osterdock</b>
</p>
"""
