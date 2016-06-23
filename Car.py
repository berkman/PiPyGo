class Car(object):
	steering_direction = None
	motor_speed = None
	pedal_engaged = False
	steering_engaged = False

	STEERING_DIRECTIONS = ['CENTER', 'LEFT', 'RIGHT']
	MOTOR_SPEEDS = ['OFF', 'LOW', 'HIGH', 'REVERSE']
	CAMERA_STATES = ['OFF', 'STREAM', 'PICTURE', 'VIDEO']
	MUSIC_STATES = ['OFF', 'ON']

	def __init__(self, steering_direction='CENTER', motor_speed='OFF'):
		self.steering_direction = steering_direction
		self.motor_speed = motor_speed

	def get_steering_direction(self):
		return self.steering_direction

	def get_motor_speed(self):
		return self.motor_speed

	def get_pedal_engaged(self):
		return self.pedal_engaged

	def get_steering_engaged(self):
		return self.steering_engaged

	def set_steering_direction(self, steering_direction):
		if steering_direction in self.STEERING_DIRECTIONS:
			self.steering_direction = steering_direction
		else:
			raise ValueError('Invalid Steering Direction')

	def set_motor_speed(self, motor_speed):
		if motor_speed in self.MOTOR_SPEEDS:
			self.motor_speed = motor_speed
		else:
			raise ValueError('Invalid Motor Speed')

	def set_pedal_engaged(self, pedal_engaged):
		self.pedal_engaged = pedal_engaged

	def set_steering_engaged(self, steering_engaged):
		self.steering_engaged = steering_engaged

'''

steer (on/off, direction

gas pedal (on/off, speed)
'''
