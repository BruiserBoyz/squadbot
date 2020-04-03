# import propulsion_system
# this just assembles your bot.
engine_list = [
    ["basic electric", 5.0, 20.0, 5.0, 1, 150],
    ["medium electric", 10.0, 45, 4, 2, 300],
    ["high electric", 15.5, 80, 3.5, 3, 500]]


class RobotEngine:
    def __init__(self, engine_name, engine_weight, engine_speed, engine_power_weight_ratio, engine_class, engine_cost):
        self.engine_name = engine_name
        self.engine_weight = engine_weight
        self.engine_speed = engine_speed
        self.engine_power_weight_ratio = engine_power_weight_ratio
        # for every kilogram, you lose this much speed
        self.engine_class = engine_class
        self.engine_cost = engine_cost


class Robot:
    """basic machine guidance class"""
    def __init__(self, robot_id):
        self.robot_id = robot_id
        self.easting = 0.0
        self.northing = 0.0
        self.elevation = 0.0
        self.bearing = 0.0
        self.speed = 0
        self.max_speed = 200.0
        self.base_weight = 5
        self.overall_weight = self.base_weight
        self.battery_array = [[5, 100.0]]
        self.fuel_array = [0.0]
        self.body_components = {}
        self.weapon_components = {}
        self.engine_components = {'engine': 1}
        self.sensors = {}

    def calculate_weight(self):
        # list anything with a weight, sum the values, add to base weight
        # probably best to create an array of items_with_weight
        battery_weight = 0
        for x in self.battery_array:
            battery_weight += x[0]

        self.overall_weight += battery_weight
