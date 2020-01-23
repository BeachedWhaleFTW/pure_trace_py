import math

class Vec3():
    """implements a vector of size 3. Components to be passed as floats."""
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def magnitude(self):
        return math.sqrt(self.dot_product(self))

    def normalize(self):
        mag = self.magnitude()

        return Vec3(self.x/mag, self.y/mag, self.z/mag)

    def dot_product(self, vec2):
        dp = (self.x * vec2.x) + (self.y * vec2.y) + (self.z * vec2.z)

        return dp

    def __add__(self, vec2):
        return Vec3(self.x + vec2.x, self.y + vec2.y, self.z + vec2.z)
    
    def __sub__(self, vec2):
        return Vec3(self.x - vec2.x, self.y - vec2.y, self.z - vec2.z)

    def __mul__(self, scalar):
        return Vec3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __truediv__(self, divisor):
        return Vec3(self.x / divisor, self.y / divisor, self.z / divisor)
