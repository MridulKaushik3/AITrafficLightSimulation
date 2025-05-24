# yolov8_vehicle_counter.py
import cv2
from ultralytics import YOLO
import numpy as np

model = YOLO("yolov8n.pt")
vehicle_classes = [2, 3, 5, 7]
class_names = model.names

def count_vehicles_at_second_zero(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return 0
    
    ret, frame = cap.read()  # Read first frame
    if not ret:
        return 0
    
    # Resize frame for fast detection
    height, width = frame.shape[:2]
    if width > 320:
        scale = 320 / width
        frame = cv2.resize(frame, (320, int(height * scale)))

    result = model(frame, verbose=False)[0]

    count = sum(1 for box in result.boxes if int(box.cls) in vehicle_classes)
    cap.release()
    return count
