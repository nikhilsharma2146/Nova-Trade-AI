import streamlit as st
from streamlit_lottie import st_lottie

import sys
import os
# Force Python to find local modules (Fixes ModuleNotFoundError on Streamlit Cloud)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.theme import load_css
from components.sidebar import render_sidebar
from components.charts import plot_candlestick, plot_line_chart
from utils.data_fetcher import get_dummy_data
from utils.animations import load_lottieurl, ANIMATIONS
import plotly.graph_objects as go

st.set_page_config(page_title="Terminal - NovaTrade", page_icon="📈", layout="wide")
load_css()
symbol, market, theme = render_sidebar()

# Ticker Tape (Simulated)
st.markdown("""
<div style="display: flex; gap: 2rem; padding: 0.8rem; background: var(--bg-surface); border-bottom: 1px solid var(--glass-border); border-top: 1px solid var(--glass-border); font-size: 0.85rem; font-family: monospace; overflow-x: auto; white-space: nowrap; margin-bottom: 1rem; border-radius: 8px;">
    <span><strong style="color:var(--text-secondary)">NIFTY 50</strong> 23,606.20 <span style="color:var(--danger)">-209.65 (-0.88%)</span></span>
    <span><strong style="color:var(--text-secondary)">SENSEX</strong> 75,214.48 <span style="color:var(--danger)">-800.80 (-1.05%)</span></span>
    <span><strong style="color:var(--text-secondary)">Crude Oil</strong> ₹9,458.00 <span style="color:var(--success)">82.00 (+0.87%)</span></span>
    <span><strong style="color:var(--text-secondary)">Natural Gas</strong> ₹281.00 <span style="color:var(--success)">3.40 (+1.22%)</span></span>
    <span><strong style="color:var(--text-secondary)">BANKNIFTY</strong> 53,980.60 <span style="color:var(--danger)">-459.30 (-0.84%)</span></span>
</div>
""", unsafe_allow_html=True)

# Toolbar
col_tool1, col_tool2, col_tool3, col_tool4 = st.columns([1, 1, 1, 2])
with col_tool1:
    st.markdown(f"<h3 style='margin:0; padding-top:0.3rem;'>🔍 {symbol}</h3>", unsafe_allow_html=True)
with col_tool2:
    timeframe = st.selectbox("Timeframe", ["1D", "1W", "1M", "3M", "1Y", "All"], index=2, label_visibility="collapsed")
with col_tool3:
    chart_type = st.selectbox("Chart Type", ["Candlestick", "Line", "Area"], label_visibility="collapsed")
with col_tool4:
    indicators = st.multiselect("Indicators 𝒇x", ["SMA 20", "SMA 50", "EMA 100", "Volume"], label_visibility="collapsed", placeholder="Add Indicators...")

# Calculate timeframe
tf_map = {"1D": 2, "1W": 7, "1M": 30, "3M": 90, "1Y": 365, "All": 1000}
days = tf_map.get(timeframe, 60)
df = get_dummy_data(days)

# Apply Indicators
if "SMA 20" in indicators:
    df['SMA 20'] = df['Close'].rolling(window=min(20, len(df))).mean()
if "SMA 50" in indicators:
    df['SMA 50'] = df['Close'].rolling(window=min(50, len(df))).mean()
if "EMA 100" in indicators:
    df['EMA 100'] = df['Close'].ewm(span=min(100, len(df)), adjust=False).mean()

# Chart selection
if chart_type == "Candlestick":
    fig = plot_candlestick(df, "")
elif chart_type == "Line":
    fig = plot_line_chart(df, "")
    fig.data[0].fill = 'none' # Remove fill for pure line
else:
    # Area chart
    fig = plot_line_chart(df, "")
    fig.data[0].fill = 'tozeroy'

# Add indicator traces
if "SMA 20" in indicators:
    fig.add_trace(go.Scatter(x=df.index, y=df['SMA 20'], mode='lines', name='SMA 20', line=dict(color='#d946ef', width=2)))
if "SMA 50" in indicators:
    fig.add_trace(go.Scatter(x=df.index, y=df['SMA 50'], mode='lines', name='SMA 50', line=dict(color='#f59e0b', width=2)))
if "EMA 100" in indicators:
    fig.add_trace(go.Scatter(x=df.index, y=df['EMA 100'], mode='lines', name='EMA 100', line=dict(color='#8b5cf6', width=2)))

st.plotly_chart(fig, width="stretch")
