from Canvas import Init, Swap, Render
from Vector2 import Vect2, Vect2_Zero
from GL_func import GL_String
from sys import platform
from Shapes import *
import traceback
from time import sleep
from Input import GetCh

type = -1
selected = 4
args = []
maxX = 0
MaxY = 0

colors = {
	"Red": 41,
	"Green": 42,
	"Yellow": 43,
	"Navy": 44,
	"Magenta": 45,
	"Blue": 46,
	"White": 47,
	"Black": 48 }
	
def GetSColor(y: int):
	return colors["Navy"] if selected == y else colors["Black"]
	
def clamp(min, max, v):
	return min if v < min else (max if v > max else v)
	
def GetNumerical(text: str, min: int, max: int):
	global selected
	selected = 0
	while (True):
		GL_String(Vect2_Zero, text + str(selected))
		EndDraw()
		
		key = ord(GetCh())
		if (key == 224):
			key = ord(GetCh())
			if (key == 72): selected -= 1
			elif (key == 80): selected += 1
			selected = clamp(0, max, selected)
		elif (key == 13):
			return selected

def GetArgs():
	global type, selected
	while (type == -1):
		GL_String(Vect2_Zero, "Welcome to the primitive drawing program.")
		GL_String(Vect2(0, 1), "Distortion may occur as a result of the font used!")
		GL_String(Vect2(0, 2), "Please specify the primitive you would like to be drawn:")
		GL_String(Vect2(0, 4), "\"Ugly\" Smiley", GetSColor(4))
		GL_String(Vect2(0, 5), "Filled Square", GetSColor(5))
		GL_String(Vect2(0, 6), "Square", GetSColor(6))
		GL_String(Vect2(0, 7), "Rectangular Triangle", GetSColor(7))
		GL_String(Vect2(0, 8), "Isosceles Triangle", GetSColor(8))
		GL_String(Vect2(0, 9), "Filled Circle", GetSColor(9))
		EndDraw()
		
		key = ord(GetCh())
		if (key == 224): #Special
			key = ord(GetCh())
			if (key == 72): selected -= 1	# Down
			elif (key == 80): selected += 1	# Up
			selected = clamp(4, 9, selected)
		elif (key == 13): # Enter
			type = selected - 4
			
	if (type > 0):
		args.append(GetNumerical("Please specify the x component of the position: ", 0, maxX - 1))
		args.append(GetNumerical("Please specify the y component of the position: ", 0, maxY - 1))
		
		if (type < 5):
			args.append(GetNumerical("Please specify the width component: ", 1, maxX - args[0]))
			args.append(GetNumerical("Please specify the height component: ", 1, maxY - args[1]))
		else:
			args.append(GetNumerical("Please specify the radius component: ", 1, int(min(maxX, maxY)) >> 1))

def Draw():
	if (type == 0): 
		Smiley()
	else:
		pos = Vect2(args[0], args[1])
		if (type == 1): FillRect(colors["White"], pos, args[2], args[3])
		elif (type == 2): DrawRect(colors["White"], pos, args[2], args[3])
		elif (type == 3): FillRectTrgl(colors["White"],  pos, args[2], args[3])
		elif (type == 4): FillIsoTrgl(colors["White"], pos, args[2], args[3])
		elif (type == 5): FillCircle(colors["White"], pos, args[2])
	
	GL_String(Vect2_Zero, "Press any key to continue...")
	
def EndDraw():
	Swap()
	Render()
	
def Tick():
	GetArgs()
	Draw()
	EndDraw()
	
def main():
	global maxX, maxY
	if (platform == "win32"):
		# Enable console colors
		import ctypes
		kernel32 = ctypes.windll.kernel32
		kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

	try:
		Init()
		from Canvas import w, h
		maxX = w
		maxY = h
		
		Tick()
	except:
		print("\033[0;37;40m")
		traceback.print_exc()
	input()
	
if (__name__ == "__main__"): main()