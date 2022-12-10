import unittest

from EDApiConnector.connector.edsm.cubeApi import cube


class TestEdsmCube(unittest.TestCase):
    def test_get_systems_cube_by_system_name(self):
        json = cube.getSystemsCubeBySystemName("sol", 20)
        if not json:
            self.fail("Not Data found")
        system = json[0]
        self.assertEqual("Groombridge 34", system["name"])
        self.assertEqual(1410, system["id"])
        self.assertEqual(7267755828641, system["id64"])

    def test_get_systems_cube_by_coords(self):
        coords = {
            "x": 0,
            "y": 0,
            "z": 0,
        }
        json = cube.getSystemsCubeByCoords(coords, 20)
        if not json:
            self.fail("Not Data found")
        system = json[0]
        self.assertEqual("Groombridge 34", system["name"])
        self.assertEqual(1410, system["id"])
        self.assertEqual(7267755828641, system["id64"])


if __name__ == "__main__":
    unittest.main()
