from connector.edsm.bodiesApi import bodies
from connector.edsm.factionsApi import factions
from connector.edsm.marketApi import market
from connector.edsm.scanValuesApi import scan_values
from connector.edsm.shipyardApi import shipyard
from connector.edsm.stationApi import station
from connector.edsm.statusApi import server_status
from connector.edsm.trafficApi import traffic
from connector.edsm.deathsApi import deaths


class EdsmCntl():
    # TODO: Documentation
    # TODO: Implementation

    def __init__(self):
        pass

    # Get information about stations in a system
    def getStation(self, systemName):
        """
        Get information about stations in a system by a systemname

        :param systemName: Use the systemName parameter to filter flight logs by system name.
        :return: json
        """
        return station.getStation(systemName)

    def getStationById(self, systemId):
        """
        Get information about stations in a system by a systemId

        :param systemId: By passing directly our intenral ID, you can override the system name.
        :return: json
        """
        return station.getStationById(systemId)

    # Get information about celestial bodies in a system
    def getBodies(self, systemName):
        """
        get Bodies for a systemname

        :param systemName: Name of a system
        :return: bodies in json
        """
        return bodies.getBodies(systemName)

    def getBodiesById(self, systemId):
        """
        get Bodies for a systemId

        :param systemId: internal ID of a system
        :return: bodies in json
        """
        return bodies.getBodiesById(systemId)

    # Get estimated scan values of a system
    def getEstimatedValue(self, systemName):
        """
        Get estimated scan values of a system by a systemname

        :param systemName: Name of a system
        :return: json
        """
        return scan_values.getEstimatedValue(systemName)

    def getEstimatedValueById(self, systemId):
        """
        Get estimated scan values of a system by a systemId

        :param systemId: internal ID of a system
        :return: json
        """
        return scan_values.getEstimatedValueById(systemId)

    def getMarketByName(self, systemName, stationName):
        """
        Get information about market in a station by name

        :param systemName: The system name
        :param stationName: The station name inside the system.
        :return: json
        """
        return market.getMarketByName(systemName, stationName)

    def getMarketById(self, systemId, marketId):
        """
        Get information about market in a station by id

        :param systemId: The system ID
        :param marketId: The game marketId
        :return: json
        """
        return market.getMarketById(systemId, marketId)

    def getEliteServerStatus(self):
        """
        Get Elite: Dangerous server status

        :return: json
        """
        return server_status.getEliteServerStatus()

    def getShipyard(self, systemName, stationName):
        """
        Get information about shipyard in a station by name

        :param systemName: The system name
        :param stationName: The station name inside the system.
        :return: json
        """
        return shipyard.getShipyard(systemName, stationName)

    def getShipyardById(self, systemId, marketId):
        """
        Get information about shipyard in a station by id

        :param systemId: The system ID
        :param marketId: The game marketId
        :return: json
        """
        return shipyard.getShipyardById(systemId, marketId)

    def getFaction(self, systemName, showHistory=0):
        """
        Get information about factions in a system by name

        :param systemName: The system name
        :param showHistory: Set to 1 to get the factions history under the requested system.
        :return: json
        """
        return factions.getFaction(systemName, showHistory)

    def getFactionById(self, systemId, showHistory=0):
        """
        Get information about factions in a system by name

        :param systemId: The system ID
        :param showHistory: Set to 1 to get the factions history under the requested system.
        :return: json
        """
        return factions.getFactionById(systemId, showHistory)

    def getTrafficSystem(cls, systemName):
        """
        Get information about traffic in a system by a systemname

        :param systemName: The system name
        :return: json
        """
        return traffic.getTrafficSystem(systemName)

    def getTrafficById(cls, systemId):
        """
        Get information about traffic in a system by a systemId

        :param systemId: The system ID if you seek for a duplicate system and want to force a specific ID.
        :return: json
        """
        return traffic.getTrafficById(systemId)

    def getDeaths(cls, systemName):
        """
        Get information about deaths in a system by SystemName

        :param systemName: The system name
        :return: json
        """
        return deaths.getDeaths(systemName)

    def getDeathsById(cls, systemId):
        """
        Get information about deaths in a system by SystemId

        :param systemId: The system ID if you seek for a duplicate system and want to force a specific ID.
        :return: json
        """
        return deaths.getDeathsById(systemId)
# ------------------------
edsmCntl = EdsmCntl()
