import nxt.locator
import nxt.motor

class Robot:
     def __init__(self, motor_ports, sensor_ports):

        self.address = None
        self.brick = None
        self.motor_a = None
        self.motor_b = None
        self.motor_c = None
        self.synchronised_motors = None
        self.find_brick()
        self.get_motors(motor_ports)

    def find_brick(self):
        self.brick = nxt.locator.find()

    def get_motors(self, motor_ports):
        self.motor_a = self.brick.get_motor(nxt.motor.Port.A)
        self.motor_b = self.brick.get_motor(nxt.motor.Port.B)
        self.motor_c = self.brick.get_motor(nxt.motor.Port.C)
        self.synchronised_motors = nxt.motor.SynchronizedMotors(motor_a, motor_b, 1)

    def move_forward():
        self.synchronised_motors.turn(power=100, tacho_units=720, brake=True, timeout=3)

    def move_backward():
        self.synchronised_motors.turn(power=-100, tacho_units=720, brake=True, timeout=3)

    def unroll():
        self.motor_c.turn(70, 360)

    def roll_up():
        self.motor_c.turn(-70, 360)
