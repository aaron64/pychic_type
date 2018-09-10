import pyglet

import util.color as color


class Graphics:

	def __init__(self, params):
		self.main_batch = pyglet.graphics.Batch()
		self.background = pyglet.graphics.OrderedGroup(0)
		self.foreground = pyglet.graphics.OrderedGroup(1)
		pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
		pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

	def begin_drawing(self, window):
		window.clear()
		self.main_batch = pyglet.graphics.Batch()

	def finish_drawing(self, window):
		#self.main_batch.draw()
		#window.flip()
		event = window.dispatch_events()
		

	def fill_rect(self, x, y, w, h, col, render_group):
		self.main_batch.add(4, 
			pyglet.gl.GL_QUADS, 
			render_group, 
			('v2i',[x, y, x + w, y, x + w, y + h, x, y + h]), ('c4B', col))