OpenCV 4.11 Experimentation for Autonomous Navigation
This repository contains a collection of Python scripts for experimenting with computer vision using OpenCV version 4.11. The project was initially started to support autonomous navigation research for the University Rover Challenge (URC).

🚩 About The Project
The primary goal of this repository is to serve as a development and testing ground for various computer vision techniques. These experiments are foundational steps towards building a robust autonomous navigation system for a rover, as required by challenges like the URC.

Our focus includes:

Marker Detection: Identifying and tracking AR markers for precise localization.

Object Detection: Simple detection of everyday objects.

Camera Calibration: Ensuring accurate measurements and perspective correction.

Pose Estimation: Determining the position and orientation of objects in 3D space.

🚀 Getting Started
To get a local copy up and running, follow these simple steps.

Prerequisites
Make sure you have Python and OpenCV installed on your system.

Python 3.x

OpenCV 4.11

pip install opencv-python==4.11.*

NumPy

pip install numpy

Installation
Clone the repo:

git clone [https://github.com/bemndy/openCV-experimentation4.11.git](https://github.com/bemndy/openCV-experimentation4.11.git)

Navigate to the project directory:

cd openCV-experimentation4.11

💻 Usage
Each Python script is designed to run independently and test a specific feature of OpenCV.

Generate AR Markers:

python generateMarkers.py

Detect AR Markers from a camera feed:

python detectMarkers.py

Calibrate your camera:

python cameraCalibration.py

Note: You may need a checkerboard pattern for this.

📂 File Descriptions
Here's a brief overview of the key files in this repository:

File Name

Description

generateMarkers.py

Generates ArUco markers that can be printed and used for detection.

detectMarkers.py

Detects ArUco markers using a webcam or video feed.

cameraCalibration.py

A script to calibrate the camera and save the calibration matrix.

poseEstimation.py

Estimates the 3D pose of a detected ArUco marker relative to the camera.

beginnerDetection.py

A simple example script for basic object detection (e.g., color-based).

detectAirpods.py

An experimental script to detect specific objects like AirPods.

🎯 Future Goals
The long-term vision for this work is to integrate these computer vision modules into a cohesive autonomous navigation stack for the URC rover. This includes:

[ ] Real-time GPS-denied navigation using visual markers.

[ ] Obstacle detection and avoidance.

[ ] Integration with ROS (Robot Operating System).

🙏 Acknowledgments
OpenCV Documentation

University Rover Challenge (URC)
