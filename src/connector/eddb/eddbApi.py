from connector.base import exception
from connector.base.base import ApiEntryPoint


class Attractions(ApiEntryPoint):
    """
    Attractions
    """

    url = ApiEntryPoint.url_eddb + "attractions.json"

    def __init__(self):
        pass

    def query(cls, params):
        try:
            json = super().query(params)
        except exception.NotFoundError:
            raise exception.SystemNotFoundError(params)
        return json

    def get_attractions_all(cls):
        json = cls.query({})
        return json

    def get_attractions_by_name(cls, name):
        data = cls.query({"name": name})
        filtered = []
        for i in data:
            if i["name"] == name:
                filtered.append(i)
        return filtered
