import pyglet
import util.color as color
from util.Graphics import Graphics
from util.Params import Params
from scenes.Bubbles import Bubbles
from scenes.Strobe import Strobe
from scenes.Parallax import Parallax
from scenes.BigText import BigText
from scenes.BackgroundColors import BackgroundColors

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

		color.add_color("blue", [37, 70, 240, 255])
		color.add_color("purple", [184, 20, 240, 255])

		self.scenes = []
		self.scenes.append(BackgroundColors("trigger", 52, colors=[color.get_color("blue"), color.get_color("purple")]))
		self.scenes.append(Strobe("hold", 48, color=color.get_color("white"), speed=30))
		self.scenes.append(Parallax("hold", 50, "flower"))
		self.scenes.append(BigText("trigger", 54, "hello world"))

		@self.g.window.event
		def on_draw():
			self.g.render_to_window()
			
		pyglet.clock.schedule(self.run)
		pyglet.app.run()

		
		#self.scenes.append(Bubbles(pyxel, "trigger", 44))

	def run(self, dt):
			self.g.begin_drawing()
			self.update()
			self.draw()

	def update(self):
		self.params.frame_count += 1
		for scene in self.scenes:
			scene.update(self.params)

	def draw(self):
		self.g.window.clear()

		for scene in self.scenes:
			scene.draw(self.g, self.params)

App()
