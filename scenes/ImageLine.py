from util.SpriteField import SpriteField
from scenes.Scene import Scene

import pyglet

import math

class ImageLine(Scene):
	def __init__(self, switch_type, key, res, g, params, intercept, v = 1, space = 64, speed = 6, horizontal = True):
		super().__init__(switch_type, key)
		self.image = pyglet.image.load('res/' + res + '.png')	
		self.space = space
		self.speed = speed
		self.horizontal = horizontal
		self.intercept = intercept
		self.v = v

		if(self.horizontal):
			self.sprites_count = math.ceil(params.width / (self.image.width + self.space)) + 1
		else:
			self.sprites_count = math.ceil(params.height / (self.image.height + self.space)) + 1

		self.sprites = SpriteField(self.sprites_count, res, g)

	def update(self, params):
		index = 0
		arr = []
		for i in range(self.sprites_count):
			if(self.horizontal):
				arr.append((i-1) * (self.image.width + self.space) + (params.frame_count * self.speed * self.v)%(self.image.width + self.space))
				arr.append(self.intercept)
			else:
				arr.append(self.intercept)
				arr.append((i-1) * (self.image.height + self.space) + (params.frame_count * self.speed * self.v)%(self.image.height + self.space))
			index+=1
		self.sprites.set_pos(arr)

	def draw(self, g, params):
		if(self.visible):
			self.sprites.send_to_batch(g)