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

# data = pandas.read_csv("/home/amul/Documents/anjela python/Day 25/weather_data.csv")
# print(data) 

# data_list = data["temp"].to_list()
# print(data_list) 
# avg_temp = sum(data_list)/len(data_list)
# print(avg_temp)
     
# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/ 5 + 32
# print(monday_temp_f)


squirrel_data = pandas.read_csv("/home/amul/Documents/anjela python/Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# print(squirrel_data)

# data_list = squirrel_data["Primary Fur Color"].to_list()
# print(data_list)

gray_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

print(black_squirrel_count)

data_dict = {
    "Fur color" : ["Gray","Cinnamon","Red"],
    "Count" : [gray_squirrel_count,red_squirrel_count,black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
csv_file = df.to_csv()
print(csv_file)
