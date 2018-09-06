from scenes.Scene import Scene
import util.color as color

import util.color

class BackgroundColor(Scene):
	def __init__(self, switch_type, key, color1, color2=None):
		super().__init__(switch_type, key)
		self.color1 = color1
		if(color2 == None):
			self.color2 = color.get_color("transparent")
		else:
			self.color2 = color2
		self.renderColor = self.color1
		
	def draw(self, g, params):
		if(self.visible):
			g.fill_rect(0,0,params.width,params.height, self.renderColor, g.background)

	def knob(self, params, val):
		self.renderColor = color.interpolate(self.color1, self.color2, val)
		