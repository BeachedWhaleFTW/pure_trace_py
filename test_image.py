import unittest
from image import Image


class TestImage(unittest.TestCase):
    def setUp(self):
        with open("test.ppm") as f:
            self.img_data = f.read()

        args0 = {"size": (3, 2),
                 "max_color_val": 255
                 }
        self.img0 = Image(args0)

    def test_save_to_ppm(self):
        self.img0.save_to_ppm("test1.ppm")
        with open("test1.ppm") as f:
            img0_data = f.read()

        self.assertEqual(img0_data, self.img_data)


if __name__ == "__main__":
    unittest.main()

