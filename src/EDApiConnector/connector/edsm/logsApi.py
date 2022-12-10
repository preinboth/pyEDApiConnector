from EDApiConnector.connector.base import exception
from EDApiConnector.connector.base.base import ApiEntryPoint


class LogsFlightEntries(ApiEntryPoint):
    url = ApiEntryPoint.url_edsm + "logs-v1/get-logs"

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

    def get_FlightLogEntries(
        cls, cmdrname, api_key, systemName, startDateTime, endDateTime, showId
    ):
        """
        Get flight log entries

        :param cmdrname: The name of the commander as registered on EDSM.
        :param api_key: The API Key associate the commander name with his account.
        :param systemName: Use the systemName parameter to filter flight logs by system name.
        :param startDateTime: If you only want to receive flight logs after a specific date & time, use this parameter.
        :param endDateTime: If you only want to receive flight logs before a specific date & time, use this parameter.
        :param showId: Set to 1 if you want to get our internal id. Useful to handle duplicated name systems of the game.
        :return: json
        """
        params = {
            "commanderName": cmdrname,
            "apiKey": api_key,
            "systemName": systemName,
            "startDateTime": startDateTime,
            "endDateTime": endDateTime,
            "showId": showId,
        }
        json = cls.query(params)

        if json["msgnum"] == 201:
            # 201 Missing commander name
            raise exception.CommanderNotFoundError(cls.url, params)
        elif json["msgnum"] == 202:
            # 202 Missing APIkey
            params = params + "," + json["msgnum"]
            raise exception.ApiKeyNotFoundError(cls.url, params)
        elif json["msgnum"] == 203:
            # 203 Commander name / API Key not found
            params = params + "," + json["msgnum"]
            raise exception.ApiKeyNotFoundError(cls.url, params)
        elif json["msgnum"] == 207:
            # 207 No ranks stored
            raise exception.CmdrNoRanksStored(cls.url, params)
        elif json["msgnum"] == 302:
            # 302	System not in database
            raise exception.SystemNotInDatabase(cls.url, params)
        elif json["msgnum"] == 303:
            # 303	System probably non existant
            raise exception.SystemProbablyNonExistant(cls.url, params)
        elif json["msgnum"] == 429:
            # 429	Rate limit exceeded
            raise exception.RateLimitExceeded(cls.url, params)
        return json


class CommanderLastPosition(ApiEntryPoint):
    """
    Get commander last position
    """

    url = ApiEntryPoint.url_edsm + "logs-v1/get-position"

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

    def getCommanderLastPosition(cls, cmdrname, api_key, showId, showCoordinates):
        """
        Get commander last position

        :param cmdrname: The name of the commander as registered on EDSM.
        :param api_key: The API Key associate the commander name with his account.
        :param showId: Set to 1 if you want to get our internal id. Useful to handle duplicated name systems of the game.
        :param showCoordinates: Set to 1 if you want to get the coordinates of the system. If set to 1 only the last position with coordinates will be returned.
        :return:
        """
        params = {
            "commanderName": cmdrname,
            "apiKey": api_key,
            "showId": showId,
            "showCoordinates": showCoordinates,
        }
        json = cls.query(params)
        if json["msgnum"] == 201:
            # 201 Missing commander name
            raise exception.CommanderNotFoundError(cls.url, params)
        elif json["msgnum"] == 203:
            # 203 Commander name / API Key not found
            params = params + "," + json["msgnum"]
            raise exception.ApiKeyNotFoundError(cls.url, params)
        return json


class SetUpdateComment(ApiEntryPoint):
    """
    Set/Update a comment
    """

    url = ApiEntryPoint.url_edsm + "logs-v1/set-comment"

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

    def set_Comment(cls, cmdrname, api_key, systemName, systemId, comment):
        """
        Set/Update a comment

        :param cmdrname: The name of the commander as registered on EDSM.
        :param api_key: The API Key associate the commander name with his account.
        :param systemName: Use the systemName parameter to filter flight logs by system name.
        :param systemId: By passing directly our intenral ID, you can override the system name.
        :param comment: The comment you wish to store.
        :return: json
        """
        params = {
            "commanderName": cmdrname,
            "apiKey": api_key,
            "systemName": systemName,
            "systemId": systemId,
            "comment": comment,
        }
        json = cls.query(params)
        if json["msgnum"] == 201:
            # 201 Missing commander name
            raise exception.CommanderNotFoundError(cls.url, params)
        elif json["msgnum"] == 202:
            # 202 Missing APIkey
            params = params + "," + json["msgnum"]
            raise exception.ApiKeyNotFoundError(cls.url, params)
        elif json["msgnum"] == 203:
            # 203 Commander name / API Key not found
            params = params + "," + json["msgnum"]
            raise exception.ApiKeyNotFoundError(cls.url, params)
        elif json["msgnum"] == 204:
            # 204	Missing comment
            raise exception.MissingComment(cls.url, params)
        elif json["msgnum"] == 301:
            # 301	Missing system name
            raise exception.MissingSystemName(cls.url, params)
        elif json["msgnum"] == 302:
            # 302	System not in database
            raise exception.SystemNotInDatabase(cls.url, params)
        elif json["msgnum"] == 303:
            # 303	System probably non existant
            raise exception.SystemProbablyNonExistant(cls.url, params)
        elif json["msgnum"] == 305:
            # 305 System name is too long or invalid.
            raise exception.SystemTooLongInvalid(cls.url, params)
        return json


class GetComment(ApiEntryPoint):
    """
    Get a comment
    """

    url = ApiEntryPoint.url_edsm + "logs-v1/get-comment"

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

    def get_Comment(cls, cmdrname, api_key, systemName, systemId):
        """
        Get a comment

        :param cmdrname: The name of the commander as registered on EDSM.
        :param api_key: The API Key associate the commander name with his account.
        :param systemName: Use the systemName parameter to filter flight logs by system name.
        :param systemId: By passing directly our intenral ID, you can override the system name.
        :return: json

        """
        params = {
            "commanderName": cmdrname,
            "apiKey": api_key,
            "systemName": systemName,
            "systemId": systemId,
        }
        json = cls.query(params)
        if json["msgnum"] == 101:
            # 101	 OK, but no private comment stored for this system
            raise exception.NoPrivateCommentStored(cls.url, params)
        elif json["msgnum"] == 201:
            # 201 Missing commander name
            raise exception.CommanderNotFoundError(cls.url, params)
        elif json["msgnum"] == 202:
            # 202 Missing APIkey
            params = params + "," + json["msgnum"]
            raise exception.ApiKeyNotFoundError(cls.url, params)
        elif json["msgnum"] == 203:
            # 203 Commander name / API Key not found
            params = params + "," + json["msgnum"]
            raise exception.ApiKeyNotFoundError(cls.url, params)
        elif json["msgnum"] == 301:
            # 301	Missing system name
            raise exception.MissingSystemName(cls.url, params)

        elif json["msgnum"] == 302:
            # 302	System not in database
            raise exception.SystemNotInDatabase(cls.url, params)
        elif json["msgnum"] == 303:
            # 303	System probably non existant
            raise exception.SystemProbablyNonExistant(cls.url, params)
        elif json["msgnum"] == 305:
            # 305 System name is too long or invalid.
            raise exception.SystemTooLongInvalid(cls.url, params)
        return json


class GetComments(ApiEntryPoint):
    """
    Get comments
    """

    url = ApiEntryPoint.url_edsm + "logs-v1/get-comments"

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

    def get_Comments(cls, cmdrname, api_key, startDateTime, showId):
        """
        Get comments

        :param cmdrname: The name of the commander as registered on EDSM.
        :param api_key: The API Key associate the commander name with his account.
        :param startDateTime: If you only want to receive flight logs after a specific date & time, use this parameter.
        :param showId: Set to 1 if you want to get our internal id. Useful to handle duplicated name systems of the game.
        :return: json
        """
        params = {
            "commanderName": cmdrname,
            "apiKey": api_key,
            "startDateTime": startDateTime,
            "showId": showId,
        }
        json = cls.query(params)
        if json["msgnum"] == 201:
            # 201 Missing commander name
            raise exception.CommanderNotFoundError(cls.url, params)
        elif json["msgnum"] == 202:
            # 202 Missing APIkey
            params = params + "," + json["msgnum"]
            raise exception.ApiKeyNotFoundError(cls.url, params)
        elif json["msgnum"] == 203:
            # 203 Commander name / API Key not found
            params = params + "," + json["msgnum"]
            raise exception.ApiKeyNotFoundError(cls.url, params)
        return json
