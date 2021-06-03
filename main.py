import os
import cv2
import numpy as np

import handTracking as ht
import WebCamVideoStream
import mouseControl as mc
import fps

print("\n[INFO] Select Your Web cam :")
print("Press 0 if you want to use the Inbuilt Web Cam")
print(
    "Press 1 if you want to use external Web Cam.\n[NOTE] if this source doesn't work, try 2 or -1 to use external web cam")

src = int(input("Source: "))


WCam, hCam = 640, 480

# -----------------------------
# These Lines control the use of multi-threading, if you don't want to use multiThreading, Toggle the comments of following 3 lines

#cap = cv2.VideoCapture(src)
vs = WebCamVideoStream.getVideoStream(src=src)
cap = vs.start()
# -----------------------------

if(cap is None or not cap.isOpened()):
    print("\n------------------------------------------------------------")
    print('Warning: unable to open video source: {} try diffrent source'.format(src))
    print("------------------------------------------------------------\n")
    os._exit(0)

# cap.set(3,WCam)
# cap.set(4,hCam)


detector = ht.handDetector(maxHands=1)
controller = mc.Controller()
FPS = fps.FPS()

ret, frame = cap.read()
cv2.namedWindow("Video")

while ret:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = detector.findHands(imgRGB, frame)
    cx, cy = detector.findPostion(frame)
    fingers = detector.fingersUp()

    if fingers[1] == 1 and fingers[2] == 0:
        cv2.circle(frame, (cx, cy), 10, (255, 255, 255), cv2.FILLED)
        controller.Move(cx, cy)

    if fingers[1] == 1 and fingers[2] == 1:
        # Find distance between fingers
        length, img, lineInfo = detector.findDistance(8, 12, frame)
        #print(length)
        # Click mouse if distance short
        if length < 40:
            cv2.circle(frame, (lineInfo[4], lineInfo[5]),
            15, (0, 255, 0), cv2.FILLED)
            controller.click()

    # Frame Rate
    frame_rate = FPS.get_fps()
    cv2.putText(frame, "Normal fps " + str(frame_rate), (10, 70),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    # Display
    cv2.imshow("Video", frame)

    if(cv2.waitKey(20) == 27):
        vs.stop()
        break

cap.release()
cv2.destroyAllWindows()
