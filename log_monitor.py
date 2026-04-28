import pandas as pd
from datetime import datetime

def parse_logs():
    data = []

    with open("logs.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split(" ")
        timestamp = " ".join(parts[0:2])
        event = parts[2] + " " + parts[3]
        ip = parts[-1]

        data.append({
            "timestamp": datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"),
            "event": event,
            "ip": ip
        })

    return pd.DataFrame(data)