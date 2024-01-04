# with open("/home/amul/Documents/anjela python/Day 25/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv

with open("/home/amul/Documents/anjela python/Day 25/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        print(row)