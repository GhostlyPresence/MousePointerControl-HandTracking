import os
import cv2
import time
import numpy as np

import handTracking as ht
import WebCamVideoStream 
import mouseControl as mc

print("\n[INFO] Select Your Web cam :")
print("Press 0 if you want to use the Inbuilt Web Cam")
print("Press 1 if you want to use external Web Cam.\n[NOTE] if this source doesn't work, try 2 or -1 to use external web cam")
src = int(input("Source: "))
#-----------------------------
# These Lines control the use of multi-threading, if you don't want to use multiThreading, Toggle the comments of following 3 lines

#cap = cv2.VideoCapture(src)
vs = WebCamVideoStream.getVideoStream(src=src)
cap = vs.start()
#-----------------------------

if(cap is None or not cap.isOpened()):
    print("\n------------------------------------------------------------")
    print('Warning: unable to open video source: {} try diffrent source'.format(src))
    print("------------------------------------------------------------\n")
    os._exit(0)

detector = ht.handDetector(maxHands=1)
controller = mc.Controller()

ret, frame = cap.read()
cv2.namedWindow("Video")

pTime = 0
cTime = 0
while ret:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = detector.findHands(imgRGB,frame)
    cx,cy = detector.findPostion(frame)

    if cx!=-1 and cy!= -1:
    	cv2.circle(frame,(cx,cy), 10, (255,255,255), cv2.FILLED)
    	controller.Move(cx,cy)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(frame, "Normal fps " + str(int(fps)), (10, 70),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Video", frame)

    if(cv2.waitKey(20) == 27):
        vs.stop()
        break

cap.release()
cv2.destroyAllWindows()