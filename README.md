# YOLO Camera Object Detection

A real-time object detection system using YOLOv3 (You Only Look Once) algorithm with your laptop's camera.

## Features

- Real-time object detection using YOLOv3
- Detects 80 different object classes from COCO dataset
- Uses OpenCV's DNN module for inference
- Simple and easy-to-use interface
- Displays bounding boxes and confidence scores

## Requirements

- Python 3.6+
- Webcam/Camera
- Internet connection (for downloading YOLO model files)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/arehor/YOLO.git
cd YOLO
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download YOLO model files (weights, config, and class names):
```bash
python download_yolo_files.py
```

This will download:
- `yolov3.weights` (237 MB) - Pre-trained model weights
- `yolov3.cfg` - YOLOv3 configuration file
- `coco.names` - List of 80 object classes

## Usage

Run the camera detection script:
```bash
python yolo_camera.py
```

### Controls

- **q**: Quit the application
- The detection window will show:
  - Bounding boxes around detected objects
  - Object labels with confidence scores
  - Frame counter

## How it Works

1. **Camera Initialization**: Opens the default camera (usually the laptop's built-in webcam)
2. **Frame Capture**: Continuously captures frames from the camera
3. **Object Detection**: Each frame is processed by the YOLO model to detect objects
4. **Display Results**: Detected objects are highlighted with bounding boxes and labels
5. **Real-time Processing**: Runs continuously until you press 'q' to quit

## Configuration

You can adjust detection parameters in `yolo_camera.py`:

- `CONFIDENCE_THRESHOLD` (default: 0.5): Minimum confidence score for detections
- `NMS_THRESHOLD` (default: 0.4): Non-Maximum Suppression threshold
- `INPUT_WIDTH` and `INPUT_HEIGHT` (default: 416x416): Input size for YOLO model

## Detected Object Classes

The model can detect 80 different classes including:
- People, vehicles (car, truck, bus, bike)
- Animals (dog, cat, bird, horse, etc.)
- Common objects (bottle, cup, chair, laptop, etc.)
- And many more!

## Troubleshooting

### Camera not opening
- Make sure no other application is using the camera
- Check camera permissions on your system
- Try changing camera index in `cv2.VideoCapture(0)` to 1 or 2

### Model files not found
- Run `python download_yolo_files.py` first
- Ensure you have internet connection
- Files should be in `yolo_files/` directory

### Slow performance
- YOLO runs on CPU by default, which may be slow
- Consider reducing input size (INPUT_WIDTH/INPUT_HEIGHT)
- Skip frames by processing every Nth frame

## License

This project uses the YOLOv3 model from [YOLO: Real-Time Object Detection](https://pjreddie.com/darknet/yolo/)

## References

- [YOLO Paper](https://arxiv.org/abs/1506.02640)
- [YOLOv3 Paper](https://arxiv.org/abs/1804.02767)
- [Darknet Framework](https://github.com/pjreddie/darknet)
- [OpenCV DNN Module](https://docs.opencv.org/master/d2/d58/tutorial_table_of_content_dnn.html)