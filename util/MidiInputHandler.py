import time

class MidiInputHandler(object):
	def __init__(self, port, app):
		self.app = app
		self.port = port
		self._wallclock = time.time()
		self.params = app.params

	def __call__(self, event, data=None):
		message, deltatime = event
		self._wallclock += deltatime

		print(message)
		vel = message[0]
		key = message[1]
		state = message[2]

		for scene in self.app.scenes:
			if(scene.key == key):
				if(scene.switch_type == "trigger" and state != 0 ):
					scene.trigger(self.params)
				if(scene.switch_type == "toggle" and state != 0):
					scene.toggle(self.params)
				if(scene.switch_type == "hold"):
					scene.hold(self.params, state > 0)
				if(scene.switch_type == "knob"):
					scene.knob(self.params, state)