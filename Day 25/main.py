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
# print(data) 

# data_list = data["temp"].to_list()
# print(data_list) 
# avg_temp = sum(data_list)/len(data_list)
# print(avg_temp)
     
print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_f = monday_temp * 9/ 5 + 32
print(monday_temp_f)