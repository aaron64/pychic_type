import random as rand
import math
from entities.Entity import Entity
from scenes.Scene import Scene

import pyglet

class Bubbles(Scene):
	def __init__(self, switch_type, key, res):
		super().__init__(switch_type, key)
		self.bubbles=[]
		self.image = pyglet.image.load('res/' + res + '.png')

	def update(self, params):
		for b in self.bubbles:
			b.update(params)
			if(b.y < 0):
				self.bubbles.remove(b)

	def draw(self, g, params):
		for b in self.bubbles:
			b.draw(g)

	def trigger(self, params):
		for a in range(10):
			self.bubbles.append(Bubble(params, self.image))

	def hold(self, params):
		super().hold(params)
		if(params.frame_count%5 == 0):
			self.bubbles.append(Bubble(params, self.image))

class Bubble(Entity):

	def __init__(self, params):
		super().__init__(0,0)
		self.x = rand.randrange(params.width)
		self.y = params.height + rand.randrange(0, params.height/2)
		self.dx = 0
		self.yv = rand.randrange(1,3)

		self.sway = rand.randrange(3,6)
		self.phase = rand.uniform(0,3.14)
		self.r = rand.randrange(5,10)

	def update(self, params):
		self.y -= self.yv
		self.dx = self.x + self.sway * math.sin(self.phase)
		self.phase += 0.01

	def draw(self, g, params):
		for bubble in self.bubbles:
			bubble.draw(g, params)	

