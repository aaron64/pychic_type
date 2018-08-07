import pyglet

import util.color as color


class Graphics:

	def __init__(self, params):
		self.window = pyglet.window.Window(width = params.width, height = params.height)
		self.main_batch = 0
		self.background = pyglet.graphics.OrderedGroup(0)
		self.foreground = pyglet.graphics.OrderedGroup(1)

	def begin_drawing(self):
		self.main_batch = pyglet.graphics.Batch()

	def render_to_window(self):
		self.main_batch.draw()

	def fill_rect(self, x, y, w, h, col):
		self.main_batch.add(4, 
			pyglet.gl.GL_QUADS, 
			None, 
			('v2i',[x, y, x + w, y, x + w, y + h, x, y + h]), ('c4B', col))