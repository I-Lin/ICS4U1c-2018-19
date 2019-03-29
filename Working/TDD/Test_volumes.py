import unittest
import volumes


class Test_volumes(unittest.TestCase):

    def test_get_cube_vol_basic1(self):
        self.assertEqual(27, volumes.get_cube_vol(3))

    def test_get_cube_vol_basic2(self):
        self.assertEqual(64, volumes.get_cube_vol(4))

    def test_get_sphere_vol_basic3(self):
        self.assertEqual(4.18, volumes.get_sphere_vol(1))

    def test_get_cylinder_basic4(self):
        self.assertEqual(3.14, volumes.get_cylinder_vol(1, 1))
