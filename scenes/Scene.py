class Scene:
	def __init__(self, switch_type, key inverse=False):
		self.switch_type = switch_type
		self.visible = not inverse
		self.inverse = inverse
		self.key = key

		if(self.switch_type == "trigger" or self.switch_type == "knob"):
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
		self.visible = visible not inverse

	def knob(self, params, val):
		pass
