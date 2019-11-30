from scenes.Scene import Scene
from entities.Model import Model as Model_entity

from util.vec3f import vec3f

import random

class ModelRiser(Scene):

	def __init__(self, switch_type, key, res):
		super().__init__(switch_type, key)
		self.model_e = []
		for i in range(10):
			m_e_pos = vec3f(random.uniform(-3, 3), random.uniform(-4, -3), random.uniform(-20, -5))
			self.model_e.append(Model_entity(res, m_e_pos, random.uniform(0,1)))


	def update(self, params):
		for model in self.model_e:
			model.update()

	def draw(self, g, params):
		for model in self.model_e:
			model.draw(g, params)