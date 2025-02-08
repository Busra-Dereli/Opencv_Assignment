import cv2

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("kamera tanınmadı")
    exit()

while True:
    ret, frame = cam.read()
    if not ret:
        print("kameradan görüntü okunamıyor")
        break
        exit()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mirror_frame = cv2.flip(frame, 1)

    cv2.imshow("frame", mirror_frame)
    cv2.imshow("gray frame", gray_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("görüntü sonlandırıldı")
        break

cam.release()
cv2.destroyAllWindows()
