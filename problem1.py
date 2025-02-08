#bir görüntü(resim) al ekrana yansıt ve q ile kapat

import cv2

image = r"C:\Users\Busra\Desktop\busra\problems\images\image.png"
img = cv2.imread(image)


cv2.imshow("window",img)
cv2.waitKey(0) == ord("q")
cv2.destroyAllWindows()

