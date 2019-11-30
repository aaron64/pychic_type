import random as rand
import math
from entities.Entity import Entity

class Bubble(Entity):
	def __init__(self, pos, vel, params, image):
		super().__init__(pos)
		self.vel = vel

		self.sprite = pyglet.sprite.Sprite(self.image, x=pos.x, y=pos.y, batch=g.main_batch, group=g.foreground)

	def update(self, params):
		self.pos += vel

	def draw(self, g, params):
		self.sprite.batch = g.main_batch
	