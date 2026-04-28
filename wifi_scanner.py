import subprocess

def scan_wifi():
    try:
        output = subprocess.check_output(
            ["netsh", "wlan", "show", "networks", "mode=bssid"],
            encoding="utf-8"
        )
    except:
        return []

    networks = []
    current = {}

    for line in output.split("\n"):
        line = line.strip()

        if line.startswith("SSID"):
            if current:
                networks.append(current)
                current = {}
            current["SSID"] = line.split(":", 1)[1].strip()

        elif "BSSID" in line:
            current["BSSID"] = line.split(":", 1)[1].strip()

        elif "Signal" in line:
            current["Signal"] = line.split(":", 1)[1].strip()

        elif "Authentication" in line:
            current["Security"] = line.split(":", 1)[1].strip()

    if current:
        networks.append(current)

    return networks