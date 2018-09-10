from util.Image import Image as img

from scenes.Image import Image

import pyglet
import math

class ImageShake(Image):
	def __init__(self, switch_type, key, res, g, x, y, s=1, shake_x=20, shake_y=20, speed=50):
		super().__init__(switch_type, key, res, g, x, y, s)

		self.shake_x = shake_x
		self.shake_y = shake_y
		self.speed = speed

	def update(self, params):
		self.render_x = self.x + math.sin(params.frame_count * self.speed) * self.shake_x 
		self.render_y = self.y + math.cos(params.frame_count * self.speed) * self.shake_y 