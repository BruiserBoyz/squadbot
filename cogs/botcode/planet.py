class ConstructionPackage:
    def __init__(self, package_name, min_x, min_y, min_z, max_x, max_y, max_z ):
        self.cycle = 0
        self.min_x = min_x
        self.min_y = min_y
        self.min_z = min_z
        self.max_x = max_x
        self.max_y = max_y
        self.max_z= max_z
        self.package_name = package_name
        self.atmosphere = ""
        self.temperature_range = ""
        self.main_terrain = ""
        self.sensors = []
        self.radar = {"range": 15.0}
        self.target = [0.0, 0.0, 0.0]