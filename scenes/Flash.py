from scenes.Scene import Scene
import util.color as color
from random import randint

class Flash(Scene):
	def __init__(self, switch_type, key, color, speed=10):
		super().__init__(switch_type, key)
		self.color = color
		self.speed = speed
		self.opacity = 0


	def update(self, params):
		self.opacity -= self.speed
		if(self.opacity < 0):
			self.opacity = 0
		self.color = color.set_opacity(self.color, self.opacity)

	def draw(self, g, params):
		g.fill_rect(0,0,params.width,params.height, self.color)

	def trigger(self, params):
		self.opacity = 255
