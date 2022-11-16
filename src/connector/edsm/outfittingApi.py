from connector.base import exception
from connector.base.base import ApiEntryPoint
from src.utils import utils
from src.connector.edsm.systemApi import Station
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

    def getOutfittingBySystemNames(cls, systemName, exclude):
        parameters = {}
        if len(systemName) == 1:
            station = Station()
            json_stations = station.getStation(systemName[0])
            filtered = utils.filterStationsByType(json_stations, exclude)
        else:
            pass
            # parameters['systemName[]'] = list(systemName)

        return cls.query(parameters)

    def getOutfittingById(cls):
        pass


# -------------------
outfitting = Outfitting()
