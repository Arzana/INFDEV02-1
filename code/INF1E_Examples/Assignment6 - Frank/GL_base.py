from Canvas import ClearBackBuffer, Swap, Render, Plot
from Vector2 import Vect2

def Line(c: int, v0: Vect2, v1: Vect2):					# Full implementation for Bresenhams line algorithm.
	w = int(v1.X - v0.X)								# Get the normal width and height of the line.
	h = int(v1.Y - v0.Y)
	
	dX0 = -1 if w < 0 else (1 if w > 0 else 0)			# Get the delta x and y velocity for when error movement occurs.
	dY0 = -1 if h < 0 else (1 if h > 0 else 0)
	dX1 = -1 if w < 0 else (1 if w > 0 else 0)			# Get the delta x velocity for non error movement.
	dY1 = 0												# Set the delta y velocity for non error movement to zero as default.
	
	long = abs(w)										# Get the absolute distance in x and y.
	short = abs(h)
	if (long <= short):									# If the line is more vertical than horizontal, swap the x and y.
		long = abs(h)
		short = abs(w)
		dY1 = -1 if h < 0 else (1 if h > 0 else dY1)	# Get the delta y velocity for non error movement.
		dX1 = 0											# Set the delta x velocity for non error movement to zero because the x and y have been swapped.
	
	num = long >> 1										# Set the numerator to the longest component of the distance divided by two.
	x = v0.X											# Set the starting position for x and y.
	y = v0.Y
	
	for i in range(long + 1):							# Loop for the largest component of the distance in the line.
		Plot(c, Vect2(x, y))							# Put the color at position x, y.
		num += short									# Adds the smallest component of the distance to the numerator.
		if (num >= long):								# If the error in delta has become to large, offset to the correct position and reset the numerator.
			num -= long
			x += dX0
			y += dY0
		else:											# Move the normal amount.
			x += dX1
			y += dY1
		
def Triangle(c: int, v0: Vect2, v1: Vect2, v2: Vect2):	# Implementation for triangle rasterization using the barycentric algorithm.  
	maxX = max(v0.X, max(v1.X, v2.X))					# Get the bounding box for the triangle.
	minX = min(v0.X, min(v1.X, v2.X))
	maxY = max(v0.Y, max(v1.Y, v2.Y))
	minY = min(v0.Y, min(v1.Y, v2.Y))
	
	vs1 = Vect2(v1.X - v0.X, v1.Y - v0.Y)				# Get the vector distance (spanning vectors) between edges (v0, v1) and (v0, v2)
	vs2 = Vect2(v2.X - v0.X, v2.Y - v0.Y)
	
	for y in range(int(minY), int(maxY + 1)):			# Loop trough each point in the bounding box.
		for x in range(int(minX), int(maxX + 1)):
			q = Vect2(x - v0.X, y - v0.Y)				# Get the vector distance between the start point and the current point.		
			
			s = Vect2.Cross(q, vs2) / Vect2.Cross(vs1, vs2)
			t = Vect2.Cross(vs1, q) / Vect2.Cross(vs1, vs2)
			
			if (s >= 0 and t >= 0 and s + t <= 1): Plot(c, Vect2(x, y))