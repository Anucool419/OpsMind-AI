def fetch_datadog_logs():

    with open(
        "data/logs/api.json",
        "r"
    ) as file:

        return file.read()