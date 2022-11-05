from connector.base import exception
from connector.base.base import ApiEntryPoint


class System(ApiEntryPoint):
    url = ApiEntryPoint.url_edsm + "v1/system"

    def __init__(self):
        pass

    def query(cls, params):
        try:
            json = super().query(params)
        except exception.NotFoundError:
            raise exception.SystemNotFoundError(params)
        return json

    def getSystem(cls, systemName):
        json = cls.query({'systemName': systemName,
                          'showId': 1,
                          'showCoordinates': 1,
                          'showPermit': 1,
                          'showInformation': 1,
                          'showPrimaryStar': 1})
        return json

    def getIds(cls, systemName):
        json = cls.query({'systemName': systemName,
                          'showId': 1})
        return json

    def getCoordinates(cls, systemName):
        json = cls.query({'systemName': systemName,
                          'showPermit': 1})
        return json

    def getPermit(cls, systemName):
        json = cls.query({'systemName': systemName,
                          'showPermit': 1})
        return json

    def getInformation(cls, systemName):
        json = cls.query({'systemName': systemName,
                          'showInformation': 1})
        return json

    def getPrimaryStar(cls, systemName):
        json = cls.query({'systemName': systemName,
                          'showPrimaryStar': 1})
        return json


class Systems(ApiEntryPoint):
    url = ApiEntryPoint.url_edsm + "v1/systems"

    def query(cls, params):
        try:
            json = super().query(params)
        except exception.NotFoundError:
            raise exception.SystemNotFoundError(params)
        return json

    def getSystems(cls, *systemName):
        parameters = {'showId': 1,
                      'showCoordinates': 1,
                      'showPermit': 1,
                      'showInformation': 1,
                      'showPrimaryStar': 1}

        if len(systemName) == 1:
            parameters['systemName'] = systemName[0]
        else:
            parameters['systemName[]'] = list(systemName)

        return cls.query(parameters)

    def getIds(cls, *systemName):
        parameters = {'showId': 1}

        if len(systemName) == 1:
            parameters['systemName'] = systemName[0]
        else:
            parameters['systemName[]'] = list(systemName)

        return cls.query(parameters)

    def getCoordinates(cls, *systemName):
        parameters = {'showCoordinates': 1}

        if len(systemName) == 1:
            parameters['systemName'] = systemName[0]
        else:
            parameters['systemName[]'] = list(systemName)

        return cls.query(parameters)

    def getPermit(cls, *systemName):
        parameters = {'showPermit': 1}
        if len(systemName) == 1:
            parameters['systemName'] = systemName[0]
        else:
            parameters['systemName[]'] = list(systemName)
        return cls.query(parameters)

    def getInformation(cls, *systemName):
        parameters = {'showInformation': 1}

        if len(systemName) == 1:
            parameters['systemName'] = systemName[0]
        else:
            parameters['systemName[]'] = list(systemName)

        return cls.query(parameters)

    def getPrimaryStar(cls, *systemName):
        parameters = {'showPrimaryStar': 1}

        if len(systemName) == 1:
            parameters['systemName'] = systemName[0]
        else:
            parameters['systemName[]'] = list(systemName)

        return cls.query(parameters)
