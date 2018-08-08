colors = {}

def add_color(name, col):
	colors[name] = col*4

def get_color(name):
	return colors[name]




def interpolate(col1, col2, val):
	val /= 255
	R = (col2[0] - col1[0]) * val + col1[0]
	G = (col2[1] - col1[1]) * val + col1[1]
	B = (col2[2] - col1[2]) * val + col1[2]
	A = (col2[3] - col1[3]) * val + col1[3]
	return [R,G,B,A] * 4


add_color("white", [255,255,255,255])
add_color("black", [0,0,0,255])
add_color("red", [255,0,0,255])
add_color("green", [0,255,0,255])
add_color("blue", [0,0,255,255])
add_color("transparent", [255,255,255,0])