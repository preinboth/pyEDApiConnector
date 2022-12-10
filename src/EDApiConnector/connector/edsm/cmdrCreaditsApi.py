from EDApiConnector.connector.base import exception
from EDApiConnector.connector.base.base import ApiEntryPoint


class CmdrCredits(ApiEntryPoint):
    """
    Get commander credits
    """

    url = ApiEntryPoint.url_edsm + "commander-v1/get-credits"

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

    def getCmdrCredits(cls, cmdrname, api_key):
        """
        Get commander credits by CmdrName and APiKey

        :param cmdrname: The name of the commander as registered on EDSM.
        :param api_key: The API Key associate the commander name with his account.
        :return: json
        """
        params = {"commanderName": cmdrname, "apiKey": api_key}
        json = cls.query(params)
        if json["msgnum"] == 201:
            # 201 Missing commander name
            raise exception.CommanderNotFoundError(cls.url, params)
        elif json["msgnum"] == 203:
            # 203 Commander name / API Key not found
            params = params + "," + json["msgnum"]
            raise exception.ApiKeyNotFoundError(cls.url, params)
        elif json["msgnum"] == 207:
            # 207 No ranks stored
            raise exception.CmdrNoRanksStored(cls.url, params)
        return json


# -------------------
cmdrCredits = CmdrCredits()
