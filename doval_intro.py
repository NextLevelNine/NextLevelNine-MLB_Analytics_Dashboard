# This program defines the project summary and introduction for the Streamlit dashboard

project_intro = """
<h3>MLB Pitching Dashboard</h3>

<p>I decided to create a dashboard using Python programming that would analyze an MLB pitcher's last five years of performance and display interactive graphs and data summaries based on the report. For this sample, I am using San Francisco Giants reliever <b>Camilo Doval</b> as the subject of analysis.</p>

<h4>🚀 Project Purpose</h4>
<p>As an aspiring <b>MLB Player Development</b> and <b>R&D Analyst</b>, I built this interactive dashboard to demonstrate the kind of professionalism, insight, and data fluency today’s front offices expect. My work reflects a blend of <b>baseball wisdom</b>, <b>analytical rigor</b>, and <b>emotional intelligence</b>—three qualities I’ve cultivated through advanced certifications and real-world application.</p>

<p>I’ve earned four industry-recognized credentials:</p>
<ul>
  <li><b>Baseball GM & Scouting</b> – SMWW, Dec. 2024</li>
  <li><b>Baseball Player Development</b> – SMWW, Mar. 2025</li>
  <li><b>Baseball Analytics</b> – SMWW, Mar. 2025</li>
  <li><b>Analytics & Critical Thinking in Baseball (Level I)</b> – SABR, Apr. 2025</li>
</ul>

<p>I’ve developed a strategic understanding of player evaluation, high-performance culture, and statistical analysis. Beyond the technical training, I bring a curious mindset, a leader’s communication style, and the ability to connect scouting instincts with data-driven decisions. This project is more than a dashboard—it’s a showcase of how I think, lead, and build systems that translate complex performance data into clear, actionable baseball intelligence. Designed with front-office needs in mind, it reflects my commitment to helping players succeed and organizations thrive.</p>

<h4>📋 How the Dashboard Was Built</h4>
<p>I began by creating a script called <code>pull_doval_data.py</code> using the <code>pybaseball</code> library to pull Camilo Doval’s Statcast data from 2020 to 2025. This generated a raw CSV file <code>camilo_doval_5yr_statcast.csv</code>.</p>
<p>I then created <code>doval_pitching_analysis.py</code> to analyze the data and calculate key metrics like yearly averages for velocity and spin rate, pitch usage, release extension, and whiff rate. These were exported into individual CSV summaries.</p>
<p>Using <code>doval_charts.py</code>, I generated clean, well-labeled <code>.png</code> visualizations for each metric.</p>
<p><code>pull_doval_advanced.py</code> was created to explore integration with FanGraphs for advanced stats (WAR, K/9, FIP, etc.), generating a placeholder file <code>doval_advanced_stats.csv</code>.</p>
<p>Finally, <code>merge_doval_data.py</code> brought both datasets together into a unified <code>doval_complete_profile.csv</code> that can serve as a foundation for future dashboards and comparative studies.</p>

<h4>📊 What the Dashboard Displays</h4>
<p>The app presents <b>4 key pitching metrics</b> for Camilo Doval (2021–2025), each supported by a table and visual chart:</p>

<p><b>1. Velocity & Spin Rate</b><br>
<b>What it shows:</b> Yearly averages of pitch velocity and spin rate.<br>
<b>Why it matters:</b> Foundational indicators of a pitcher’s raw power and pitch movement quality. In Doval’s case, velocity peaked in 2023 (95.26 mph), with a minor dip in 2024–2025. Spin rate stayed elite, rebounding in 2025 to the highest value (2555.13 rpm), reflecting his continued ability to generate late movement and deception.</p>

<p><b>2. Pitch Usage Percentages</b><br>
<b>What it shows:</b> Year-over-year breakdown of pitch types (FC, FF, SI, SL).<br>
<b>Why it matters:</b> Provides insight into pitch selection strategy and adaptation. Doval’s slider (SL) has remained dominant, especially in 2024–2025 (over 50% usage), while sinker (SI) usage declined. His cutter (FC) remained steady, reflecting consistency in high-leverage sequences.</p>

<p><b>3. Release Extension</b><br>
<b>What it shows:</b> Average release distance from the mound.<br>
<b>Why it matters:</b> Longer release extension creates perceived velocity and improves deception. Doval’s release extension stayed consistent (6.3–6.6 ft), with a slight dip in 2024 and recovery in 2025—indicating steady mechanics with minor variance.</p>

<p><b>4. Whiff Rate</b><br>
<b>What it shows:</b> Percentage of swings that result in misses.<br>
<b>Why it matters:</b> A direct measure of “stuff” quality and strikeout ability. Doval has posted exceptional whiff rates across all five seasons (0.928–0.978), peaking in 2023 and maintaining elite dominance. This showcases his effectiveness even during slight dips in velocity.</p>

<h4>📄 Project Overview</h4>
<p>This dashboard was created to answer the following question:</p>
<blockquote><i>How can we make advanced metrics more accessible for analysts, coaches, and fans—without losing depth or meaning?</i></blockquote>

<p><b>S.M.A.R.T. Project Framework</b></p>
<ul>
  <li><b>Specific:</b> Analyze Doval’s 5-year performance using Statcast data.</li>
  <li><b>Measurable:</b> 4 metrics with year-over-year trend lines.</li>
  <li><b>Achievable:</b> Python + PyBaseball + Streamlit Cloud.</li>
  <li><b>Relevant:</b> Metrics align with real-world player development goals.</li>
  <li><b>Time-bound:</b> Completed over 3 focused days from prototype to deployment.</li>
</ul>

<h4>📈 Technical Stack</h4>
<ul>
  <li><b>Data:</b> Statcast via PyBaseball, FanGraphs (CSV)</li>
  <li><b>Processing:</b> Python (Pandas, Matplotlib)</li>
  <li><b>Frontend:</b> Streamlit</li>
  <li><b>Hosting:</b> Streamlit Community Cloud (Free)</li>
</ul>
<p><b>💎 Live App:</b> <a href="https://nextlevelnine-mlbanalyticsdashboard-camilo-doval.streamlit.app/" target="_blank">Visit Dashboard</a></p>

<h4>🎓 Certifications & Courses</h4>
<p>I’ve completed four elite baseball certifications in the past year:</p>
<ul>
  <li><b>Baseball GM & Scouting</b> – SMWW, Dec. 2024</li>
  <li><b>Baseball Player Development</b> – SMWW, Mar. 2025</li>
  <li><b>Baseball Analytics</b> – SMWW, Mar. 2025</li>
  <li><b>Analytics & Critical Thinking in Baseball (Level I)</b> – SABR, Apr. 2025</li>
</ul>
<p><b>Currently enrolled in:</b></p>
<ul>
  <li><b>Advanced Analytics in Baseball (Level II)</b> – SABR, May 2025</li>
  <li><b>Python Programming</b> – Stanford University Continuing Education, Spring 2025</li>
  <li><b>Baseball Agent Certification</b> – SMWW, June 2025</li>
</ul>

<h4> Future Enhancements</h4>
<ul>
  <li>Pitcher-to-pitcher comparisons</li>
  <li>Team-level analysis and filters</li>
  <li>Mobile view optimization</li>
  <li>WAR, FIP, K/9, xFIP, WPA metrics integration</li>
  <li>Interactive timeline and dropdown filters</li>
</ul>

<h4>📨 Contact</h4>
<p><a href="https://www.linkedin.com/in/lizaosterdock/" target="_blank">Connect with me on LinkedIn</a><br>
Email: liza@allysixconsulting.com</p>
"""
