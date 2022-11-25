import math

def time_on_starship(years, v):
    gamma = 1 / (math.sqrt(1 - v**2))
    ship_years = years / gamma
    return ship_years

earth_years = float(input("Earth years: "))
speed = float(input("Speed (factor of c): "))
ship_years = time_on_starship(earth_years, speed)

print(ship_years)