import pyglet

class Image():
	def __init__(self, res, x=0, y=0, s=1):
		self.image = pyglet.image.load('res/' + res + '.png')
		self.width = self.image.width
		self.height = self.image.height

	def draw(self, g, x = None, y = None):
		if x is None:
			x = self.x
		if y is None:
			y = self.y

		self.image.blit(x,y)
		spr = pyglet.sprite.Sprite(self.image, batch=g.main_batch, group=g.background)
		spr.x = x
		spr.y = y