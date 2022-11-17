import requests
from src.connector.edsm.outfittingApi import outfitting

exclude = ['Fleet Carrier', 'Odyssey Settlement']
systems = ["GaCrux", "Waq", "Hotaiko"]
# ---------------------------------------------
# json_stations = station.getStation(systems)

# --------------------------------------------

parameters = {'systemName': "GaCrux"}
json = outfitting.getOutfittingByName("GaCrux", "Ramanujan Terminal", exclude)
print('Hello')
