from entities.Image import Image
from scenes.Scene import Scene

class Background(Scene):
	def __init__(self, switch_type, key, res):
		super().__init__(switch_type, key)
		#self.img = Image(pyxel, "flower")
		