import pyglet

import util.color
from scenes.Scene import Scene

class BigText(Scene):
	def __init__(self, switch_type, key, text, color=color.get_color("white")):
		super().__init__(switch_type, key)
		self.text = text


	def update(self, params):
		pass

	def draw(self, g, params):
		if(self.visible):
			pyglet.text.Label(self.text,
				font_name='Impact',
				font_size=168,
				batch=g.main_batch,
				group=g.foreground,
				x=g.window.width/2, y=g.window.height/2,
				anchor_x='center', anchor_y='center')

	def knob(self, params, val):
		self.color = color.setTransparency(val)