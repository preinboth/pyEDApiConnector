from connector.base import exception
from connector.base.base import ApiEntryPoint


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

    def getStation(cls, systemName):
        """
        Get information about stations in a system by a systemname

        :param systemName: Use the systemName parameter to filter flight logs by system name.
        :return: json
        """
        parameters = {}
        parameters['systemName'] = systemName
        # if len(systemName) == 1:
        #     parameters['systemName'] = systemName[0]
        # else:
        #     parameters['systemName[]'] = list(systemName)
        json = cls.query(parameters)
        return json

    def getStationById(cls, systemId):
        """
        Get information about stations in a system by a systemId

        :param systemId: By passing directly our intenral ID, you can override the system name.
        :return: json
        """
        parameters = {'systemId': int(systemId)}
        # if len(systemId) == 1:
        # else:
        # parameters['systemId[]'] = list(systemId)

        json = cls.query(parameters)
        return json


# -------------------
station = Station()
