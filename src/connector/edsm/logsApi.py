from connector.base import exception
from connector.base.base import ApiEntryPoint


class LogsFlightEntries(ApiEntryPoint):
    url = ApiEntryPoint.url_edsm + "-logs-v1/get-logs"

    def __init__(self):
        pass

    def query(cls, params):
        try:
            json = super().query(params)
        except exception.NotFoundError:
            raise exception.SystemNotFoundError(params)
        return json
