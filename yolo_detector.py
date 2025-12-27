#!/usr/bin/env python3
"""
Simple YOLO Object Detection Script
This is an experimental implementation for demonstrating YOLO concepts.
"""

import sys
from typing import List, Tuple


class YOLODetector:
    """
    A simplified YOLO detector class for experimentation.
    This demonstrates the basic structure of YOLO object detection.
    """
    
    def __init__(self, confidence_threshold: float = 0.5):
        """
        Initialize the YOLO detector.
        
        Args:
            confidence_threshold: Minimum confidence score for detections
        """
        self.confidence_threshold = confidence_threshold
        self.classes = [
            'person', 'bicycle', 'car', 'motorcycle', 'airplane',
            'bus', 'train', 'truck', 'boat', 'traffic light'
        ]
        print(f"YOLO Detector initialized with confidence threshold: {confidence_threshold}")
    
    def detect(self, image_path: str) -> List[Tuple[str, float, Tuple[int, int, int, int]]]:
        """
        Perform object detection on an image.
        
        Args:
            image_path: Path to the image file
            
        Returns:
            List of detections as (class_name, confidence, bbox) tuples
        """
        print(f"Processing image: {image_path}")
        
        # This is a placeholder for actual YOLO detection
        # In a real implementation, this would use a trained model
        detections = [
            ('person', 0.95, (100, 100, 200, 300)),
            ('car', 0.87, (300, 200, 500, 400)),
        ]
        
        # Filter by confidence threshold
        filtered_detections = [
            d for d in detections if d[1] >= self.confidence_threshold
        ]
        
        return filtered_detections
    
    def print_detections(self, detections: List[Tuple[str, float, Tuple[int, int, int, int]]]):
        """
        Print detection results in a formatted way.
        
        Args:
            detections: List of detections to print
        """
        print(f"\nFound {len(detections)} objects:")
        for idx, (class_name, confidence, bbox) in enumerate(detections, 1):
            x1, y1, x2, y2 = bbox
            print(f"  {idx}. {class_name}: {confidence:.2%} confidence at [{x1}, {y1}, {x2}, {y2}]")


def main():
    """Main function to run YOLO detection."""
    print("=" * 60)
    print("YOLO Object Detection - Experimental Implementation")
    print("=" * 60)
    
    # Create detector instance
    detector = YOLODetector(confidence_threshold=0.5)
    
    # Example usage
    image_path = "sample_image.jpg"
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
    
    # Perform detection
    detections = detector.detect(image_path)
    
    # Display results
    detector.print_detections(detections)
    
    print("\n" + "=" * 60)
    print("Detection completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
