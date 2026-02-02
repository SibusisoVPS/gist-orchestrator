import streamlit as st
import requests

st.set_page_config(page_title="Gist Hub", layout="wide")
st.title("🚀 GitHub Gist AI Systems Hub")
st.success("Welcome sibusisovps!")

# Your links
links = [
    "https://gist.github.com/SibusisoVPS/619d26651dbac7ecf2fa3b2c2b52feba",
    "https://gist.github.com/SibusisoVPS/e5e8fe3e5dc4454558fea98ee926551f",
]

for url in links:
    with st.expander(f"📦 {url.split('/')[-1]}"):
        st.write(url)
        if st.button("Load", key=url):
            st.info("Loading...")

st.info("Live at: https://gist-orchestrator-qcjthzkk5c8zykdbuucsz7.streamlit.app")
