import streamlit as st
import os

def render_sidebar():
    # Native Top-Left Logo placement
    if os.path.exists("assets/logo.png"):
        if hasattr(st, "logo"):
            # 'large' makes it quite big, letting it default is cleaner.
            st.logo("assets/logo.png")
            
    with st.sidebar:
        if not hasattr(st, "logo") and os.path.exists("assets/logo.png"):
            # Set explicit moderate width instead of use_container_width=True
            st.image("assets/logo.png", width=140)
        else:
            st.markdown("## ⚡ NovaTrade")
        st.markdown("---")
        
        symbol = st.text_input("🔍 Search Stock", value="AAPL")
        market = st.selectbox("🌍 Select Market", ["US (S&P 500)", "Crypto", "European", "Asian"])
        
        st.markdown("---")
        theme = st.radio("🌗 Theme", ["Dark", "Light"], index=0)
        
        return symbol, market, theme
