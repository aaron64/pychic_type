colors = {}

def add_color(name, col):
	colors[name] = col*4

def get_color(name):
	return colors[name]

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

WHITE = [255,255,255,255,
		255,255,255,255,
		255,255,255,255,
		255,255,255,255]