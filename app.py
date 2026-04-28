import streamlit as st
import pandas as pd

from wifi_scanner import scan_wifi
from device_tracker import scan_devices
from log_monitor import parse_logs

st.set_page_config(layout="wide")

st.title("🛡️ Personal Cyber Defense Suite")

tab1, tab2, tab3 = st.tabs(["📡 WiFi Security", "👀 Devices", "🧠 SOC Logs"])

# ---------------- WIFI ----------------
with tab1:
    st.header("WiFi Security Analyzer")

    if st.button("Scan WiFi"):
        networks = scan_wifi()
        df = pd.DataFrame(networks)

        st.dataframe(df)

# ---------------- DEVICES ----------------
with tab2:
    st.header("Network Device Tracker")

    if st.button("Scan Devices"):
        devices = scan_devices()
        df = pd.DataFrame(devices)

        # ✅ STEP 2 — ADD THIS FUNCTION HERE
        def device_risk(ip):
            if ip.endswith(".1"):
                return "Router"
            elif ip.endswith(".255"):
                return "Broadcast"
            else:
                return "Unknown Device"

        # ✅ Apply classification
        df["Type"] = df["IP"].apply(device_risk)

        st.dataframe(df)

# ---------------- LOGS ----------------
with tab3:
    st.header("Security Log Monitor")

    df = parse_logs()

    st.dataframe(df)