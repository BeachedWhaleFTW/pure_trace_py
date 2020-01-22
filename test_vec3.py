import unittest
from vec3 import Vec3


class TestVec3(unittest.TestCase):
    def setUp(self):
        self.v1 = Vec3(1., -2., -2.)

    def test_magnitude(self):
        self.assertEqual(self.v1.magnitude(), 3.)
    

if __name__ == '__main__':
    unittest.main()
