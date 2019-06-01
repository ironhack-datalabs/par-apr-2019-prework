# Assign problem data to variables with representative names
# well height, daily advance, night retreat, accumulated distance

well_height = 125
daily_advance = 30
night_retreat = 20
accumulated_distance = 0


# Assign 0 to the variable that represents the solution

days_needed = 0

# Write the code that solves the problem

while accumulated_distance <= well_height:
    accumulated_distance = accumulated_distance + (daily_advance - night_retreat)
    days_needed = days_needed + 1

else :
    print('Days =', days_needed)
# Print the result with print('Days =', days)


