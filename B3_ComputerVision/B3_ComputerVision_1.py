import cv2
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread("abhiyaan_opencv_qn1.png")
roi = image[50:80,304:330]
hsv_roi = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
M = cv2.calcHist([hsv_roi],[0, 1], None, [180, 256], [0, 180, 0, 256] )
cv2.normalize(M,M,0,255,cv2.NORM_MINMAX)
B = cv2.calcBackProject([hsv_image],[0,1],M,[0,180,0,256],1)
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
cv2.filter2D(B,-1,disc,B)
B = np.uint8(B)
cv2.normalize(B,B,0,255,cv2.NORM_MINMAX)
ret,thresh = cv2.threshold(B,10,255,0)
thresh = cv2.merge((thresh,thresh,thresh))
res = cv2.bitwise_and(image,thresh)
img = res.copy()
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray,20,255,0)
cnts,heir = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
min_area = 250
for c in cnts:
    area = cv2.contourArea(c)
    if area > min_area:
        cv2.drawContours(image,[c], 0, (0,0,0),2)
cv2.imshow('a1',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
