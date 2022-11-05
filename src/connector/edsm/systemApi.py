from connector.base import exception
from connector.base.base import ApiEntryPoint


class Bodies(ApiEntryPoint):
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
        :param systemName:
        :return: bodies in json
        """
        json = cls.query({'systemName': systemName})
        return json

    def getBodiesById(cls, systemId):
        """
        get Bodies for a systemId
        :param systemId:  ID of a system
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
        try:
            json = super().query(params)
        except exception.NotFoundError:
            raise exception.SystemNotFoundError(params)
        return json

    def getEstimatedValue(cls, systemName):
        """
        Get estimated scan values of a system by a systemname
        :param systemName:
        :return:
        """
        json = cls.query({'systemName': systemName})
        return json

    def getEstimatedValueById(cls, systemId):
        """
        Get estimated scan values of a system by a systemId
        :param systemId:
        :return:
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
        try:
            json = super().query(params)
        except exception.NotFoundError:
            raise exception.SystemNotFoundError(params)
        return json

    def getStation(cls, systemName):
        """
        Get information about stations in a system by a systemname
        :param systemName:
        :return:
        """
        json = cls.query({'systemName': systemName})
        return json

    def getStationById(cls, systemId):
        """
        Get information about stations in a system by a systemId
        :param systemId:
        :return:
        """
        json = cls.query({'systemId': str(systemId)})
        return json
