from scenes.Scene import Scene

class BackgroundColor(Scene):
	def __init__(self, switch_type, key, color):
		super().__init__(switch_type, key)
		self.color = color
		
	def draw(self, g, params):
		if(self.state)
			g.fill_rect(0,0,params.width,params.height, self.color)