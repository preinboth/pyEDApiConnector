import unittest

from connector.edsm.marketApi import market


class TestEdsmMarketApi(unittest.TestCase):
    def test_get_market_by_name(self):
        json = market.getMarketByName('Honoto', 'Morelli Synthetics Exchange')
        if not json:
            self.fail("Not Data found")

    def test_get_market_by_id(self):
        json = market.getMarketById(9324, 3928035072)
        if not json:
            self.fail("Not Data found")


if __name__ == '__main__':
    unittest.main()
