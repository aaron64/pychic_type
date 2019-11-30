from util.Image import Image as img

from scenes.Scene import Scene

import pyglet

class Image(Scene):
	def __init__(self, switch_type, key, res, g, pos, s=1):
		super().__init__(switch_type, key)
		self.image = img(res, g, pos, s=s)	
		self.pos = pos
		self.render_pos = pos

	def draw(self, g, params):
		if(self.visible):
			self.image.draw(g, pos=self.render_pos)