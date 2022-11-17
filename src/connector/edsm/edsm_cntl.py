from connector.edsm.systemApi import station
from connector.edsm.systemApi import bodies
from connector.edsm.systemApi import scan_values
from connector.edsm.systemsApi import systems
from connector.edsm.cubeApi import cube
from connector.edsm.sphereApi import sphere


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

    # Get information about systems
    def getSystems(self, *systemName):
        """
        Get information about systems

        :param systemName: Name of a system(s)
        :return: json
        """
        return systems.getSystems(*systemName)

    # Get systems in a cube
    def getSystemsCubeBySystemName(self, systemName, size):
        """
        Get systems in a cube by a system name which will be the center of the sphere.

        :param systemName: The system name which will be the center of the sphere.
        :param coords: If you don't want to use a system name, you can use coordinates as the center of the sphere.
        :param size: Set to the desired size of the cube In ly. Maximum value is 200.
        """
        return cube.getSystemsCubeBySystemName(systemName, size)

    def getSystemsCubeByCoords(self, coords, size):
        """
        Get systems in a cube by a coords which will be the center of the sphere.

        :param coords: If you don't want to use a system name, you can use coordinates as the center of the sphere.
                      Format Coords:
                      coords = {
                            'x': 0,
                            'y': 0,
                            'z': 0,
                            }
        :param size: Set to the desired size of the cube In ly. Maximum value is 200.
        """
        return cube.getSystemsCubeByCoords(coords, size)

    def getSystemsSphereBySystemName(self, systemName, minradius=0, radius=0):
        """
        Get systems in a sphere radius

        :param systemName: The system name which will be the center of the sphere.
        :param minradius: Set to a value between 0 and radius to reduce the returned results. In ly.
        :param radius: Set to the desired radius In ly. Maximum value is 100.
        """
        return sphere.getSystemsSphereBySystemName(systemName, minradius, radius)

    def getSystemsSphereByCoords(cls, coords, minradius=0, radius=0):
        """
        Get systems in a sphere radius

        :param coords: If you don't want to use a system name, you can use coordinates as the center of the sphere.
                      Format Coords:
                      coords = {
                            'x': 0,
                            'y': 0,
                            'z': 0,
                            }
        :param minradius: Set to a value between 0 and radius to reduce the returned results. In ly.
        :param radius: Set to the desired radius In ly. Maximum value is 100.
        """
        return sphere.getSystemsSphereByCoords(coords, minradius, radius)


# ------------------------
edsmCntl = EdsmCntl()
