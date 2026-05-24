import random
import pandas as pd


def generate_metrics(
    logs,
    incident_type
):

    timestamps = []

    values = []

    if "OOM" in incident_type:

        for i in range(5):

            timestamps.append(f"10:0{i}")

            values.append(
                random.randint(70, 100)
            )

        metric_name = "memory_usage"

    elif "Database" in incident_type:

        for i in range(5):

            timestamps.append(f"10:0{i}")

            values.append(
                random.randint(40, 95)
            )

        metric_name = "active_connections"

    else:

        for i in range(5):

            timestamps.append(f"10:0{i}")

            values.append(
                random.randint(10, 80)
            )

        metric_name = "error_rate"

    df = pd.DataFrame({

        "time": timestamps,

        metric_name: values
    })

    return df