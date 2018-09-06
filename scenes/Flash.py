from scenes.Scene import Scene
import util.color as color_util
from random import randint

class Flash(Scene):
	def __init__(self, switch_type, key, color=None, speed=10):
		super().__init__(switch_type, key)
		self.color = color
		if(self.color == None):
			self.color = color_util.get_color("white")

		self.speed = speed
		self.opacity = 0


	def update(self, params):
		self.opacity -= self.speed
		if(self.opacity < 0):
			self.visible = False
			self.opacity = 0
		self.color = color_util.set_opacity(self.color, self.opacity)

	def draw(self, g, params):
		if(self.visible):
			g.fill_rect(0,0,params.width,params.height, self.color, g.foreground)

	def trigger(self, params):
		self.opacity = 255
		self.visible = True
