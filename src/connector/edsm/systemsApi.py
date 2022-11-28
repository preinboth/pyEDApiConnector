from connector.base import exception
from connector.base.base import ApiEntryPoint


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
        parameters = {
            "showId": 1,
            "showCoordinates": 1,
            "showPermit": 1,
            "showInformation": 1,
            "showPrimaryStar": 1,
        }
        if len(systemName) == 1:
            parameters["systemName"] = systemName[0]
        else:
            parameters["systemName[]"] = list(systemName)
        return cls.query(parameters)


# -------------------
systems = Systems()
