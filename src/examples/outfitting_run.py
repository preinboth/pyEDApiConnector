import requests
from src.connector.edsm import edsmCntl
from src.connector.edsm.outfittingApi import outfitting
from src.connector.edsm.systemApi import Station

exclude = ['Fleet Carrier', 'Odyssey Settlement']
systems = ["GaCrux", "Waq", "Hotaiko"]
# ---------------------------------------------
json_stations = station.getStation(systems)
print('Hello')
# --------------------------------------------
url = "https://www.edsm.net/api-system-v1/stations/outfitting"

response = requests.get(cls.url, params=params)
if response.status_code != 200:
    raise exception.ServerError(url, params)
json = response.json()
if not json:
    raise exception.NotFoundError()
