import unittest

from src.connector.edsm.shipyardApi import shipyard


class TestShipyard(unittest.TestCase):
    def test_get_shipyard(self):
        json = shipyard.getShipyard('Gacrux', 'Ramanujan Terminal')
        # System
        assert json['id'] == 7564
        assert json['id64'] == 672028239289
        assert json['name'] == 'Gacrux'

        # Market
        assert json['marketId'] == 3228596736
        assert json['sId'] == 1644
        assert json['sName'] == "Ramanujan Terminal"

        # Ship

    def test_get_shipyard_by_id(self):
        json = shipyard.getShipyardById(7564, 3228596736)
        # System
        assert json['id'] == 7564
        assert json['id64'] == 672028239289
        assert json['name'] == 'Gacrux'

        # Market
        assert json['marketId'] == 3228596736
        assert json['sId'] == 1644
        assert json['sName'] == "Ramanujan Terminal"


if __name__ == '__main__':
    unittest.main()
