# 🚦 Smart Traffic Light Simulation

This is a Streamlit web application that simulates a smart traffic light system using real-time or uploaded video input. The system analyzes traffic flow using a YOLO-based object detection model and counts the number of vehicles on the road.

🔗 **Live App**: [Click here to try it out](https://aitrafficlightsimulation.streamlit.app/)

## 🔍 Features

- Upload a video or use your camera feed.
- Detect and count vehicles using YOLOv8.
- Display total vehicles on each side of the road.
- Simulate dynamic traffic signal behavior based on congestion.

## 🛠️ Tech Stack

- Python
- Streamlit
- OpenCV
- YOLOv8 (Ultralytics)
- TensorFlow (for optional emergency vehicle detection)

## 🚧 Future Work

In future updates, the system will include **priority for emergency vehicles** like ambulances and fire trucks. The traffic light will automatically turn green for lanes with emergency vehicles detected using EfficientNet or other pre-trained classifiers.

## 📁 Project Structure

