import unittest
from vec3 import Vec3


class TestVec3(unittest.TestCase):
    def setUp(self):
        self.v1 = Vec3(1., -2., -2.)
        self.v2 = Vec3(3., 6., 9.)

    def test_magnitude(self):
        self.assertEqual(self.v1.magnitude(), 3.)

    def test_normalize(self):
        v1_mag = 3
        v1_normal = self.v1.normalize()
        normal_comp = [v1_normal.x, v1_normal.y, v1_normal.z]
        self.assertEqual(normal_comp, [1/3., -2/3., -2/3.])

    def test_dot_product(self):
        self.assertEqual(self.v1.dot_product(self.v2), -27)

    def test_add(self):
        v1_2 = self.v1 + self.v2
        v1_2_comp = [v1_2.x, v1_2.y, v1_2.z]
        self.assertEqual(v1_2_comp, [4., 4., 7.])

    def test_sub(self):
        v1_2 = self.v1 - self.v2
        v1_2_comp = [v1_2.x, v1_2.y, v1_2.z]
        self.assertEqual(v1_2_comp, [-2., -8., -11])

    def test_mul(self):
        v1_2 = self.v1 * -2
        v1_2_comp = [v1_2.x, v1_2.y, v1_2.z]
        self.assertEqual(v1_2_comp, [-2., 4., 4.])

    def test_div(self):
        v1_2 = self.v1 / -1
        v1_2_comp = [v1_2.x, v1_2.y, v1_2.z]
        self.assertEqual(v1_2_comp, [-1., 2., 2.])
    

if __name__ == '__main__':
    unittest.main()
