from connector.edsm.systemApi import station
from connector.edsm.systemApi import bodies

class EdsmCntl():
    # TODO: Documentation
    # TODO: Implementation

    def __init__(self):
        pass

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
# ------------------------
edsmCntl = EdsmCntl()
