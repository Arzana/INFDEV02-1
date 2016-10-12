from math import pi, cos, sin
from Canvas import GetCenter
from Vector2 import Vect2
from GL_func import *

tau = pi * 2.0

def DrawRect(c: int, pos: Vect2, w: int, h: int):
	GL_Line_Loop(c, [pos, Vect2(pos.X + w, pos.Y), Vect2(pos.X + w, pos.Y + h), Vect2(pos.X, pos.Y + h)])
	
def FillRect(c: int, pos: Vect2, w: int, h: int):
	GL_Triangle_Strip(c, [Vect2(pos.X, pos.Y + h), pos, Vect2(pos.X + w, pos.Y + h), Vect2(pos.X + w, pos.Y)])
	
def DrawRectTrgl(c: int, pos: Vect2, w: int, h: int):
	GL_Line_Loop(c, [pos, Vect2(pos.X, pos.Y + h), Vect2(pos.X + w, pos.Y + h)])
	
def FillRectTrgl(c: int, pos: Vect2, w: int, h: int):
	GL_Triangles(c, [pos, Vect2(pos.X, pos.Y + h), Vect2(pos.X + w, pos.Y + h)])
	
def DrawIsoTrgl(c: int, pos: Vect2, w: int, h: int):
	GL_Line_Loop(c, [Vect2(pos.X + (w >> 1), pos.Y), Vect2(pos.X, pos.Y + h), Vect2(pos.X + w, pos.Y + h)])

def FillIsoTrgl(c: int, pos: Vect2, w: int, h: int):
	GL_Triangles(c, [Vect2(pos.X + (w >> 1), pos.Y), Vect2(pos.X, pos.Y + h), Vect2(pos.X + w, pos.Y + h)])
	
def DrawCircle(c: int, pos: Vect2, r: float):
	lines = 64
	
	vertices = []
	for i in range(lines + 1):
		x = pos.X + (r * cos(i * tau / lines))
		y = pos.Y + (r * sin(i * tau / lines))
		vertices.append(Vect2(x, y))
	
	GL_Line_Loop(c, vertices)
	
def FillCircle(c: int, pos: Vect2, r: float):
	trgls = 32
	
	vertices = [pos]
	for i in range(trgls + 1):
		x = pos.X + (r * cos(i * tau / trgls))
		y = pos.Y + (r * sin(i * tau / trgls))
		vertices.append(Vect2(x, y))
	
	GL_Triangle_Fan(c, vertices)
	
def Smiley():
	center = GetCenter()
	r = int(center.Y - 2)
	hr = r >> 1
	qr = r >> 2
	tqr = r - qr
	scalar = 0 if r <= 10 else r / 10
	
	# Head shape
	DrawCircle(47, center, r)
	
	# Nose
	size = int(max(1, scalar))
	FillIsoTrgl(43, center - Vect2(size >> 1, 0), size, size)
	
	# Eyebrows
	GL_Lines(44, [
		center - Vect2(hr + scalar, hr + scalar * 1.5), center - Vect2(hr - scalar, hr + scalar * 1.5),
		center - Vect2(-hr + scalar, hr + scalar * 1.5), center - Vect2(-hr - scalar, hr + scalar * 1.5)])
	
	# Eyes
	DrawCircle(46, center - Vect2(hr, hr - 1), scalar)
	DrawCircle(46, center - Vect2(-hr, hr - 1), scalar)
	
	# Mouth
	GL_Lines(41, [center + Vect2(tqr, qr), center + Vect2(hr, hr)])
	GL_Lines(41, [center + Vect2(-tqr, qr), center + Vect2(-hr, hr)])
	GL_Lines(41, [center + Vect2(-hr, hr), center + Vect2(hr, hr)])