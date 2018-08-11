from scenes.Scene import Scene

import util.color

class BackgroundColor(Scene):
	def __init__(self, switch_type, key, color, color2=color.TRANSPARENT):
		super().__init__(switch_type, key)
		self.color = color
		self.color2 = color2
		self.renderColor = self.color
		
	def draw(self, g, params):
		if(self.visible)
			g.fill_rect(0,0,params.width,params.height, self.renderColor, g.background)

	def knob(self, params, val):
