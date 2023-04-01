import numpy as np
import cv2

ff = np.fromfile(r'/Users/chung_sungwoong/Desktop/Practice/Practice_Python/Project24_Travel_Pic.jpg',np.uint8)
img = cv2.imdecode(ff,cv2.IMREAD_UNCHANGED)
img = cv2.resize(img,dsize=(0,0),fx=1.0,fy=1.0,interpolation=cv2.INTER_LINEAR)

def onChange(pos):
    pass

cv2.nameWindow("Trackbar Windows")
cv2.createTrackbar('sigma_s', "Trackbar Windows", 0, 200, onChange)
cv2.createTrackbar('sigma_r', "Trackbar Windows", 0, 100, onChange)

cv2.setTrackbarPos("sigma_s",'Trackbar Windows', 100)
cv2.setTrackbarPos("sigma_r",'Trackbar Windows', 10)

while True:
    if cv2.waitKey(100) == ord('q'):
        break
    sigma_s_value = cv2.getTrackbarPos("sigma_s", "Trackbar Windows")
    sigma_r_value = cv2.getTrackbarPos("sigma_r", "Trackbar Windows") /100

    print("sigma_s_value", sigma_s_value)
    print("sigma_r_value", sigma_r_value)

    cartoon_img = cv2.stylization(img, sigma_s = sigma_s_value, sigma_r=sigma_r_value)
    cv2.imshow("Trackbar Windows", cartoon_img)

cv2.destroyAllWindows()
""" 
CARTOON_IMG = cv2.stylization(img,sigma_s = 100, sigma_r = 0.1)
cv2.imshow('cartoon view', CARTOON_IMG)
cv2.waitKey(0)
cv2.destroyAllWindows()
""" 