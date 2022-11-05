from connector.base import exception
from connector.base.base import ApiEntryPoint


class CommanderRanks(ApiEntryPoint):
    url = ApiEntryPoint.url_edsm + "-commander-v1/get-ranks"

    def __init__(self):
        pass

    def query(cls, params):
        try:
            json = super().query(params)
        except exception.NotFoundError:
            raise exception.SystemNotFoundError(params)
        return json


class CommanderCredits(ApiEntryPoint):
    url = ApiEntryPoint.url_edsm + "-commander-v1/get-credits"

    def __init__(self):
        pass

    def query(cls, params):
        try:
            json = super().query(params)
        except exception.NotFoundError:
            raise exception.SystemNotFoundError(params)
        return json


class CommanderMaterials(ApiEntryPoint):
    url = ApiEntryPoint.url_edsm + "-commander-v1/get-materials"

    def __init__(self):
        pass

    def query(cls, params):
        try:
            json = super().query(params)
        except exception.NotFoundError:
            raise exception.SystemNotFoundError(params)
        return json
