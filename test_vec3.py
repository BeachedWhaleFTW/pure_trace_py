import unittest
from vec3 import Vec3


class TestVec3(unittest.TestCase):
    def setUp(self):
        self.v1 = Vec3(1, -2, -2)
        self.v2 = Vec3(3, 6, 9)

    def test_magnitude(self):
        self.assertEqual(self.v1.magnitude(), 3)

    def test_normalize(self):
        v1_normal = self.v1.normalize()
        self.assertEqual(getattr(v1_normal, "x"), 1/3.)

    def test_dot_product(self):
        self.assertEqual(self.v1.dot_product(self.v2), -27)

    def test_add(self):
        sum_v1_v2 = self.v1 + self.v2
        self.assertEqual(getattr(sum_v1_v2, "x"), 4.)

    def test_sub(self):
        diff_v1_v2 = self.v1 - self.v2
        self.assertEqual(getattr(diff_v1_v2, "x"), -2.)

    def test_mul(self):
        prod_v1_2 = self.v1 * -2
        self.assertEqual(getattr(prod_v1_2, "x"), -2.)

    def test_div(self):
        quot_v1_1 = self.v1 / -1
        self.assertEqual(getattr(quot_v1_1, "x"), -1.)
    

if __name__ == '__main__':
    unittest.main()
