import unittest

from src.connector.edsm.systemsApi import systems


class Test_Systems(unittest.TestCase):
    def test_get_systems(self):
        json = systems.getSystems("Gacrux", "Achali")

        # System Achali
        system = json[0]
        self.assertEqual("Achali", system['name'])
        self.assertEqual(4532, system['id'])
        self.assertEqual(3657332462314, system['id64'])
        self.assertFalse(system['requirePermit'])
        self.assertTrue(system['information'])

        self.assertEqual("K (Yellow-Orange) Star", system['primaryStar']['type'])
        self.assertEqual("Achali", system['primaryStar']['name'])
        self.assertTrue(system['primaryStar']['isScoopable'])

        # System Gacrux
        system = json[1]
        self.assertEqual("Gacrux", system['name'])
        self.assertEqual(7564, system['id'])
        self.assertEqual(672028239289, system['id64'])
        self.assertFalse(system['requirePermit'])
        self.assertTrue(system['information'])

        self.assertEqual("M (Red giant) Star", system['primaryStar']['type'])
        self.assertEqual("Gacrux", system['primaryStar']['name'])
        self.assertTrue(system['primaryStar']['isScoopable'])


if __name__ == '__main__':
    unittest.main()
