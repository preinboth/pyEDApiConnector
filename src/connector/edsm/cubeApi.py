from connector.base import exception
from connector.base.base import ApiEntryPoint


class Cube(ApiEntryPoint):
    """
    Get systems in a cube
    """

    url = ApiEntryPoint.url_edsm + "v1/cube-systems"

    def __init__(self):
        pass

    def query(cls, params):
        """
        Build the query for call of the api

        :param params:
        :return:
        """
        try:
            json = super().query(params)
        except exception.NotFoundError:
            raise exception.SystemNotFoundError(params)
        return json

    def getSystemsCubeBySystemName(cls, systemName, size):
        """
        Get systems in a cube by a system name which will be the center of the sphere.

        :param systemName: The system name which will be the center of the sphere.
        :param coords: If you don't want to use a system name, you can use coordinates as the center of the sphere.
        :param size: Set to the desired size of the cube In ly. Maximum value is 200.
        """
        parameters = {
            "showId": 1,
            "showCoordinates": 1,
            "showPermit": 1,
            "showInformation": 1,
            "showPrimaryStar": 1,
            "systemName": systemName,
            "size": size,
        }
        return cls.query(parameters)

    def getSystemsCubeByCoords(cls, coords, size):
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
        parameters = {
            "showId": 1,
            "showCoordinates": 1,
            "showPermit": 1,
            "showInformation": 1,
            "showPrimaryStar": 1,
            "x": 0,
            "y": 0,
            "z": 0,
            "size": size,
        }
        return cls.query(parameters)


# -------------------
cube = Cube()
