# Quick Start Guide

## Setup (First Time Only)

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Download YOLO model files:**
   ```bash
   python download_yolo_files.py
   ```
   This downloads ~240MB of files. Be patient!

## Running the Detection

```bash
python yolo_camera.py
```

**That's it!** The camera window will open and start detecting objects in real-time.

## Tips

- **Good Lighting**: Make sure you have good lighting for better detection
- **Distance**: Objects should be at a reasonable distance from the camera
- **Press 'q'**: To quit the application
- **Performance**: First run may be slow as models load. Subsequent frames will be faster.

## Common Issues

### "No module named 'cv2'"
Run: `pip install -r requirements.txt`

### "YOLO files not found"
Run: `python download_yolo_files.py`

### "Could not open camera"
- Check if another app is using the camera
- Try restarting your computer
- Check camera permissions

### Detection is slow
This is normal on CPU. The model processes each frame which takes time.

## What Objects Can Be Detected?

The model can detect 80 different types of objects including:
- **People**: person
- **Vehicles**: bicycle, car, motorcycle, airplane, bus, train, truck, boat
- **Animals**: bird, cat, dog, horse, sheep, cow, elephant, bear, zebra, giraffe
- **Common Items**: backpack, umbrella, handbag, suitcase, bottle, cup, fork, knife, spoon, bowl
- **Furniture**: chair, couch, bed, dining table, toilet
- **Electronics**: TV, laptop, mouse, remote, keyboard, cell phone
- And many more!

## Next Steps

Try these experiments:
1. Show different objects to the camera
2. Adjust `CONFIDENCE_THRESHOLD` in `yolo_camera.py` for more/fewer detections
3. Try detecting multiple objects at once
4. Test in different lighting conditions

Have fun with YOLO! 🎯
