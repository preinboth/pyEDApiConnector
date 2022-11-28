from connector.base import exception
from connector.base.base import ApiEntryPoint


class Shipyard(ApiEntryPoint):
    """
    Get information about shipyard in a station
    """

    url = ApiEntryPoint.url_edsm + "system-v1/stations/shipyard"

    def query(cls, params):
        """
        create the query based on the parameters and retrieve data from Api

        :param params:
        :return: json
        """
        try:
            json = super().query(params)
        except exception.NotFoundError:
            raise exception.SystemNotFoundError(params)
        return json

    def getShipyard(cls, systemName, stationName):
        """
        Get information about shipyard in a station by name

        :param systemName: The system name
        :param stationName: The station name inside the system.
        :return: json
        """
        json = cls.query({"systemName": systemName, "stationName": stationName})
        return json

    def getShipyardById(cls, systemId, marketId):
        """
        Get information about shipyard in a station by id

        :param systemId: The system ID
        :param marketId: The game marketId
        :return: json
        """
        json = cls.query({"systemId": systemId, "marketId": marketId})
        return json


# -------------------
shipyard = Shipyard()
