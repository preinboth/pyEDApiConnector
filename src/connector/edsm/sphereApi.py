from connector.base import exception
from connector.base.base import ApiEntryPoint


class Sphere(ApiEntryPoint):
    """
    Get systems in a sphere radius
    """

    url = ApiEntryPoint.url_edsm + "v1/sphere-systems"

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

    def getSystemsSphereBySystemName(cls, systemName, minradius=0, radius=0):
        """
        Get systems in a sphere radius

        :param systemName: The system name which will be the center of the sphere.
        :param minradius: Set to a value between 0 and radius to reduce the returned results. In ly.
        :param radius: Set to the desired radius In ly. Maximum value is 100.
        """
        parameters = {
            "showId": 1,
            "showCoordinates": 1,
            "showPermit": 1,
            "showInformation": 1,
            "showPrimaryStar": 1,
            "systemName": systemName,
            "minradius": minradius,
            "radius": radius,
        }
        json = cls.query(parameters)
        return json

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
        parameters = {
            "showId": 1,
            "showCoordinates": 1,
            "showPermit": 1,
            "showInformation": 1,
            "showPrimaryStar": 1,
            "x": coords["x"],
            "y": coords["y"],
            "z": coords["z"],
            "minradius": minradius,
            "radius": radius,
        }
        json = cls.query(parameters)
        return json


# -------------------
sphere = Sphere()
