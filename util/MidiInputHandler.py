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

		self.app.sm.trigger(message, self.params)