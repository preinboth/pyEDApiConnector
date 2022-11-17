import unittest

from connector.edsm.edsm_cntl import edsmCntl


class EdsmApiTests(unittest.TestCase):

    # Api System Station
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

    # Api System Bodies
    def test_get_bodies(self):
        json = edsmCntl.getBodies("HD 43193")
        # system data
        self.assertEqual(85920, json['id'])
        self.assertEqual("HD 43193", json['name'])
        # body count
        self.assertEqual(17, len(json['bodies']))
        # star
        star = json['bodies'][0]
        self.assertEqual(219074, star['id'])
        self.assertEqual("HD 43193 A", star['name'])
        self.assertEqual("Star", star['type'])
        self.assertEqual("B (Blue-White) Star", star['subType'])
        self.assertEqual(0, star['distanceToArrival'])
        self.assertTrue(star['isMainStar'])
        self.assertTrue(star['isScoopable'])
        self.assertFalse(star['rotationalPeriodTidallyLocked'])
        self.assertEqual(None, star['axialTilt'])

        # planet
        planet = json['bodies'][15]
        self.assertEqual(311417, planet['id'])
        self.assertEqual("HD 43193 CD 7 a", planet['name'])
        self.assertEqual("Planet", planet['type'])
        self.assertEqual("Class IV gas giant", planet['subType'])

        self.assertFalse(planet['isLandable'])
        self.assertEqual("No volcanism", planet['volcanismType'])
        self.assertEqual("No atmosphere", planet['atmosphereType'])
        self.assertEqual("Not terraformable", planet['terraformingState'])
        self.assertEqual(None, planet['orbitalEccentricity'])
        self.assertFalse(planet['rotationalPeriodTidallyLocked'])

    def test_get_bodies_by_id(self):
        json = edsmCntl.getBodiesById(85920)

        # system data
        self.assertEqual(85920, json['id'])
        self.assertEqual("HD 43193", json['name'])
        # body count
        self.assertEqual(17, len(json['bodies']))
        # star
        star = json['bodies'][0]
        self.assertEqual(219074, star['id'])
        self.assertEqual("HD 43193 A", star['name'])
        self.assertEqual("Star", star['type'])
        self.assertEqual("B (Blue-White) Star", star['subType'])
        self.assertEqual(0, star['distanceToArrival'])
        self.assertTrue(star['isMainStar'])
        self.assertTrue(star['isScoopable'])
        self.assertFalse(star['rotationalPeriodTidallyLocked'])
        self.assertEqual(None, star['axialTilt'])

        # planet
        planet = json['bodies'][15]
        self.assertEqual(311417, planet['id'])
        self.assertEqual("HD 43193 CD 7 a", planet['name'])
        self.assertEqual("Planet", planet['type'])
        self.assertEqual("Class IV gas giant", planet['subType'])

        self.assertFalse(planet['isLandable'])
        self.assertEqual("No volcanism", planet['volcanismType'])
        self.assertEqual("No atmosphere", planet['atmosphereType'])
        self.assertEqual("Not terraformable", planet['terraformingState'])
        self.assertEqual(None, planet['orbitalEccentricity'])
        self.assertFalse(planet['rotationalPeriodTidallyLocked'])

    def test_get_estimated_value(self):
        json = edsmCntl.getEstimatedValue("Sol")
        # system data
        self.assertEqual(27, json['id'])
        self.assertEqual("Sol", json['name'])

    def test_get_estimated_value_by_id(self):
        json = edsmCntl.getEstimatedValueById(27)
        # system data
        self.assertEqual(27, json['id'])
        self.assertEqual("Sol", json['name'])

    def test_get_market_by_name(self):
        json = edsmCntl.getMarketByName('Gacrux', 'Ramanujan Terminal')
        if not json:
            self.fail("Not Data found")
        # System
        assert json['id'] == 7564
        assert json['id64'] == 672028239289
        assert json['name'] == 'Gacrux'

        # Market
        assert json['marketId'] == 3228596736
        assert json['sId'] == 1644
        assert json['sName'] == "Ramanujan Terminal"

    def test_get_market_by_id(self):
        pass
        json = edsmCntl.getMarketById(7564, 3228596736)
        if not json:
            self.fail("Not Data found")
        # System
        assert json['id'] == 7564
        assert json['id64'] == 672028239289
        assert json['name'] == 'Gacrux'

        # Market
        assert json['marketId'] == 3228596736
        assert json['sId'] == 1644
        assert json['sName'] == "Ramanujan Terminal"

    def test_get_elite_server_status(self):
        json = edsmCntl.getEliteServerStatus()
        if not json:
            self.fail("Not Data found")


if __name__ == '__main__':
    unittest.main()
