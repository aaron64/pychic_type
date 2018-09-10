from util.Image import Image as img

from scenes.Scene import Scene

import pyglet

class Image(Scene):
	def __init__(self, switch_type, key, res, g, x, y, s=1):
		super().__init__(switch_type, key)
		self.image = img(res, g, x, y, s=s)	
		self.x = x
		self.y = y

		self.render_x = x
		self.render_y = y

	def draw(self, g, params):
		if(self.visible):
			self.image.draw(g, x=self.render_x, y=self.render_y)