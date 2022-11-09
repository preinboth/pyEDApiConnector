from src.connector.eddb.eddbApi import Attractions


class EddbCntl():
    """

    """
    __eddb_attractions = Attractions()

    def __init__(self):
        pass

    def get_attractions_all(self):
        """
        get all attractions (Attention: large amount of data)

        :return:  List
        """
        return self.__eddb_attractions.get_attractions_all()

    def get_attractions_by_name(self, name):
        """
        get attraction by name of attraction

        :param name: Use the name parameter to filter flight logs by attraction name.
        :return: List
        """
        return self.__eddb_attractions.get_attractions_by_name(name)
