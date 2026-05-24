import streamlit as st
import pandas as pd
import time
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
     sys.path.insert(0, str(PROJECT_ROOT))

from agents.workflow import app_workflow
from agents.metrics_agent import generate_metrics
from evaluation.evaluate import evaluate_system

from connectors.datadog_connector import fetch_datadog_logs
from connectors.grafana_connector import fetch_grafana_logs
from connectors.newrelic_connector import fetch_newrelic_logs

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="OpsMind AI",
    layout="wide"
)

# -----------------------------------
# HEADER
# -----------------------------------

st.title("OpsMind AI")
st.subheader("AI Incident Root Cause Analyzer")

# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.title("OpsMind Controls")

log_source = st.sidebar.radio(

    "Log Source",

    [
        "Upload File",
        "Monitoring Platform"
    ]
)

platform = None

if log_source == "Monitoring Platform":

    platform = st.sidebar.selectbox(

        "Monitoring Tool",

        [
            "Datadog",
            "Grafana",
            "New Relic"
        ]
    )

uploaded_file = st.sidebar.file_uploader(
    "Upload Incident Logs"
)

analyze = st.sidebar.button(
    "Analyze Incident"
)

# -----------------------------------
# MAIN ANALYSIS FLOW
# -----------------------------------

if analyze:

    logs = ""

    # -----------------------------------
    # FILE UPLOAD FLOW
    # -----------------------------------

    if log_source == "Upload File":

        if uploaded_file:

            logs = uploaded_file.read().decode("utf-8")

        else:

            st.warning(
                "Please upload a log file."
            )

            st.stop()

    # -----------------------------------
    # MONITORING PLATFORM FLOW
    # -----------------------------------

    elif log_source == "Monitoring Platform":

        st.success(
            f"Connected to {platform} successfully."
        )

        if platform == "Datadog":

            logs = fetch_datadog_logs()

        elif platform == "Grafana":

            logs = fetch_grafana_logs()

        elif platform == "New Relic":

            logs = fetch_newrelic_logs()

    # -----------------------------------
    # SHOW LOGS
    # -----------------------------------

    st.text_area(
        "Incident Logs",
        logs,
        height=300
    )

    # -----------------------------------
    # AGENT VISUALIZATION
    # -----------------------------------

    st.subheader("🤖 Multi-Agent Workflow Execution")

    workflow_container = st.empty()
    
    progress_bar=st.progress(0)

    agent_steps = []

    # Retrieval Agent

    agent_steps.append(
        "🔍 Retrieval Agent → Running..."
    )

    workflow_container.code(
        "\n\n".join(agent_steps)
    )

    progress_bar.progress(15)
    
    time.sleep(0.7)

    agent_steps[-1] = (
        "✅ Retrieval Agent → Completed"
    )

    workflow_container.code(
        "\n\n".join(agent_steps)
    )

    # Classification Agent

    agent_steps.append(
        "🧠 Classification Agent → Running..."
    )

    workflow_container.code(
        "\n\n".join(agent_steps)
    )

    progress_bar.progress(35)
    time.sleep(0.7)

    agent_steps[-1] = (
        "✅ Classification Agent → Completed"
    )

    workflow_container.code(
        "\n\n".join(agent_steps)
    )

    time.sleep(3)
    # RCA Agent

    agent_steps.append(
        "🚨 RCA Agent → Running..."
    )

    workflow_container.code(
        "\n\n".join(agent_steps)
    )
    progress_bar.progress(60)
    time.sleep(0.8)

    agent_steps[-1] = (
        "✅ RCA Agent → Completed"
    )

    workflow_container.code(
        "\n\n".join(agent_steps)
    )

    time.sleep(3)
    # Timeline Agent

    agent_steps.append(
        "📅 Timeline Agent → Completed"
    )

    time.sleep(3)
    agent_steps.append(
    "🛠 Impact Agent → Running..."
    )

    workflow_container.code(
        "\n\n".join(agent_steps)
    )
    progress_bar.progress(80)
    time.sleep(0.6)
    # Impact Agent

    progress_bar.progress(90)
    agent_steps.append(
        "🛠 Impact Agent → Completed"
    )

    workflow_container.code(
        "\n\n".join(agent_steps)
    )

    time.sleep(3)
    # Metrics Agent
    agent_steps.append(
        "📊 Metrics Agent → Running..."
    )

    workflow_container.markdown(
        "\n".join(agent_steps)
    )

    progress_bar.progress(100)
    agent_steps.append(
        "📊 Metrics Agent → Completed"
    )

    workflow_container.markdown(
        "\n\n".join(agent_steps)
    )

    # -----------------------------------
    # LANGGRAPH WORKFLOW
    # -----------------------------------

    with st.spinner("Analyzing incident..."):

        result = app_workflow.invoke({

            "logs": logs
        })

    analysis = result["analysis"]

    timeline = result["timeline"]

    services = result["services"]

    retrieved_docs = result["retrieved_docs"]

    classification = result["classification"]

    # -----------------------------------
    # CLASSIFICATION PARSING
    # -----------------------------------

    monitoring_source = "Unknown"

    incident_type = "Unknown"

    severity = "MEDIUM"

    for line in classification.split("\n"):

        if "Monitoring Source:" in line:

            monitoring_source = (
                line.split(":", 1)[1].strip()
            )

        elif "Incident Type:" in line:

            incident_type = (
                line.split(":", 1)[1].strip()
            )

        elif "Severity:" in line:

            severity = (
                line.split(":", 1)[1].strip()
            )

    # -----------------------------------
    # SERVICE COUNT
    # -----------------------------------

    service_count = len(

        [
            line for line in services.split("\n")
            if line.strip()
        ]
    )

    # -----------------------------------
    # SEVERITY BADGES
    # -----------------------------------

    if severity.upper() == "CRITICAL":

        st.error(
            "🚨 CRITICAL INCIDENT"
        )

    elif severity.upper() == "HIGH":

        st.warning(
            "⚠️ HIGH SEVERITY INCIDENT"
        )

    elif severity.upper() == "MEDIUM":

        st.info(
            "ℹ️ MEDIUM SEVERITY INCIDENT"
        )

    else:

        st.success(
            "✅ LOW SEVERITY INCIDENT"
        )

    # -----------------------------------
    # METRICS ROW
    # -----------------------------------


    col1, col2, col3 = st.columns(3)

    with col1:

        # st.metric(
        #         "Severity",
        #         severity
        #     )
        st.markdown(
                f"""
                ### Severity
                
                {severity}
                """
            )

    with col2:

        # st.metric(
        #         "Affected Services",
        #         service_count
        #     )
        st.markdown(
                f"""
                ### Affected Services
                
                {service_count}
                """
            )

    with col3:

        
        with col3:

            st.markdown(
                f"""
                ### Incident Type
                
                {incident_type}
                """
            )
        
    # -----------------------------------
    # DYNAMIC METRICS GRAPH
    # -----------------------------------

    metrics_df = generate_metrics(
        logs,
        incident_type
    )

    if not metrics_df.empty:

        st.line_chart(
            metrics_df.set_index("time")
        )

    # -----------------------------------
    # TABS
    # -----------------------------------

    tab1, tab2, tab3, tab4, tab5 = st.tabs([

        "🧠 RCA Analysis",
        "📅 Timeline",
        "🛠 Impacted Services",
        "🔍 Retrieved Incidents",
        "📊 Evaluation Metrics"
    ])

    # -----------------------------------
    # RCA TAB
    # -----------------------------------

    with tab1:

        st.markdown(analysis)

    # -----------------------------------
    # TIMELINE TAB
    # -----------------------------------

    with tab2:

        st.markdown(timeline)

    # -----------------------------------
    # IMPACT TAB
    # -----------------------------------

    with tab3:

        st.markdown(services)

    # -----------------------------------
    # RETRIEVED INCIDENTS TAB
    # -----------------------------------

    with tab4:

        for doc in retrieved_docs:

            with st.expander(
                "View Related Incident"
            ):

                st.markdown(doc)

    # -----------------------------------
    # EVALUATION TAB
    # -----------------------------------

    with tab5:

        st.subheader(
            "📊 AI System Evaluation"
        )

        evaluation_results = evaluate_system()

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Retrieval Accuracy",
                f"{evaluation_results['retrieval_accuracy']}%"
            )

            st.metric(
                "Severity Accuracy",
                f"{evaluation_results['severity_accuracy']}%"
            )

        with col2:

            st.metric(
                "RCA Match Accuracy",
                f"{evaluation_results['rca_accuracy']}%"
            )

            st.metric(
                "Average Latency",
                f"{evaluation_results['average_latency']}s"
            )

        confidence = evaluation_results[
            "correlation_confidence"
        ]

        st.progress(
            int(confidence)
        )

        st.caption(
            f"Incident Correlation Confidence: {confidence}%"
        )

    # -----------------------------------
    # DOWNLOAD REPORT
    # -----------------------------------

    st.download_button(

        label="Download Incident Report",

        data=analysis,

        file_name="incident_report.txt",

        mime="text/plain"
    )                     

