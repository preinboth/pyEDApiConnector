from connector.base import exception
from connector.base.base import ApiEntryPoint


class Traffic(ApiEntryPoint):
    """
    Get information about traffic in a system
    """
    url = ApiEntryPoint.url_edsm + "system-v1/traffic"

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

    def getTrafficSystem(cls, systemName, systemId):
        """
        Get information about traffic in a system

        :param systemName: The system name
        :param systemId: The system ID if you seek for a duplicate system and want to force a specific ID.
        """
        json = cls.query({'systemName': systemName, 'systemId': systemId})
        return json


# --------------
traffic = Traffic()
