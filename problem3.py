# q renkli img çık
# w gri kapat
# s ile kaydet


import cv2

image = r"C:\Users\Busra\Desktop\busra\problems\images\image.png"

img = cv2.imread(image)
img_gray = cv2.imread(image,0)


cv2.imshow("gray",img_gray)
cv2.imshow("window",img)

a = cv2.waitKey(0)

if a == ord("s"):
    cv2.imwrite("gray",img_gray)
    cv2.imwrite("color",img)

elif a == ord("w"):
    cv2.destroyWindow("gray")

elif a == ord("q"):
    cv2.destroyWindow("window")

cv2.waitKey(0)
cv2.destroyAllWindows()


# ilk önce w ile çıkıldığında pencereleri tek tek kapatabilmekte iken q ile çıkmaya çalıştığımda ikisi de kapanmaktadır.Bunu düzeltemedim.