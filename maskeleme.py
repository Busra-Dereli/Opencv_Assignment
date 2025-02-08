import cv2
import numpy as np
from problem11 import get_limits

blue = [255,0,0] #blue in BGR colorspace
kamera = cv2.VideoCapture(0)

while True:
    ret,frame = kamera.read()

    hsvImage = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=blue)
    
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    cv2.imshow('mask', mask)
    cv2.imshow("goruntu",frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break


kamera.release()
cv2.destroyAllWindows()


#cv2.rectangle(goruntu,(x,y))