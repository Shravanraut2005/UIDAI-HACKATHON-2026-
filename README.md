# UIDAI-HACKATHON-2026-
Predictive Aadhaar Operational Strategy portal using Python, Streamlit, and Plotly. Features include Maintenance Burden Ratio (MBR) analysis, temporal trend forecasting, and anomaly intelligence for national resource optimization.

## 📌 Problem Statement  
The purpose of this project is to analyze Aadhaar enrolment and demographic update records for the year 2025, identify meaningful patterns, trends, anomalies, or indicators, and convert those observations into actionable insights that can support decision-making and system improvements.

---

## 🎯 Strategic Approach  
We treated the Aadhaar lifecycle as a continuous journey — starting from **new enrolments** and extending to **demographic updates**.

Instead of only focusing on totals, we studied how the data varies across:
- Different **age groups**
- Different **regions and states**
- **Monthly timelines** across 2025

This helps highlight areas with high activity, uneven workloads, and future planning requirements.

---

## 📂 Datasets Used  
This project uses two main datasets from 2025:

### 1) Aadhaar Enrolment Dataset (2025)  
Contains details about new Aadhaar registrations in India, categorized by:
- State/region  
- Age groups (0–5, 5–17, 18+)  
- Regional distribution patterns  

### 2) Aadhaar Demographic Update Dataset (2025)  
Contains details about demographic changes and update activities (corrections/modifications) in Aadhaar records across India.

---

## ⚙️ Methodology  
We followed a structured data science pipeline:

### ✅ 1. Data Cleaning  
Since the dataset contained nearly **1 million records**, we performed:
- Standardization of state/region names  
- Handling missing and inconsistent values  
- Formatting for uniformity across datasets  

🔹 We used **Polars + Python** for faster processing on large-scale data.

### ✅ 2. Dataset Integration  
After cleaning, both datasets were aligned to enable lifecycle-level comparisons between enrolment and update activities.

### ✅ 3. Exploratory Data Analysis (EDA)  
We explored:
- Top contributing states  
- Category-wise distribution  
- Overall patterns and changes across time  

This helped decide meaningful KPIs and the most useful visuals for dashboard reporting.

### ✅ 4. KPI Calculation  
We computed key performance indicators to summarize national activity and regional workload distribution.

---

## 📊 KPI Dashboard (2025)  
| KPI | Value |
|-----|------|
| **Total Enrolments (India)** | 2,057,960 |
| **Total Demographic Updates (India)** | 36,597,559 |
| **Top Enrolment State** | Uttar Pradesh → 338,863 |
| **Top Update State** | Uttar Pradesh → 6,460,511 |
| **Major Enrolment Share** | Age group 0–5 |
| **Major Update Share** | Age group 17+ |

---

## 🏗️ System Architecture  
The project workflow follows a modular approach:

1. Raw CSV Data (2025)  
2. Data Cleaning (Pandas / Polars)  
3. Feature Engineering  
4. Lifecycle Activity Classification  
5. Visualization + Report Generation  
6. Dashboard Output  

---

## 🔍 Key Findings & Insights  

✅ **1. Child-Centric Enrollment**  
Most Aadhaar enrolments are from the **0–5 age group**, indicating early-life identity creation and documentation needs.

✅ **2. Adult-Centric Maintenance**  
Most demographic updates occur in the **18+ age group**, mainly due to address changes, corrections, and record maintenance.

✅ **3. Geographic Concentration**  
Enrolments and updates are not evenly distributed. A few major states dominate overall Aadhaar activity.

✅ **4. Operational Shift**  
The Aadhaar ecosystem is shifting from a **growth phase (enrolments)** to a **maintenance phase (updates)**, showing the increasing importance of efficient update services and workload management.

---

## 📈 Visualizations Included  
This project includes the following major analysis charts:

- **Top 10 States by Aadhaar Enrolment (2025)**
- **Top 10 States by Aadhaar Demographic Updates (2025)**
- **State-wise Enrolment vs Update Summary (Update/Enrolment Ratio)**
- **Monthly Enrolment vs Update Trend Analysis**
- **Main Dashboard Output**
- **Inclusion Intensity and Maintenance Burden Map**
- **Top 10 Priority States**

---

## ✅ Conclusion  
The analysis shows that Aadhaar activity differs strongly across age groups and regions:

- New enrolments are highly driven by **children below 5 years**
- Updates are highly driven by **adults**, highlighting the need for long-term record maintenance

Since activity is concentrated in a few states, UIDAI can improve operational efficiency through:
- Better regional planning  
- Improved resource allocation  
- Strong monitoring of update-heavy states  
- Faster demographic update processing

## Tech Stack  
- **Python**
- **Polars / Pandas**
- **Matplotlib / Plotly (for visualizations)**
- **Google Colab**
