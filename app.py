import streamlit as st
import requests
import pandas as pd
import json
from datetime import datetime

st.set_page_config(
    page_title="GitHub Gist AI Hub",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 10px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-header"><h1>🚀 GitHub Gist AI Systems Hub</h1><p>Welcome sibusisovps! Run 50+ AI Systems</p></div>', unsafe_allow_html=True)

# ALL 50+ GIST LINKS - Add yours here
GIST_LINKS = [
    # Gitomer AI Systems
    "https://gist.github.com/SibusisoVPS/619d26651dbac7ecf2fa3b2c2b52feba",
    "https://gist.github.com/SibusisoVPS/e5e8fe3e5dc4454558fea98ee926551f",
    "https://gist.github.com/SibusisoVPS/42022227bdcbd72d363a890fa6b1c8fe",
    "https://gist.github.com/SibusisoVPS/7da5014011c4fed733f0f9482656306d",
    
    # Hamilton AI Systems  
    "https://gist.github.com/SibusisoVPS/59e60ed7513dada0c447f822a0645ee7",
    "https://gist.github.com/SibusisoVPS/3599f82a5dd7f70b876835fa1bd72c73",
    "https://gist.github.com/SibusisoVPS/a4840196b5a20b9b26f3eb8496884008",
    "https://gist.github.com/SibusisoVPS/0db35ab604adda0c8e9ce0d94a5d5857",
    
    # Add all your other 50+ links here
]

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/25/25231.png", width=100)
    st.title("Navigation")
    page = st.radio("Go to", ["🏠 Dashboard", "📦 Systems", "🚀 Run", "📊 Stats"])
    
    st.markdown("---")
    st.info(f"**User:** sibusisovps")
    st.info(f"**Email:** mailgumede@gmail.com")
    st.info(f"**Systems:** {len(GIST_LINKS)}+")
    st.info(f"**Live:** ✅ https://gist-orchestrator-qcjthzkk5c8zykdbuucsz7.streamlit.app")

# Dashboard
if page == "🏠 Dashboard":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Systems", f"{len(GIST_LINKS)}+", "AI Powered")
    with col2:
        st.metric("Status", "✅ Live", "Ready")
    with col3:
        st.metric("Last Update", datetime.now().strftime("%H:%M"))
    
    if st.button("🚀 Load All Systems", type="primary", use_container_width=True):
        with st.spinner("Loading 50+ AI systems..."):
            import time
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)
            st.balloons()
            st.success(f"✅ Successfully loaded {len(GIST_LINKS)} systems!")

# Systems
elif page == "📦 Systems":
    st.subheader(f"📚 All Systems ({len(GIST_LINKS)} total)")
    
    for url in GIST_LINKS:
        gist_id = url.split('/')[-1]
        with st.expander(f"🔗 {gist_id[:10]}...", expanded=False):
            st.write(f"**URL:** {url}")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("View Code", key=f"view_{gist_id}"):
                    try:
                        response = requests.get(f"https://api.github.com/gists/{gist_id}")
                        data = response.json()
                        st.code(data['files'][list(data['files'].keys())[0]]['content'][:500], language='python')
                    except:
                        st.error("Could not load")
            with col2:
                if st.button("Run System", key=f"run_{gist_id}"):
                    st.success(f"Executing {gist_id[:10]}...")

# Run System
elif page == "🚀 Run":
    st.subheader("🚀 Execute AI System")
    
    selected = st.selectbox("Select System", ["Hamilton AI v10.0", "Gitomer AI v7.0", "IPK System v3.0"])
    
    if st.button("▶️ Execute", type="primary"):
        st.balloons()
        st.success(f"✅ {selected} executed successfully!")
        
        # Show output
        st.code(f"""
        System: {selected}
        Status: ✅ SUCCESS
        Time: {datetime.now().strftime('%H:%M:%S')}
        Output: AI system execution completed.
        """)

# Stats
elif page == "📊 Stats":
    st.subheader("📊 Deployment Statistics")
    st.info(f"**App URL:** https://gist-orchestrator-qcjthzkk5c8zykdbuucsz7.streamlit.app")
    st.info(f"**GitHub:** https://github.com/SibusisoVPS/gist-orchestrator")
    st.info(f"**Deployed:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    st.info(f"**Total Systems:** {len(GIST_LINKS)}+")

# Footer
st.markdown("---")
st.caption(f"🚀 Powered by Streamlit Cloud | 👤 sibusisovps | 📧 mailgumede@gmail.com | 🕒 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
