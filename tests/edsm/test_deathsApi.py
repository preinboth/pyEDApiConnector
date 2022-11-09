import unittest

from connector.edsm.deathsApi import deaths


class TestEdsmDeaths(unittest.TestCase):
    def test_get_system_deaths_by_system_name(self):
        json = deaths.getSystemDeathsBySystemName('Sol')
        if not json:
            self.fail("Not Data found")

    def test_get_system_deaths_by_system_id(self):
        json = deaths.getSystemDeathsBySystemId(27)
        if not json:
            self.fail("Not Data found")


if __name__ == '__main__':
    unittest.main()
