# with open(file="weather_data.csv") as weather_data:
#     wt_data = weather_data.readlines()
#     data = []
#     for each_data in wt_data:
#         data.append(each_data.strip())

# print(data)

# import csv

# with open(file="weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         try:
#             temp = int(row[1])
#             temperatures.append(int(row[1]))
#         except ValueError:
#             pass

# print(temperatures)

import pandas as pd
import numpy as np
import pprint

# data = pd.read_csv("weather_data.csv")
# print(data["temp"])
# print(type(data)) # <- Dataframe object
# print(type(data["temp"])) # <- Series object
# data_dict = data.to_dict()

# pprint.pprint(data_dict)


# Calculating average temperature

# temp_list = data["temp"].to_list()
# avg_temp = sum(temp_list) / len(temp_list)
# print(f"[normal]average temp: {round(avg_temp, 2)} degreeC")

# Using numpy
# avg_of_temp = np.average(temp_list)
# print(f"[numpy]average temp: {round(avg_of_temp, 2)} degreeC")

# Using pandas method
# print(f"[pandas]average temp: {round(data["temp"].mean(), 2)} degreeC")

# Get Data In Row
# print(data[data["day"] == "Monday"])

# Get the Data of highest temperature
# highest_temp = data["temp"].max()
# print(data[data.temp == highest_temp])

# monday = data[data.day == "Monday"]
# print(monday)
# monday_tempC = monday["temp"][0]
# print(monday_tempC)
# monday_tempF = monday_tempC * 9 / 5 + 32
# print(f"Temp in degreeF of Monday: {monday_tempF}")

# Create a dataframe from scratch
data_dict = {"student": ["Amy", "James", "Angela"], "score": [76, 56, 65]}
data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")
