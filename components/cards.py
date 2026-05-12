import streamlit as st

def metric_card(title, value, change, is_positive=True):
    change_class = "positive" if is_positive else "negative"
    sign = "+" if is_positive else ""
    
    html = f"""
    <div class="glass-card">
        <div class="metric-title">{title}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-change {change_class}">{sign}{change}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)
