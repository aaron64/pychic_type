

class vec2f:
	def __init__(self, x=0, y=0, vec=None):
		self.x = x
		self.y = y

		if vec is not None:
			self.x = pos.x
			self.y = pos.y

	def __add__(self, other):
		return vec2f(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return vec2f(self.x + other.x, self.y + other.y)

	def __mul__(self, val):
		return vec2f(self.x * val, self.y * val)

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __iadd__(self, other):
		self.x += other.x
		self.y += other.y