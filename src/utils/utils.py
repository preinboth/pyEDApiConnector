import math


def filterStationsByType(system, exclude_type: list):
    """
    filter a List of station by exluded types

    :param system: the system
    :param exclude_type: List of exluded station types

    :return: filtered
    """
    for i in system['stations']:
        # print(x['type'])
        if (i['type']) in exclude_type:
            system['stations'].remove(i)
    print('Hallo')
    return system


def calculate_distance(coords_1, coords_2):
    """
    calculate the distance for two systems

    :param coords_1: start
    :param coords_2: target
    :return:
    """
    distance = math.sqrt((coords_1['coords']["x"] - coords_2['coords']["x"]) ** 2 + (
        coords_1['coords']["y"] - coords_2['coords']["y"]) ** 2 + (
                             coords_1['coords']["z"] - coords_2['coords']["z"]) ** 2)
    distance = '{0:.2f}'.format(distance)
    return distance
