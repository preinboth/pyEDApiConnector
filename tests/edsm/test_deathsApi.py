import unittest

from EDApiConnector.connector.edsm.deathsApi import deaths


class TestEdsmDeaths(unittest.TestCase):
    def test_get_Deaths(self):
        json = deaths.getDeaths("Gacrux")
        if not json:
            self.fail("Not Data found")
        # System
        assert json["id"] == 7564
        assert json["id64"] == 672028239289
        assert json["name"] == "Gacrux"

    def test_get_Deaths_By_Id(self):
        json = deaths.getDeathsById(7564)
        if not json:
            self.fail("Not Data found")
        # System
        assert json["id"] == 7564
        assert json["id64"] == 672028239289
        assert json["name"] == "Gacrux"


if __name__ == "__main__":
    unittest.main()
