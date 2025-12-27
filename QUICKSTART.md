# Quick Start Guide

## Installation

```bash
pip install -r requirements.txt
```

## Basic Usage

```bash
# Run with default settings (YOLOv8n model, 0.25 confidence threshold, camera 0)
python yolo_camera.py
```

## Advanced Usage

```bash
# Use a larger model for better accuracy
python yolo_camera.py --model yolov8m.pt

# Increase confidence threshold to reduce false detections
python yolo_camera.py --conf 0.5

# Use a different camera
python yolo_camera.py --camera 1

# Combine options
python yolo_camera.py --model yolov8s.pt --conf 0.4 --camera 0
```

## Available Models

- `yolov8n.pt` - Nano (fastest, good accuracy)
- `yolov8s.pt` - Small (fast, better accuracy)
- `yolov8m.pt` - Medium (balanced speed and accuracy)
- `yolov8l.pt` - Large (slower, excellent accuracy)
- `yolov8x.pt` - Extra Large (slowest, best accuracy)

## Controls

- Press `q` to quit the application

## Troubleshooting

**Camera not working?**
- Make sure no other application is using the camera
- Try different camera indices: `--camera 1` or `--camera 2`
- Check camera permissions in your OS settings

**Slow performance?**
- Use a smaller model: `--model yolov8n.pt`
- Increase confidence threshold: `--conf 0.5`

**Installation issues?**
```bash
pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
```
