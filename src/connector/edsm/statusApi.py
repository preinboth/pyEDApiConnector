from connector.base.base import ApiEntryPoint


class ServerStatus(ApiEntryPoint):
    url = ApiEntryPoint.url_edsm + "status-v1/elite-server"

    def __init__(self):
        pass

    def getEliteServerStatus(cls):
        """
        Get Elite: Dangerous server status

        :return: json
        """
        return cls.query()


# --------------------------------------
server_status = ServerStatus()
