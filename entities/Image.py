from entities.Entity import Entity

class Image(Entity):
	def __init__(self, pyxel, res, x=0, y=0, s=1):
		super().__init__(x,y)
		pyxel.image(0).load(0, 0, 'res/' + res + '.png')
		self.x = x
		self.y = y
		self.s = s
		self.w = pyxel.image(0).width * s
		self.h = pyxel.image(0).height * s

	def update(self, pyxel):
		pass

	def draw(self, pyxel, x = -1, y = -1):
		if(x == -1 and y == -1):
			pyxel.blt(self.x, self.y, 0, 0,0, self.w, self.h)
		else:
			pyxel.blt(x,y, 0, 0,0, self.w, self.h)