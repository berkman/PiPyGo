class Car(object):
	steering_direction = None
	motor_direction = None
	#pedal_engaged = False
	#steering_engaged = False

	STEERING_DIRECTIONS = ['LEFT', 'RIGHT', 'NONE']
	MOTOR_DIRECTIONS = ['FORWARD', 'REVERSE', 'NONE']
	#CAMERA_STATES = ['OFF', 'STREAM', 'PICTURE', 'VIDEO']
	#MUSIC_STATES = ['OFF', 'ON']

	def __init__(self, steering_direction='NONE', motor_direction='NONE'):
		self.steering_direction = steering_direction
		self.motor_direction = motor_direction

	def get_steering_direction(self):
		return self.steering_direction

	def get_motor_direction(self):
		return self.motor_direction

	#def get_pedal_engaged(self):
	#	return self.pedal_engaged

	#def get_steering_engaged(self):
	#	return self.steering_engaged

	def set_steering_direction(self, steering_direction):
		if steering_direction in self.STEERING_DIRECTIONS:
			self.steering_direction = steering_direction
		else:
			raise ValueError('Invalid Steering Direction')

	def set_motor_direction(self, motor_direction):
		if motor_direction in self.MOTOR_DIRECTIONS:
			self.motor_direction = motor_direction
		else:
			raise ValueError('Invalid Motor Direction')

	#def set_pedal_engaged(self, pedal_engaged):
	#	self.pedal_engaged = pedal_engaged

	#def set_steering_engaged(self, steering_engaged):
	#	self.steering_engaged = steering_engaged
