from image import Image
from color import Color
from point import Point
from sphere import Sphere

WIDTH = 2560
HEIGHT = 1600
CAMERA = Point(0, 0, -1)
BLACK = Point(0, 0, 0)
RED = Color(1, 0, 0)


def create_background(img, color):
    for i in range(img.width):
        for j in range(img.height):
            img.set_pixel(i, j, color)

    return 1


def main():
    img = Image(WIDTH, HEIGHT)
    create_background(img, BLACK)

    sphere = Sphere(Point(0, 0, 0), 0.5, RED)


    with open("rad_gradient_test.ppm", 'w') as img_file:
        img.write_ppm(img_file)


if __name__ == "__main__":
    main()
