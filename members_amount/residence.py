"""
Here will be residence data input
"""

from main_data import residence_data

places = residence_data.split(",")

city = places[0]
country = places[1]

print(city,country)