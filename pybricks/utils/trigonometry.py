from utils.angle_utils import Angle_Utils
from utils.point import Point
import umath as math


# Angle -> degrees counter clockwise
# Degrees -> degrees clockwise


class Trigonometry:
    # d1 = Direction 1
    def calc_diff(degrees1: float, degrees2: float):
        r1 = degrees2 - degrees1
        r2 = degrees2 - degrees1 - 360
        r3 = degrees2 - degrees1 + 360
        return min(r1, r2, r3, key=lambda r: abs(r))

    def calc_mid(degrees1: float, degrees2: float):
        diff = Trigonometry.calc_diff(degrees1, degrees2)
        return (max(degrees1, degrees2) - (diff / 2)) % 360

    def degrees_from_points(point1: Point, point2: Point):
        vx, vy = point1.to_vector(point2)

        radians = math.atan2(vy, vx)
        angle = math.degrees(radians)

        print(f"degrees_from_points -> {angle} => {Angle_Utils.convert_degrees(angle)}")

        return Angle_Utils.convert_degrees(angle)

    def calc_side_dist(magnitude, degrees_between_vectors): # How far are we off course
        angle = Angle_Utils.convert_degrees(degrees_between_vectors)
        unit_distance = -math.sin(angle)
        return unit_distance * magnitude
