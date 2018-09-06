from scenes.Scene import Scene
import util.color as color_util
from random import randint

class Strobe(Scene):
	def __init__(self, switch_type, key, color=None, speed=1):
		super().__init__(switch_type, key)
		self.strobe = True
		self.speed = speed
		
		self.color = color
		if(self.color == None):
			self.color = color_util.get_color("white")
		self.render_color = self.color

	def update(self, params):
		if(params.frame_count%self.speed == 0):
			self.strobe = not self.strobe

		if(self.color == "rand"):
			self.color = color_util.get_color("blue")
			self.render_color = self.color

	def draw(self, g, params):
		if(self.strobe and self.visible):
			g.fill_rect(0,0,params.width,params.height, self.render_color, g.foreground)

	def knob(self, params, val):
		self.render_color = color_util.interpolate(self.color, color_util.get_color("transparent"), val)
