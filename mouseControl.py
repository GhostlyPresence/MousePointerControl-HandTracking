import pyautogui as gui
import numpy as np


class Controller:
    def __init__(self):
        self.smoothConstant = 4
        self.prev_x = self.prev_y = 0
        self.curr_x = self.curr_y = 0

        self.wScr, self.hScr = gui.size()

    def Move(self, x, y, delay=0.1):
        x = np.interp(x, (0, 640), (0, self.wScr))
        y = np.interp(y, (0, 480), (0, self.hScr))

        self.curr_x = self.prev_x + (x - self.prev_x) / self.smoothConstant
        self.curr_y = self.prev_y + (y - self.prev_y) / self.smoothConstant

        self.prev_x, self.prev_y = self.curr_x, self.curr_y
        gui.moveTo(self.curr_x, self.curr_y, delay)

    def click(self):
        gui.click()


if __name__ == '__main__':
    print("[INFO] This is the mouse controller .....")
