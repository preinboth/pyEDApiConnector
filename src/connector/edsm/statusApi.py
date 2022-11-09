from connector.base import exception
from connector.base.base import ApiEntryPoint


class ServerStatus(ApiEntryPoint):
    url = ApiEntryPoint.url_edsm + "status-v1/elite-server"

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

    def getEliteServerStatus(self):
        """
        getEliteServerStatus

        :return: jeson
        """
        return self.query()


# --------------------------------------
server_status = ServerStatus()
