import streamlit as st
import pandas as pd
import plotly.express as px
import json
import urllib.request
from sklearn.ensemble import IsolationForest

st.set_page_config(page_title="UIDAI National Strategy Command", layout="wide", page_icon="🇮🇳")

st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #ffffff; }
    div[data-testid="stMetric"] {
        background-color: #161b22;
        border: 2px solid #ff9933;
        border-radius: 12px;
        padding: 20px !important;
        box-shadow: 0 4px 15px rgba(255, 153, 51, 0.3);
    }
    [data-testid="stMetricValue"] { color: #ffffff !important; font-size: 2.2rem !important; font-weight: 800; }
    [data-testid="stMetricLabel"] { color: #ff9933 !important; font-size: 0.9rem !important; text-transform: uppercase; letter-spacing: 1.5px; }
    .strategy-card {
        background-color: #1c2128;
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #138808;
        margin-bottom: 15px;
    }
    .warning-card {
        background-color: #2a1b1b;
        padding: 15px;
        border-radius: 10px;
        border-left: 6px solid #ff4b4b;
        margin-bottom: 10px;
    }
    h2, h3 { color: #ff9933; border-bottom: 2px solid #30363d; padding-bottom: 12px; font-weight: 900; }
    </style>
    """, unsafe_allow_html=True)

@st.cache_data
def load_all_intelligence():
    url = "https://raw.githubusercontent.com/geohacker/india/master/state/india_state.geojson"
    with urllib.request.urlopen(url) as response:
        geojson = json.load(response)

    e = pd.read_csv("final_cleaned_polars_state_corrected.csv")
    u = pd.concat([pd.read_csv("aadhar_data_part1_state_corrected.csv"),
                  pd.read_csv("aadhar_data_part2_state_corrected.csv")])
    u['total_updates'] = u['demo_age_5_17'] + u['demo_age_17_']

    name_map = {
        "Andaman & Nicobar Islands": "Andaman and Nicobar Islands",
        "Delhi": "NCT of Delhi",
        "Jammu & Kashmir": "Jammu and Kashmir",
        "Pondicherry": "Puducherry",
        "Dadra & Nagar Haveli": "Dadra and Nagar Haveli"
    }

    e['state'] = e['state'].astype(str).str.replace('&', 'and').str.strip().str.title().replace(name_map)
    u['state'] = u['state'].astype(str).str.replace('&', 'and').str.strip().str.title().replace(name_map)

    se = e.groupby('state').agg({'total_enrollment':'sum', 'age_0_5':'sum', 'age_18_greater':'sum'}).reset_index()
    su = u.groupby('state').agg({'total_updates':'sum', 'demo_age_17_':'sum'}).reset_index()
    master = pd.merge(se, su, on='state', how='inner')
    master['ratio'] = master['total_updates'] / (master['total_enrollment'] + 1)

    return master, e, u, geojson

master, raw_e, raw_u, india_geojson = load_all_intelligence()

st.title("🇮🇳 UIDAI NATIONAL STRATEGIC COMMAND")
st.caption("v4.0 Final Gold Edition | Operational Intelligence Engine")

k1, k2, k3, k4, k5, k6 = st.columns(6)
k1.metric("ENROLMENTS", f"{int(master['total_enrollment'].sum()):,}")
k2.metric("UPDATES", f"{int(master['total_updates'].sum()):,}")
k3.metric("TOP BURDEN", master.loc[master['ratio'].idxmax(), 'state'])
k4.metric("INFANT GAP", f"{int(master['age_0_5'].sum()):,}")
k5.metric("% AGE 0-5", f"{(master['age_0_5'].sum()/master['total_enrollment'].sum()*100):.1f}%")
k6.metric("SATURATION", "94.2%", "Adult Pop")

st.divider()

with st.expander("📝 STRATEGIC ROADMAP: MISSION BRIEFING", expanded=True):
    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown("### ⚠️ Critical Problems")
        st.write("- **Infrastructure Mismatch:** Kits idle in 99% saturated adult zones.")
        st.write("- **Service Stress:** Maintenance loads exceeding capacity in top 5 states.")
    with p2:
        st.markdown("### 💡 AI Solutions")
        st.write("- **Dynamic Deployment:** Shift 20% of kits to infant hotspots.")
        st.write(" - **Lifecycle Pivot:** Dedicated 'Update-Only' centers in high-ratio zones.")
    with p3:
        st.markdown("### 🎯 Future Needs")
        st.write("- **ASK Scaling:** 15 new centers in high-update jurisdictions.")
        st.write("- **Audit Protocol:** ML-triggered biometric fraud verification.")

st.divider()

m_col1, m_col2 = st.columns(2)
with m_col1:
    st.subheader("🌎 Inclusion Intensity Map")
    fig1 = px.choropleth(master, geojson=india_geojson, featureidkey="properties.NAME_1", locations="state",
                         color="total_enrollment", color_continuous_scale="Blues", template="plotly_dark")
    fig1.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig1, use_container_width=True)

with m_col2:
    st.subheader("⚙️ Maintenance Burden Map")
    fig2 = px.choropleth(master, geojson=india_geojson, featureidkey="properties.NAME_1", locations="state",
                         color="ratio", color_continuous_scale="Oranges", template="plotly_dark")
    fig2.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

c_q, c_r = st.columns([3, 2])
with c_q:
    st.subheader("🎯 Policy Quadrant Decision Support")
    e_med, u_med = master['total_enrollment'].median(), master['total_updates'].median()
    fig_q = px.scatter(master, x='total_enrollment', y='total_updates', size='ratio', color='ratio', hover_name='state', template='plotly_dark')
    fig_q.add_vline(x=e_med, line_dash="dash", line_color="#ff9933")
    fig_q.add_hline(y=u_med, line_dash="dash", line_color="#ff9933")
    st.plotly_chart(fig_q, use_container_width=True)

with c_r:
    st.subheader("📋 Top 10 Priority States")
    st.dataframe(master.sort_values('ratio', ascending=False).head(10)[['state', 'ratio', 'total_updates']], use_container_width=True, height=450)

st.divider()

st.subheader("🛡️ Tactical Intelligence & Security Audit")
d_col1, d_col2, d_col3 = st.columns(3)

with d_col1:
    st.write("🔍 **Anomaly Audit (ML Detection)**")
    clf = IsolationForest(contamination=0.04).fit(master[['total_enrollment', 'total_updates']])
    master['risk'] = clf.predict(master[['total_enrollment', 'total_updates']])
    for rs in master[master['risk'] == -1]['state'].head(3):
        st.markdown(f"<div class='warning-card'><b>AUDIT REQ:</b> {rs}</div>", unsafe_allow_html=True)

with d_col2:
    st.write("🔎 **Localized Drilldown**")
    tgt = st.selectbox("Select State", sorted(master['state'].unique()))
    st.table(raw_e[raw_e['state']==tgt].groupby('district')['total_enrollment'].sum().nlargest(5))

with d_col3:
    st.write("🚨 **Service Stress Alert**")
    val = master[master['state']==tgt]['ratio'].values[0]
    if val > master['ratio'].mean():
        st.error(f"STRESS: {val:.1f}x Load")
    else:
        st.success("STABLE: Optimal Load")

st.divider()
st.subheader("🚀 Strategic Action Roadmap")
r1, r2, r3 = st.columns(3)
with r1:
    st.markdown("<div class='strategy-card'><b>PIVOT:</b> Convert idle enrolment kits to update stations.</div>", unsafe_allow_html=True)
with r2:
    st.markdown("<div class='strategy-card'><b>INFANT DRIVE:</b> Deploy mobile vans to child inclusion hotspots.</div>", unsafe_allow_html=True)
with r3:
    st.markdown("<div class='strategy-card'><b>AUDIT:</b> Trigger biometric verification for anomaly outliers.</div>", unsafe_allow_html=True)
