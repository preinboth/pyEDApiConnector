class ServerError(Exception):
    """
    Exception used for everything server-related; basically every time the API
    doesn’t reply with a `200 OK`, this is what’s going to be raised.
    """

    def __str__(self):
        return "Server Error fetching {}, params: {}.".format(
            self.args[0], self.args[1]
        )


class NotFoundError(Exception):
    """ """


class SystemNotFoundError(NotFoundError):
    def __str__(self):
        params = self.args[0]
        if "systemName" in params:
            return "System {} not found.".format(params["systemName"])
        else:
            return "Systems {} not found.".format(params["systemName[]"])


class CommanderNotFoundError(NotFoundError):
    def __str__(self):
        params = self.args[0]
        return "Commander {} not found or has not made his flight logs public.".format(
            params["commanderName"]
        )


class MissingCmdrName(NotFoundError):
    def __str__(self):
        self.args[0]
        return "Missing commander name"


class ApiKeyNotFoundError(NotFoundError):
    def __str__(self):
        params = self.args[0]
        return "Commander name/API Key not found {} not found.".format(
            params["commanderName"]
        )


class CmdrNoRanksStored:
    def __str__(self):
        self.args[0]
        return "No ranks are stored in our database yet, or the apiKey was not provided on a private profile."


class SystemNotInDatabase(Exception):
    def __str__(self):
        params = self.args[0]
        if "systemName" in params:
            return "System {} not found.".format(params["systemName"])
        else:
            return "Systems {} not found.".format(params["systemName[]"])


class SystemProbablyNonExistant:
    def __str__(self):
        params = self.args[0]
        if "systemName" in params:
            return "System {} probably non existant.".format(params["systemName"])
        else:
            return "Systems {} probably non existant.".format(params["systemName[]"])


class RateLimitExceeded:
    def __str__(self):
        self.args[0]
        return "Rate limit exceeded"


class SystemTooLongInvalid:
    def __str__(self):
        params = self.args[0]
        if "systemName" in params:
            return "System {} is too long or invalid.".format(params["systemName"])
        else:
            return "Systems {} is too long or invalid.".format(params["systemName[]"])


class NoPrivateCommentStored:
    def __str__(self):
        params = self.args[0]
        return "OK, but no private comment stored for this System {}".format(
            params["systemName"]
        )


class MissingComment:
    def __str__(self):
        self.args[0]
        return "Missing comment"


class MissingSystemName:
    def __str__(self):
        self.args[0]
        return "Missing system name"
