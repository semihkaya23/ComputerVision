import time

import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLMS in results.multi_hand_landmarks:
            for lm_id, lm in enumerate(handLMS.landmark):
                print(lm_id, lm)
                img_height, img_width, img_channels = img.shape
                center_x = center_y = int(lm.x * img_width), int(lm.y * img_height)
                print(lm_id,"\t",center_x,"\t",center_x)

            mpDraw.draw_landmarks(img, handLMS, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow('Image', img)
    cv2.waitKey(1)
