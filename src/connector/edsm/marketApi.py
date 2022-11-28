from connector.base import exception
from connector.base.base import ApiEntryPoint


class Market(ApiEntryPoint):
    """
    Get information about market in a station
    """

    url = ApiEntryPoint.url_edsm + "system-v1/stations/market"

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

    def getMarketByName(cls, systemName, stationName):
        """
        Get information about market in a station by name

        :param systemName: The system name
        :param stationName: The station name inside the system.
        :return: json
        """
        json = cls.query({"systemName": systemName, "stationName": stationName})
        return json

    def getMarketById(cls, systemId, marketId):
        """
        Get information about market in a station by id

        :param systemId: The system ID
        :param marketId: The game marketId
        :return: json
        """
        json = cls.query({"systemId": systemId, "marketId": marketId})
        return json


# -------------------
market = Market()
