import unittest

from connector.edsm.sphereApi import sphere


class TestSphere(unittest.TestCase):
    def test_get_systems_sphere_by_system_name(self):
        json = sphere.getSystemsSphereBySystemName('sol', 20, 50)
        if not json:
            self.fail("Not Data found")

    def test_get_systems_sphere_by_coords(self):
        coords = {
            'x': 0,
            'y': 0,
            'z': 0,
        }
        json = sphere.getSystemsSphereByCoords(coords, 20, 50)
        if not json:
            self.fail("Not Data found")


if __name__ == '__main__':
    unittest.main()
