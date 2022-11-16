from connector.base import exception
from connector.base.base import ApiEntryPoint


class System(ApiEntryPoint):
    """
    get Information of a System
    """
    url = ApiEntryPoint.url_edsm + "v1/system"

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

    def getSystem(cls, systemName):
        """
        get Systeminformation by a Systemname

        :param systemName: Use the systemName parameter to filter flight logs by system name.
        :return: json
        """
        json = cls.query({'systemName': systemName,
                          'showId': 1,
                          'showCoordinates': 1,
                          'showPermit': 1,
                          'showInformation': 1,
                          'showPrimaryStar': 1})
        return json

    def getIds(cls, systemName):
        """
        get SystemId by a Systemname

        :param systemName: Name of a system
        :return: json
        """
        json = cls.query({'systemName': systemName,
                          'showId': 1})
        return json

    def getCoordinatesBySystemname(cls, systemName):
        """
        get Coordinates by a Systemname

        :param systemName: Name of a system
        :return: json
        """
        json = cls.query({'systemName': systemName,
                          'showCoordinates': 1})
        return json

    def getPermit(cls, systemName):
        """
        get Permit by a Systemname

        :param systemName: Name of a system
        :return:  json
        """
        json = cls.query({'systemName': systemName,
                          'showPermit': 1})
        return json

    def getInformation(cls, systemName):
        """
        get information by a systemname

        :param systemName: Name of a system
        :return:  json
        """
        json = cls.query({'systemName': systemName,
                          'showInformation': 1})
        return json

    def getPrimaryStar(cls, systemName):
        """
        get the primarystar by a systemname

        :param systemName: Name of a system
        :return:  json
        """
        json = cls.query({'systemName': systemName,
                          'showPrimaryStar': 1})
        return json


class Systems(ApiEntryPoint):
    """
    get Information for Systems
    """
    url = ApiEntryPoint.url_edsm + "v1/systems"

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

    def getSystems(cls, *systemName):
        """
        Get information about systems

        :param systemName: Name of a system(s)
        :return: json
        """
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


# -------------------
system = System()
systems = Systems()
