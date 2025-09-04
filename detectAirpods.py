import cv2
import numpy as np

# --- 1. Initialize video capture ---
cap = cv2.VideoCapture(1)

# Check if the webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

# --- 2. Main loop to process video frames ---
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # --- 3. Image Preparation (Preprocessing) ---
    # Convert the frame to grayscale for shape analysis
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply a Gaussian blur to reduce noise and improve edge detection
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)

    # Use Canny edge detection to find the outlines of objects
    edges = cv2.Canny(blurred, 50, 150)

    # --- 4. Finding Outlines (Contours) ---
    # Find all contours in the edge-detected image
    # cv2.RETR_EXTERNAL means we only get the outermost contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # --- 5. Filtering and Analyzing Shapes ---
    for contour in contours:
        # Filter out small contours that are likely noise
        if cv2.contourArea(contour) < 1000:
            continue

        # Approximate the contour to a simpler polygon
        # The 0.02 is a sensitivity parameter; smaller values mean more sensitivity
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

        # Check if the approximated shape has 4 vertices (is a quadrilateral)
        if len(approx) == 4:
            # Get the bounding box to calculate the aspect ratio
            x, y, w, h = cv2.boundingRect(approx)
            
            # Calculate aspect ratio (width / height)
            aspect_ratio = float(w) / h

            # Check if the aspect ratio is close to 1 (a square)
            # We allow a 20% tolerance (0.8 to 1.2)
            if 0.8 <= aspect_ratio <= 1.2:
                # If it passes all tests, we'll draw it on the frame
                cv2.drawContours(frame, [approx], -1, (0, 255, 0), 3)
                
                # Add a label
                cv2.putText(frame, 'Squareish Object', (x, y - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)


    # --- 6. Display the results ---
    cv2.imshow('Square Detection', frame)
    # Optional: show the edge detection result in another window for debugging
    # cv2.imshow('Canny Edges', edges)

    # --- 7. Exit condition ---
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# --- 8. Clean up ---
cap.release()
cv2.destroyAllWindows()