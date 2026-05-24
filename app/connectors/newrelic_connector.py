def fetch_newrelic_logs():

    with open(
        "data/logs/api.json",
        "r"
    ) as file:

        logs = file.read()

    return logs