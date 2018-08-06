from entities.Image import Image
from scenes.Scene import Scene

class Parallax(Scene):
	def __init__(self, switch_type, key, res):
		super().__init__(switch_type, key)
		#self.img = Image(pyxel, "flower")
		#self.space = max(self.img.w, self.img.h)
		print(self.space)

	def update(self, params):
		pass

	def draw(self, g, params):
		pass
		#if(self.state):
		#	for i in range(6):
		#		for j in range(7):
		#			self.img.draw(pyxel, x = (i-1) * 32 + pyxel.frame_count%32, y = (j-1) * 32 + pyxel.frame_count%32)