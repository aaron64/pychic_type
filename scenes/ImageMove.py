from util.Image import Image as img

from scenes.Image import Image

import pyglet
import math

class ImageMove(Image):
	def __init__(self, switch_type, key, res, g, x1, y1, x2, y2, s=1):
		super().__init__(switch_type, key, res, g, x1, y1, s)

		self.x2 = x2
		self.y2 = y2

	def knob(self, params, val):
		self.render_x = self.x + (self.x2 - self.x) * val
		self.render_y = self.y + (self.y2 - self.y) * val
