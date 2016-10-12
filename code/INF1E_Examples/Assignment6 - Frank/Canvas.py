from Vector2 import Vect2
import shutil

frontBuffer = ''
backBuffer = []
w = None
h = None

def GetConsoleSize():
	return shutil.get_terminal_size()

def GetConsoleWidth():
	return GetConsoleSize().columns

def GetConsoleHeight():
	return GetConsoleSize().lines
	
def GetCenter():
	return Vect2(w >> 1, h >> 1)

def ClearBackBuffer():
	global backBuffer
	backBuffer = []

	for y in range(h):
		for x in range(w):
			backBuffer.append("\033[0;30;48m ")
			
def Init():
	global w
	global h
	
	try:
		w = GetConsoleWidth()
		h = GetConsoleHeight()
	except:
		w = 80
		h = 25
		
	ClearBackBuffer()

def Swap():
	global frontBuffer

	frontBuffer = ''.join(backBuffer)
	ClearBackBuffer()

def Render():
	print(frontBuffer, end = '')
	
def PlotBase(value: str, v: Vect2):
	global backBuffer
	if (v.X < w and v.Y < h):
		backBuffer[round(v.Y) * w + round(v.X)] = value

def Plot(c: int, v: Vect2):
	PlotBase("\033[0;30;%dm " % c, v)
		
def PlotChar(c: chr, v: Vect2, color: int):
	PlotBase("\033[0;37;%dm%s" % (color, c), v)