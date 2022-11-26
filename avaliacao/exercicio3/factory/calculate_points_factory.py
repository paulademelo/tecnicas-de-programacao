from singleton.dashboard_singleton import CalculatePointsSingleton

class CalculatePointsFactory:
    @classmethod
    def create_instance(self):
        return CalculatePointsSingleton.instance__()