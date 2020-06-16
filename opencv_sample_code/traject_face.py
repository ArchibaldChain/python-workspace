# coding=utf-8
# 追踪人脸运动轨迹 使用python2运行

from collections import deque
import cv2
import numpy as np
import argparse

import time
from FlppyBird import FlppyBird

ap = argparse.ArgumentParser()
args = vars(ap.parse_args())
face_cascade = cv2.CascadeClassifier(
    "C:/Programming/OpenCV/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml")
#      "/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml")
# eye_cascade=cv2.CascadeClassifier("/usr/share/opencv/haarcascades/haarcascade_eye.xml")

cap = cv2.VideoCapture(0)
pts = deque(maxlen=100)


ret, frame = cap.read()
fp = FlppyBird(frame)


while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # print i.shape
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    l = len(faces)

    center = None
    for (x, y, w, h) in faces:
        # cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # cv2.putText(frame, 'face', (w/2+x, y-h/5),
        #             cv2.FONT_HERSHEY_PLAIN, 2.0, (255, 255, 255), 2, 1)
        center = (x+w/2, y+h/2)

        # pts.appendleft(center)
        # for i in range(1, len(pts)):
        #     if pts[i-1] is None or pts[i] is None:
        #         continue
        #     thickness = int(np.sqrt(64 / float(i + 1)) * 2.5)
        #     cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)

    if center is not None:
        fp.drawBird(frame, center)
        if fp.isOver(center, 1, 1):
            print("Game Over!")

    fp.setTubes(frame)

    cv2.imshow("rstp", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 摄像头释放
cap.release()
# 销毁所有窗口
# cv2.destroyAllWindows()
