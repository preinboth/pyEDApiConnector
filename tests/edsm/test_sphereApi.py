import unittest

from connector.edsm.sphereApi import sphere


class TestSphere(unittest.TestCase):
    def test_get_systems_sphere_by_system_name(self):
        json = sphere.getSystemsSphereBySystemName("sol", 0, 30)
        if not json:
            self.fail("Not Data found")
        system = json[0]
        self.assertEqual("Hyroks", system["name"])
        self.assertEqual(18795, system["id"])
        self.assertEqual(7230611002066, system["id64"])
        self.assertFalse(system["requirePermit"])
        self.assertTrue(system["coordsLocked"])

    def test_get_systems_sphere_by_coords(self):
        coords = {
            "x": 0,
            "y": 0,
            "z": 0,
        }
        json = sphere.getSystemsSphereByCoords(coords, 0, 30)
        if not json:
            self.fail("Not Data found")
        system = json[0]
        self.assertEqual("Hyroks", system["name"])
        self.assertEqual(18795, system["id"])
        self.assertEqual(7230611002066, system["id64"])
        self.assertFalse(system["requirePermit"])
        self.assertTrue(system["coordsLocked"])


if __name__ == "__main__":
    unittest.main()
