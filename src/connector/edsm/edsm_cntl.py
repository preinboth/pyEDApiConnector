from connector.edsm.cubeApi import cube
from connector.edsm.marketApi import market
from connector.edsm.sphereApi import sphere
from connector.edsm.statusApi import server_status
from connector.edsm.systemApi import Bodies
from connector.edsm.systemsApi import System, Systems
from connector.edsm.trafficApi import traffic


class EdsmCntl():
    # TODO: Documentation
    # TODO: Implementation
    __edsm_system = System()
    __edsm_systems = Systems()
    __edsm_bodies = Bodies()

    def __init__(self):
        pass

    ########################################
    ##           System/Systems           ##
    ########################################
    def getSystem(self, systemName):
        """
        get Systeminformation by a Systemname

        :param systemName: Name of a system
        :return: json
        """
        return self.__edsm_system.getSystem(systemName)

    def getSystems(self, *systemName):
        """
        get complete information of a list of systems

        :param systemName: List of system names
        :return:  json
        """
        return self.__edsm_systems.getSystems(*systemName)

    def getSystemId(self, systemName):
        """
        get SystemId by a Systemname

        :param systemName: Name of a system
        :return: json
        """
        return self.__edsm_system.getIds(systemName)

    def getSystemsIds(self, *systemName):
        """
        get SystemIds of a list of systems

        :param systemName: List of system names
        :return:  json:
        """
        return self.__edsm_systems.getIds(*systemName)

    def getSystemCoordinate(self, systemName):
        """
        get Coordinates by a Systemname

        :param systemName: Name of a system
        :return: json
        """
        return self.__edsm_system.getCoordinates_by_systemname(systemName)

    def getSystemsCoordinates(self, *systemName):
        """
        get coordinates of a list of systems

        :param systemName: List of system names
        :return:  json:
        """
        return self.__edsm_systems.getCoordinates_by_SystemList(*systemName)

    def getSystemPermit(self, systemName):
        """
        get Permit by a Systemname

        :param systemName: Name of a system
        :return:  json
        """
        return self.__edsm_system.getPermit(systemName)

    def getSystemsPermit(self, *systemName):
        """
        get permits of a list of systems

        :param systemName: List of system names
        :return:  json:
        """
        return self.__edsm_systems.getPermit(*systemName)

    def getSystemInformation(self, systemName):
        """
        get Information of a system

        :param systemName: Name of a system
        :return:  json
        """
        return self.__edsm_system.getInformation(systemName)

    def getSystemsInformation(self, *systemName):
        """
        get Information of a list of systems

        :param systemName: List of system names
        :return:  json:
        """
        return self.__edsm_systems.getInformation(*systemName)

    def getSystemPrimaryStar(self, systemName):
        """
        get primary Star of a system

        :param systemName: Name of a system
        :return:  json
        """
        return self.__edsm_system.getPrimaryStar(systemName)

    def getSystemsPrimaryStar(self, *systemName):
        return self.__edsm_systems.getPrimaryStar(*systemName)

    #### Bodies ####
    def getBodies(self, systemName):
        return self.__edsm_bodies.getBodies(systemName)

    def getBodiesById(self, systemId):
        return self.__edsm_bodies.getBodiesById(systemId)

    ########################################
    ##          EdServerStatus            ##
    ########################################
    def getEdServerStatus(self):
        """
        getEliteServerStatus

        :return: json
        """
        return server_status.getEliteServerStatus()

    ########################################
    ##               Deaths               ##
    ########################################

    ########################################
    ##              Factions              ##
    ########################################

    ########################################
    ##             Commander              ##
    ########################################

    ########################################
    ##               Logs                 ##
    ########################################

    ########################################
    ##              Market                ##
    ########################################
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

    ########################################
    ##            Outfitting              ##
    ########################################

    ########################################
    ##              Shipyard              ##
    ########################################

    ########################################
    ##               Cube                 ##
    ########################################
    def getSystemsCube(self, systemName, coords, size):
        """
        Get systems in a cube

        :param systemName: The system name which will be the center of the sphere.
        :param coords: If you don't want to use a system name, you can use coordinates as the center of the sphere.
        :param size: Set to the desired size of the cube In ly. Maximum value is 200.
        """

        return cube.getSystemsCube(systemName, coords, size)

    ########################################
    ##             Sphere                 ##
    ########################################
    def getSystemsSphere(self, systemName, coords, minradius, radius):
        """
        Get systems in a sphere radius

        :param systemName: The system name which will be the center of the sphere.
        :param coords: If you don't want to use a system name, you can use coordinates as the center of the sphere.
        :param minradius: Set to a value between 0 and radius to reduce the returned results. In ly.
        :param radius: Set to the desired radius In ly. Maximum value is 100.
        """
        return sphere.getSystemsSphere(systemName, coords, minradius, radius)

    ########################################
    ##               Traffic              ##
    ########################################
    def getTrafficSystem(self, systemName, systemId):
        """
        Get information about traffic in a system

        :param systemName: The system name
        :param systemId: The system ID if you seek for a duplicate system and want to force a specific ID.
        """
        return traffic.getTrafficSystem(systemName, systemId)


# ------------------------
edsmCntl = EdsmCntl()
