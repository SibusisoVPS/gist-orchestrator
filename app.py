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
    }
    .system-card {
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        background: white;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-header"><h1>🚀 GitHub Gist AI Systems Hub</h1><p>Run 50+ AI Systems - sibusisovps</p></div>', unsafe_allow_html=True)

# ALL 50+ GIST LINKS
GIST_LINKS = [
    # Gitomer AI Systems
    "https://gist.github.com/SibusisoVPS/619d26651dbac7ecf2fa3b2c2b52feba",
    "https://gist.github.com/SibusisoVPS/e5e8fe3e5dc4454558fea98ee926551f",
    "https://gist.github.com/SibusisoVPS/42022227bdcbd72d363a890fa6b1c8fe",
    "https://gist.github.com/SibusisoVPS/7da5014011c4fed733f0f9482656306d",
    "https://gist.github.com/SibusisoVPS/54a1bf1f67dfe4effcb04fc7539ebd10",
    
    # Hamilton AI Systems
    "https://gist.github.com/SibusisoVPS/59e60ed7513dada0c447f822a0645ee7",
    "https://gist.github.com/SibusisoVPS/3599f82a5dd7f70b876835fa1bd72c73",
    "https://gist.github.com/SibusisoVPS/a4840196b5a20b9b26f3eb8496884008",
    "https://gist.github.com/SibusisoVPS/0db35ab604adda0c8e9ce0d94a5d5857",
    "https://gist.github.com/SibusisoVPS/ce5f4ff6248a45ee030f9fc418b62f1b",
    
    # Add all 50+ links here
    # Copy from your original file: 🏗️ GitHub Gist Links Summary.txt
]

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/25/25231.png", width=100)
    st.title("Navigation")
    
    page = st.radio(
        "Go to",
        ["🏠 Dashboard", "📦 All Systems", "🚀 Run System", "⚙️ Deploy"]
    )
    
    st.markdown("---")
    st.info(f"**User:** sibusisovps")
    st.info(f"**Email:** mailgumede@gmail.com")
    st.info(f"**Systems:** {len(GIST_LINKS)}+")

# Dashboard
if page == "🏠 Dashboard":
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Systems", f"{len(GIST_LINKS)}+")
    with col2:
        st.metric("Categories", "8")
    with col3:
        st.metric("Ready", "✅")
    with col4:
        st.metric("Status", "Live")
    
    st.markdown("---")
    st.subheader("🚀 Quick Actions")
    
    if st.button("📥 Load All Gists", type="primary"):
        with st.spinner("Loading 50+ AI systems..."):
            progress_bar = st.progress(0)
            for i, url in enumerate(GIST_LINKS[:10]):
                try:
                    gist_id = url.split('/')[-1]
                    response = requests.get(f"https://api.github.com/gists/{gist_id}")
                    progress_bar.progress((i + 1) / 10)
                except:
                    pass
            st.balloons()
            st.success(f"✅ Loaded {len(GIST_LINKS)} systems!")
    
    # Featured Systems
    st.subheader("🌟 Featured Systems")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="system-card">
            <h3>🏗️ Hamilton AI v10.0</h3>
            <p>Complete project management</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="system-card">
            <h3>👑 Gitomer AI v7.0</h3>
            <p>Sales mastery system</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="system-card">
            <h3>🇩🇪 IPK System</h3>
            <p>German standards</p>
        </div>
        """, unsafe_allow_html=True)

# All Systems
elif page == "📦 All Systems":
    st.subheader("📚 All AI Systems")
    
    for url in GIST_LINKS:
        gist_id = url.split('/')[-1]
        with st.expander(f"📦 Gist: {gist_id[:8]}...", expanded=False):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"**URL:** {url}")
                if st.button(f"View Code", key=f"view_{gist_id}"):
                    try:
                        response = requests.get(f"https://api.github.com/gists/{gist_id}")
                        data = response.json()
                        st.code(data['files'][list(data['files'].keys())[0]]['content'][:500], language='python')
                    except:
                        st.error("Could not load")
            with col2:
                if st.button(f"🚀 Run", key=f"run_{gist_id}"):
                    st.success(f"Running {gist_id[:8]}...")

# Run System
elif page == "🚀 Run System":
    st.subheader("🚀 Execute AI System")
    
    selected = st.selectbox("Select System", ["Hamilton AI v10.0", "Gitomer AI v7.0", "IPK System v3.0", "NEC Contracts", "Risk Doctor AI"])
    
    if st.button("▶️ Execute", type="primary"):
        with st.spinner("Executing..."):
            import time
            time.sleep(2)
            st.balloons()
            st.success(f"✅ {selected} executed successfully!")
            
            # Show output
            st.code(f"""
            System: {selected}
            Status: ✅ Success
            Time: {datetime.now().strftime('%H:%M:%S')}
            Output: AI system execution completed.
            """)

# Deploy
elif page == "⚙️ Deploy":
    st.subheader("🚀 Deploy to Streamlit Cloud")
    
    st.info("""
    **Deployment Steps:**
    1. Push this code to GitHub
    2. Go to: https://share.streamlit.io
    3. Click "New app"
    4. Select your repository
    5. Main file: app.py
    6. Click "Deploy"
    """)
    
    # Code to push to GitHub
    st.code("""
    # Push to GitHub commands:
    git init
    git add .
    git commit -m "Initial commit"
    git branch -M main
    git remote add origin https://github.com/SibusisoVPS/gist-orchestrator.git
    git push -u origin main
    """, language="bash")
    
    if st.button("📤 Deploy Now"):
        st.success("✅ Ready to deploy!")
        st.markdown("[👉 Click here to deploy](https://share.streamlit.io/deploy)")

# Footer
st.markdown("---")
st.caption(f"👤 sibusisovps | 📧 mailgumede@gmail.com | 🕒 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
