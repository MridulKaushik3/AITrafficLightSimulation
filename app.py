# traffic_control_app.py
import streamlit as st
import tempfile
import os
import time
import cv2
from yolov8_vehicle_counter import count_vehicles_at_second_zero

st.set_page_config(layout="wide")
st.title("Smart Traffic Light Simulation 🚦")

st.write("### Upload 4 road videos (one per side)")
uploaded_videos = st.file_uploader("Upload 4 videos", type=["mp4"], accept_multiple_files=True)

if uploaded_videos and len(uploaded_videos) == 4:
    temp_video_paths = []
    for video in uploaded_videos:
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
        temp_file.write(video.read())
        temp_video_paths.append(temp_file.name)

    # Vehicle counts for each video
    vehicle_counts = [count_vehicles_at_second_zero(path) for path in temp_video_paths]

    st.write("### Intersection Overview")
    video_cols = st.columns(4)

    for i in range(4):
        video_cols[i].video(temp_video_paths[i], format="video/mp4")
        video_cols[i].write(f"**Vehicles:** {vehicle_counts[i]}")

    if st.button("Simulate Traffic Lights"):
        # Sort videos by vehicle count descending
        order = sorted(enumerate(vehicle_counts), key=lambda x: -x[1])  # [(index, count)]

        for step, (green_index, count) in enumerate(order):
            st.markdown(f"### Step {step + 1}: Road {green_index + 1} gets GREEN")

            signal_cols = st.columns(4)
            for i in range(4):
                signal = "🟢 **GREEN**" if i == green_index else "🔴 RED"
                signal_cols[i].markdown(signal, unsafe_allow_html=True)

            time.sleep(1.5)
else:
    st.warning("Please upload **exactly 4 videos**.")
