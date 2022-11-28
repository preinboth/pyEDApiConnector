import json
import logging
import time

import requests

from connector.base.base import ApiEntryPoint
from connector.edsm.edsm_cntl import EdsmCntl
from utils.utils import calculate_distance

log = logging.getLogger(__name__)


class RoutePlanner(ApiEntryPoint):
    def __init__(self):
        pass

    def planRoute(self, system1, system2, efficiency, range):
        __edsm_cntl = EdsmCntl()
        s1_coords = __edsm_cntl.getSystemCoordinate(system1)
        s2_coords = __edsm_cntl.getSystemCoordinate(system2)
        job = self.__getRoute(s1_coords, s2_coords, efficiency, range)
        route = self.__getResults(job)
        return route

    def __getRequestHeaders(self):
        __version__ = "v0.0.1"
        REQUEST_HEADERS = {"user-agent": f"SpanshApi_{__version__}"}
        return REQUEST_HEADERS

    def __getRoute(self, coords_1, coords_2, efficiency, range):
        calculate_distance(coords_1, coords_2)
        REQUEST_HEADERS = self.__getRequestHeaders()
        payload = {
            "efficiency": efficiency,
            "range": range,
            "from": coords_1["name"],
            "to": coords_2["name"],
        }
        response = requests.post(
            "https://www.spansh.co.uk/api/route", data=payload, headers=REQUEST_HEADERS
        )
        job = eval(response.text)

        if "error" in job:
            # TODO: Raise exception
            # log_function(f"ERROR OCCURRED: {job['error']}")
            quit()
        return job

    def __getResults(self, job):
        REQUEST_HEADERS = self.__getRequestHeaders()
        # Wait for job completion
        while 1:
            response = requests.get(
                "https://www.spansh.co.uk/api/results/" + job["job"],
                headers=REQUEST_HEADERS,
            )
            response_dict = json.loads(response.text)
            if response_dict["status"] == "ok":
                # log_function("Route successfully received")
                break
            time.sleep(1)
        systems = response_dict["result"]["system_jumps"]
        return systems

# class _GenericRoute(ApiEntryPoint):
#     url = ApiEntryPoint.url_edsm + "generic/route"
#
#     def query(cls, params):
#         """
#          create the query based on the parameters and retrieve data from Api
#
#          :param params:
#          :return: json
#          """
#         try:
#             json = super().query(params)
#         except exception.NotFoundError:
#             raise exception.SystemNotFoundError(params)
#         return json
#
#
# class _Plotter(ApiEntryPoint):
#     url = ApiEntryPoint.url_edsm + "plotter"
#
#     def query(cls, params):
#         """
#          create the query based on the parameters and retrieve data from Api
#
#          :param params:
#          :return: json
#          """
#         try:
#             json = super().query(params)
#         except exception.NotFoundError:
#             raise exception.SystemNotFoundError(params)
#         return json
