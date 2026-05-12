import streamlit as st
from streamlit_lottie import st_lottie
from utils.theme import load_css
from components.sidebar import render_sidebar
from utils.animations import load_lottieurl, ANIMATIONS

st.set_page_config(page_title="Market News", page_icon="📰", layout="wide")
load_css()
symbol, market, theme = render_sidebar()

col1, col2 = st.columns([3, 1])
with col1:
    st.title("📰 AI Curated Market News")
with col2:
    lottie_anim = load_lottieurl(ANIMATIONS["news"])
    if lottie_anim:
        st_lottie(lottie_anim, height=100, key="news_anim")

news_items = [
    {
        "title": f"Tech Stocks Rally on {symbol} Earnings Beat",
        "time": "2 hours ago",
        "sentiment": "Positive",
        "summary": f"Major indices saw a significant boost today as {symbol} reported Q3 earnings that exceeded analyst expectations across the board.",
        "source": "Financial Times"
    },
    {
        "title": "Fed Rate Hike Signals Mixed Reactions",
        "time": "4 hours ago",
        "sentiment": "Neutral",
        "summary": "The Federal Reserve's latest meeting minutes suggest a potential pause in rate hikes, leading to volatile trading sessions.",
        "source": "Bloomberg"
    },
    {
        "title": "New Regulations Threaten Crypto Market",
        "time": "5 hours ago",
        "sentiment": "Negative",
        "summary": "Proposed regulatory frameworks in Europe could impose strict constraints on major cryptocurrency exchanges.",
        "source": "CoinDesk"
    }
]

for item in news_items:
    sentiment_color = "#10b981" if item["sentiment"] == "Positive" else "#ef4444" if item["sentiment"] == "Negative" else "#f59e0b"
    
    st.markdown(f"""
    <div class="glass-card">
        <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
            <span style="color: var(--text-muted); font-size: 0.8rem;">{item["time"]} • {item["source"]}</span>
            <span style="color: {sentiment_color}; font-weight: 600; font-size: 0.8rem;">{item["sentiment"]}</span>
        </div>
        <h3 style="margin-bottom: 0.5rem; background: none; -webkit-text-fill-color: var(--text-main); font-size: 1.2rem;">{item["title"]}</h3>
        <p style="color: var(--text-muted);">{item["summary"]}</p>
    </div>
    """, unsafe_allow_html=True)
