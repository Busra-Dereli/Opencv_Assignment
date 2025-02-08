# webcam üzerinden alınan kaydı kaydedicez ve 
# kamera da bir pencereden trackbar olacak h1 h2 s1 s2  
# yani bir normal üstünde tracbar olan pencere bir de trackbarla oynadığımızda etki eden başka bir pencere daha olması gerekiyor

import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("frame")

cv2.createTrackbar("H1","frame",0,179,nothing)
cv2.createTrackbar("H2","frame",0,179,nothing)
cv2.createTrackbar("S1","frame",0,255,nothing)
cv2.createTrackbar("S2","frame",0,255,nothing)
cv2.createTrackbar("V1","frame",0,255,nothing)
cv2.createTrackbar("V2","frame",0,255,nothing)

camera = cv2.VideoCapture(0)


while camera.isOpened():
    _,frame = camera.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mirror_frame = cv2.flip(frame,1)

    
    H1 = cv2.getTrackbarPos("H1","frame")
    H2 = cv2.getTrackbarPos("H2","frame")
    S1 = cv2.getTrackbarPos("S1","frame")
    S2 = cv2.getTrackbarPos("S2","frame")
    V1 = cv2.getTrackbarPos("V1","frame")
    V2 = cv2.getTrackbarPos("V2","frame")
    
    lower = np.array([H1,S1,V1])
    upper = np.array([H2,S2,V2])

    mask = cv2.inRange(hsv,lower,upper)

    res = cv2.bitwise_and(mirror_frame, mirror_frame, mask=mask)
    
    contours = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (200,50,200),2)

    cv2.imshow("frame",mirror_frame)

    cv2.imshow("result",res)

    if cv2.waitKey(1) == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
