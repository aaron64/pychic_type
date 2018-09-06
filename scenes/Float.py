from util.Image import Image as img

from scenes.Scene import Scene

import pyglet

class Float(Scene):
	def __init__(self, switch_type, key, res, g, x, y, s=1, speed=1, amount=10):
		super().__init__(switch_type, key)
		self.image = img(res, g, x, y, s=s)#pyglet.image.load('res/' + res + '.png')	
		self.x = x
		self.y = y

		self.speed = speed
		self.amount = amount

		self.draw_x = x
		self.draw_y = y

	def update(self, params):
		self.draw_x = self.x + math.sin(params.frame_count * self.speed) * self.amount
		self.draw_y = self.y + math.cos(params.frame_count * self.speed) * self.amount

	def draw(self, g, params):
		if(self.visible):
			self.image.draw(g, self.draw_x, self.draw_y)