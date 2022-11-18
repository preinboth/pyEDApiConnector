import unittest

from connector.edsm.outfittingApi import outfitting


class TestCmdrRanks(unittest.TestCase):
    def test_get_outfitting_by_name(self):
        json = outfitting.getOutfittingByName("Gacrux", "Ramanujan Terminal")
        if not json:
            self.fail("Not Data found")
        # System
        assert json['id'] == 7564
        assert json['id64'] == 672028239289
        assert json['name'] == 'Gacrux'

    def test_get_outfitting_by_id(self):
        json = outfitting.getOutfittingById(7564, 3228596736)
        if not json:
            self.fail("Not Data found")
        # System
        assert json['id'] == 7564
        assert json['id64'] == 672028239289
        assert json['name'] == 'Gacrux'


if __name__ == '__main__':
    unittest.main()
