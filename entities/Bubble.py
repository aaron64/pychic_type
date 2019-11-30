import random as rand
import math
from entities.Entity import Entity

class Bubble(Entity):
	def __init__(self, params, image):
		super().__init__()
		self.pos = vec2f(rand.randrange(params.width), params.height + rand.randrange(0, params.height/2))

		self.dx = 0
		self.yv = rand.randrange(1,3)

		self.sway = rand.randrange(3,6)
		self.phase = rand.uniform(0,3.14)
		self.r = rand.randrange(5,10)

		self.sprite = pyglet.sprite.Sprite(self.image, x=x, y=y, batch=g.main_batch, group=g.foreground)

	def update(self, params):
		self.pos.y -= self.yv
		self.dx = self.pos.x + self.sway * math.sin(self.phase)
		self.phase += 0.01

	def draw(self, g, params):
		self.sprite.batch = g.main_batch	
	