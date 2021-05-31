import mediapipe as mp


class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionConfidence=0.5, trackConfidence=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionConfidence = detectionConfidence
        self.trackConfidence = trackConfidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                        self.detectionConfidence, self.trackConfidence)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self,imgRGB,frame,draw=True):
    	self.results = self.hands.process(imgRGB)

    	if self.results.multi_hand_landmarks and draw:
    		for handLms in self.results.multi_hand_landmarks:
    			self.mpDraw.draw_landmarks(frame, handLms, self.mpHands.HAND_CONNECTIONS)

    	return frame

    def findPostion(self, frame, idx=8,handNo=0, draw=True):
    	h, w, c = frame.shape
    	cx = cy = -1
    	if self.results.multi_hand_landmarks:
    		myHand = self.results.multi_hand_landmarks[handNo]
    		for id,lm in enumerate(myHand.landmark):
    			if id == idx:
    				cx, cy = int(lm.x*w), int(lm.y*h) 
    			
    	return cx, cy

    		


if __name__ == "__main__":
    print("[INFO] This is the Hand Detector class....")
