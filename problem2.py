#görüntü griye çevir

import cv2
import matplotlib as plt


image = r"C:\Users\Busra\Desktop\busra\problems\images\image.png"

img = cv2.imread(image)
img_gray = cv2.imread(image,0)

cv2.imshow("window",img)
cv2.imshow("gray",img_gray)
cv2.waitKey(0) == ord("q")
cv2.destroyAllWindows()
