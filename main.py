import pyglet
import util.color as color
from util.Graphics import Graphics
from util.Params import Params
from scenes.Bubbles import Bubbles
from scenes.Strobe import Strobe
from scenes.Parallax import Parallax
from scenes.BigText import BigText

from util.MidiInputHandler import MidiInputHandler

import rtmidi.midiutil as midiutil
import sys

class App:
	def __init__(self):
		port = sys.argv[1] if len(sys.argv) > 1 else None
		midiin, port_name = midiutil.open_midiinput(port)
		midiin.set_callback(MidiInputHandler(port_name, self))

		self.params = Params()
		self.g = Graphics(self.params)

		self.scenes = []
		self.scenes.append(Strobe("hold", 48, color=color.WHITE, speed=30))


		@self.g.window.event
		def on_draw():
			self.g.render_to_window()

		pyglet.clock.schedule(self.run)
		pyglet.app.run()

		

		#pyxel.init(160, 120)
		#self.scenes.append(Parallax(pyxel, "hold", 50, "flower"))
		#self.scenes.append(Bubbles(pyxel, "trigger", 44))
	

		#pyxel.run(self.update, self.draw)

	def run(self, dt):
			self.g.begin_drawing()

			self.update()
			self.draw()

	def update(self):
		for scene in self.scenes:
			scene.update(self.params)

	def draw(self):
		for scene in self.scenes:
			scene.draw(self.g, self.params)

App()
