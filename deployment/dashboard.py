import streamlit as st
import requests
import yaml
from datetime import datetime

st.set_page_config(page_title="Gist Orchestrator Dashboard", layout="wide")

# Load config
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

st.title("🚀 Gist Orchestrator Dashboard")
st.success("Enterprise AI Systems Federation")

# Sidebar
with st.sidebar:
    st.header("📊 System Status")
    st.metric("Active Nodes", len([n for n in config['nodes'] if n['active']]))
    st.metric("Registered Systems", len(config['systems']))
    st.metric("Status", "✅ Operational")
    
    st.header("⚡ Quick Actions")
    if st.button("🔄 Refresh All Systems"):
        st.rerun()
    
    if st.button("📊 View Execution Logs"):
        st.info("Opening logs...")

# Main tabs
tab1, tab2, tab3 = st.tabs(["🏗️ Systems", "🖥️ Nodes", "📈 Analytics"])

with tab1:
    st.subheader("Registered AI Systems")
    for system_name, system_info in config['systems'].items():
        with st.expander(f"🔧 {system_name} v{system_info['version']}"):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Category:** {system_info['category']}")
                st.write(f"**Required Maturity:** {system_info['required_maturity']}")
            with col2:
                if st.button(f"Execute {system_name}", key=f"exec_{system_name}"):
                    st.info(f"Executing {system_name}...")

with tab2:
    st.subheader("Execution Nodes")
    for node in config['nodes']:
        status = "🟢 Active" if node['active'] else "🔴 Inactive"
        st.write(f"**{node['id']}** - {status}")
        st.write(f"CPU: {node['cpu']} cores | Memory: {node['memory']} MB")

with tab3:
    st.subheader("System Analytics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Executions", "1,248")
    with col2:
        st.metric("Success Rate", "98.2%")
    with col3:
        st.metric("Avg Response Time", "1.4s")

st.markdown("---")
st.caption(f"👤 sibusisovps | 📧 mailgumede@gmail.com | 🕒 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
