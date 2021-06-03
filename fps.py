import time


class FPS:
    def __init__(self):
        self.cTime = 0
        self.pTime = 0

    def get_fps(self):
        self.cTime = time.time()
        fps = 1 / (self.cTime - self.pTime)
        self.pTime = self.cTime
        return int(fps)
