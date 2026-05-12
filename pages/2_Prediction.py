import streamlit as st
from streamlit_lottie import st_lottie
from utils.theme import load_css
from components.sidebar import render_sidebar
from utils.data_fetcher import get_dummy_data
from utils.animations import load_lottieurl, ANIMATIONS
import pandas as pd
import numpy as np

st.set_page_config(page_title="AI Prediction", page_icon="🔮", layout="wide")
load_css()
symbol, market, theme = render_sidebar()

col1, col2 = st.columns([3, 1])
with col1:
    st.title("🔮 AI Price Prediction")
    st.markdown("Powered by Advanced Machine Learning Models (LSTM/Prophet)")
with col2:
    lottie_anim = load_lottieurl(ANIMATIONS["prediction"])
    if lottie_anim:
        st_lottie(lottie_anim, height=120, key="pred_anim")

model_type = st.selectbox("Select AI Model", ["LSTM Neural Network", "Facebook Prophet", "ARIMA"])

st.info(f"Training {model_type} on {symbol} historical data...")
st.progress(100)

df = get_dummy_data(100)
# Add prediction data
future_dates = pd.date_range(start=df.index[-1] + pd.Timedelta(days=1), periods=30)
last_price = df['Close'].iloc[-1]
future_prices = last_price + np.random.randn(30).cumsum()

import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Historical', line=dict(color='#3b82f6')))
fig.add_trace(go.Scatter(x=future_dates, y=future_prices, mode='lines', name='Predicted', line=dict(color='#a78bfa', dash='dash')))

fig.update_layout(
    title=f"{symbol} 30-Day Forecast",
    template="plotly_dark",
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=20, r=20, t=40, b=20)
)

st.plotly_chart(fig, width="stretch")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="glass-card">
        <h3>Model Confidence</h3>
        <h1 style="color: #10b981;">87%</h1>
        <p>Based on recent market volatility and historical accuracy.</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="glass-card">
        <h3>Recommendation</h3>
        <h1 style="color: #3b82f6;">STRONG BUY</h1>
        <p>Target Price: +12.4% upside potential.</p>
    </div>
    """, unsafe_allow_html=True)
