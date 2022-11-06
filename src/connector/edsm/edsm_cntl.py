from connector.edsm.systemApi import Bodies
from connector.edsm.systemsApi import System, Systems


class EdsmCntl():
    # TODO: Documentation
    # TODO: Implementation
    __edsm_system = System()
    __edsm_systems = Systems()
    __edsm_bodies = Bodies()

    def __init__(self):
        pass

    #### System ####
    def getSystem(self, systemName):
        return self.__edsm_system.getSystem(systemName)

    def getSystemIds(self, systemName):
        return self.__edsm_system.getIds(systemName)

    def getSystemCoordinates(self, systemName):
        return self.__edsm_system.etCoordinates(systemName)

    def getSystemPermit(self, systemName):
        return self.__edsm_system.getPermit(systemName)

    def getSystemInformation(self, systemName):
        return self.__edsm_system.getInformation(systemName)

    def getSystemPrimaryStar(self, systemName):
        return self.__edsm_system.getPrimaryStar(systemName)

    #### Systems ####
    def getSystems(self, *systemName):
        return self.__edsm_systems.getSystems(*systemName)

    def getSystemsIds(self, *systemName):
        return self.__edsm_systems.getIds(*systemName)

    def getSystemsCoordinates(self, *systemName):
        return self.__edsm_systems.getCoordinates(*systemName)

    def getSystemsPermit(self, *systemName):
        return self.__edsm_systems.getPermit(*systemName)

    def getSystemsInformation(self, *systemName):
        return self.__edsm_systems.getInformation(*systemName)

    def getSystemsPrimaryStar(self, *systemName):
        return self.__edsm_systems.getPrimaryStar(*systemName)

    #### Bodies ####
    def getBodies(self, systemName):
        return self.__edsm_bodies.getBodies(systemName)

    def getBodiesById(self, systemId):
        return self.__edsm_bodies.getBodiesById(systemId)
