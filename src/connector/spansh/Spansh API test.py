import json
import math
import time

import requests

from connector.edsm.edsm_cntl import EdsmCntl

edsm_cntl = EdsmCntl()


def calculate_distance(coords_1, coords_2):
    distance = math.sqrt(
        (coords_1["x"] - coords_2["x"]) ** 2
        + (coords_1["y"] - coords_2["y"]) ** 2
        + (coords_1["z"] - coords_2["z"]) ** 2
    )
    distance = "{0:.2f}".format(distance)
    return distance


s1_coords = edsm_cntl.getSystemCoordinate("HIP 117029")
s2_coords = edsm_cntl.getSystemCoordinate("Drojia YW-B d13-4")

calculated = calculate_distance(s1_coords["coords"], s2_coords["coords"])
print("calculated distance: " + calculated)

__version__ = "v0.0.1"
REQUEST_HEADERS = {"user-agent": f"SpanshApi_{__version__}"}
payload = {
    "efficiency": 1,
    "range": 20,
    "from": "HIP 117029",
    "to": "Drojia YW-B d13-4",
}
response = requests.post(
    "https://www.spansh.co.uk/api/route", data=payload, headers=REQUEST_HEADERS
)
job = eval(response.text)

if "error" in job:
    # TODO: Raise exception
    # log_function(f"ERROR OCCURRED: {job['error']}")
    quit()

# Wait for job completion
while 1:
    response = requests.get(
        "https://www.spansh.co.uk/api/results/" + job["job"], headers=REQUEST_HEADERS
    )
    response_dict = json.loads(response.text)
    if response_dict["status"] == "ok":
        # log_function("Route successfully received")
        break
    time.sleep(1)
systems = response_dict["result"]["system_jumps"]
print("Hallo")
