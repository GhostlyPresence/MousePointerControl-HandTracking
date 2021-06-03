from threading import Thread
import cv2
import time


class getVideoStream:
    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)
        self.ret, self.frame = self.stream.read()

        self.stopped = False

    def start(self):
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        while True:
            if self.stopped:
                return
            self.ret, self.frame = self.stream.read()

    def read(self):
        return self.ret, self.frame

    def stop(self):
        self.stopped = True

    def set(self, idx, val):
        self.stream.set(idx, val)

    def release(self):
        print("\n[INFO] Realeasing Cap.....")
        self.stream.release()

    def isOpened(self):
        return self.stream.isOpened()


if __name__ == "__main__":
    print("[INFO] This is the multithreading video capture class....")
