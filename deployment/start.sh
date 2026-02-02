#!/bin/bash
echo "🚀 Starting Gist Orchestrator..."
python orchestrator.py &
streamlit run dashboard.py --server.port 8501 &
echo "✅ Orchestrator running on port 8000"
echo "📊 Dashboard available at: http://localhost:8501"
wait
