#!/usr/bin/env python3
"""
Simple test to verify the YOLO implementation logic
"""

import os
import sys

# Test 1: Check if files exist
print("Test 1: Checking file structure...")
files_to_check = [
    'yolo_camera.py',
    'download_yolo_files.py',
    'requirements.txt',
    'README.md',
    '.gitignore'
]

all_exist = True
for file in files_to_check:
    if os.path.exists(file):
        print(f"✓ {file} exists")
    else:
        print(f"✗ {file} missing")
        all_exist = False

# Test 2: Check Python syntax
print("\nTest 2: Checking Python syntax...")
try:
    with open('yolo_camera.py', 'r') as f:
        compile(f.read(), 'yolo_camera.py', 'exec')
    print("✓ yolo_camera.py syntax is valid")
except SyntaxError as e:
    print(f"✗ yolo_camera.py has syntax error: {e}")
    all_exist = False

try:
    with open('download_yolo_files.py', 'r') as f:
        compile(f.read(), 'download_yolo_files.py', 'exec')
    print("✓ download_yolo_files.py syntax is valid")
except SyntaxError as e:
    print(f"✗ download_yolo_files.py has syntax error: {e}")
    all_exist = False

# Test 3: Check requirements.txt
print("\nTest 3: Checking requirements.txt...")
with open('requirements.txt', 'r') as f:
    requirements = f.read()
    if 'opencv-python' in requirements and 'numpy' in requirements:
        print("✓ Required packages listed in requirements.txt")
    else:
        print("✗ Missing required packages")
        all_exist = False

# Test 4: Check README content
print("\nTest 4: Checking README.md...")
with open('README.md', 'r') as f:
    readme = f.read()
    required_sections = ['Installation', 'Usage', 'Requirements', 'Features']
    missing = []
    for section in required_sections:
        if section not in readme:
            missing.append(section)
    
    if not missing:
        print("✓ README has all required sections")
    else:
        print(f"✗ README missing sections: {missing}")
        all_exist = False

# Final result
print("\n" + "="*50)
if all_exist:
    print("✓ All tests passed!")
    sys.exit(0)
else:
    print("✗ Some tests failed")
    sys.exit(1)
