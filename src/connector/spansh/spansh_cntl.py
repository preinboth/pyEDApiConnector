from connector.spansh.spanshApi import RoutePlanner


class SpanshCntl:
    __route_planner = RoutePlanner()

    def __init__(self):
        pass

    def routePlanner(self, system1, system2, efficiency, range):
        return self.__route_planner.planRoute(system1, system2, efficiency, range)
