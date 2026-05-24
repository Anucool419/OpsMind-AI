from app.rag.embeddings import retrieve_similar_incidents

query = "Pod CrashLoopBackOff due to memory issue"

results = retrieve_similar_incidents(query)

for result in results:
    print(result)
    print("=" * 50)