import cv2
import numpy as np

"""
功能：通过滑块调整摄像头图像的HSV阈值
"""

# 打开摄像头（默认为摄像头0，如果有多个摄像头可以尝试不同的索引）
cap = cv2.VideoCapture(0)

# 创建一个窗口用于显示调整阈值的滑块
cv2.namedWindow('Trackbar')

# 初始化阈值范围
hsv_low = np.array([0, 0, 0])
hsv_high = np.array([179, 255, 255])


# 回调函数，用于调整HSV阈值
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


# 创建滑块
cv2.createTrackbar('H low', 'Trackbar', 0, 179, h_low)
cv2.createTrackbar('H high', 'Trackbar', 179, 179, h_high)
cv2.createTrackbar('S low', 'Trackbar', 0, 255, s_low)
cv2.createTrackbar('S high', 'Trackbar', 255, 255, s_high)
cv2.createTrackbar('V low', 'Trackbar', 130, 255, v_low)
cv2.createTrackbar('V high', 'Trackbar', 255, 255, v_high)

while True:
    # 读取摄像头图像
    ret, img = cap.read()
    if not ret:
        print("bad")
        break

    # 将图像转换为HSV空间
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 应用阈值
    res = cv2.inRange(hsv_img, hsv_low, hsv_high)

    # 显示结果
    cv2.imshow('Original', img)
    cv2.imshow('Threshold', res)

    # 检测按键，如果按下 'q' 键则退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头并关闭窗口
cap.release()
cv2.destroyAllWindows()
