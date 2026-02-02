import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="Gist Hub", layout="wide")

# Title
st.title("🚀 GitHub Gist AI Systems Hub")
st.success("Welcome sibusisovps!")

# Your Gist links
links = [
    "https://gist.github.com/SibusisoVPS/619d26651dbac7ecf2fa3b2c2b52feba",
    "https://gist.github.com/SibusisoVPS/e5e8fe3e5dc4454558fea98ee926551f",
    "https://gist.github.com/SibusisoVPS/42022227bdcbd72d363a890fa6b1c8fe",
    "https://gist.github.com/SibusisoVPS/7da5014011c4fed733f0f9482656306d",
]

# Sidebar
with st.sidebar:
    st.title("Stats")
    st.metric("Systems", len(links))
    st.metric("Status", "✅ Live")
    st.write(f"**User:** sibusisovps")

# Main content
st.subheader(f"📚 Your Systems ({len(links)} total)")

for url in links:
    gist_id = url.split('/')[-1]
    with st.expander(f"🔗 {gist_id[:10]}..."):
        st.write(f"**URL:** {url}")
        if st.button("Load", key=gist_id):
            try:
                response = requests.get(f"https://api.github.com/gists/{gist_id}")
                if response.status_code == 200:
                    data = response.json()
                    st.success("✅ Loaded!")
                    st.code(data['files'][list(data['files'].keys())[0]]['content'][:200], language='python')
                else:
                    st.error("Failed to load")
            except:
                st.error("Error loading")

# Footer
st.markdown("---")
st.info(f"🌐 **Live App:** https://gist-orchestrator-qcjthzkk5c8zykdbuucsz7.streamlit.app")
st.caption(f"👤 sibusisovps | 📧 mailgumede@gmail.com | 🕒 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
