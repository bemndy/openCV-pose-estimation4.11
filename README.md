# OpenCV 4.11 Experimentation for Autonomous Navigation

This repository contains a collection of Python scripts for experimenting with computer vision using OpenCV version 4.11+ (api overhaul).  
The project was initially started to support autonomous navigation research for the University Rover Challenge (URC). But now I will literally use this for whatever weird projects come to fruition. 

---

## About The Project

The primary goal of this repository is to serve as a development and testing ground for various computer vision techniques. These experiments are foundational steps towards building a robust autonomous navigation stack.

**Our focus includes:**
- **Marker Detection:** Identifying and tracking AR markers for precise localization.
- **Object Detection:** Simple detection of everyday objects.
- **Camera Calibration:** Ensuring accurate measurements and perspective correction.
- **Pose Estimation:** Determining the position and orientation of objects in 3D space.

---

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Make sure you have **Python** and **OpenCV** installed on your system:

```bash
# Python 3.x
# OpenCV 4.11+
pip install opencv-python==4.11+

# NumPy
pip install numpy
```

### Installation

Clone the repo:

```bash
git clone https://github.com/bemndy/openCV-experimentation4.11.git
```

Navigate to the project directory:

```bash
cd openCV-experimentation4.11
```

---

## 💻 Usage

Each Python script is designed to run independently and test a specific feature of OpenCV.

**Generate AR Markers:**
```bash
python generateMarkers.py
```

**Detect AR Markers from a camera feed:**
```bash
python detectMarkers.py
```

**Calibrate your camera:**
```bash
python cameraCalibration.py
# Note: You need checkerboard pattern for this (pose estimation doesn't work well without it).
```

---

## Future Goals

The long-term vision for this work is to integrate these computer vision modules into small weird OpenCV projects. The motivation is that OpenCV is heavily used in my clubs, so anything I find interesting I will place in here!

---
