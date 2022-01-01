import cv2
import mediapipe as mp


def say_hi ():
    print('Hello Camera')

cap = cv2.VideoCapture(1)

while True:
    success, img = cap.read()
    cv2.imshow("Image",img)
    cv2.waitKey(1)