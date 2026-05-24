from typing import TypedDict


class IncidentState(TypedDict):

    logs: str

    retrieved_docs: list

    retrieved_context: str

    analysis: str

    timeline: str

    services: str

    classification: str

from langgraph.graph import StateGraph, END

from rag.embeddings import retrieve_similar_incidents

from agents.rca_agent import (
    analyze_incident,
    generate_timeline,
    extract_impacted_services,
    classify_incident
)

def retrieval_agent(state):

    retrieved_docs = retrieve_similar_incidents(
        state["logs"]
    )

    retrieved_context = "\n\n".join(
        retrieved_docs
    )

    return {
        "retrieved_docs": retrieved_docs,
        "retrieved_context": retrieved_context
    }

def classification_agent(state):

    classification = classify_incident(
        state["logs"]
    )

    return {
        "classification": classification
    }

def rca_agent(state):

    classification = state["classification"]

    monitoring_source = "Unknown"
    incident_type = "Unknown"

    for line in classification.split("\n"):

        if "Monitoring Source:" in line:
            monitoring_source = line.split(":")[1].strip()

        elif "Incident Type:" in line:
            incident_type = line.split(":")[1].strip()

    analysis = analyze_incident(
        state["logs"],
        state["retrieved_context"],
        monitoring_source,
        incident_type
    )

    return {
        "analysis": analysis
    }

def timeline_agent(state):

    timeline = generate_timeline(
        state["logs"]
    )

    return {
        "timeline": timeline
    }

def impact_agent(state):

    services = extract_impacted_services(
        state["logs"]
    )

    return {
        "services": services
    }
workflow = StateGraph(
    IncidentState
)

workflow.add_node(
    "retrieval_agent",
    retrieval_agent
)

workflow.add_node(
    "classification_agent",
    classification_agent
)

workflow.add_node(
    "rca_agent",
    rca_agent
)

workflow.add_node(
    "timeline_agent",
    timeline_agent
)

workflow.add_node(
    "impact_agent",
    impact_agent
)

workflow.set_entry_point(
    "retrieval_agent"
)

workflow.add_edge(
    "retrieval_agent",
    "classification_agent"
)

workflow.add_edge(
    "classification_agent",
    "rca_agent"
)

workflow.add_edge(
    "rca_agent",
    "timeline_agent"
)

workflow.add_edge(
    "timeline_agent",
    "impact_agent"
)

workflow.add_edge(
    "impact_agent",
    END
)

app_workflow = workflow.compile()