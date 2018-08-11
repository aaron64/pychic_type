import copy
import math

colors = {}

def add_color(name, col):
	colors[name] = col*4

def get_color(name):
	return copy.deepcopy(colors[name])

def convert_to_4(col):
	return [col[0],col[1],col[2],col[3]]

def set_red(col, red):
	col[0] = red
	col[4] = red
	col[8] = red
	col[12] = red
	return col

def set_green(col, green):
	col[1] = green
	col[5] = green
	col[9] = green
	col[13] = green
	return col

def set_blue(col, blue):
	col[2] = blue
	col[6] = blue
	col[10] = blue
	col[14] = blue
	return col

def set_opacity(col, opacity):
	col[3] = opacity
	col[7] = opacity
	col[11] = opacity
	col[15] = opacity
	return col

def interpolate(col1, col2, val):
	val /= 127
	R = math.floor((col2[0] - col1[0]) * val + col1[0])
	G = math.floor((col2[1] - col1[1]) * val + col1[1])
	B = math.floor((col2[2] - col1[2]) * val + col1[2])
	A = math.floor((col2[3] - col1[3]) * val + col1[3])
	return [R,G,B,A] * 4

def init_colors():
	add_color("white", [255,255,255,255])
	add_color("black", [0,0,0,255])
	add_color("red", [255,0,0,255])
	add_color("green", [0,255,0,255])
	add_color("blue", [0,0,255,255])
	add_color("transparent", [255,255,255,0])
