# line rectangle, circle çiz; text ekle, ipucu:np zero
import cv2
import numpy as np


img = np.zeros((600,600,3),np.uint8)


line = np.zeros((800,880,880),np.uint8)
cv2.line(img,(20,10),(100,50),color=(200,300,100),thickness=2)

cv2.rectangle(img,(150,70),(30,200),color=(100,100,200),thickness=4)

cv2.circle(img,(200,70),30,color=(210,150,300),thickness=3)

cv2.putText(img,"olsun artik!",(200,300),cv2.FONT_HERSHEY_PLAIN,3,color=(10,200,210),thickness=2)

cv2.imshow("resim", img)
cv2.waitKey(0)
cv2.destroyAllWindows()