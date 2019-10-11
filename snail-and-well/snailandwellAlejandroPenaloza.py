well_height = 125
daily_advance = 30
night_retreat = 20
accumulated_distance = 0
number_of_days = 0

while True:
    number_of_days += 1
    accumulated_distance += daily_advance
    if accumulated_distance >= well_height:
        print("Days =", number_of_days, sep=" ")
        break
    else:
        accumulated_distance -= night_retreat

advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
advance = 0
count = 0
daily_travel_in_well = []
for daily_travel in advance_cm:
    advance += daily_travel
    count += 1
    if advance >= well_height:
        print("Days =", count, sep=" ")
        break
    daily_travel_in_well.append(daily_travel)

daily_travel_in_well.append(well_height - sum(daily_travel_in_well))

#Maximum and minimum daily displacement
print("Maximum daily displacement: ", max(daily_travel_in_well), " cm\n")
print("Minimum daily displacement: ", min(daily_travel_in_well), " cm")

#Average progress
average_progress = sum(daily_travel_in_well) / count
print("Its average progress is ", average_progress, " cm by day")

#Standard deviation
mean = average_progress

squared_deviation_list = []
for i in daily_travel_in_well:
    squared_deviation = (i - mean)**2
    squared_deviation_list.append(squared_deviation)

import math
variance = sum(squared_deviation_list) / count
standard_deviation = math.sqrt(variance)
print("Its standard deviation is ", standard_deviation)
