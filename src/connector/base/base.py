import requests

from connector import base as exception


class ApiEntryPoint:
    """
    Parent class for all API endpoints.
    """

    url_edsm = "https://www.edsm.net/api-"
    url_eddb = "https://eddb.io/archive/v6/"
    url_bgs = "https://elitebgs.app/api/ebgs/v5/"
    url_spansh = "https://www.spansh.co.uk/api/"

    def __init__(self):
        pass

    def query(cls, params={}):
        """
        Queries the API endpoint with the given parameters.

        :param params: the parameters to append to the base URL
        """

        response = requests.get(cls.url, params=params)
        if response.status_code != 200:
            raise exception.ServerError(cls.url, params)
        json = response.json()
        if not json:
            raise exception.NotFoundError()
        return json
