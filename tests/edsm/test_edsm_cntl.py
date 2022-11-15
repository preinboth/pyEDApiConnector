import unittest

from connector.edsm.edsm_cntl import edsmCntl


class EdsmApiTests(unittest.TestCase):
    def test_getStation(self):
        json = edsmCntl.getStation("Gacrux")
        # System
        assert json['id'] == 7564
        assert json['id64'] == 672028239289
        assert json['name'] == 'Gacrux'
        # TODO: Stations checken

    def test_get_station_by_id(self):
        json = edsmCntl.getStationById(9324)
        assert json['id'] == 9324
        assert json['id64'] == 2871051494841
        assert json['name'] == 'Honoto'

if __name__ == '__main__':
    unittest.main()
