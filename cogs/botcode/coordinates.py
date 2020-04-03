from math import radians, sin, cos, sqrt, atan, degrees


def bdc(coordinate_1, coordinate_2):
    """Bearing and Distance from Coordinates."""
    c1e = coordinate_1[0]
    c1n = coordinate_1[1]
    c2e = coordinate_2[0]
    c2n = coordinate_2[1]
    # logging.info(("fn: move, inputs", c1e, c1n, c2e, c2n))

    # Distance
    delta_e = c2e - c1e
    delta_n = c2n - c1n
    # logging.info("delta_e: " + str(delta_e) + " delta_n: " + str(delta_n))
    distance = sqrt(delta_e ** 2 + delta_n ** 2)
    # logging.info("distance: " + str(distance))

    # Bearing
    # Check for E W, N S movement.
    if delta_n == 0:
        bearing = 90.0
        if delta_e < 0:
            bearing = 270.0

    elif delta_e == 0:
        bearing = 0.0
        if delta_n < 0:
            bearing = 180.0

    else:
        tan_results = delta_n / delta_e
        tan_results = atan(tan_results)
        tan_results = degrees(tan_results)
        # logging.info("tan_results: " + str(tan_results))

        if delta_e > 0 and delta_n > 0:
            bearing = 90 - abs(tan_results)
        # TODO refactor, chain.
        elif delta_e > 0 and delta_n < 0:
            bearing = 90 + abs(tan_results)
        elif delta_e < 0 and delta_n < 0:
            bearing = 270 - abs(tan_results)
        else:
            bearing = 270 + abs(tan_results)

    # logging.info("bearing: " + str(bearing))
    return {"bearing": round(bearing, 3), "distance": round(distance, 3)}


def cbd(start_coords, bearing, distance):
    # Coordinates from Bearing and Distance
    # logging.info("fn: move")
    sin_dist = sin(radians(bearing))
    cos_dist = cos(radians(bearing))
    move_opposite = sin_dist * distance
    move_adjacent = cos_dist * distance
    # hyp_check = sqrt(move_opposite ** 2 + move_adjacent ** 2)

    move_elevation = 0.0

    # logging.info((move_opposite, move_adjacent, hyp_check))

    # logging.info("fn: update_locations")
    new_e = start_coords[0] + move_opposite
    new_n = start_coords[1] + move_adjacent
    new_z = start_coords[2] + move_elevation
    return {"new_e": round(new_e, 3), "new_n": round(new_n, 3), "new_z": round(new_z,  3)}


def dst(movement_speed, movement_time):
    """Returns distance from speed and time"""
    # logging.info("fn: move")
    # logging.info("determine distances moved")
    distance_moved = movement_time * movement_speed * 1000 / 3600
    return distance_moved


def ttt(movement_speed, movement_distance):
    # Calculates Time to Target
    time_to_target = movement_distance / 1000 / movement_speed
    return time_to_target


def f_ttt(time_to_target_in):
    # Formats time to target
    time_to_target_h = int(time_to_target_in)
    time_to_target_m = (time_to_target_in * 60) % 60
    time_to_target_s = (time_to_target_in * 3600) % 60
    return [time_to_target_h, time_to_target_m, time_to_target_s]

# test_time_to_target = time_to_target(20, 75537.71)
# test_format_time_to_target = format_time_to_target(test_time_to_target)

# print test_format_time_to_target
