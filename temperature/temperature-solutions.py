
#Problem
# assign a variable to the list of temperatures
temperatures_C = [33,66,65,0,59,60,62,64,70,76,80,69,80,83,68,79,61,53,50,49,53,48,45,39]


# 1. Calculate the minimum of the list and print the value using print()

print("the minimum temperature is", min(temperatures_C), "°C")

# 2. Calculate the maximum of the list and print the value using print()

print("the maximum temperature is", max(temperatures_C), "°C")

# 3. Items in the list that are greater than 70ºC and print the result

temp_greater_70 = []

for i in range (0,len(temperatures_C)):
    if temperatures_C[i] >= 70:
        temp_greater_70.append(temperatures_C[i])

print("Temperatures greater than 70°C are", temp_greater_70)

# 4. Calculate the mean temperature throughout the day and print the result

print("The mean temperature throughout the day is", round(sum(temperatures_C)/len(temperatures_C),2),"°C")

# 5.1 Solve the fault in the sensor by estimating a value

updated_temperature_C = temperatures_C

for i in range (0,len(updated_temperature_C)):
    if i == 0 and updated_temperature_C[i] == 0:
        updated_temperature_C[i] = int(updated_temperature_C[i+1])
    elif i == 0 and updated_temperature_C[i] ==0:
        updated_temperature_C[i] = int(updated_temperature_C[i-1])
    elif i!= 0 and updated_temperature_C[i] == 0:
        updated_temperature_C[i] = int((updated_temperature_C[i-1]+updated_temperature_C[i+1])/2)


# 5.2 Update of the estimated value at 03:00 on the list

print("The updated list of temperature is", updated_temperature_C)

# Bonus: convert the list of ºC to ºFarenheit

temperatures_F = []

#F = 1.8 * C + 32

for i in range (0, len(temperatures_C)):
    temperatures_F.append(round((1.8 * temperatures_C[i] +32),2))

print(temperatures_F)

#Take the decision
# Print True or False depending on whether you would change the cooling system or not
print(temperatures_C)
true = []
false = []

for i in range (0, len(temperatures_C)):
    if temperatures_C[i] >= 70  and temperatures_C[i+1] >= 70 and temperatures_C[i+2] >= 70 and temperatures_C[i+3] >= 70:
        true.append('true')
    elif temperatures_C[i] > 80:
        true.append('true')
    elif round(sum(temperatures_C)/len(temperatures_C),2) > 65:
        true.append('true')
    else:
        false.append(('false'))

if len(true) > 0:
    print("The cooling system needs to be changed")
else:
    print("The cooling system is still ok")

#Future Improvements

# 1. We want the hours (not the temperatures) whose temperature exceeds 70ºC

temp_greater_70 = []
time_greater_70 = []


for i in range (0,len(temperatures_C)):
    if temperatures_C[i] >= 70:
        temp_greater_70.append(temperatures_C[i])
        time_greater_70.append(i)

print("The hours whose temperature exceeds 70°C is", time_greater_70)

# 2. Condition that those hours are more than 4 consecutive and consecutive, not simply the sum of the whole set. Is this condition met?

for i in range (0, len(time_greater_70)-3):
        if time_greater_70[i]-time_greater_70[i+3] != 3:
            print("The cooling system is still ok")
            break
        else:
            print("The cooling system needs to be changed")

# 3. Average of each of the lists (ºC and ºF). How they relate?

mean_temperature_C=round(sum(temperatures_C)/len(temperatures_C))

mean_temperature_F=1.8*mean_temperature_C+32


