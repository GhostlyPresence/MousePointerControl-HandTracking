import cv2
import time
import numpy as np

import handTracking as ht
import WebCamVideoStream 
import mouseControl as mc

src = 2
#cap = cv2.VideoCapture(src)
vs = WebCamVideoStream.getVideoStream(src=src)
cap = vs.start()

detector = ht.handDetector(maxHands=1)
controller = mc.Controller()

ret, frame = cap.read()

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
    cv2.imshow("video", frame)

    if(cv2.waitKey(20) == 27):
        vs.stop()
        break

cap.releaseCap()
cv2.destroyAllWindows()