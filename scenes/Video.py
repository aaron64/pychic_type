
from scenes.Scene import Scene

import pyglet

class Video(Scene):
	def __init__(self, switch_type, key, res, g, pos, s=1, restart=False):
		super().__init__(switch_type, key)
		self.player = pyglet.media.Player()
		self.video_source = pyglet.media.StreamingSource()
		self.video = pyglet.media.load('res/video/' + res)	
		self.pos = pos
		self.render_pos = pos

		self.restart = restart

		self.player.queue(self.video)
		self.player.volume = 0
		self.player.eos_action = pyglet.media.SourceGroup.loop
		self.player.play()

	def hold(self, params, visible):
		super().hold(params, visible)
		if(visible):
			self.player.seek(0.01)
		
	def draw(self, g, params):
		if(self.visible):
			g.add_batch_video(self.player.get_texture(), self.render_pos)