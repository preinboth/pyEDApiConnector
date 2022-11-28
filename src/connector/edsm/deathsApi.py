from connector.base import exception
from connector.base.base import ApiEntryPoint


class Deaths(ApiEntryPoint):
    """
    Get information about deaths in a system
    """

    url = ApiEntryPoint.url_edsm + "system-v1/deaths"

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

    def getDeaths(cls, systemName):
        """
        Get information about deaths in a system by SystemName

        :param systemName: The system name
        :return: json
        """
        return cls.query({"systemName": systemName})

    def getDeathsById(cls, systemId):
        """
        Get information about deaths in a system by SystemId

        :param systemId: The system ID if you seek for a duplicate system and want to force a specific ID.
        :return: json
        """
        return cls.query({"systemId": systemId})


# -------------------
deaths = Deaths()
