# video normal görüntü, gri görüntü ve tuşla kapatma

import cv2
#import numpy as np
cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("kamera acilmadi")
    exit()
    
while True:

    ret, frame = cam.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    print("görüntü alındı.")
    if not ret:
        print("kameradan görüntü okunamıyor")
        break

    cv2.imshow("frame",frame)
    cv2.imshow("gray frame",gray_frame)

    if cv2.waitKey(1) == ord("q"):
        print("görüntü sonlandırıldı.")
        break

cam.release()
cv2.destroyAllWindows()