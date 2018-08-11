class Scene:
	def __init__(self, switch_type, key, visible=False):
		self.switch_type = switch_type
		self.visible = visible
		self.key = key

	def update(self, params):
		pass

	def draw(self, g, params):
		pass

	def trigger(self, params):
		pass

	def toggle(self, params):
		self.visible = not visible

	def hold(self, params, visible):
		self.visible = visible

	def knob(self, params, val):
		pass
