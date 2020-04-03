from __future__ import absolute_import
"""~~~DON'T USE THIS CODE YET~~~
Still a lot of work todo before it's a game"""
import logging
# import math
import random

from unmanned_vehicle import Robot
from planet import ConstructionPackage
from armament import hit_or_miss
from coordinates import bdc, cbd, ttt, dst, f_ttt

import threading

# Machine Control simulation software.

TIMER_VAL = 5
MISSILE_RANGE = 20000

# robots_list = ["grader"]
robots_list = ["grader", "dozer", "grader_2", "digger_1", "digger_2"]
available_engines = {}
active_robots = {}
logging.basicConfig(level=logging.DEBUG)


# setup the package
ruby_jo = ConstructionPackage("Ruby Jo", 0.0, 0.0, 0.0, 5000.0, 5000.0, 300.0)
ruby_jo.target = [random.randint(ruby_jo.min_x, ruby_jo.max_x), random.randint(ruby_jo.min_y, ruby_jo.max_y),
                  random.randint(ruby_jo.min_z, ruby_jo.max_z)]

for y in robots_list:
    active_robots[y] = Robot(y)
    active_robots[y].easting = float(random.randint(ruby_jo.min_x, ruby_jo.max_x))
    active_robots[y].northing = float(random.randint(ruby_jo.min_y, ruby_jo.max_y))


def rolling_thunder():
    threading.Timer(TIMER_VAL, rolling_thunder).start()
    kill_bots = []
    for x in active_robots:
        east = active_robots[x].easting
        north = active_robots[x].northing
        elev = active_robots[x].elevation

        # BDC to target.
        bdc_to_target = bdc([east, north], (ruby_jo.target[0], ruby_jo.target[1]))
        bearing = bdc_to_target["bearing"]
        distance = bdc_to_target["distance"]

        if ruby_jo.cycle == 0:
            active_robots[x].speed = random.randint(1, active_robots[x].max_speed)
            print("status of " + active_robots[x].robot_id + " Bg: " + str(bearing) + " DTT: " + str(distance) +\
                  "\nSpeed is set to: " + str(active_robots[x].speed) + "kph")
        else:
            # print active_robots[x].speed
            time_to_target = f_ttt(ttt(active_robots[x].speed, distance))
            print("time to target: %d:%02d.%02d" % (time_to_target[0], time_to_target[1], time_to_target[2]))

            # update_locations()
            new_coordinates = cbd([east, north, elev], bearing, dst(active_robots[x].speed, 5))
            active_robots[x].easting = new_coordinates["new_e"]
            active_robots[x].northing = new_coordinates["new_n"]
            active_robots[x].elevation = new_coordinates["new_z"]

            print("Status of " + active_robots[x].robot_id + ":\n")
            # scan_nearby_area()

            for robots in active_robots:
                if active_robots[robots].robot_id != active_robots[x].robot_id:
                    bdc_to_alt = bdc([east, north], (active_robots[robots].easting, active_robots[robots].northing))
                    bdc_to_alt = bdc_to_alt["distance"]
                    # print "Dist to " + active_robots[robots].robot_id + ": " + str(bdc_to_alt["distance"])
                    print("Dist to " + active_robots[robots].robot_id + ": " + str(bdc_to_alt))
                    if bdc_to_alt < MISSILE_RANGE:
                        print("firing at " + active_robots[robots].robot_id)
                        if hit_or_miss():
                            print("Reporting target destroyed")
                            # add to kill list
                            kill_bots.append(active_robots[robots].robot_id)
            # check_for_collisions()
            # check_priorities()
            # check_instruments()
            # check_for_actions()
            # check_new_communications()
            # make_required_changes()
            # transmit_status_to_owner()
            print("E: " + str(east) + " N: " + str(north) + " Bg: " + str(bearing) + " D: " + str(distance) +\
                  " ++ " + "time to target: %d:%02d.%02d" % (time_to_target[0], time_to_target[1], time_to_target[2]))
            print("========================================================================")

    ruby_jo.cycle += 1
    # print kill_bots
    for x in kill_bots:
        if x in active_robots:
            # print "active_robots", active_robots
            del active_robots[x]
            # print "revised active_robots", active_robots


rolling_thunder()
