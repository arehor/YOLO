#!/usr/bin/env python3
"""
YOLO Object Detection with Camera
This script uses YOLOv8 to detect objects in real-time using the laptop's camera.
"""

import sys
import cv2
import argparse
from ultralytics import YOLO


def main():
    """Main function to run YOLO object detection with camera."""
    parser = argparse.ArgumentParser(description='YOLO Object Detection with Camera')
    parser.add_argument('--model', type=str, default='yolov8n.pt',
                        help='YOLO model to use (yolov8n.pt, yolov8s.pt, yolov8m.pt, yolov8l.pt, yolov8x.pt)')
    parser.add_argument('--conf', type=float, default=0.25,
                        help='Confidence threshold for detections (0.0 to 1.0)')
    parser.add_argument('--camera', type=int, default=0,
                        help='Camera device index (default: 0)')
    args = parser.parse_args()

    # Validate confidence threshold
    if not 0.0 <= args.conf <= 1.0:
        print(f"Error: Confidence threshold must be between 0.0 and 1.0, got {args.conf}")
        sys.exit(1)

    print(f"Loading YOLO model: {args.model}")
    print("This may take a moment on first run as the model is downloaded...")
    
    # Load the YOLO model with error handling
    try:
        model = YOLO(args.model)
    except Exception as e:
        print(f"Error loading YOLO model '{args.model}': {e}")
        print("Please ensure you have a valid model name or file path.")
        sys.exit(1)
    
    print(f"Opening camera device {args.camera}...")
    # Open the camera
    cap = cv2.VideoCapture(args.camera)
    
    if not cap.isOpened():
        print(f"Error: Could not open camera device {args.camera}")
        print("Please check that your camera is connected and not in use by another application.")
        sys.exit(1)
    
    print("Camera opened successfully!")
    print("Press 'q' to quit")
    
    # Process video frames
    try:
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
    except KeyboardInterrupt:
        print("\nInterrupted by user")
    except Exception as e:
        print(f"\nError during detection: {e}")
    finally:
        # Release resources
        cap.release()
        cv2.destroyAllWindows()
        print("Detection stopped. Camera released.")


if __name__ == '__main__':
    main()
