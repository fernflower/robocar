import motors


class CarControl(object):
    def __init__(self):
        self.left_motors, self.right_motors = motors.init_motors()

    def backward(self):
        self.left_motors.backward()
        self.right_motors.backward()

    def forward(self):
        self.left_motors.forward()
        self.right_motors.forward()

    def stop(self):
        self.left_motors.stop()
        self.right_motors.stop()

    def right(self):
        self.left_motors.forward()
        self.right_motors.stop()

    def left(self):
        self.left_motors.stop()
        self.right_motors.forward()
