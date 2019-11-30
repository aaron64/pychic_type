import pyglet
import loader as loader
import util.color as color
from util.Graphics import Graphics
from util.Params import Params
from util.SceneContainer import SceneContainer
from util.SceneManager import SceneManager

from util.MidiInputHandler import MidiInputHandler

from pyglet.gl import *

import rtmidi.midiutil as midiutil
import sys

class main(pyglet.window.Window):
	def __init__(self):
		#super(main, self).__init__(1920, 1080, fullscreen = True)
		super(main, self).__init__(600,400)
		self.alive = True

		color.init_colors()
		self.params = Params()
		self.g = Graphics(self.params)
		
		# Setup Midi device to read from
		port = sys.argv[1] if len(sys.argv) > 1 else None
		midiin, port_name = midiutil.open_midiinput(port)
		midiin.set_callback(MidiInputHandler(port_name, self))

		self.sm = SceneManager()

		loader.init_scenes(self.sm, self.params, self.g)
			
		pyglet.clock.schedule(self.run)
		pyglet.app.run()

	def on_draw(self):
		self.draw()

	def on_close(self):
		pyglet.app.exit()
		self.alive = 0

		
	def run(self, dx):
		self.g.begin_drawing(self)
		self.update()
		self.draw()
		self.g.finish_drawing(self)

	def update(self):
		self.params.frame_count += 1
		self.sm.update_scenes(self.params)

	def draw(self):
		self.g.main_batch.draw()
		self.sm.draw_scenes(self.params, self.g)

x = main()
