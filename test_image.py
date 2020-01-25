import unittest
from image import Image
from color import Color


class TestImage(unittest.TestCase):
    def setUp(self):
        with open("test.ppm") as f:
            self.img_data = f.read()

        self.img0 = Image(3, 2)

        red = Color(1, 0, 0)
        green = Color(0, 1, 0)
        blue = Color(0, 0, 1)

        self.img0.set_pixel(0, 0, red)
        self.img0.set_pixel(1, 0, green)
        self.img0.set_pixel(2, 0, blue)

        self.img0.set_pixel(0, 1, red + green)
        self.img0.set_pixel(1, 1, red + green + blue)
        self.img0.set_pixel(2, 1, red * 0.001)

    def test_set_pixel(self):

        self.assertEqual(type(self.img0.pixels), type([]))
        self.assertEqual(type(self.img0.pixels[0]), type([]))
        self.assertEqual(getattr(self.img0.pixels[0][0], "x"), 1)
        self.assertEqual(getattr(self.img0.pixels[1][2], "x"), 0.001)

    def test_save_to_ppm(self):
        with open("test1.ppm", "w") as img_file:
            self.img0.write_ppm(img_file)

        with open("test1.ppm") as f:
            img0_data = f.read()

        self.assertEqual(img0_data, self.img_data)


if __name__ == "__main__":
    unittest.main()

