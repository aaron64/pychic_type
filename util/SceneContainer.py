
class SceneContainer():
	def __init__(self, id):
		self.id = id
		self.scenes = []

	def add(self, scene):
		self.scenes.append(scene)