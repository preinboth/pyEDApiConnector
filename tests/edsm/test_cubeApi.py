import unittest

from connector.edsm.cubeApi import cube


class TestEdsmCube(unittest.TestCase):
    def test_get_systems_cube_by_system_name(self):
        json = cube.getSystemsCubeBySystemName('sol', 20)
        if not json:
            self.fail("Not Data found")

    def test_get_systems_cube_by_coords(self):
        coords = {
            'x': 0,
            'y': 0,
            'z': 0,
        }
        json = cube.getSystemsCubeByCoords(coords, 100)
        if not json:
            self.fail("Not Data found")


if __name__ == '__main__':
    unittest.main()
