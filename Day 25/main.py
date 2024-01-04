# with open("/home/amul/Documents/anjela python/Day 25/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("/home/amul/Documents/anjela python/Day 25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temprature = []
#     for row in data:
#         if row[1] != "temp":
#             temprature.append(int(row[1]))     
#     print(temprature)

import pandas

data = pandas.read_csv("/home/amul/Documents/anjela python/Day 25/weather_data.csv")
print(data)       