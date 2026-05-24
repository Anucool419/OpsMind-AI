def fetch_kubernetes_logs():

    with open(
        "data/logs/kubernetes.txt",
        "r"
    ) as file:

        return file.read()