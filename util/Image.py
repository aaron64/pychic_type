import pyglet

class Image():
	def __init__(self, res, g, x=0, y=0, s=1):
		self.image = pyglet.image.load('res/' + res + '.png')
		self.width = self.image.width
		self.height = self.image.height

		self.spr = pyglet.sprite.Sprite(self.image, batch=g.main_batch, group=g.background)
		self.spr.scale = s
		self.spr.x = x
		self.spr.y = y

	def draw(self, g, x = None, y = None, render_group=None):
		if x is None:
			x = self.x
		if y is None:
			y = self.y

		if render_group is None:
			render_group = g.background
		
		self.spr.x = x
		self.spr.y = y
		self.spr.batch = g.main_batch

		#self.image.blit(x,y)

		