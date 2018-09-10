import pyglet

import util.color as color_util
from scenes.Scene import Scene

class BigWord(Scene):
	def __init__(self, switch_type, key, text, color=None):
		super().__init__(switch_type, key)
		self.text = text
		
		self.color = color
		if(self.color == None):
			self.color = color_util.get_color("white")


	def update(self, params):
		pass

	def draw(self, g, params):
		if(self.visible):
			pyglet.text.Label(self.text,
				font_name='Impact',
				font_size=168,
				batch=g.main_batch,
				group=g.foreground,
				x=params.width/2, y=params.height/2,
				anchor_x='center', anchor_y='center')

	def knob(self, params, val):
		self.color = color_util.setTransparency(val)