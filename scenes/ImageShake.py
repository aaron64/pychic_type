from util.Image import Image as img

from scenes.Image import Image

import pyglet
import math

class ImageShake(Image):
	def __init__(self, switch_type, key, res, g, pos, s=1, shake=vec2f(20,20), speed=50):
		super().__init__(switch_type, key, res, g, pos, s)

		self.shake = shake
		self.speed = speed

	def update(self, params):
		self.render_pos.x = self.pos.x + math.sin(params.frame_count * self.speed) * self.shake.x 
		self.render_pos.y = self.pos.y + math.cos(params.frame_count * self.speed) * self.shake.y 