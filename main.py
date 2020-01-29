from color import Color
from point import Point
from vec3 import Vec3
from sphere import Sphere
from scene import Scene
from engine import RenderEngine

WIDTH = 320
HEIGHT = 200


def main():
    camera = Vec3(0, 0, -1)
    objects = [Sphere(Point(0, 0, 0), 0.5, Color.from_hex("#FF0000"))]
    scene = Scene(camera, objects, WIDTH, HEIGHT)
    engine = RenderEngine()
    img = engine.render(scene)

    with open("sphere_test.ppm", 'w') as img_file:
        img.write_ppm(img_file)


if __name__ == "__main__":
    main()
