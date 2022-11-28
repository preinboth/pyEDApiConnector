from connector.base import exception
from connector.base.base import ApiEntryPoint


class Factions(ApiEntryPoint):
    """
    Get information about factions in a system
    """

    url = ApiEntryPoint.url_edsm + "system-v1/factions"

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

    def getFaction(cls, systemName, showHistory=0):
        """
        Get information about factions in a system by name

        :param systemName: The system name
        :param showHistory: Set to 1 to get the factions history under the requested system.
        :return: json
        """
        return cls.query({"systemName": systemName, "showHistory": showHistory})

    def getFactionById(cls, systemId, showHistory=0):
        """
        Get information about factions in a system by name

        :param systemId: The system ID
        :param showHistory: Set to 1 to get the factions history under the requested system.
        :return: json
        """
        return cls.query({"systemId": systemId, "showHistory": showHistory})


# -------------------
factions = Factions()
