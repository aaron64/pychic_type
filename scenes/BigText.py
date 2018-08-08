import pyglet

from scenes.Scene import Scene

class BigText(Scene):
	def __init__(self, switch_type, key, text):
		super().__init__(switch_type, key)
		self.text = text.split()
		self.step = 0

	def update(self, params):
		pass

	def draw(self, g, params):
		if(self.visible):
			pyglet.text.Label(self.text[self.step],
	                          font_name='Impact',
	                          font_size=168,
	                          batch=g.main_batch,
	                          group=g.foreground,
	                          x=g.window.width/2, y=g.window.height/2,
	                          anchor_x='center', anchor_y='center')

	def trigger(self, params):
		self.step += 1