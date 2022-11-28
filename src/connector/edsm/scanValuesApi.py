from connector.base import exception
from connector.base.base import ApiEntryPoint


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
        json = cls.query({"systemName": systemName})
        return json

    def getEstimatedValueById(cls, systemId):
        """
        Get estimated scan values of a system by a systemId

        :param systemId: internal ID of a system
        :return: json
        """
        json = cls.query({"systemId": str(systemId)})
        return json


# ------------------------
scan_values = ScanValues()
