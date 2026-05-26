# OpsMind AI — Multi-Agent Incident RCA Architecture

<img width="1811" height="735" alt="image" src="https://github.com/user-attachments/assets/0aaf7e0d-9ed4-4af3-8356-8ed11b1f001b" />


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
<img width="783" height="1100" alt="Dia drawio" src="https://github.com/user-attachments/assets/936108a1-80b8-43d0-a2bb-f0f3855cc2cf" />



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
<img width="1314" height="777" alt="Screenshot 2026-05-24 172751" src="https://github.com/user-attachments/assets/0aab40f1-f8c5-4a3d-b8fa-3360cc6fa54e" />

<img width="1303" height="785" alt="Screenshot 2026-05-24 172819" src="https://github.com/user-attachments/assets/ecd1b3c8-03e7-4b75-819a-3f702eba795b" />

<img width="1319" height="572" alt="Screenshot 2026-05-24 172835" src="https://github.com/user-attachments/assets/15cfa0f4-e56f-4e0a-9f1c-7677bbd380e3" />

## Demo
#### Video link : https://www.youtube.com/watch?v=OTj5cE5ortQ

#### Deployed link : https://opsmind-ai-fuonkmwfprksqhivxcddh6.streamlit.app/

#### Dev.io post : https://dev.to/zeroshotanu/how-i-built-an-ai-powered-incident-rca-platform-with-langgraph-and-rag-423j
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

## Note

This project uses simulated observability logs and monitoring connectors to demonstrate incident analysis workflows in a production-inspired environment.
The architecture is designed to support integration with real monitoring platforms such as Datadog, Grafana, and New Relic APIs.

## Contributors

- Ananya Srinivasan  
  - AI Agent Workflow
  - RAG + FAISS Retrieval
  - LangGraph Orchestration
  - Streamlit Dashboard
  - Evaluation Framework
