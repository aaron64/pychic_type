import pyglet

import util.color as color
from scenes.Scene import Scene

class BigText(Scene):

	def __init__(self, switch_type, key, color, text, startHidden=True):
		super().__init__(switch_type, key)
		self.visible = not startHidden
		self.text = text.split()
		self.step = (0, -1)[startHidden]
		self.words = len(self.text)
		self.color = color

	def update(self, params):
		pass

	def draw(self, g, params):
		if(self.visible):
			pyglet.text.Label(self.text[self.step%self.words],
	                          font_name='Impact',
	                          font_size=168,
	                          batch=g.main_batch,
	                          group=g.foreground,
	                          color=color.convert_to_4(self.color),
	                          x=params.width/2, y=params.height/2,
	                          anchor_x='center', anchor_y='center')

	def trigger(self, params):
		self.visible = True
		self.step += 1