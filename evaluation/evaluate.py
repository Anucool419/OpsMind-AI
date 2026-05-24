import time

from evaluation.test_cases import test_cases

from app.rag.embeddings import retrieve_similar_incidents
from app.agents.rca_agent import analyze_incident


def evaluate_system():

    retrieval_correct = 0

    severity_correct = 0

    rca_correct = 0

    total_latency = 0

    total_cases = len(test_cases)

    for case in test_cases:

        start_time = time.time()

        retrieved_docs = retrieve_similar_incidents(
            case["query"]
        )

        retrieved_context = "\n".join(
            retrieved_docs
        )

        analysis = analyze_incident(
            logs=case["query"],
            retrieved_context=retrieved_context,
            monitoring_source=case["monitoring_source"],
            incident_type=case["incident_type"] 
            
        )

        end_time = time.time()

        latency = end_time - start_time

        total_latency += latency

        # --------------------------
        # Retrieval Accuracy
        # --------------------------

        combined_docs = " ".join(
            retrieved_docs
        )

        if case["expected_keyword"] in combined_docs:
            retrieval_correct += 1

        # --------------------------
        # Severity Accuracy
        # --------------------------

        if case["expected_severity"] in analysis:
            severity_correct += 1

        # --------------------------
        # RCA Match Accuracy
        # --------------------------

        if case["expected_root_cause"].lower() in analysis.lower():
            rca_correct += 1

    results = {

        "retrieval_accuracy":
            round(
                retrieval_correct / total_cases * 100,
                2
            ),

        "severity_accuracy":
            round(
                severity_correct / total_cases * 100,
                2
            ),

        "rca_accuracy":
            round(
                rca_correct / total_cases * 100,
                2
            ),

        "average_latency":
            round(
                total_latency / total_cases,
                2
            ),

        "correlation_confidence":
            round(
                (
                    retrieval_correct +
                    severity_correct +
                    rca_correct
                ) / (3 * total_cases) * 100,
                2
            )
    }

    return results