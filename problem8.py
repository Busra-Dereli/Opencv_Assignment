#videolu grafik çizimi
import cv2

cam = cv2.VideoCapture(0)
#cam = np.zeros((600,600,3),np.uint8)

while True:

    ret, frame = cam.read()
    if not ret:
        print("kameradan görüntü okunamıyor")
        break

    cv2.line(frame,(230,0),(100,30),(200,100,50),3)
    cv2.rectangle(frame,(100,200),(20,100),(100,200,100),4)
    cv2.circle(frame,(250,300),120,(0,0,255),2)
    cv2.imshow("window",frame)
    if cv2.waitKey(1) == ord("q"):
        print("görüntü sonlandırıldı.")
        break
    
cam.release()
cv2.destroyAllWindows()
