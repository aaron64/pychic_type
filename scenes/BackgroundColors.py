from scenes.Scene import Scene

class BackgroundColors(Scene):
	def __init__(self, switch_type, key, colors):
		super().__init__(switch_type, key)
		self.colors = colors
		self.color_counter = 0
		
	def draw(self, g, params):
		if(self.visible):
			g.fill_rect(0,0,params.width,params.height, self.colors[self.color_counter])

	def trigger(self, params):
		self.color_counter = [len(self.colors)%self.color_counter]
