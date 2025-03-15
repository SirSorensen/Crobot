from robot_eyes import RobotEyes
from robot_legs import RobotLegs
from pybricks.parameters import Port
from pybricks.hubs import PrimeHub


class Robot:
    def __init__(self):
        # Initialise Motors (wheels)
        self.legs : RobotLegs = RobotLegs(Port.B, Port.F)

        # Initialize & calibrate the sensors
        self.eyes : RobotEyes = RobotEyes(Port.A, Port.E)

        # Initialise PrimeHub
        self.prime_hub: PrimeHub = PrimeHub()
        self.prime_hub.speaker.volume(50)


