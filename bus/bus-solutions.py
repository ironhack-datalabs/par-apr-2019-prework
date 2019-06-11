# variables

stops = [(5,3),(5,5),(6,3),(5,1)]
number_of_person = 0
number_of_person_accumulated = 0
list_number_of_person_accumulated = []

# 1. Calculate the number of stops.
number_of_stops = len(stops)
print('the number of stops is', number_of_stops)

# 2. Assign a variable a list whose elements are the number of passengers in each stop:
# Each item depends on the previous item in the list + in - out.
for i in range (0,number_of_stops):
    bus_stop = stops[i]
    number_of_person = bus_stop[0] - bus_stop[1]
    number_of_person_accumulated += number_of_person
    list_number_of_person_accumulated.append(number_of_person_accumulated)

print('The number of passengers in each stop is', list_number_of_person_accumulated)

# 3. Find the maximum occupation of the bus.
max_occupation = max(list_number_of_person_accumulated)
print('The maximum occupation of the bus is', max_occupation, 'passengers')

# 4. Calculate the average occupation. And the standard deviation.
average_occupation = sum(list_number_of_person_accumulated[0:4])/len(list_number_of_person_accumulated)
print('The average occupation is', average_occupation, 'passengers')
import statistics
standard_deviation = round (statistics.stdev(list_number_of_person_accumulated[0:4]), 3)
print('The standard deviation is', standard_deviation)
