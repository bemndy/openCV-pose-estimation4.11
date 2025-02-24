import numpy as np
import cv2 

# version check
print(cv2.__version__)

# dictionary of ArUCo tags
ARUCO_DICT = {
	"DICT_4X4_50": cv2.aruco.DICT_4X4_50,
	"DICT_4X4_100": cv2.aruco.DICT_4X4_100,
	"DICT_4X4_250": cv2.aruco.DICT_4X4_250,
	"DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
	"DICT_5X5_50": cv2.aruco.DICT_5X5_50,
	"DICT_5X5_100": cv2.aruco.DICT_5X5_100,
	"DICT_5X5_250": cv2.aruco.DICT_5X5_250,
	"DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
	"DICT_6X6_50": cv2.aruco.DICT_6X6_50,
	"DICT_6X6_100": cv2.aruco.DICT_6X6_100,
	"DICT_6X6_250": cv2.aruco.DICT_6X6_250,
	"DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
	"DICT_7X7_50": cv2.aruco.DICT_7X7_50,
	"DICT_7X7_100": cv2.aruco.DICT_7X7_100,
	"DICT_7X7_250": cv2.aruco.DICT_7X7_250,
	"DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
	"DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
	"DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
	"DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
	"DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
	"DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11
}

def pose_estimation(frame, aruco_selection_type, matrix_coefficients, distortion_coefficients):

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = cv2.aruco.getPredefinedDictionary(aruco_selection_type)
    parameters = cv2.aruco.DetectorParameters()
    aruco_detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)
    
    corners, ids, _ = aruco_detector.detectMarkers(gray)
    distance = None

    if ids is not None and len(corners) > 0: 
        for i in range(0, len(ids)):
            
			#length in meters
            marker_length = 7.62
            marker_points = np.array([
                [-marker_length / 2, marker_length / 2, 0],
                [marker_length / 2, marker_length / 2, 0],
                [marker_length / 2, -marker_length / 2, 0],
                [-marker_length / 2, -marker_length / 2, 0]
            ], dtype=np.float32)
            
            success, r_vec, t_vec = cv2.solvePnP(marker_points, corners[i].reshape(4,1,2), matrix_coefficients, distortion_coefficients)
  
            if success: 
                print("[POSE] ArUCo marker generation:")
                frame = cv2.aruco.drawDetectedMarkers(frame, corners, ids)
                frame = cv2.drawFrameAxes(frame, matrix_coefficients, distortion_coefficients, r_vec, t_vec, 0.01)
                distance = np.linalg.norm(t_vec[0][0])
            else: 
                print("[POSE] ArUCo marker generation failed")
                distance = 0

    return frame, distance

 # def get_distance_to_camera(self): 
    #if len(corners) > 0: 
		# ArUCo marker is 5 cm
		#marker_length = 5

		# compute and return the distance from the maker to the camera
		#return (marker_length * self.focal_length) / marker_length[0][0]
    
	#return None

#select the ArUCo tag type and ID
aruco_selection = "DICT_4X4_50"
arucoDict = cv2.aruco.getPredefinedDictionary(ARUCO_DICT[aruco_selection])
arucoParams = cv2.aruco.DetectorParameters()

#needs to actually be calibrated based on camera details. (with checkerboard)
intrinsic_camera = np.array(((1.0, 0, 0), (0, 1.0, 0), (0, 0, 1.0)))
distortion = np.array(((0, 0, 0, 0)))

# start the video stream
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) #faster with 840? 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

#opencv to draw lines on (loops?)
while cap.isOpened(): 
    ret, img = cap.read()

    if not ret: 
        break

    output, distance = pose_estimation(img, ARUCO_DICT[aruco_selection], intrinsic_camera, distortion)

    
    cv2.imshow("Estimated Pose", output)
    cv2.putText(
        output,
        f"Dist: {(distance)}",
        (10, 30),
        cv2.FONT_HERSHEY_PLAIN,
        1.3,
        (0, 0, 255),
        2,
        cv2.LINE_AA,
 )

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()