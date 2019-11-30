from scenes.Scene import Scene
from entities.Model import Model as Model_entity

from util.vec3f import vec3f

class Model(Scene):

	def __init__(self, switch_type, key, res, pos, rot=0.0):
		super().__init__(switch_type, key)
		self.model_e = Model_entity(res, pos, rot)

	def update(self, params):
		self.model_e.update()

	def draw(self, g, params):
		self.model_e.draw(g,params)