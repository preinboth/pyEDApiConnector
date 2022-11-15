from connector.edsm.systemApi import station

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

# ------------------------
edsmCntl = EdsmCntl()
