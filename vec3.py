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

    def dot_product(self, vec2):
        sum = 0
        for i, c in enumerate(self.components):
            sum += (c * vec2.components[i])

        return sum
    
