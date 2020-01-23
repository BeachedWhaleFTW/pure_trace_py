import math


class Vec3:
    """implements a vector of size 3. Components to be passed as floats."""

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def magnitude(self):
        return math.sqrt(self.dot_product(self))

    def normalize(self):
        mag = self.magnitude()

        return Vec3(self.x / mag, self.y / mag, self.z / mag)

    def dot_product(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vec3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __truediv__(self, divisor):
        return Vec3(self.x / divisor, self.y / divisor, self.z / divisor)
