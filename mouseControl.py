import pyautogui as gui

class Controller:
	def __init__(self):
		self.x, self.y = gui.size()

	def Move(self,x,y,delay=0.1):
		x,y = int(x*3), int(y*2.25)
		gui.moveTo(x,y,delay)



if __name__ == '__main__':
	print("[INFO] This is the mouse controller .....")