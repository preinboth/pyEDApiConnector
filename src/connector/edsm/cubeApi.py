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

        json = cls.query({'systemName': systemName, 'size': size})
        return json

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
        json = cls.query({'x': coords['x'], 'y': coords['y'], 'z': coords['z'], 'size': size})
        return json


# -------------------
cube = Cube()
