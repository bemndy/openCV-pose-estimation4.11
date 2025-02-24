import cv2 
import numpy as np
import time
import glob
import os


# version check
print(cv2.__version__)

cap = cv2.VideoCapture(1)
previous_time = time.time()
frame_count = 0 

## printing images out for each frame needed to callibrate 
while True: 

    _, frame = cap.read()
    current_time = time.time()
    cv2.imshow("Frame", frame)

    if (current_time - previous_time) >= 1: 
        image_path = r'/Users/brandowitabanjo/Documents/DomerRover/Measure/calibration_image{}.png'.format(frame_count)
        #cv2.imwrite("calibration_image{}".format(frame_count), frame)
        cv2.imwrite(image_path, frame)
        frame_count += 1
        previous_time = current_time

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()

chessboardSize = (9, 6)
frameSize = (1280, 720)
#termination criteria 
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

#prepare object points, like (0, 0, 0), (1, 0, 0), (2, 0, 0) ...., (6, 5, 0)
obj_points = np.zeros((9*6, 3), np.float32)
obj_points[:, :2] = np.mgrid[0:9, 0:6].T.reshape(-1, 2)

obj_array = []
img_array = []

images = glob.glob('*.png')

for fname in images: 
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray, (9,6), None)
 
    # If found, add object points, image points (after refining them)
    if ret == True:
        obj_array.append(obj_points)
        corners2 = cv2.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        img_array.append(corners2)
 
        # Draw and display the corners
        cv2.drawChessboardCorners(img, (9,6), corners2, ret)
        cv2.imshow('img', img)
        cv2.waitKey(500)
 
cv2.destroyAllWindows()



