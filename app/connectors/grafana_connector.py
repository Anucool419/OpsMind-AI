def fetch_grafana_logs():

    with open(
        "data/logs/database.txt",
        "r"
    ) as file:

        return file.read()