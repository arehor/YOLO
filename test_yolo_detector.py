#!/usr/bin/env python3
"""
Unit tests for YOLO Detector
"""

import unittest
from yolo_detector import YOLODetector


class TestYOLODetector(unittest.TestCase):
    """Test cases for YOLODetector class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.detector = YOLODetector(confidence_threshold=0.5)
    
    def test_initialization(self):
        """Test detector initialization"""
        self.assertEqual(self.detector.confidence_threshold, 0.5)
        self.assertIsNotNone(self.detector.classes)
        self.assertGreater(len(self.detector.classes), 0)
    
    def test_detect_returns_list(self):
        """Test that detect returns a list"""
        detections = self.detector.detect("test_image.jpg")
        self.assertIsInstance(detections, list)
    
    def test_confidence_threshold(self):
        """Test confidence threshold filtering"""
        detector_high_threshold = YOLODetector(confidence_threshold=0.9)
        detections = detector_high_threshold.detect("test_image.jpg")
        
        # All detections should meet the threshold
        for _, confidence, _ in detections:
            self.assertGreaterEqual(confidence, 0.9)
    
    def test_detection_format(self):
        """Test that detections have the correct format"""
        detections = self.detector.detect("test_image.jpg")
        
        for detection in detections:
            # Should be a tuple with 3 elements
            self.assertEqual(len(detection), 3)
            
            class_name, confidence, bbox = detection
            
            # Validate types
            self.assertIsInstance(class_name, str)
            self.assertIsInstance(confidence, float)
            self.assertIsInstance(bbox, tuple)
            
            # Validate bbox format (x1, y1, x2, y2)
            self.assertEqual(len(bbox), 4)
            for coord in bbox:
                self.assertIsInstance(coord, int)
    
    def test_print_detections(self):
        """Test that print_detections doesn't raise errors"""
        detections = self.detector.detect("test_image.jpg")
        try:
            self.detector.print_detections(detections)
        except Exception as e:
            self.fail(f"print_detections raised {type(e).__name__}: {e}")


if __name__ == "__main__":
    unittest.main()
