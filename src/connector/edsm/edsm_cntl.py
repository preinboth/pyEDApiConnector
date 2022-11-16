
from connector.edsm.systemApi import station
from connector.edsm.systemApi import bodies
from connector.edsm.systemApi import scan_values


class EdsmCntl():
    # TODO: Documentation
    # TODO: Implementation


    def __init__(self):
        pass

    # Get information about stations in a system
    def getStation(self, systemName):
=======
    ########################################
    ##               Status               ##
    ########################################
    def getEliteServerStatus(self):
        """
        getEliteServerStatus

        :return: json
        """
        return server_status.getEliteServerStatus()

    ########################################
    ##           System/Systems           ##
    ########################################
    def getSystem(self, systemName):
        """
        get Systeminformation by a Systemname

        :param systemName: Name of a system
        :return: json
        """
        return system.getSystem(systemName)

    def getSystems(self, *systemName):
        """
        get complete information of a list of systems

        :param systemName: List of system names
        :return:  json
        """
        return systems.getSystems(*systemName)

    def getSystemId(self, systemName):

        """
        Get information about stations in a system by a systemname

        :param systemName: Use the systemName parameter to filter flight logs by system name.
        :return: json
        """

        return station.getStation(systemName)

    def getSystemsIds(self, *systemName):
        """
        get SystemIds of a list of systems

        :param systemName: List of system names
        :return:  json:
        """
        return systems.getIds(*systemName)


    def getStationById(self, systemId):
        """
        Get information about stations in a system by a systemId

        :param systemId: By passing directly our intenral ID, you can override the system name.
        :return: json
        """

        return station.getStationById(systemId)

    # Get information about celestial bodies in a system
    def getBodies(self, systemName):
=======
        return system.getCoordinatesBySystemname(systemName)

    def getSystemsCoordinates(self, *systemName):
        """
        get coordinates of a list of systems

        :param systemName: List of system names
        :return:  json:
        """
        return systems.getCoordinates_by_SystemList(*systemName)

    def getSystemPermit(self, systemName):
        """
        get Permit by a Systemname

        :param systemName: Name of a system
        :return:  json
        """
        return system.getPermit(systemName)

    def getSystemsPermit(self, *systemName):
        """
        get permits of a list of systems

        :param systemName: List of system names
        :return:  json:
        """
        return systems.getPermit(*systemName)

    def getSystemInformation(self, systemName):
        """
        get Information of a system

        :param systemName: Name of a system
        :return:  json
        """
        return system.getInformation(systemName)

    def getSystemsInformation(self, *systemName):
        """
        get Information of a list of systems

        :param systemName: List of system names
        :return:  json:
        """
        return systems.getInformation(*systemName)

    def getSystemPrimaryStar(self, systemName):

        """
        get Bodies for a systemname

        :param systemName: Name of a system
        :return: bodies in json
        """

        return system.getPrimaryStar(systemName)

    def getSystemsPrimaryStar(self, *systemName):
        return systems.getPrimaryStar(*systemName)

    #### Bodies ####
    def getBodies(self, systemName):
        return self.__edsm_bodies.getBodies(systemName)


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


# ------------------------
edsmCntl = EdsmCntl()
