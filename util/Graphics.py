import pyglet
from pyglet.gl import *

import util.color as color


class Graphics:

	def __init__(self, params):
		self.video_batch = []
		self.model_batch = []

		self.main_batch = pyglet.graphics.Batch()
		self.background = pyglet.graphics.OrderedGroup(0)
		self.foreground = pyglet.graphics.OrderedGroup(1)
		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
		glEnable(GL_DEPTH_TEST)

	def begin_drawing(self, window):
		window.clear()

		glDrawArrays(GL_TRIANGLES, 0, len(self.model_batch))

		for video_texture in self.video_batch:
			video_texture['tex'].blit(video_texture['pos'].x, video_texture['pos'].y)

		self.main_batch = pyglet.graphics.Batch()

	def finish_drawing(self, window):
		#self.main_batch.draw()
		#window.flip()
		event = window.dispatch_events()
		self.video_batch = []

	def add_batch_video(self, texture, position):
		self.video_batch.append({'tex': texture, 'pos': position})
		

	def fill_rect(self, x, y, w, h, col, render_group):
		self.main_batch.add(4, 
			GL_QUADS, 
			render_group, 
			('v2i',[x, y, x + w, y, x + w, y + h, x, y + h]), ('c4B', col))