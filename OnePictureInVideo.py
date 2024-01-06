import cv2

"""
功能：按下C键保存视频中的一帧画面
"""


# 填写视频地址
cap = cv2.VideoCapture("test.mp4")

if not cap.isOpened():
    print("ERROR: Can't open the video")

frame_id = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 显示视频帧
    cv2.imshow('Video', frame)

    # 按下 'C' or 'c' 键保存图片
    key = cv2.waitKey(30) & 0xFF
    if key == ord('c') or key == ord('C'):
        cv2.imwrite(f"frame_{frame_id}.jpg", frame)
        print(f"Saved frame {frame_id}")

    # 按下 'Q' 退出
    if key == ord('q') or key == ord('Q'):
        break

    frame_id += 1

    cv2.waitKey(100)

# 释放资源并关闭窗口
cap.release()
cv2.destroyAllWindows()

