import pyglet
import util.color as color
from util.Graphics import Graphics
from util.Params import Params
from scenes.Bubbles import Bubbles
from scenes.Strobe import Strobe
from scenes.Parallax import Parallax
from scenes.BigText import BigText
from scenes.BigWord import BigWord
from scenes.Flash import Flash
from scenes.BackgroundColors import BackgroundColors
from scenes.BackgroundColor import BackgroundColor
from scenes.ImageLine import ImageLine
from scenes.ImageMove import ImageMove

from util.MidiInputHandler import MidiInputHandler

from pyglet.gl import *

import rtmidi.midiutil as midiutil
import sys

class main(pyglet.window.Window):
	def __init__(self):
		#super(main, self).__init__(1920, 1080, fullscreen = True)
		super(main, self).__init__(600,400)

		self.alive = True

		self.params = Params()
		color.init_colors()

		port = sys.argv[1] if len(sys.argv) > 1 else None
		midiin, port_name = midiutil.open_midiinput(port)
		midiin.set_callback(MidiInputHandler(port_name, self))

		self.g = Graphics(self.params)

		color.add_color("terq", [0, 255, 128, 255])
		color.add_color("blue", [37, 70, 240, 255])
		color.add_color("purple", [184, 20, 240, 255])

		self.scenes = []

		self.scenes.append(BackgroundColor("knob", 3, color.get_color("red")))
		self.scenes.append(BackgroundColor("knob", 7, color.get_color("blue")))
		# # #self.scenes.append(BackgroundColors("trigger", 44, colors=[color.get_color("terq"), color.get_color("blue"), color.get_color("purple")]))
		self.scenes.append(Strobe("hold", 48, speed=3))
		self.scenes.append(Parallax("hold", 45, "flower", self.g, self.params))
		self.scenes.append(BigText("trigger", 50, '''I I I I I do what I wanna wanna do wanna wanna do what I
		 											I I I I I do what I wanna wanna do what I what I want
		 											I I I do what I wanna wanna do wanna wanna do what I
		 											I do what I wanna wanna do I do what I like'''))

		self.scenes.append(Flash("trigger", 51))

		self.scenes.append(BigWord("hold", 60, "MAKE"))
		self.scenes.append(BigWord("hold", 61, "SOME"))
		self.scenes.append(BigWord("hold", 62, "NOISE"))

		self.scenes.append(ImageLine("hold", 44, "flower", self.g, self.params, 30, horizontal=False))
		self.scenes.append(ImageLine("hold", 44, "flower", self.g, self.params, 570, horizontal=False))
		self.scenes.append(ImageLine("hold", 44, "flower", self.g, self.params, 30, horizontal=True))
		self.scenes.append(ImageLine("hold", 44, "flower", self.g, self.params, 370, horizontal=True))

		self.scenes.append(ImageMove("knob", 8, "flower", self.g, 10, 10, 50, 50))
			
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
		for scene in self.scenes:
			scene.update(self.params)

	def draw(self):
		self.g.main_batch.draw()
		for scene in self.scenes:
			scene.draw(self.g, self.params)

x = main()
