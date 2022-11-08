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

    def getSystemsSphere(cls, systemName, coords, minradius, radius):
        """
        Get systems in a sphere radius

        :param systemName: The system name which will be the center of the sphere.
        :param coords: If you don't want to use a system name, you can use coordinates as the center of the sphere.
        :param minradius: Set to a value between 0 and radius to reduce the returned results. In ly.
        :param radius: Set to the desired radius In ly. Maximum value is 100.
        """
        # TODO: Implementation
        pass


# -------------------
sphere = Sphere()
