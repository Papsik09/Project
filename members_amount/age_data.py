"""
Here will be age data
"""
from main_data import birthday_data


numbers_split = birthday_data.split("/")

day = numbers_split[0]
mounth = numbers_split[1]
year = numbers_split[2]
print(day,mounth,year)