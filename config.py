""" CONFIG FILE """
import math

updates = True # If planets positions update each frame.  Does not affect collisions
collisions = True # If planets can collide and consequently merge
clr_changes_on_impact = False # If planets become red when collided
bright_planets = True # Whether planets emit light or not
g_constant = 6.67408 * 10 ** (-11) # The universal gravitational constant
max_proximity = 0 # The closest two planets can be (from surface to surface)
max_vel = 670560 # The fastest valid velocity of a planet.  Obtained this from some article

rotate_speed_min = 0 # Speed at which planet rotates.
rotate_speed_max = 0

# Variables relating to the initial parameters of the planets =
init_rad_min = 10 ** 6 # Radii of planets, measured in metres.
init_rad_max = 10 ** 9
init_mass_min = 10 ** 23 # Measured in kilograms
init_mass_max = 10 ** 30
init_max_pos = 2.5 * 10 ** 10 # Farthest rectangular distance from origin each planet can spawn
init_max_vel = 1000 # Fastest rectangular speed, measured in metres/second

dt = 150 # Time increment (in seconds)
