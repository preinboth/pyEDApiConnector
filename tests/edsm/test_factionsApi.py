import unittest

from src.connector.edsm.factionsApi import factions


class TestEdsmFactions(unittest.TestCase):
    def test_get_faction(self):
        json = factions.getFaction("Gacrux", 1)
        if not json:
            self.fail("Not Data found")
        # System
        assert json['id'] == 7564
        assert json['id64'] == 672028239289
        assert json['name'] == 'Gacrux'

    def test_get_faction_by_id(self):
        json = factions.getFactionById(7564, 1)
        if not json:
            self.fail("Not Data found")
        # System
        assert json['id'] == 7564
        assert json['id64'] == 672028239289
        assert json['name'] == 'Gacrux'


if __name__ == '__main__':
    unittest.main()
