from util.SpriteField import SpriteField
from scenes.Scene import Scene

import pyglet

import math

class Parallax(Scene):
	def __init__(self, switch_type, key, res, g, params):
		super().__init__(switch_type, key)
		#self.image = Image("flower")
		self.image = pyglet.image.load('res/' + res + '.png')	
		self.space = 3
		self.speed = 6
		self.sprites_x = math.ceil(params.width / (self.image.width + self.space)) + 1
		self.sprites_y = math.ceil(params.height / (self.image.height + self.space)) + 1
		self.sprites = SpriteField(self.sprites_x * self.sprites_y, res, g)

	def update(self, params):
		index = 0
		arr = []
		for i in range(self.sprites_x):
			for j in range(self.sprites_y):
				# arr.append(5 * j)
				# arr.append(10)
				arr.append((i-1) * self.image.width * self.space + (params.frame_count * self.speed)%(self.image.width * self.space))
				arr.append((j-1) * self.image.height * self.space + (params.frame_count * self.speed)%(self.image.height * self.space))
				index+=1
				#print((j-1) * self.image.height * self.space + (params.frame_count * self.speed)%(self.image.height * self.space))
		self.sprites.set_pos(arr)

	def draw(self, g, params):
		self.sprites.send_to_batch(g)