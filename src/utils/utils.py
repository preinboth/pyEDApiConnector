import math


def filterStationsByType(system, exclude_type: list):
    """
    filter a List of station by exluded types

    :param system: the system
    :param exclude_type: List of exluded station types

    :return: filtered
    """
    # filtered = []
    # for station in system['stations']:
    #     if (station['type']) not in exclude_type:
    #         filtered.append(station)
    # print('Hallo')
    # system['stations'] == filtered
    # print('Hallo')

    for station in system["stations"]:
        if (station["type"]) in exclude_type:
            system["stations"].remove(station)
    for station in system["stations"]:
        if (station["type"]) in exclude_type:
            print(station["type"])
    return system


def calculate_distance(coords_1, coords_2):
    """
    calculate the distance for two systems

    :param coords_1: start
    :param coords_2: target
    :return:
    """
    distance = math.sqrt(
        (coords_1["coords"]["x"] - coords_2["coords"]["x"]) ** 2
        + (coords_1["coords"]["y"] - coords_2["coords"]["y"]) ** 2
        + (coords_1["coords"]["z"] - coords_2["coords"]["z"]) ** 2
    )
    distance = "{0:.2f}".format(distance)
    return distance
