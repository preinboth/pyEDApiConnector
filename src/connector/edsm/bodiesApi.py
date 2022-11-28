from connector.base import exception
from connector.base.base import ApiEntryPoint


class Bodies(ApiEntryPoint):
    """
    Informastion of Bodies
    """

    url = ApiEntryPoint.url_edsm + "system-v1/bodies"

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

    def getBodies(cls, systemName):
        """
        get Bodies for a systemname

        :param systemName: Name of a system
        :return: bodies in json
        """
        json = cls.query({"systemName": systemName})
        return json

    def getBodiesById(cls, systemId):
        """
        get Bodies for a systemId

        :param systemId: internal ID of a system
        :return: bodies in json
        """
        json = cls.query({"systemId": str(systemId)})
        return json


# -------------------
bodies = Bodies()
