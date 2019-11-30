from util.Image import Image as img

from scenes.Image import Image

import pyglet
import math

class ImageMove(Image):
	def __init__(self, switch_type, key, g, res, pos1, pos2, s=1):
		super().__init__(switch_type, key, res, g, pos1, s)

		self.pos2 = pos2

	def knob(self, params, val):
		self.render_pos = self.pos + (self.pos2 - self.pos) * val
