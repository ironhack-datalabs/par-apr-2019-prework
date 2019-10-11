points = [(4, 5), (0, 2), (4, 7), (1, -3), (3, -2), (4, 5), (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2), (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2), (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]

points_and_times = {}
for point in points:
    times_arrows_hit = points.count(point)
    if times_arrows_hit > 1:
        points_and_times[point] = times_arrows_hit
print("The points and the times arrows were hit with another arrow are")
print(points_and_times)

first_quadrant_arrows, second_quadrant_arrows = 0, 0
third_quadrant_arrows, fourth_quadrant_arrows = 0, 0

for point in points:
    if point[0] > 0 and point[1] > 0:
        first_quadrant_arrows += 1
    elif point[0] < 0 and point[1] > 0:
        second_quadrant_arrows += 1
    elif point[0] < 0 and point[1] < 0:
        third_quadrant_arrows += 1
    elif point[0] > 0 and point[1] < 0:
        fourth_quadrant_arrows += 1

print(first_quadrant_arrows, " arrows fell on the first quadrant")
print(second_quadrant_arrows, "arrows fell on the second quadrant")
print(third_quadrant_arrows, " arrows fell on the third quadrant")
print(fourth_quadrant_arrows, " arrows fell on the fourth quadrant")

def distance_to_center(x1, y1):
    import math
    #formula is math.sqrt((x2 - x1)**2 + (y2 - y1)**2) but P2(x2, y2) = center = O(0, 0)
    return math.sqrt((x1)**2 + (y1)**2)

closest_distance = distance_to_center(points[0][0], points[0][1])
closest_distance_points = []
for point in points:
    distance = distance_to_center(point[0], point[1])
    if distance < closest_distance:
        closest_distance = distance
        closest_distance_points = []
        closest_distance_points.append(point)
    elif distance == closest_distance:
        closest_distance_points.append(point)

print("The closest point(s) to the center is/are ")
for close_point in closest_distance_points:
    print(close_point)
print("and its distance to the center is ", closest_distance)

arrows_in_forest = 0
for arrow in points:
    if distance_to_center(arrow[0], arrow[1]) > 9:
        arrows_in_forest += 1

print("The number of arrows picked up from the forest are ", arrows_in_forest)
