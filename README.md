# YOLO

An experimental YOLO (You Only Look Once) object detection project.

## About

This repository contains experimental code for demonstrating YOLO object detection concepts. YOLO is a state-of-the-art, real-time object detection system.

## Features

- Simple YOLO detector class structure
- Configurable confidence threshold
- Easy-to-understand demonstration code

## Usage

Run the YOLO detector:

```bash
python3 yolo_detector.py [image_path]
```

Example:
```bash
python3 yolo_detector.py sample_image.jpg
```

## Requirements

- Python 3.7 or higher
- See `requirements.txt` for dependencies

## Installation

```bash
pip install -r requirements.txt
```

## Project Structure

- `yolo_detector.py` - Main YOLO detector implementation
- `test_yolo_detector.py` - Unit tests for the detector
- `requirements.txt` - Project dependencies
- `README.md` - Project documentation

## Note

This is an experimental implementation for learning and demonstration purposes. For production YOLO implementations, consider using:
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [YOLOv5](https://github.com/ultralytics/yolov5)
- [Darknet YOLO](https://github.com/AlexeyAB/darknet)

## License

MIT