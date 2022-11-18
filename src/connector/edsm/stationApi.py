from connector.base import exception
from connector.base.base import ApiEntryPoint
from utils.utils import filterStationsByType


class Station(ApiEntryPoint):
    """
    Get information about stations in a system
    """
    url = ApiEntryPoint.url_edsm + "system-v1/stations"

    def __init__(self):
        pass

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

    def getStation(cls, systemName, exclude: list):
        """
        Get information about stations in a system by a systemname

        :param systemName: Use the systemName parameter to filter flight logs by system name.
        :param exclude: List of excluded stationtypes
        :return: json
        """
        parameters = {'systemName': systemName}
        system = cls.query(parameters)
        # TODO: Stations filtern
        filtered = filterStationsByType(system, exclude)
        return filtered

    def getStationById(cls, systemId, exclude: list):
        """
        Get information about stations in a system by a systemId

        :param systemId: By passing directly our intenral ID, you can override the system name.
        :param exclude: List of excluded stationtypes
        :return: json
        """
        parameters = {'systemId': int(systemId)}
        # TODO: Stations filtern
        return cls.query(parameters)


# -------------------
station = Station()
