import streamlit as st
import pandas as pd

st.set_page_config(page_title="Train Dashboard", page_icon="🚆")

api_response = {
    "train_name": "Rajdhani Express",
    "train_number": "12301",
    "route": [
        {"station": "New Delhi", "arrival": "Source", "departure": "07:05"},
        {"station": "Kanpur Central", "arrival": "10:10", "departure": "10:15"},
        {"station": "Allahabad Jn", "arrival": "12:00", "departure": "12:10"},
        {"station": "Patna Jn", "arrival": "16:30", "departure": "16:40"},
        {"station": "Howrah Jn", "arrival": "21:30", "departure": "Destination"}
    ]
}

route_data = []
for stop in api_response["route"]:
    route_data.append({
        "Station": stop["station"],
        "Arrival": stop["arrival"],
        "Departure": stop["departure"]
    })

df = pd.DataFrame(route_data)

st.title("🚆 Train Route Dashboard")

st.markdown(f"### Train: {api_response['train_name']} ({api_response['train_number']})")

st.subheader("📍 Route Details")
st.dataframe(df)

st.subheader("🔍 Check Station Timing")

selected_station = st.selectbox("Select a station:", df["Station"])

station_info = df[df["Station"] == selected_station].iloc[0]

st.write(f"Arrival Time: {station_info['Arrival']}")
st.write(f"Departure Time: {station_info['Departure']}")
