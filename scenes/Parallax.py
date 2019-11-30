from util.SpriteField import SpriteField
from util.vec2f import vec2f
from scenes.Scene import Scene

import pyglet

import math

class Parallax(Scene):
	def __init__(self, switch_type, key, g, params, res, v=vec2f(1,1), space = 64, speed = 6):
		super().__init__(switch_type, key)
		self.image = pyglet.image.load('res/image/' + res + '.png')	
		self.space = space
		self.speed = speed

		self.v = v

		self.sprites_x = math.ceil(params.width / (self.image.width + self.space)) + 1
		self.sprites_y = math.ceil(params.height / (self.image.height + self.space)) + 1
		self.sprites = SpriteField(self.sprites_x * self.sprites_y, res, g)

	def update(self, params):
		index = 0
		arr = []
		for i in range(self.sprites_x):
			for j in range(self.sprites_y):
				arr.append((i-1) * (self.image.width + self.space) + (params.frame_count * self.speed * self.v.x)%(self.image.width + self.space))
				arr.append((j-1) * (self.image.height + self.space) + (params.frame_count * self.speed * self.v.y)%(self.image.height + self.space))
				index+=1
		self.sprites.set_pos(arr)

	def draw(self, g, params):
		if(self.visible):
			self.sprites.send_to_batch(g)