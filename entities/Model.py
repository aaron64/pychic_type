from util.ModelLoader import ModelLoader
from entities.Entity import Entity
import util.color as color

from pyglet.gl import *

class Model(Entity):
	def __init__(self, res, pos, rot=0.0, color=None):
		super().__init__(pos)
		self.model_l = ModelLoader(res)
		self.rot = rot
		self.color = color

	def update(self):
		self.model_l.rotate(self.rot)
		self.model_l.translate(self.pos)

	def rotate(self, r):
		self.rot += r

	def translate(self, p):
		self.pos += p

	def draw(self, g, params):
		self.model_l.verts.draw(GL_TRIANGLES)
		# g.main_batch.add(len(self.model_l.mesh.vertex_index)//3, 
		# 	GL_TRIANGLES, 
		# 	g.background, 
		# 	('v3f',self.model_l.mesh.model_vertices), ('c4B', self.model_l.mesh.model_textures))
		#g.model_batch.append(self.model_l.mesh.vertex_index)
		#glDrawArrays(GL_TRIANGLES, 0, len())