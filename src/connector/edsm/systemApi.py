from connector.base import exception
from connector.base.base import ApiEntryPoint


class Bodies(ApiEntryPoint):
    url = ApiEntryPoint.url_edsm + "system-v1/bodies"

    def __init__(self):
        pass

    def query(cls, params):
        try:
            json = super().query(params)
        except exception.NotFoundError:
            raise exception.SystemNotFoundError(params)
        return json

    def getBodies(cls, systemName):
        json = cls.query({'systemName': systemName})
        return json

    def getBodiesById(cls, systemId):
        json = cls.query({'systemId': str(systemId)})
        return json


class ScanValues(ApiEntryPoint):
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
        json = cls.query({'systemName': systemName})
        return json

    def getEstimatedValueById(cls, systemId):
        json = cls.query({'systemId': str(systemId)})
        return json


class Station(ApiEntryPoint):
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
        json = cls.query({'systemName': systemName})
        return json

    def getStationById(cls, systemId):
        json = cls.query({'systemId': str(systemId)})
        return json
