import pyglet

class Image():
	def __init__(self, res, g, pos, s=1):
		self.image = pyglet.image.load('res/image/' + res + '.png')
		self.width = self.image.width
		self.height = self.image.height

		self.spr = pyglet.sprite.Sprite(self.image, batch=g.main_batch, group=g.background)
		self.spr.scale = s
		self.spr.x = pos.x
		self.spr.y = pos.y

	def draw(self, g, pos=None, render_group=None):
		if pos is None:
			pos = vec2f(vec=self.pos)

		if render_group is None:
			render_group = g.background
		
		self.spr.x = pos.x
		self.spr.y = pos.y
		self.spr.batch = g.main_batch

		#self.image.blit(x,y)

		