

class vec3f:
	def __init__(self, x=0, y=0, z=0, vec=None):
		self.x = x
		self.y = y
		self.z = z

		if vec is not None:
			self.x = vec.x
			self.y = vec.y
			self.z = vec.z

	def __add__(self, other):
		return vec3f(self.x + other.x, self.y + other.y, self.z + other.z)

	def __sub__(self, other):
		return vec3f(self.x - other.x, self.y - other.y, self.z - other.z)

	def __mul__(self, val):
		return vec3f(self.x * val, self.y * val, self.z * val)

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y and self.z == other.z

	def __iadd__(self, other):
		self.x += other.x
		self.y += other.y
		self.z += other.z
		return self