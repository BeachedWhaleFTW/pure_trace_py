from math import sqrt


class Sphere:
    """Sphere is defined by a point and radius as well as color"""
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = color

    def intersects(self, ray):
        """Checks if ray intersects self. Returns distance to intersection or None"""
        sphere_to_ray = ray.origin - self.center
        b = 2 * ray.direction.dot_product(sphere_to_ray)
        c = sphere_to_ray.dot_product(sphere_to_ray) - self.radius * self.radius
        disc = b * b - 4 * c

        if disc >= 0:
            dist = (-b - sqrt(disc)) / 2
            if dist > 0:
                return dist
        return None
