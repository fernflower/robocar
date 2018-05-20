import machine


# D0 = GPIO16;
# D1 = GPIO5;
# D2 = GPIO4;
# D3 = GPIO0;
# D4 = GPIO2;
# D5 = GPIO14;
# D6 = GPIO12;
# D7 = GPIO13;
# D8 = GPIO15;
# D9 = GPIO3;
# D10 = GPIO1;

# D1 - motor A speed (pwm)
# D3 - motor A direction
# D2 - motor B speed (pwm)
# D4 - motor B direction
MOTOR_L = {'direction': 0, 'speed': 5}
MOTOR_R = {'direction': 2, 'speed': 4}


class Motor(object):
    def __init__(self, direction, speed, freq=500, duty=128):
        self.direction_pin = machine.Pin(direction, machine.Pin.OUT)
        self.speed_pin = machine.Pin(speed, machine.Pin.OUT)
        # XXX FIXME figure out how to change speed with pwm
        # self._pwm = machine.PWM(self.speed_pin, freq=freq, duty=duty)

    def forward(self):
        self.direction_pin.on()
        self.speed_pin.off()

    def stop(self):
        self.direction_pin.off()
        self.speed_pin.off()

    def backward(self):
        self.direction_pin.off()
        self.speed_pin.on()


def init_motors():
    left = Motor(**MOTOR_L)
    right = Motor(**MOTOR_R)
    return (left, right)


def main():
    return init_motors()


if __name__ == "__main__":
    main()
