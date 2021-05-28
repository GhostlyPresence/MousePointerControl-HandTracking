import cv2
import mediapipe as mp
import numpy as np
import time

cap  = cv2.VideoCapture(2)


mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

ret, frame = cap.read()
if ret:
	h,w,c = frame.shape

pTime = 0
cTime = 0
while ret:
	ret, frame = cap.read()
	frame = cv2.flip(frame, 1)
	imgRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
	results = hands.process(imgRGB)
	#print(results)
	blackImg = np.zeros((h,w,c))

	if results.multi_hand_landmarks:
		for handLms in results.multi_hand_landmarks:
			for id, lm in enumerate(handLms.landmark):
				cx, cy = int(lm.x*w), int(lm.y*h)
				# print(cx,cy)
				if id == 8:
					cv2.circle(frame, (cx,cy), 20,(255,0,0), cv2.FILLED)


			mpDraw.draw_landmarks(frame,handLms,mpHands.HAND_CONNECTIONS)

	cTime = time.time()
	fps = 1/(cTime-pTime)
	pTime = cTime

	cv2.putText(frame, str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
	cv2.imshow("video",frame)
	if(cv2.waitKey(20) == 27):
		break