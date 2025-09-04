import cv2
import numpy as np

# --- 1. Define the range for dark green color in HSV ---
# Hue for green is typically around 60 (out of 180).
# For 'dark' green, we'll want higher saturation and lower value.
lower_green = np.array([40, 50, 20])   # Adjust these values as needed
upper_green = np.array([80, 255, 150]) # Adjust these values as needed

# --- 2. Initialize video capture ---
cap = cv2.VideoCapture(1)

# Check if the webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

# --- 3. Main loop to process video frames ---
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # --- 4. Color Detection Steps ---
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask to isolate pixels within the dark green color range
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # --- 5. Draw bounding boxes around detected objects ---
    for contour in contours:
        # Filter out small contours (noise)
        if cv2.contourArea(contour) > 500: # Minimum area threshold
            x, y, w, h = cv2.boundingRect(contour)

            # Draw the green rectangle on the original frame
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # Add text label
            cv2.putText(frame, 'Dark Green Object', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # --- 6. Display the results ---
    cv2.imshow('Dark Green Object Detection', frame)
    cv2.imshow('Dark Green Mask', mask)

    # --- 7. Exit condition ---
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# --- 8. Clean up ---
cap.release()
cv2.destroyAllWindows()