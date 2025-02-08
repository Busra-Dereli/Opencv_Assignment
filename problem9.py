# verilen resmi rotate yapmamız lazım.
import cv2

image = r"C:\Users\Busra\Desktop\busra\problems\images\bulmaca.jpg"
img = cv2.imread(image)

if img is None:
    print("resim yüklenemedi. Dosya yolunu kontrol edin: ", image)
else:
    print(img.shape)

res = cv2.resize(img, (300, 300))

(h, w) = res.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 90, 1.0)  # 90 derece döndürmek için
rotated = cv2.warpAffine(res, M, (w, h))

cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", res)
cv2.imshow("Rotated Image", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
