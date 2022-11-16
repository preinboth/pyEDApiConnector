import math


def filterStationsByType(stations: list, exlude_type: list):
    """
    filter a List of station by exluded types

    :param stations: List of stations
    :param exlude_type: List of exluded station types
    :return:
    """
    filtered = []
    for station in stations['stations']:
        if station.get("type") not in exlude_type:
            filtered.append(station)
    return filtered


def calculate_distance(coords_1, coords_2):
    """
    calculate the distance for two systems

    :param coords_1:
    :param coords_2:
    :return:
    """
    distance = math.sqrt((coords_1['coords']["x"] - coords_2['coords']["x"]) ** 2 + (
        coords_1['coords']["y"] - coords_2['coords']["y"]) ** 2 + (
                             coords_1['coords']["z"] - coords_2['coords']["z"]) ** 2)
    distance = '{0:.2f}'.format(distance)
    return distance
