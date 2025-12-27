#!/usr/bin/env python3
"""
Download YOLO model files
This script downloads YOLOv3 weights, config, and class names files
"""

import os
import urllib.request
import sys

YOLO_DIR = "yolo_files"
FILES = {
    "yolov3.weights": "https://pjreddie.com/media/files/yolov3.weights",
    "yolov3.cfg": "https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg",
    "coco.names": "https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names"
}


def download_file(url, filepath):
    """
    Download a file from URL with progress indicator
    """
    print(f"Downloading {os.path.basename(filepath)}...")
    
    def report_progress(block_num, block_size, total_size):
        downloaded = block_num * block_size
        percent = min(downloaded * 100 / total_size, 100)
        sys.stdout.write(f"\rProgress: {percent:.1f}%")
        sys.stdout.flush()
    
    try:
        urllib.request.urlretrieve(url, filepath, reporthook=report_progress)
        print(f"\n{os.path.basename(filepath)} downloaded successfully!")
        return True
    except Exception as e:
        print(f"\nError downloading {os.path.basename(filepath)}: {e}")
        return False


def main():
    """
    Main function to download all YOLO files
    """
    print("=" * 50)
    print("YOLO Files Downloader")
    print("=" * 50)
    
    # Create directory if it doesn't exist
    if not os.path.exists(YOLO_DIR):
        os.makedirs(YOLO_DIR)
        print(f"Created directory: {YOLO_DIR}")
    
    # Download each file
    success_count = 0
    for filename, url in FILES.items():
        filepath = os.path.join(YOLO_DIR, filename)
        
        # Skip if file already exists
        if os.path.exists(filepath):
            print(f"\n{filename} already exists, skipping...")
            success_count += 1
            continue
        
        print(f"\nDownloading {filename}...")
        if download_file(url, filepath):
            success_count += 1
    
    print("\n" + "=" * 50)
    print(f"Download complete: {success_count}/{len(FILES)} files")
    
    if success_count == len(FILES):
        print("All files downloaded successfully!")
        print("You can now run: python yolo_camera.py")
    else:
        print("Some files failed to download. Please try again.")
    
    print("=" * 50)


if __name__ == "__main__":
    main()
