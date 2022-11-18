import unittest

from src.connector.edsm.stationApi import station


class TestSystemStation(unittest.TestCase):
    def test_get_station(self):
        excludes = ["Fleet Carrier", "Odyssey Settlement"]
        json = station.getStation("Gacrux", excludes)
        # System
        assert json['id'] == 7564
        assert json['id64'] == 672028239289
        assert json['name'] == 'Gacrux'
        # TODO: Stations checken

    def test_get_station_by_id(self):
        json = station.getStationById(9324, "Fleet Carrier")
        assert json['id'] == 9324
        assert json['id64'] == 2871051494841
        assert json['name'] == 'Honoto'


if __name__ == '__main__':
    unittest.main()
