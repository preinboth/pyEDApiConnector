import unittest

from src.connector.edsm.trafficApi import traffic


class TestEdsmTraffic(unittest.TestCase):
    def test_get_traffic_system(self):
        json = traffic.getTrafficSystem("Gacrux")
        # System
        assert json['id'] == 7564
        assert json['id64'] == 672028239289
        assert json['name'] == 'Gacrux'

    def test_get_traffic_by_id(self):
        json = traffic.getTrafficById(7564)
        # System
        assert json['id'] == 7564
        assert json['id64'] == 672028239289
        assert json['name'] == 'Gacrux'


if __name__ == '__main__':
    unittest.main()
