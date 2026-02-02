import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="Gist Hub", layout="wide")
st.title("🚀 GitHub Gist AI Systems Hub")
st.success("Welcome sibusisovps!")

links = [
    "https://gist.github.com/SibusisoVPS/619d26651dbac7ecf2fa3b2c2b52feba",
    "https://gist.github.com/SibusisoVPS/e5e8fe3e5dc4454558fea98ee926551f",
]

for url in links:
    st.write(f"• {url}")

st.info(f"Live: https://gist-orchestrator-qcjthzkk5c8zykdbuucsz7.streamlit.app")
st.caption(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
