class ServerError(Exception):
    """
    Exception used for everything server-related; basically every time the API
    doesn’t reply with a `200 OK`, this is what’s going to be raised.
    """

    def __str__(self):
        return "Server Error fetching {}, params: {}.".format(self.args[0],
                                                              self.args[1])

    pass


class NotFoundError(Exception):
    """

    """


class SystemNotFoundError(NotFoundError):
    def __str__(self):
        params = self.args[0]
        if 'systemName' in params:
            return "System {} not found.".format(params['systemName'])
        else:
            return "Systems {} not found.".format(params['systemName[]'])


class CommanderNotFoundError(NotFoundError):
    def __str__(self):
        params = self.args[0]
        return "Commander {} not found or has not made his flight logs public.".format(params['commanderName'])
