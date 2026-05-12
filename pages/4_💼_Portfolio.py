import streamlit as st
from streamlit_lottie import st_lottie
from utils.theme import load_css
from components.sidebar import render_sidebar
from components.cards import metric_card
from utils.animations import load_lottieurl, ANIMATIONS
import plotly.graph_objects as go

st.set_page_config(page_title="Portfolio", page_icon="💼", layout="wide")
load_css()
symbol, market, theme = render_sidebar()

col1, col2 = st.columns([3, 1])
with col1:
    st.title("💼 Portfolio Tracker")
with col2:
    lottie_anim = load_lottieurl(ANIMATIONS["portfolio"])
    if lottie_anim:
        st_lottie(lottie_anim, height=120, key="port_anim")

# Summary Cards
cols = st.columns(3)
with cols[0]:
    metric_card("Total Balance", "$124,500.00", "$4,200 (3.5%)", True)
with cols[1]:
    metric_card("Day P&L", "$1,250.00", "1.0%", True)
with cols[2]:
    metric_card("Available Cash", "$15,200.00", "0.0%", True)

st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Holdings")
    holdings = [
        {"Asset": "AAPL", "Shares": 150, "Avg Price": "$145.20", "Current": "$150.10", "Return": "+3.37%"},
        {"Asset": "TSLA", "Shares": 50, "Avg Price": "$180.50", "Current": "$165.23", "Return": "-8.46%"},
        {"Asset": "MSFT", "Shares": 80, "Avg Price": "$270.00", "Current": "$289.10", "Return": "+7.07%"},
    ]
    st.dataframe(holdings, width="stretch")

with col2:
    st.subheader("Asset Allocation")
    labels = ['Tech', 'Automotive', 'Cash', 'Crypto']
    values = [60, 15, 12, 13]
    
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5, marker_colors=['#3b82f6', '#10b981', '#f59e0b', '#8b5cf6'])])
    fig.update_layout(
        template="plotly_dark",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=0, b=0)
    )
    st.plotly_chart(fig, width="stretch")
