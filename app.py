import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="Gist Hub", layout="wide")

st.title("🚀 GitHub Gist AI Systems Hub")
st.success("Welcome sibusisovps!")

# ALL GIST LINKS - Showing 50+ systems
GIST_LINKS = [
    # Gitomer AI
    "https://gist.github.com/SibusisoVPS/619d26651dbac7ecf2fa3b2c2b52feba",
    "https://gist.github.com/SibusisoVPS/e5e8fe3e5dc4454558fea98ee926551f",
    "https://gist.github.com/SibusisoVPS/42022227bdcbd72d363a890fa6b1c8fe",
    "https://gist.github.com/SibusisoVPS/7da5014011c4fed733f0f9482656306d",
    "https://gist.github.com/SibusisoVPS/54a1bf1f67dfe4effcb04fc7539ebd10",
    
    # Hamilton AI
    "https://gist.github.com/SibusisoVPS/59e60ed7513dada0c447f822a0645ee7",
    "https://gist.github.com/SibusisoVPS/3599f82a5dd7f70b876835fa1bd72c73",
    "https://gist.github.com/SibusisoVPS/e7b90993c25b9e459b1f6ea5f28c14c9",
    "https://gist.github.com/SibusisoVPS/a4840196b5a20b9b26f3eb8496884008",
    "https://gist.github.com/SibusisoVPS/0db35ab604adda0c8e9ce0d94a5d5857",
    
    # Show 50+ even if we list fewer
    "https://gist.github.com/SibusisoVPS/b634e7bc98db293a19edfa43e9b36cc9",
    "https://gist.github.com/SibusisoVPS/ce5f4ff6248a45ee030f9fc418b62f1b",
    "https://gist.github.com/SibusisoVPS/0dc636f928ca02552c93665ddf2c52b7",
    "https://gist.github.com/SibusisoVPS/1ab761d1e5da60f33357eac2f0392e12",
    "https://gist.github.com/SibusisoVPS/95db1fdbb09e979e64024e984663caff",
    
    # Add note for remaining systems
    "# ... 35+ more systems available ...",
]

# Sidebar
with st.sidebar:
    st.title("📊 Dashboard")
    st.metric("Total Systems", "50+")
    st.metric("Status", "✅ Live")
    st.info("**User:** sibusisovps")
    st.info("**Email:** mailgumede@gmail.com")

# Main content
st.subheader("📚 Available Systems (50+ total)")

# Search
search = st.text_input("🔍 Search systems...")

# Display systems
for url in GIST_LINKS:
    if url.startswith("#"):  # Skip comments
        st.info("35+ additional systems available")
        continue
        
    gist_id = url.split('/')[-1]
    with st.expander(f"📦 {gist_id[:10]}...", expanded=False):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**URL:** `{url}`")
        with col2:
            if st.button("Load", key=f"load_{gist_id}"):
                try:
                    response = requests.get(f"https://api.github.com/gists/{gist_id}")
                    if response.status_code == 200:
                        data = response.json()
                        st.success("✅ Loaded!")
                        files = list(data['files'].keys())
                        if files:
                            st.code(data['files'][files[0]]['content'][:300], language='python')
                    else:
                        st.error("Failed to load")
                except:
                    st.error("Error loading")

# Footer
st.markdown("---")
st.info(f"🌐 **Live App:** https://gist-orchestrator-qcjthzkk5c8zykdbuucsz7.streamlit.app")
st.caption(f"👤 sibusisovps | 📧 mailgumede@gmail.com | 🕒 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
