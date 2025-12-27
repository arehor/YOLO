#!/usr/bin/env python3
"""
Test script to verify the YOLO camera implementation structure.
This tests the imports and basic functionality without requiring a camera.
"""

import sys
import ast


def test_script_structure():
    """Test that the yolo_camera.py script has the correct structure."""
    print("Testing yolo_camera.py structure...")
    
    with open('yolo_camera.py', 'r') as f:
        content = f.read()
    
    # Parse the Python file
    try:
        tree = ast.parse(content)
        print("✓ Python syntax is valid")
    except SyntaxError as e:
        print(f"✗ Syntax error: {e}")
        return False
    
    # Check for required imports
    required_imports = ['cv2', 'argparse', 'YOLO']
    found_imports = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                found_imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                for alias in node.names:
                    found_imports.append(f"{node.module}.{alias.name}")
    
    for imp in required_imports:
        if any(imp in found for found in found_imports):
            print(f"✓ Found required import: {imp}")
        else:
            print(f"✗ Missing required import: {imp}")
            return False
    
    # Check for main function
    has_main = False
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == 'main':
            has_main = True
            print("✓ Found main() function")
            break
    
    if not has_main:
        print("✗ Missing main() function")
        return False
    
    # Check for argparse arguments
    if 'argparse' in content and '--model' in content and '--conf' in content and '--camera' in content:
        print("✓ Found expected command-line arguments (--model, --conf, --camera)")
    else:
        print("✗ Missing expected command-line arguments")
        return False
    
    # Check for camera capture
    if 'VideoCapture' in content:
        print("✓ Found camera capture code")
    else:
        print("✗ Missing camera capture code")
        return False
    
    # Check for YOLO inference
    if 'model(' in content or 'model.predict' in content:
        print("✓ Found YOLO inference code")
    else:
        print("✗ Missing YOLO inference code")
        return False
    
    print("\n✓ All structure tests passed!")
    return True


def test_requirements():
    """Test that requirements.txt exists and has necessary packages."""
    print("\nTesting requirements.txt...")
    
    try:
        with open('requirements.txt', 'r') as f:
            content = f.read()
        
        required_packages = ['ultralytics', 'opencv-python', 'numpy']
        for pkg in required_packages:
            if pkg in content:
                print(f"✓ Found required package: {pkg}")
            else:
                print(f"✗ Missing required package: {pkg}")
                return False
        
        print("✓ All required packages found in requirements.txt")
        return True
    except FileNotFoundError:
        print("✗ requirements.txt not found")
        return False


def test_readme():
    """Test that README.md exists and has basic content."""
    print("\nTesting README.md...")
    
    try:
        with open('README.md', 'r') as f:
            content = f.read()
        
        required_sections = ['Installation', 'Usage', 'YOLO']
        for section in required_sections:
            if section in content:
                print(f"✓ Found section: {section}")
            else:
                print(f"✗ Missing section: {section}")
                return False
        
        print("✓ README.md has required sections")
        return True
    except FileNotFoundError:
        print("✗ README.md not found")
        return False


if __name__ == '__main__':
    print("=" * 60)
    print("YOLO Camera Implementation Tests")
    print("=" * 60)
    
    results = []
    results.append(test_script_structure())
    results.append(test_requirements())
    results.append(test_readme())
    
    print("\n" + "=" * 60)
    if all(results):
        print("ALL TESTS PASSED ✓")
        print("=" * 60)
        sys.exit(0)
    else:
        print("SOME TESTS FAILED ✗")
        print("=" * 60)
        sys.exit(1)
