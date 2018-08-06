from scenes.Scene import Scene

class BigText(Scene):
	def __init__(self, switch_type, key, text):
		super().__init__(switch_type, key)
		self.text = text.split()
		self.step = 0

	def update(self, params):
		pass

	def draw(self, g, params):
		pass
		#pyxel.text(10,10, self.text[self.step], 7)

	def trigger(self, params):
		self.step += 1