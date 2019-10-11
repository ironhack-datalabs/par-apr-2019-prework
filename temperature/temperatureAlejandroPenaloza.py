#PROCESSOR TEMPERATURE

temperatures_C = [33,66,65,0,59,60,62,64,70,76,80,69,80,83,68,79,61,53,50,49,53,48,45,39]

#Minimum temperature
min_temperature = min(temperatures_C)
print("Minimum temperature is ", min_temperature)

#Maximum temperature
max_temperature = max(temperatures_C)
print("Maximum temperature is ", max_temperature)

#Temperatures equal or greater than 70 degrees C
temp_greater_or_equal_70 = []
for temp in temperatures_C:
    if temp >= 70:
        temp_greater_or_equal_70.append(temp)
print("Temperatures greater or equal to 70 degrees C are: ", temp_greater_or_equal_70)

#Average temperatures throughout the day
mean = sum(temperatures_C)/len(temperatures_C)
print("Average of temperatures throughout the day is ", mean)

#We would estimate its value with an average of the rest of the values
updated_temperatures_C = temperatures_C
updated_temperatures_C.remove(0)
mean_correct_data = sum(updated_temperatures_C) / 23
updated_temperatures_C.insert(3, mean_correct_data)
print("The estimated temperature at 3:00 is ", mean_correct_data)

#Passing temperatures from Celsius degrees to Fahrenheit degrees
updated_temperatures_in_Fahrenheit = []
for temperature in updated_temperatures_C:
    temp_in_Fahrenheit = 1.8*temperature + 32
    updated_temperatures_in_Fahrenheit.append(temp_in_Fahrenheit)

temperatures_C_in_Fahrenheit = updated_temperatures_in_Fahrenheit
temperatures_C_in_Fahrenheit.insert(3, 32)
print("Initial temperatures in Fahrenheit degrees: ", temperatures_C_in_Fahrenheit)
print("Updated temperatures in Fahrenheit degrees : ", updated_temperatures_in_Fahrenheit)

#Decision

#"If at least one of these three is met, the cooling system must be changed:
#"more than 4 hours with temperatures greater than or equal to 70ºC;
#"some temperature higher than 80ºC;
#"average was higher than 65 degrees C throughout the day.

higher_than_eighty = any(t > 80 for t in temperatures_C)
if len(temp_greater_or_equal_70) > 4 or higher_than_eighty or mean > 65:
    #"The cooling system must be changed, given that at least one of the conditions is met"
    print(True)

#Hours whose temperature exceeds 70 degrees C
hours = []
for ind in range(len(temperatures_C)):
    if temperatures_C[ind] > 70:
        hours.append(ind)
print("Hours whose temperature exceeds 70 degrees C are the following: ", hours)

#Are they consecutive?

indexes = []
for i in range(24):
    if temperatures_C[i] > 70:
        indexes.append(i)
print("The number of temperatures which exceeds 70 C degrees is: ", len(indexes))
        
#indexes has 5 elements
def consecutive_checker(a, b, c, d, e):
    if e - d == d - c == c - b == b - a == 1:
        return True
    else:
        return False
        
if consecutive_checker(indexes[0], indexes[1], indexes[2], indexes[3], indexes[4]):
    print("They are consecutive")
else:
    print("They are not consecutive")

#Average of each of the lists: degrees C - degrees F
#Updated mean: average_Celsius = sum(updated_temperatures_C) / 24
average_Celsius = mean_correct_data
average_Fahrenheit = sum(updated_temperatures_in_Fahrenheit) / 24
print("Average of temperatures in Celsius degrees is: ", average_Celsius, " and average of temperatures in Fahrenheit degrees is: ", average_Fahrenheit)
print("The relation between both averages are the same formula of conversion from Celsius degrees to Fahrenheit degrees")

#Standard Deviation of each list
import math
squared_deviations_C_list = []
for element in updated_temperatures_C:
    squared_deviation_C = (element - average_Celsius)**2
    squared_deviations_C_list.append(squared_deviation_C)

variance_C = sum(squared_deviations_C_list) / 24
standard_deviation_C = math.sqrt(variance_C)
print("Standard Deviation of the temperatures in Celsius degrees is ", standard_deviation_C)

squared_deviations_F_list = []
for element in updated_temperatures_in_Fahrenheit:
    squared_deviation_F = (element - average_Fahrenheit)**2
    squared_deviations_F_list.append(squared_deviation_F)

variance_F = sum(squared_deviations_F_list) / 24
standard_deviation_F = math.sqrt(variance_F)
print("Standard Deviation of the temperatures in Fahrenheit degrees is ", standard_deviation_F)
