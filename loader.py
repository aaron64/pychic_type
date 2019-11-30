import util.color as color
from util.vec2f import vec2f
from util.vec3f import vec3f

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
from scenes.Video import Video
from scenes.Model import Model
from scenes.ModelRiser import ModelRiser

def init_scenes(sm, params, g):
	sm.add_scene(Model("TRIGGER", 64, "xmas_tree", vec3f(0.0, 0.0, 0.0)))
	sm.add_scene(Model("TRIGGER", 64, "xmas_tree", vec3f(2.0, 0.0, 0.0)))
	# sm.add_scene(BackgroundColor("KNOB", 3, color.get_color("red")))
	# sm.add_scene(BackgroundColor("KNOB", 7, color.get_color("blue")))
	# # sm.add_scene(BackgroundColors("trigger", 44, colors=[color.get_color("terq"), color.get_color("blue"), color.get_color("purple")]))
	# # sm.add_scene(Video("HOLD", 63, "DUBPLATE.mp4", g, vec2f(0,0)))
	# sm.add_scene(Strobe("HOLD", 48, speed=3))
	# sm.add_scene(Parallax("HOLD", 45, g, params, "flower"))
	# sm.add_scene(BigText("TRIGGER", 50, '''I I I I I do what I wanna wanna do wanna wanna do what I
	#  											I I I I I do what I wanna wanna do what I what I want
	#  											I I I do what I wanna wanna do wanna wanna do what I
	#  											I do what I wanna wanna do I do what I like'''))

	# sm.add_scene(Flash("TRIGGER", 51))

	# sm.add_scene(BigWord("HOLD", 60, "MAKE"))
	# sm.add_scene(BigWord("HOLD", 61, "SOME"))
	# sm.add_scene(BigWord("HOLD", 62, "NOISE"))

	# sm.add_scene(ImageLine("HOLD", 44, g, params, "flower", 30, horizontal=False))
	# sm.add_scene(ImageLine("HOLD", 44, g, params, "flower", 570, horizontal=False))
	# sm.add_scene(ImageLine("HOLD", 44, g, params, "flower", 30, horizontal=True))
	# sm.add_scene(ImageLine("HOLD", 44, g, params, "flower", 370, horizontal=True))

	# sm.add_scene(ImageMove("KNOB", 8, g, "flower", vec2f(10,10), vec2f(50,50)))



"""
Scenes:

BackgroundColor		|	Single background color
BackgroundColors	|	Multiple background colors
BigText				|	Big text that switches words each trigger
BigWord				|	Single big word
Bubbles				|	Moves images upward in a "bubble" fashion
Flash				|	Single bright flash that fades
Float				|	# Same as ImageShake???
Image				|	Single image to display
ImageBurst			|	Burst of images
ImageLine			|	Single line of images that moves
ImageMove			|	An image that moves between two points
ImageShake			|	An image that follows circular motion
Parallax			|	a 2D grid of images that moves in a certian direction
Strobe				|	Strobe light
Video				|	Video stream
"""
