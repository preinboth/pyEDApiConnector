import unittest

from EDApiConnector.connector.edsm.marketApi import market


class TestEdsmMarketApi(unittest.TestCase):
    def test_get_market_by_name(self):
        json = market.getMarketByName("Gacrux", "Ramanujan Terminal")
        if not json:
            self.fail("Not Data found")
        # System
        assert json["id"] == 7564
        assert json["id64"] == 672028239289
        assert json["name"] == "Gacrux"

        # Market
        assert json["marketId"] == 3228596736
        assert json["sId"] == 1644
        assert json["sName"] == "Ramanujan Terminal"

    def test_get_market_by_id(self):
        json = market.getMarketById(7564, 3228596736)
        if not json:
            self.fail("Not Data found")
        # System
        assert json["id"] == 7564
        assert json["id64"] == 672028239289
        assert json["name"] == "Gacrux"

        # Market
        assert json["marketId"] == 3228596736
        assert json["sId"] == 1644
        assert json["sName"] == "Ramanujan Terminal"


if __name__ == "__main__":
    unittest.main()
