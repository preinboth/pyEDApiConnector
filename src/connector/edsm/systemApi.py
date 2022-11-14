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
        json = cls.query({'systemName': systemName})
        return json

    def getBodiesById(cls, systemId):
        """
        get Bodies for a systemId

        :param systemId: internal ID of a system
        :return: bodies in json
        """
        json = cls.query({'systemId': str(systemId)})
        return json


class ScanValues(ApiEntryPoint):
    """
    Get estimated scan values of a system
    """
    url = ApiEntryPoint.url_edsm + "system-v1/estimated-value"

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

    def getEstimatedValue(cls, systemName):
        """
        Get estimated scan values of a system by a systemname

        :param systemName: Name of a system
        :return: json
        """
        json = cls.query({'systemName': systemName})
        return json

    def getEstimatedValueById(cls, systemId):
        """
        Get estimated scan values of a system by a systemId

        :param systemId: internal ID of a system
        :return: json
        """
        json = cls.query({'systemId': str(systemId)})
        return json


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

    def getStation(cls, *systemName):
        """
        Get information about stations in a system by systemname

        :param systemName: Use the systemName parameter to filter flight logs by system name.
        :return: json
        """
        parameters = {}
        if len(systemName) == 1:
            parameters['systemName'] = systemName[0]
        else:
            parameters['systemName[]'] = list(systemName)

        json = cls.query({'systemName': systemName})
        return json

    def getStationById(cls, *systemId):
        """
        Get information about stations in a system by systemId

        :param systemId: By passing directly our intenral ID, you can override the system name.
        :return: json
        """
        parameters = {}
        if len(systemId) == 1:
            parameters['systemId'] = systemId[0]
        else:
            parameters['systemId[]'] = list(systemId)

        json = cls.query({'systemName': systemId})

        json = cls.query({'systemId': str(systemId)})
        return json
