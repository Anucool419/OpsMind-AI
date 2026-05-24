# OpsMind AI

AI-powered incident root cause analysis platform
for DevOps and SRE teams.

## Problem Statement
During outages, engineers waste valuable time searching logs, dashboards, and alerts to identify the root cause.

Solution:  An AI agent that connects with monitoring tools like Datadog, Grafana, or New Relic, analyzes logs and incidents in real-time, identifies probable root causes, and suggests fixes instantly.

## Features
- Multi-agent workflow orchestration using LangGraph
- Retrieval-Augmented Generation (RAG) for historical incident matching
- FAISS vector similarity search
- Monitoring platform connector architecture
- Automated incident timeline generation
- Impacted service detection
- Dynamic incident metrics visualization
- AI system evaluation dashboard
- Downloadable incident reports
- Streamlit-based observability dashboard

## Architecture
(add architecture image)


## Tech Stack
- Python
- Streamlit
- LangGraph
- FAISS
- Groq LLM API
- SentenceTransformers

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Anucool419/OpsMind-AI.git

cd OpsMind-AI
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

#### Windows
```bash
venv\Scripts\activate
```

#### Mac/Linux
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key
```

### 5. Run the Application

```bash
streamlit run app/streamlit_app.py
```


## Screenshots
(add screenshots)

## Demo
(add deployed link)

## Evaluation Metrics
OpsMind AI includes an evaluation layer to measure
system reliability and incident analysis quality.

### Metrics Tracked

| Metric | Description |
|---|---|
| Retrieval Accuracy | Measures whether relevant historical incidents were retrieved correctly |
| RCA Match Accuracy | Measures similarity between generated RCA and expected RCA |
| Severity Accuracy | Evaluates incident severity classification correctness |
| Average Latency | Measures end-to-end AI analysis response time |
| Correlation Confidence | Indicates confidence in incident correlation analysis |

## Future Improvements

- Real-time observability ingestion
- Slack/MS Teams alert integrations
- Kubernetes event streaming
- Live Datadog/New Relic APIs
- Autonomous remediation agents
- Multi-tenant incident analytics

## Contributors

- Ananya Srinivasan  
  - AI Agent Workflow
  - RAG + FAISS Retrieval
  - LangGraph Orchestration
  - Streamlit Dashboard
  - Evaluation Framework