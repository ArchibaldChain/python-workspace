# coding=utf-8
# 追踪人脸运动轨迹 使用python2运行

from collections import deque
import cv2
import numpy as np
import argparse

from FlppyBird import FlppyBird

ap = argparse.ArgumentParser()
args = vars(ap.parse_args())

# eye_cascade=cv2.CascadeClassifier("/usr/share/opencv/haarcascades/haarcascade_eye.xml")

# test = cv2.imread(
#     "I:/Programming/Cpp_workspace/CppLearningCode/CppAssignment/opencv_test/sample_code/pictures/bird1.png")
# cv2.imshow('Example - Show image in window', test)
frame = cv2.imread(
    "I:\\Programming\\Cpp_workspace\\CppLearningCode\\CppAssignment\\opencv_test\\Lab_10\\circle-detection.jpg")


fp = FlppyBird(origin_frame)

while True:
    frame = cv2.imread(
        "I:\\Programming\\Cpp_workspace\\CppLearningCode\\CppAssignment\\opencv_test\\Lab_10\\circle-detection.jpg")

    fp.setTubes(frame)
    cv2.imshow("rstp", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# 摄像头释放
# cap.release()
# 销毁所有窗口
cv2.destroyAllWindows()
