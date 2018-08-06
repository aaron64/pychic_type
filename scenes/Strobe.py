from scenes.Scene import Scene
import util.color as color
from random import randint

class Strobe(Scene):
	def __init__(self, switch_type, key, color=7, speed=1):
		super().__init__(switch_type, key)
		self.strobe = True
		self.color = color
		self.speed = speed

	def update(self, params):
		#if(pyxel.frame_count%self.speed == 0):
		self.strobe = not self.strobe

	def draw(self, g, params):
		if(self.strobe and self.state):
			if(self.color == "rand"):
				g.draw_rect(0,0,params.width,params.height, color.WHITE)
			else:
				g.draw_rect(0,0,params.width,params.height, color.WHITE)
