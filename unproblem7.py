#Opencv ile trackbar üzerinden ayarlanan hsv değerlerine göre ayarlanan rengi algılayıp dikdörtgen içine alan proje yapılacak(Yapanlar da yaptıkları şekilde rapora ekleyebilir)

import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("Trackbars")

cv2.createTrackbar("H1", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("H2", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("S1", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("S2", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("V1", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("V2", "Trackbars", 0, 255, nothing)

image = r"C:\Users\Busra\Desktop\busra\problems\images\renklibalon.jpg" 
img = cv2.imread(image)

if img is None:
    print("Resim yüklenemedi, dosya yolunu kontrol edin")
    exit()

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mirror_image = cv2.flip(img, 1)

while True:
    H1 = cv2.getTrackbarPos("H1", "Trackbars")
    H2 = cv2.getTrackbarPos("H2", "Trackbars")
    S1 = cv2.getTrackbarPos("S1", "Trackbars")
    S2 = cv2.getTrackbarPos("S2", "Trackbars")
    V1 = cv2.getTrackbarPos("V1", "Trackbars")
    V2 = cv2.getTrackbarPos("V2", "Trackbars")

    lower = np.array([H1, S1, V1])
    upper = np.array([H2, S2, V2])

    mask = cv2.inRange(hsv, lower, upper)
    sonuc = cv2.bitwise_and(mirror_image, mirror_image, mask=mask)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        cv2.rectangle(mirror_image, (x, y), (x + w, y + h), (200, 50, 200), 2)

    cv2.imshow("Original", img)
    cv2.imshow("Trackbars", mirror_image)
    cv2.imshow("Result", sonuc)

    if cv2.waitKey(0) == ord("q"):
        break

cv2.destroyAllWindows()
