import math

class Vec3():
    """implements a vector of size 3. Components to be passed as floats."""
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def magnitude(self):
        radicand = (self.x ** 2) + (self.y ** 2) + (self.z ** 2)

        return math.sqrt(radicand)

    def normalize(self):
        normal_v_l = []
        magnitude = self.magnitude()
        for c in self.components:
            normal_v_l.append(c / magnitude)

        return Vect(normal_v_l)

    def dot_product(self, vec2):
        sum = 0
        for i, c in enumerate(self.components):
            sum += (c * vec2.components[i])

        return sum

    def __add__(self, vec2):
        out_components = []
        for i, c1 in enumerate(self.components):
            out_components.append(c1 + vec2.components[i])

        return Vect(out_components)
    
    def __sub__(self, vec2):
        out_components = []
        for i, c1 in enumerate(self.components):
            out_components.append(c1 - vec2.components[i])

        return Vect(out_components)

    def __mul__(self, scalar):
        out_components = []
        for c in self.components:
            out_components.append(c * scalar)

        return Vect(out_components)

    def __truediv__(self, divisor):
        out_components = []
        for c in self.components:
            out_components.append(c / divisor)

        return Vect(out_components)
