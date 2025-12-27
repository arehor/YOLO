#!/usr/bin/env python3
"""
YOLO Object Detection with Camera
This script uses YOLOv8 to detect objects in real-time using the laptop's camera.
"""

import cv2
import argparse
from ultralytics import YOLO


def main():
    """Main function to run YOLO object detection with camera."""
    parser = argparse.ArgumentParser(description='YOLO Object Detection with Camera')
    parser.add_argument('--model', type=str, default='yolov8n.pt',
                        help='YOLO model to use (yolov8n.pt, yolov8s.pt, yolov8m.pt, yolov8l.pt, yolov8x.pt)')
    parser.add_argument('--conf', type=float, default=0.25,
                        help='Confidence threshold for detections')
    parser.add_argument('--camera', type=int, default=0,
                        help='Camera device index (default: 0)')
    args = parser.parse_args()

    print(f"Loading YOLO model: {args.model}")
    print("This may take a moment on first run as the model is downloaded...")
    
    # Load the YOLO model
    model = YOLO(args.model)
    
    print(f"Opening camera device {args.camera}...")
    # Open the camera
    cap = cv2.VideoCapture(args.camera)
    
    if not cap.isOpened():
        print(f"Error: Could not open camera device {args.camera}")
        return
    
    print("Camera opened successfully!")
    print("Press 'q' to quit")
    
    # Process video frames
    while True:
        # Read frame from camera
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Could not read frame from camera")
            break
        
        # Run YOLO inference on the frame
        results = model(frame, conf=args.conf, verbose=False)
        
        # Visualize the results on the frame
        annotated_frame = results[0].plot()
        
        # Display the annotated frame
        cv2.imshow('YOLO Object Detection', annotated_frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release resources
    cap.release()
    cv2.destroyAllWindows()
    print("Detection stopped. Camera released.")


if __name__ == '__main__':
    main()

