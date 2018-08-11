import pyglet

class SpriteField():
	def __init__(self, amount, res, g):
		self.image = pyglet.image.load('res/' + res + '.png')
		self.size = amount
		self.sprites = []#[pyglet.sprite.Sprite(self.image, 0,0, batch=g.main_batch, group=g.foreground)]*amount
		for i in range (amount):
			self.sprites.append(pyglet.sprite.Sprite(self.image, x=0, y=0, batch=g.main_batch, group=g.foreground))
	def set_pos(self, pos_arr):
		pass
		for i in range (self.size):
		 	self.sprites[i].x = pos_arr[i*2]
		 	self.sprites[i].y = pos_arr[i*2 + 1]

	def send_to_batch(self, g):
		for spr in self.sprites:
			spr.batch = g.main_batch	