import streamlit as st
import requests
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Gist Hub", layout="wide")

st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header"><h1>🚀 GitHub Gist AI Systems Hub</h1><p>Welcome sibusisovps! Run 50+ AI Systems</p></div>', unsafe_allow_html=True)

# ========== ALL YOUR 50+ GIST LINKS ==========
GIST_LINKS = [
    # Gitomer AI Systems
    "https://gist.github.com/SibusisoVPS/619d26651dbac7ecf2fa3b2c2b52feba",
    "https://gist.github.com/SibusisoVPS/e5e8fe3e5dc4454558fea98ee926551f",
    "https://gist.github.com/SibusisoVPS/42022227bdcbd72d363a890fa6b1c8fe",
    "https://gist.github.com/SibusisoVPS/7da5014011c4fed733f0f9482656306d",
    "https://gist.github.com/SibusisoVPS/54a1bf1f67dfe4effcb04fc7539ebd10",
    "https://gist.github.com/SibusisoVPS/e0a548cb27d297f6052f398b69fe6df9",
    "https://gist.github.com/SibusisoVPS/7c74257a5c1f9c534e152b2debeb25a0",
    "https://gist.github.com/SibusisoVPS/cd31ac48a4028806e552e51123457f0c",
    
    # Hamilton AI Systems
    "https://gist.github.com/SibusisoVPS/59e60ed7513dada0c447f822a0645ee7",
    "https://gist.github.com/SibusisoVPS/3599f82a5dd7f70b876835fa1bd72c73",
    "https://gist.github.com/SibusisoVPS/e7b90993c25b9e459b1f6ea5f28c14c9",
    "https://gist.github.com/SibusisoVPS/a4840196b5a20b9b26f3eb8496884008",
    "https://gist.github.com/SibusisoVPS/8884640a95c6e3b5aca0546194c789a2",
    "https://gist.github.com/SibusisoVPS/0db35ab604adda0c8e9ce0d94a5d5857",
    "https://gist.github.com/SibusisoVPS/b634e7bc98db293a19edfa43e9b36cc9",
    "https://gist.github.com/SibusisoVPS/ce5f4ff6248a45ee030f9fc418b62f1b",
    
    # Add ALL other links from your summary file here
    # Copy all 50+ links
]

st.sidebar.title("📊 Stats")
st.sidebar.metric("Systems", f"{len(GIST_LINKS)}+")
st.sidebar.metric("Status", "✅ Live")
st.sidebar.info(f"**User:** sibusisovps")

st.subheader(f"📚 Available Systems ({len(GIST_LINKS)} total)")

# Search
search = st.text_input("🔍 Search systems...")

# Filter
filtered = GIST_LINKS
if search:
    filtered = [url for url in GIST_LINKS if search.lower() in url.lower()]

# Display
for url in filtered:
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
                        st.success(f"✅ Loaded: {data.get('description', 'No description')}")
                        # Show first file content
                        files = list(data['files'].keys())
                        if files:
                            st.code(data['files'][files[0]]['content'][:500], language='python')
                except:
                    st.error("Failed to load")

st.markdown("---")
st.info(f"🌐 **Live App:** https://gist-orchestrator-qcjthzkk5c8zykdbuucsz7.streamlit.app")
st.info(f"💻 **GitHub:** https://github.com/SibusisoVPS/gist-orchestrator")
st.caption(f"👤 sibusisovps | 📧 mailgumede@gmail.com | 🕒 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
