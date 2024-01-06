import cv2
import numpy as np

"""
功能：通过滑块调整HSV阈值
"""

img = cv2.imread('2.jpg')
cv2.imshow("src", img)

hsv_low = np.array([0, 0, 0])
hsv_high = np.array([0, 0, 0])


def h_low(value):
    hsv_low[0] = value


def h_high(value):
    hsv_high[0] = value


def s_low(value):
    hsv_low[1] = value


def s_high(value):
    hsv_high[1] = value


def v_low(value):
    hsv_low[2] = value


def v_high(value):
    hsv_high[2] = value


cv2.namedWindow('Trackbar')

# value参数为默认值, count参数为上限
cv2.createTrackbar('H low', 'Trackbar', 0, 179, h_low)
cv2.createTrackbar('H high', 'Trackbar', 179, 179, h_high)
cv2.createTrackbar('S low', 'Trackbar', 0, 255, s_low)
cv2.createTrackbar('S high', 'Trackbar', 255, 255, s_high)
cv2.createTrackbar('V low', 'Trackbar', 130, 255, v_low)
cv2.createTrackbar('V high', 'Trackbar', 255, 255, v_high)

while True:
    res = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    res = cv2.inRange(res, hsv_low, hsv_high)

    # 形态学操作
    # kernel1 = np.ones((1, 1), np.uint8)
    # kernel2 = np.ones((3, 3), np.uint8)
    # res = cv2.erode(res, kernel1, iterations=1)
    # res = cv2.dilate(res, kernel2, iterations=1)

    cv2.imshow('res', res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
