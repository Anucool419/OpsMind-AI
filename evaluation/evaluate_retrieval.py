from app.rag.embeddings import retrieve_similar_incidents
from evaluation.test_cases import test_cases

correct = 0

for case in test_cases:

    results = retrieve_similar_incidents(case["query"])

    combined = " ".join(results)

    if case["expected_keyword"] in combined:
        correct += 1

accuracy = correct / len(test_cases)

print(f"Retrieval Accuracy: {accuracy * 100:.2f}%")