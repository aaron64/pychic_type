class Scene:
	def __init__(self, switch_type, key, inverse=False):
		self.switch_type = switch_type.upper()
		self.visible = inverse
		self.inverse = inverse
		self.key = key

		if(self.switch_type == "TRIGGER" or self.switch_type == "KNOB"):
			self.visible = True

	def update(self, params):
		pass

	def draw(self, g, params):
		pass

	def trigger(self, params):
		pass

	def toggle(self, params):
		self.visible = not self.visible

	def hold(self, params, visible):
		self.visible = visible != self.inverse

	def knob(self, params, val):
		pass
