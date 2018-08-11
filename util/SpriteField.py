import pyglet

class SpriteField():
	def __init__(self, amount, res, g):
		self.image = pyglet.image.load('res/' + res + '.png')
		self.size = amount
		self.sprites = [pyglet.sprite.Sprite(self.image, 0,0, batch=g.main_batch, group=g.foreground)]*amount
	def set_pos(self, pos_arr):
		for i in range(self.size):
			print(i)
			self.sprites[i].x = pos_arr[i*2]
			self.sprites[i].y = pos_arr[i*2 + 1]

