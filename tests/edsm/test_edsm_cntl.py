import unittest

from connector.edsm.edsm_cntl import EdsmCntl


class EdsmApiTests(unittest.TestCase):

    def test_getBodies_HD43193(self):
        edsmCntl = EdsmCntl()
        json = edsmCntl.getBodies("HD 43193")
        # system data
        assert json['id'] == 85920
        assert json['name'] == "HD 43193"

        # body count
        assert len(json['bodies']) == 17

        # star
        star = json['bodies'][0]
        assert star['id'] == 219074
        assert star['name'] == "HD 43193 A"
        assert star['type'] == "Star"
        assert star['subType'] == "B (Blue-White) Star"
        assert star['distanceToArrival'] == 0
        assert star['isMainStar'] == True
        assert star['isScoopable'] == True
        assert star['age'] == 760
        assert star['luminosity'] == "V"
        assert star['absoluteMagnitude'] == 0.443283
        assert star['solarMasses'] == 14.5625
        assert star['solarRadius'] == 5.3612057397555715
        assert star['surfaceTemperature'] == 30995
        assert star['orbitalPeriod'] == 277.5355276686227
        assert star['semiMajorAxis'] == 0.46155863848693135
        assert star['orbitalEccentricity'] == 0.275417
        assert star['orbitalInclination'] == 73.390816
        assert star['argOfPeriapsis'] == 23.460679
        assert star['rotationalPeriod'] == 2.2797341189814815
        assert False == star['rotationalPeriodTidallyLocked']
        assert star['axialTilt'] == None

        # planet
        planet = json['bodies'][15]
        assert planet['id'] == 311417
        assert planet['name'] == "HD 43193 CD 7 a"
        assert planet['type'] == "Planet"
        assert planet['subType'] == "Class IV gas giant"
        assert False == planet['isLandable']
        assert planet['gravity'] == 11.175634423255477
        assert planet['earthMasses'] == 1574.405762
        assert planet['radius'] == 75701.896
        assert planet['surfaceTemperature'] == 1021
        assert planet['volcanismType'] == "No volcanism"
        assert planet['atmosphereType'] == "No atmosphere"
        assert planet['terraformingState'] == "Not terraformable"
        assert planet['orbitalPeriod'] == 55.3160257361574
        assert planet['semiMajorAxis'] == 0.1110330249988177
        assert planet['orbitalEccentricity'] == None
        assert planet['orbitalInclination'] == 28.739708
        assert planet['argOfPeriapsis'] == 248.851365
        assert planet['rotationalPeriod'] == 57.64743373635417
        assert planet['rotationalPeriodTidallyLocked'] == True
        assert planet['axialTilt'] == 0.198277

    def test_getBodiesById_HD43193(self):
        edsmCntl = EdsmCntl()
        json = edsmCntl.getBodiesById(85920)

        # system data
        assert json['id'] == 85920
        assert json['name'] == "HD 43193"

        # body count
        assert len(json['bodies']) == 17

        # star
        star = json['bodies'][0]
        assert star['id'] == 219074
        assert star['name'] == "HD 43193 A"
        assert star['type'] == "Star"
        assert star['subType'] == "B (Blue-White) Star"
        assert star['distanceToArrival'] == 0
        assert star['isMainStar'] == True
        assert star['isScoopable'] == True
        assert star['age'] == 760
        assert star['luminosity'] == "V"
        assert star['absoluteMagnitude'] == 0.443283
        assert star['solarMasses'] == 14.5625
        assert star['solarRadius'] == 5.3612057397555715
        assert star['surfaceTemperature'] == 30995
        assert star['orbitalPeriod'] == 277.5355276686227
        assert star['semiMajorAxis'] == 0.46155863848693135
        assert star['orbitalEccentricity'] == 0.275417
        assert star['orbitalInclination'] == 73.390816
        assert star['argOfPeriapsis'] == 23.460679
        assert star['rotationalPeriod'] == 2.2797341189814815
        assert False == star['rotationalPeriodTidallyLocked']
        assert star['axialTilt'] == None

        # planet
        planet = json['bodies'][15]
        assert planet['id'] == 311417
        assert planet['name'] == "HD 43193 CD 7 a"
        assert planet['type'] == "Planet"
        assert planet['subType'] == "Class IV gas giant"
        assert False == planet['isLandable']
        assert planet['gravity'] == 11.175634423255477
        assert planet['earthMasses'] == 1574.405762
        assert planet['radius'] == 75701.896
        assert planet['surfaceTemperature'] == 1021
        assert planet['volcanismType'] == "No volcanism"
        assert planet['atmosphereType'] == "No atmosphere"
        assert planet['terraformingState'] == "Not terraformable"
        assert planet['orbitalPeriod'] == 55.3160257361574
        assert planet['semiMajorAxis'] == 0.1110330249988177
        assert planet['orbitalEccentricity'] == None
        assert planet['orbitalInclination'] == 28.739708
        assert planet['argOfPeriapsis'] == 248.851365
        assert planet['rotationalPeriod'] == 57.64743373635417
        assert planet['rotationalPeriodTidallyLocked'] == True
        assert planet['axialTilt'] == 0.198277


if __name__ == '__main__':
    unittest.main()
