import cv2

aruco_dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_7X7_250)
parameters = cv2.aruco.DetectorParameters_create()
capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    corners, ids, rejected_corners = cv2.aruco.detectMarkers(gray_frame, aruco_dictionary, parameters=parameters)
    frame = cv2.aruco.drawDetectedMarkers(image=frame, corners=corners, ids=ids, borderColor=(255, 0, 0))
    frame = cv2.aruco.drawDetectedMarkers(image=frame, corners=rejected_corners, borderColor=(0, 255, 255))
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == 0x1B:
        break

cv2.destroyAllWindows()