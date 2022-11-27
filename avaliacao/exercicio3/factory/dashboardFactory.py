from singleton.dashboardSingleton import DashboardSingleton

class DashboardFactory():
    @classmethod
    def create_instance(self):
        return DashboardFactory.instance__()