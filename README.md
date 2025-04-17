# MLB Pitching Analysis Dashboard  
**Scouting & Player Development Insights Through a Woman’s Lens**

## 🚀 Project Purpose  
As a bilingual, purpose-driven professional transitioning into Major League Baseball, I built this dashboard to merge scouting instincts with modern analytics—through the lens of leadership, player development, and human performance.

This project demonstrates my ability to design tools that not only visualize performance metrics but also mirror the decision-making needs of MLB front offices. With a foundation in baseball analytics, scouting, and player development, I aimed to deliver clean data storytelling and actionable insights aligned with long-term athlete growth.

---

## 📄 Project Overview  
This dashboard evaluates the past five seasons of San Francisco Giants reliever **Camilo Doval** using real Statcast data (2020–2025). Before coding, I reviewed his pitch arsenal, usage trends, and scouting reports to align the analysis with real-world context.

The final product is a public-facing, interactive Streamlit app that helps coaches, scouts, and player development teams track performance trends and metrics.

---

## 🛠️ Development Process

- `pull_doval_data.py`: Pulled Statcast pitch-level data (2020–2025) via PyBaseball.
- `doval_pitching_analysis.py`: Aggregated 4 key metrics:
  - Velocity & Spin Rate
  - Pitch Usage
  - Release Extension
  - Whiff Rate  
- `doval_charts.py`: Created PNG visualizations using matplotlib.
- `pull_doval_advanced.py`: Added placeholder for advanced stats (WAR, FIP, K/9).
- `merge_doval_data.py`: Combined Statcast and FanGraphs data into `doval_complete_profile.csv`.

---

## 📊 What the Dashboard Displays

**1. Velocity & Spin Rate**  
**What it shows:** Yearly averages for pitch velocity and spin rate.  
**Why it matters:** Measures raw arm strength and late movement potential.

**2. Pitch Usage Breakdown**  
**What it shows:** Annual percentages of each pitch type (SL, SI, FC, etc.).  
**Why it matters:** Reflects strategic evolution, role changes, and adaptation.

**3. Release Extension**  
**What it shows:** Distance off the mound where pitches are released.  
**Why it matters:** Influences hitter reaction time and perceived velocity.

**4. Whiff Rate**  
**What it shows:** Swing-and-miss ratio by year.  
**Why it matters:** Indicates strikeout power and deception.

---

## 🎯 S.M.A.R.T. Framework

- **Specific**: Analyze Doval’s trends from 2020–2025  
- **Measurable**: Four core metrics across 5 years  
- **Achievable**: Python, PyBaseball, Pandas, Streamlit  
- **Relevant**: Matches player dev and scouting goals  
- **Time-bound**: Completed in one week as an MVP

---

## ⚙️ Technical Stack

- **Data Sources**: Statcast (via PyBaseball), FanGraphs (CSV)
- **Languages/Libraries**: Python, pandas, matplotlib, pybaseball
- **App Framework**: Streamlit
- **Hosting**: Streamlit Community Cloud (Free Tier)
- **Repo**: [GitHub – NextLevelNine](https://github.com/NextLevelNine/MLB_Analytics_Dashboard)

---

## 🌱 Version 1: MVP Scope

✅ Pull, clean, and analyze 5 years of Statcast data  
✅ Visualize 4 performance metrics  
✅ Fully interactive, branded Streamlit dashboard  
✅ Lightweight, clean, and scalable

---

## 🔮 Version 2: Future Enhancements

- Advanced stats: WAR, FIP, xFIP, WPA, K/9
- Pitcher-to-pitcher comparisons
- Strike zone visualizations
- Export PDF/CSV features for coaching staff
- Mobile optimization

---

## 👩🏻 About the Creator

Hi, I’m **Liza Osterdock**—a bilingual (English/Spanish), purpose-driven professional pivoting into MLB after 20+ years in tech, data, and program leadership. I specialize in bridging performance analytics and athlete development through high-performance culture and strategic thinking.

I’m deeply passionate about creating development-first environments rooted in resilience, preparation, and emotional intelligence.

---

## 🎓 Certifications

- Baseball GM & Scouting – SMWW, Dec. 2024  
- Baseball Player Development – SMWW, Mar. 2025  
- Baseball Analytics – SMWW, Mar. 2025  
- Analytics & Critical Thinking in Baseball (Level I) – SABR, Apr. 2025

📚 **Currently Enrolled** (Expected by July 2025):  
- Advanced Analytics in Baseball (Level II) – SABR  
- Python Programming – Stanford Continuing Education  
- Baseball Agent Certification – SMWW  

---

## 📬 Contact

- LinkedIn: [linkedin.com/in/lizaosterdock](https://www.linkedin.com/in/lizaosterdock/)  
- Email: liza@allysixconsulting.com  
- Website: [nextlevelnine.com](https://nextlevelnine.com) *(Coming Soon)*

---
