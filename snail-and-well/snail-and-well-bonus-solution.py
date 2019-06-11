# Assign problem data to variables with representative names
# well height, daily advance, night retreat, accumulated distance

well_height = 125
accumulated_distance = 0
advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
i=0
# Assign 0 to the variable that represents the solution

days_needed = 0

# Write the code that solves the problem

while accumulated_distance <= well_height:
    accumulated_distance = accumulated_distance + advance_cm[i]
    days_needed = days_needed + 1
    i=i+1

# Print the result with print('Days =', days)
else :
    print('Days =', days_needed)


# What is its maximum displacement in a day? And its minimum?
max_displacement = max(advance_cm[0:4])
min_displacement = min(advance_cm[0:4])
print ('The maximum displacement in a day is',max_displacement,'cm' )
print ('The minimum displacement in a day is',min_displacement,'cm' )

# What is its average progress?


average_progress = sum(advance_cm[0:4])/len(advance_cm[0:4])
print ('The average progress is',average_progress,'cm/day' )


# What is the standard deviation of your displacement during the day?
import statistics
standard_deviation = round (statistics.stdev(advance_cm[0:4]), 3)
print('The standard deviation during the day is', standard_deviation, 'cm')
