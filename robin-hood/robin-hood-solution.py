# Variables

points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5),
          (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2),
          (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]

shot_number = len(points)

# 1 Robin Hood is famous for hitting an arrow with another arrow. Did you get it?

unique_shot = set(points)
unique_shot_number=len(unique_shot)
two_arrows = (shot_number - unique_shot_number)/2

print('Robin Hood hit an arrow with another arrow', two_arrows, 'times')

# 2. Calculate how many arrows have fallen in each quadrant.
Q1=[]
Q2=[]
Q3=[]
Q4=[]

for i in range(0, len(points)):
    if points[i][0] >= 0 and points[i][1] >= 0:
        Q1.append(points[i])
    elif points[i][0] >= 0 and points[i][1] <= 0:
        Q2.append(points[i])
    elif points[i][0] <= 0 and points[i][1] <= 0:
        Q3.append(points[i])
    else:
        Q4.append(points[i])

print("There are", len(Q1), "arrows that have fallen in Q1")
print("There are", len(Q2), "arrows that have fallen in Q2")
print("There are", len(Q3), "arrows that have fallen in Q3")
print("There are", len(Q4), "arrows that have fallen in Q4")

# 3. Find the point closest to the center. Calculate its distance to the center
# Defining a function that calculates the distance to the center can help.

new_points = points
for i in range(0, len(new_points)):
    new_points[i] = list(new_points[i])
    new_points[i][0] = abs(0-new_points[i][0])
    new_points[i][1] = abs(0-new_points[i][1])
print(new_points)

print("the point closest to the center is", min(new_points))

# 4. If the target has a radius of 9, calculate the number of arrows that
# must be picked up in the forest.

radius_pov = 9
radius_neg = -9

list_out = []
for i in range(0, len(points)):
    if points[i][0] > radius_pov or points[i][1] > radius_pov or points[i][0] < radius_neg or points[i][1] < radius_neg:
        list_out.append(points[i])

print("There is", len(list_out), "arrow that must be picked up in the forest")

