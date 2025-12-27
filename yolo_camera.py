#!/usr/bin/env python3
"""
YOLO Object Detection using Laptop Camera
This script performs real-time object detection using YOLOv3 algorithm
"""

import cv2
import numpy as np
import os
import sys

# Configuration
CONFIDENCE_THRESHOLD = 0.5
NMS_THRESHOLD = 0.4
INPUT_WIDTH = 416
INPUT_HEIGHT = 416

# Paths for YOLO files
YOLO_DIR = "yolo_files"
WEIGHTS_PATH = os.path.join(YOLO_DIR, "yolov3.weights")
CONFIG_PATH = os.path.join(YOLO_DIR, "yolov3.cfg")
NAMES_PATH = os.path.join(YOLO_DIR, "coco.names")


def download_yolo_files():
    """
    Instructions to download YOLO files if they don't exist
    """
    if not os.path.exists(YOLO_DIR):
        os.makedirs(YOLO_DIR)
    
    files_exist = (
        os.path.exists(WEIGHTS_PATH) and
        os.path.exists(CONFIG_PATH) and
        os.path.exists(NAMES_PATH)
    )
    
    if not files_exist:
        print("YOLO files not found. Please download the following files:")
        print("\n1. YOLOv3 Weights (237 MB):")
        print("   wget https://pjreddie.com/media/files/yolov3.weights")
        print(f"   Move to: {WEIGHTS_PATH}")
        print("\n2. YOLOv3 Config:")
        print("   wget https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg")
        print(f"   Move to: {CONFIG_PATH}")
        print("\n3. COCO Names:")
        print("   wget https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names")
        print(f"   Move to: {NAMES_PATH}")
        print("\nOr run: python download_yolo_files.py")
        return False
    
    return True


def load_yolo_model():
    """
    Load YOLO model from weights and configuration files
    """
    print("Loading YOLO model...")
    net = cv2.dnn.readNetFromDarknet(CONFIG_PATH, WEIGHTS_PATH)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
    
    # Get output layer names
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    
    print("YOLO model loaded successfully!")
    return net, output_layers


def load_class_names():
    """
    Load class names from coco.names file
    """
    with open(NAMES_PATH, 'r') as f:
        classes = [line.strip() for line in f.readlines()]
    return classes


def detect_objects(frame, net, output_layers, classes):
    """
    Detect objects in a frame using YOLO
    """
    height, width, _ = frame.shape
    
    # Create blob from frame
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (INPUT_WIDTH, INPUT_HEIGHT),
                                  swapRB=True, crop=False)
    
    # Set input and perform forward pass
    net.setInput(blob)
    outputs = net.forward(output_layers)
    
    # Initialize lists for detection results
    boxes = []
    confidences = []
    class_ids = []
    
    # Process each output
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            
            if confidence > CONFIDENCE_THRESHOLD:
                # Get bounding box coordinates
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                
                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    
    # Apply Non-Maximum Suppression
    indices = cv2.dnn.NMSBoxes(boxes, confidences, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
    
    return boxes, confidences, class_ids, indices


def draw_detections(frame, boxes, confidences, class_ids, indices, classes):
    """
    Draw bounding boxes and labels on the frame
    """
    if len(indices) > 0:
        for i in indices.flatten():
            x, y, w, h = boxes[i]
            
            # Generate random color for each class
            color = (0, 255, 0)
            
            # Draw bounding box
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            
            # Draw label
            label = f"{classes[class_ids[i]]}: {confidences[i]:.2f}"
            cv2.putText(frame, label, (x, y - 10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
    return frame


def main():
    """
    Main function to run YOLO detection on camera feed
    """
    print("=" * 50)
    print("YOLO Camera Object Detection")
    print("=" * 50)
    
    # Check if YOLO files exist
    if not download_yolo_files():
        print("\nPlease download the required files first.")
        sys.exit(1)
    
    # Load YOLO model and class names
    try:
        net, output_layers = load_yolo_model()
        classes = load_class_names()
        print(f"Loaded {len(classes)} object classes")
    except Exception as e:
        print(f"Error loading YOLO model: {e}")
        sys.exit(1)
    
    # Initialize camera
    print("\nInitializing camera...")
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open camera")
        sys.exit(1)
    
    print("Camera initialized successfully!")
    print("\nPress 'q' to quit")
    print("=" * 50)
    
    frame_count = 0
    
    try:
        while True:
            # Capture frame
            ret, frame = cap.read()
            
            if not ret:
                print("Error: Could not read frame")
                break
            
            frame_count += 1
            
            # Perform detection every frame (can be optimized to skip frames)
            boxes, confidences, class_ids, indices = detect_objects(
                frame, net, output_layers, classes
            )
            
            # Draw detections
            frame = draw_detections(frame, boxes, confidences, class_ids, indices, classes)
            
            # Add FPS counter
            cv2.putText(frame, f"Frame: {frame_count}", (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            # Display frame
            cv2.imshow('YOLO Camera Detection', frame)
            
            # Check for quit key
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("\nQuitting...")
                break
    
    except KeyboardInterrupt:
        print("\nInterrupted by user")
    
    finally:
        # Release resources
        cap.release()
        cv2.destroyAllWindows()
        print("Resources released. Goodbye!")


if __name__ == "__main__":
    main()
