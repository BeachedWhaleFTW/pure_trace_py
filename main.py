from image import Image
from color import Color

WIDTH = 2560
HEIGHT = 1600
BLUE = Color(0, 0, 1)
WHITE = Color(1, 1, 1)


def main():
    img = Image(WIDTH, HEIGHT)
    for i in range(WIDTH):
        for j in range(HEIGHT):
            color = Color(i / WIDTH, j / HEIGHT, 1)
            img.set_pixel(i, j, color)

    with open("gradient_test.ppm", 'w') as img_file:
        img.write_ppm(img_file)


if __name__ == "__main__":
    main()
