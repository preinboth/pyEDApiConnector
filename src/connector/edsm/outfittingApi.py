from connector.base import exception
from connector.base.base import ApiEntryPoint


class Outfitting(ApiEntryPoint):
    """
    Get information about outfitting in a station
    """

    url = ApiEntryPoint.url_edsm + "system-v1/stations/outfitting"

    def __init__(self):
        pass

    def query(cls, params):
        """
        Build the query for call of the api

        :param params:
        :return: json
        """
        try:
            json = super().query(params)
        except exception.NotFoundError:
            raise exception.SystemNotFoundError(params)
        return json

    def getOutfittingByName(cls, systemName, stationName):
        """
        Get information about outfitting in a station by name

        :param systemName: The system name
        :param stationName: The station inside the system.
        :return: json
        """
        parameters = {"systemName": systemName, "stationName": stationName}
        return cls.query(parameters)

    def getOutfittingById(cls, systemId, marketId):
        """
        Get information about outfitting in a station by id

        :param systemId: The system ID if you seek for a duplicate system and want to force a specific ID.
        :param marketId: The game marketId, if used no other parameters are needed.
        :return: json
        """
        parameters = {"systemId": systemId, "marketId": marketId}
        return cls.query(parameters)


# -------------------
outfitting = Outfitting()
