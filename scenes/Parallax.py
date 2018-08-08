from util.Image import Image
from scenes.Scene import Scene

import math

class Parallax(Scene):
	def __init__(self, switch_type, key, res):
		super().__init__(switch_type, key)
		self.image = Image("flower")
		self.space = 3
		self.speed = 6

	def update(self, params):
		pass

	def draw(self, g, params):
		i_range = math.ceil(params.width / (self.image.width + self.space)) + 1
		j_range = math.ceil(params.height / (self.image.height + self.space)) + 1
		if(True):
			for i in range(i_range):
				for j in range(j_range):
					self.image.x = (i-1) * self.image.width * self.space + (params.frame_count * self.speed)%(self.image.width * self.space)
					self.image.y = (j-1) * self.image.height * self.space + (params.frame_count * self.speed)%(self.image.height * self.space)
					self.image.draw(g)