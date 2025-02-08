# videodan aldığın görüntüyü mirrorlayalım  ipucu: cv2.flip
import cv2
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   
    mirror_frame = cv2.flip(frame,1)
    print("görüntü alındı.")

    if not ret:
        print("kameradan görüntü okunamıyor")
        break
    cv2.imshow("frame",mirror_frame)
    cv2.imshow("gray frame",gray_frame)

    if cv2.waitKey(1) == ord("q"):
        print("görüntü sonlandırıldı")
        break

cam.release()
cv2.destroyAllWindows()