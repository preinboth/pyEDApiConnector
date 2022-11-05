from connector.base import base


class StatusApi(base.ApiEntryPoint):
    url = base.ApiEntryPoint.url_edsm + "status-v1/elite-server"

    @classmethod
    def getServerStatus(self):
        return self.query()

    def checkEliteServerStatus(self):
        pass
        # json = requests.get(url)
