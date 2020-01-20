import math

class Vect():
    """implements a vector of n size where n is the len(components).
Components to be passed as an array [c1, c2, c3, ..., cn] of numerics."""
    def __init__(self, components):
        self.components = components
        self.size = len(components)

    def magnitude(self):
        radicand = 0
        for c in self.components:
            radicand += (c ** 2)

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
    
