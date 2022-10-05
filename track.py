#code heavily inspired from https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html

import cv2 as cv
import numpy as np

cap = cv.VideoCapture('mov_4-3.mov')

while(1):
    _, frame = cap.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_blue = np.array([100, 25, 25])
    upper_blue = np.array([130, 255, 255])
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    res = cv.bitwise_and(frame, frame, mask = mask)
    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()