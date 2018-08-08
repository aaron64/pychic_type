class Scene:
	def __init__(self, switch_type, key, state=False):
		self.switch_type = switch_type
		self.state = state
		self.key = key

	def update(self, params):
		pass

	def draw(self, g, params):
		pass

	def trigger(self, params):
		pass

	def toggle(self, params):
		self.state = not state

	def hold(self, params, state):
		print(state)
		self.state = state