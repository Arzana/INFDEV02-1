import math

class Vect2:
	""" Defines a 2-dimentional vector """

	X = 0
	Y = 0

	def __init__(self, x = float(0), y = float(0)):
		self.X = x
		self.Y = y

	def __add__(self, v2):
		return Vect2.Add(self, v2)

	def __sub__(self, v2):
		return Vect2.Subtract(self, v2)

	def __mul__(self, v2):
		return Vect2.Multiply(self, v2)

	def __div__(self, v2):
		return Vect2.Divide(self, v2)

	def __eq__(self, v2):
		return Vect2.Equals(self, v2)

	def __ne__(self, v2):
		return not Vect2.Equals(self, v2)

	def Area(self):
		return self.X * self.Y

	def Length(self):
		return math.sqrt(self.LengthSquared())

	def LengthSquared(self):
		return math.pow(self.X, 2) + math.pow(self.Y, 2)

	@staticmethod
	def Add(v1, v2):
		return Vect2(v1.X + v2.X, v1.Y + v2.Y)

	@staticmethod
	def Angle(v1, v2):
		return math.atan2(v2.Y - v1.Y, v2.X - v1.X)

	@staticmethod
	def Clamp(min, max, v):
		cX = min.X if v.X < min.X else (max.X if v.X > max.X else v.X)
		cY = min.Y if v.Y < min.Y else (max.Y if v.Y > max.Y else v.Y)
		return Vect2(cX, cY)

	# Prep dot product:
	# = 0: v1 and v2 are parallel
	# > 0: v2 is clockwise from v1
	# < 0: v1 is counter-clockwise from v2
	@staticmethod
	def Cross(v1, v2):
		return float((v1.X * v2.Y) - (v1.Y * v2.X))

	@staticmethod
	def Distance(v1, v2):
		return math.sqrt(Vect2.DistanceSquared(v1, v2))

	@staticmethod
	def DistanceManhattan(v1, v2):
		return math.fabs(v1.X - v2.X) + math.fabs(v1.Y - v2.Y)

	@staticmethod
	def DistanceSquared(v1, v2):
		diffX = v2.X - v1.X
		diffY = v2.Y - v1.Y

		distX = diffX * diffX
		distY = diffY * diffY

		return distX + distY

	@staticmethod
	def Divide(v1, v2):
		return Vect2(v1.X / v2.X, v1.Y / v2.Y)

	@staticmethod
	def Dot(v1, v2):
		return float((v1.X * v2.X) + (v1.Y * v2.Y))

	def Equals(self, v):
		return self.X == v.X and self.Y == v.Y;

	@staticmethod 
	def Max(v1, v2):
		mX = max(v1.X, v2.X)
		mY = max(v1.Y, v2.Y)
		return Vect2(mX, mY)

	@staticmethod 
	def Min(v1, v2):
		mX = min(v1.X, v2.X)
		mY = min(v1.Y, v2.Y)
		return Vect2(mX, mY)

	@staticmethod
	def Multiply(v1, v2):
		return Vect2(v1.X * v2.X, v1.Y * v2.Y)

	@staticmethod
	def Negate(v):
		return Vect2(-v.X, -v.Y)

	@staticmethod
	def Normalize(v):
		l = v.Length()
		return Vect2(v.X / l, v.Y / l)

	@staticmethod 
	def Reflect(v, n):
		dot = Vect2.Dot(v, n)
		diff = Vect2.Subtract(n, v)
		return Vect2.Multiply(diff, 2 * dot)

	@staticmethod
	def Subtract(v1, v2):
		return Vect2(v1.X - v2.X, v1.Y - v2.Y)

	def __str__(self):
		return "{X: %d, Y: %d}" % (self.X, self.Y)

Vect2_Zero = Vect2()
Vect2_One = Vect2(1, 1)
Vect2_UnitX = Vect2(1, 0)
Vect2_UnitY = Vect2(0, 1)
Vect2_Negative = Vect2(-1, -1)
