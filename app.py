import streamlit as st
from streamlit_lottie import st_lottie

import sys
import os
# Force Python to find local modules (Fixes ModuleNotFoundError on Streamlit Cloud)
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from utils.theme import load_css
from components.sidebar import render_sidebar
from components.cards import metric_card
from components.charts import plot_line_chart
from utils.data_fetcher import get_dummy_data, get_market_summary
from utils.animations import load_lottieurl, ANIMATIONS
import time
import base64
import os

st.set_page_config(
    page_title="NovaTrade AI - Market Terminal",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
load_css()

# Render Sidebar
symbol, market, theme = render_sidebar()

# Get base64 logo for inline HTML display
def get_base64_of_bin_file(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

logo_b64 = get_base64_of_bin_file("assets/logo.png")
logo_html = f'<img src="data:image/png;base64,{logo_b64}" width="240" style="margin-bottom: 1rem; filter: drop-shadow(0 0 30px rgba(139, 92, 246, 0.5)); border-radius: 30px;">' if logo_b64 else ""

# Simulated Top Ticker
st.markdown("""
<div style="display: flex; justify-content: center; gap: 3rem; padding: 0.5rem; font-size: 0.9rem; font-weight: 600; white-space: nowrap; margin-bottom: 2rem; opacity: 0.8;">
    <span><span style="color:var(--text-secondary)">NIFTY 50</span> 23,602.15 <span style="color:var(--danger)">↓ 0.90%</span></span>
    <span><span style="color:var(--text-secondary)">SENSEX</span> 75,214.48 <span style="color:var(--danger)">↓ 1.05%</span></span>
    <span><span style="color:var(--text-secondary)">BANKNIFTY</span> 53,980.60 <span style="color:var(--danger)">↓ 0.84%</span></span>
    <span><span style="color:var(--text-secondary)">FINNIFTY</span> 25,358.70 <span style="color:var(--danger)">↓ 1.16%</span></span>
</div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown(f"""
<div style="text-align: center; margin-top: 1rem; margin-bottom: 1rem;">
    {logo_html}
    <h1 style="font-size: 5rem; font-weight: 800; margin-bottom: 0.5rem; line-height: 1.1; background: linear-gradient(135deg, #fff 0%, #a5b4fc 50%, #c084fc 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-shadow: 0 0 40px rgba(139, 92, 246, 0.3);">NovaTrade your wealth</h1>
    <p style="font-size: 1.3rem; color: var(--text-secondary); margin-bottom: 2rem; font-weight: 400;">Next-generation algorithmic trading, built on advanced machine learning.</p>
    <a href="/Live_Tracker" target="_self" style="background: linear-gradient(90deg, var(--neon-green), #059669); color: white; padding: 14px 36px; border-radius: 30px; text-decoration: none; font-weight: 600; font-size: 1.1rem; box-shadow: 0 10px 25px rgba(16, 185, 129, 0.4); transition: all 0.3s ease; display: inline-block;">Get started</a>
</div>
""", unsafe_allow_html=True)

# Massive Lottie Graphic Area
col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    lottie_anim = load_lottieurl(ANIMATIONS["dashboard"])
    if lottie_anim:
        st_lottie(lottie_anim, height=400, key="hero_anim")

st.markdown("<br><br>", unsafe_allow_html=True)

# KPI Cards (Moved down)
st.subheader("Market Overview")
market_data = get_market_summary()
cols = st.columns(4)

for i, data in enumerate(market_data):
    with cols[i]:
        metric_card(data['name'], data['value'], data['change'], data['positive'])

# Main Charts Area
st.markdown("---")
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"Trending: {symbol}")
    df = get_dummy_data(180)
    st.plotly_chart(plot_line_chart(df, f"{symbol} 6-Month Trend"), width="stretch")

with col2:
    st.subheader("Top Gainers 🔥")
    gainers = [
        ("NVDA", "$278.45", "+5.4%"),
        ("TSLA", "$165.23", "+4.2%"),
        ("AMD", "$92.11", "+3.8%"),
        ("META", "$212.89", "+2.9%"),
        ("MSFT", "$289.10", "+1.5%")
    ]
    for gainer in gainers:
        st.markdown(f'''
        <div class="glass-card" style="padding: 1rem; margin-bottom: 0.5rem; display: flex; justify-content: space-between;">
            <span style="font-weight: 600;">{gainer[0]}</span>
            <span>{gainer[1]}</span>
            <span style="color: var(--neon-green);">{gainer[2]}</span>
        </div>
        ''', unsafe_allow_html=True)
