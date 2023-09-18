# Calculate the velocity required to escape a circular orbit of Earth,
# depending on a user-entered orbital distance.

import math

escape_velocity_meters_per_sec = 0  # Required velocity to escape orbit
grav_constant = 6.67384e-11  # Earth's gravitational constant
earth_mass_kilograms = 5.972e24  # Mass of the Earth

# Sea level is roughly 3,000,000 meters from the center of the Earth
radius_meters = float(input('Enter distance from center of Earth: '))
print()

if radius_meters < 6317000:  # 6317 km is the average radius of the Earth
    escape_velocity_meters_per_sec = 0  # No escape possible!
    print('Houston, we have a problem')


else:
    standard_grav_param = grav_constant * earth_mass_kilograms
    escape_velocity_meters_per_sec = math.sqrt(2 * standard_grav_param / radius_meters)
    print(f'Thrust to {escape_velocity_meters_per_sec:.0f} m/s to escape these Earthly shackles.')
