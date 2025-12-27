# YOLO Object Detection with Camera

A Python application that uses YOLOv8 (You Only Look Once) algorithm to recognize objects in real-time using your laptop's camera.

## Features

- Real-time object detection using YOLOv8
- Live camera feed with bounding boxes and labels
- Configurable model size and confidence threshold
- Support for 80+ object classes (COCO dataset)
- Easy-to-use command-line interface

## Installation

### Prerequisites

- Python 3.8 or higher
- Webcam/camera device
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/arehor/YOLO.git
cd YOLO
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

On first run, YOLOv8 will automatically download the pre-trained model weights.

## Usage

### Basic Usage

Run object detection with default settings (YOLOv8n model):
```bash
python yolo_camera.py
```

### Advanced Options

**Use a different model size:**
```bash
python yolo_camera.py --model yolov8s.pt  # Small model
python yolo_camera.py --model yolov8m.pt  # Medium model
python yolo_camera.py --model yolov8l.pt  # Large model
python yolo_camera.py --model yolov8x.pt  # Extra large model
```

**Adjust confidence threshold:**
```bash
python yolo_camera.py --conf 0.5  # Only show detections with 50%+ confidence
```

**Use a different camera:**
```bash
python yolo_camera.py --camera 1  # Use camera device 1 instead of 0
```

**Combine options:**
```bash
python yolo_camera.py --model yolov8m.pt --conf 0.4 --camera 0
```

### Controls

- Press `q` to quit the application

## Model Information

The application uses YOLOv8 models trained on the COCO dataset, which can detect 80 different object classes including:
- People
- Vehicles (car, bicycle, motorcycle, bus, truck, etc.)
- Animals (cat, dog, bird, horse, etc.)
- Common objects (chair, bottle, phone, laptop, etc.)
- And many more!

### Model Sizes

| Model | Size | Speed | Accuracy |
|-------|------|-------|----------|
| yolov8n.pt | Nano | Fastest | Good |
| yolov8s.pt | Small | Fast | Better |
| yolov8m.pt | Medium | Moderate | Very Good |
| yolov8l.pt | Large | Slower | Excellent |
| yolov8x.pt | Extra Large | Slowest | Best |

Choose a smaller model for faster performance or a larger model for better accuracy.

## Troubleshooting

### Camera not opening
- Make sure your camera is not being used by another application
- Try a different camera index with `--camera 1` or `--camera 2`
- Check camera permissions on your operating system

### Slow performance
- Use a smaller model (e.g., `yolov8n.pt`)
- Increase the confidence threshold to reduce false detections
- Close other resource-intensive applications

### Installation issues
If you encounter issues installing OpenCV or other dependencies:
```bash
pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
```

## Requirements

See `requirements.txt` for the complete list of Python dependencies.

## License

This project uses the Ultralytics YOLOv8 implementation, which is licensed under AGPL-3.0.

## Acknowledgments

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) - The YOLO implementation used in this project
- [OpenCV](https://opencv.org/) - Computer vision library for camera access and image processing