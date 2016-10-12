from GL_base import Line, Triangle
from Vector2 import Vect2
from Canvas import Plot, PlotChar

def GL_Points(c: int, v):
	for i in range(len(v)):
		Plot(c, v[i])
		
def GL_Lines(c: int, v):
	if (len(v) & 1): return
	for i in range(0, len(v), 2):
		Line(c, v[i], v[i + 1])
		
def GL_Line_Strip(c: int, v):	
	for i in range(len(v) - 1):
		Line(c, v[i], v[i + 1])
		
def GL_Line_Loop(c: int, v):	
	for i in range(len(v)):
		Line(c, v[i], v[i + 1 if i + 1 < len(v) else 0])
		
def GL_Triangles(c: int, v):
	if (len(v) % 3): return
	for i in range(0, len(v), 3):
		Triangle(c, v[i], v[i + 1], v[i + 2])
		
def GL_Triangle_Strip(c: int, v):
	if (len(v) < 3): return
	for i in range(2, len(v)):
		Triangle(c, v[i - 2], v[i - 1], v[i])
		
def GL_Triangle_Fan(c: int, v):
	if (len(v) < 3): return
	for i in range(1, len(v) - 1):
		Triangle(c, v[0], v[i], v[i + 1])

def GL_String(v: Vect2, text: str, c = 40):
	i = 0
	for char in text:
		PlotChar(char, v + Vect2(i, 0), c)
		i += 1