from util.SceneContainer import SceneContainer

class SceneManager:
	def __init__(self):
		self.sc = []
		self.sc.append(SceneContainer(0))

		self.loading_container = 0
		self.current_container = 0
		self.containers = 1

	def update_scenes(self, params):
		container = self.sc[self.current_container]
		for scene in container.scenes:
			scene.update(params)

	def draw_scenes(self, params, g):
		container = self.sc[self.current_container]
		for scene in container.scenes:
			scene.draw(g, params)

	def trigger(self, message, params):
		vel = message[0]
		key = message[1]
		state = message[2]

		for scene in self.sc[self.current_container].scenes:
			if(scene.key == key):
				if(scene.switch_type == "TRIGGER" and state != 0 ):
					scene.trigger(params)
				if(scene.switch_type == "TOGGLE" and state != 0):
					scene.toggle(params)
				if(scene.switch_type == "HOLD"):
					scene.hold(params, state > 0)
				if(scene.switch_type == "KNOB"):
					scene.knob(params, state/127)

	def new_scene_container(self):
		self.sc.append(SceneContainer(self.containers))
		self.loading_container = self.containers
		self.containers += 1

	def add_scene(self, scene):
		self.sc[self.loading_container].add(scene)