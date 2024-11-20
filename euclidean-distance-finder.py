import math

def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

points = [(2, 3), (5, 7), (1, 1), (8, 8), (4, 6)]
distances_with_points = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances_with_points.append((distance, points[i], points[j]))

min_distance, point1, point2 = min(distances_with_points, key=lambda x: x[0])

print("Distances between points:")
for distance, p1, p2 in distances_with_points:
    print(f"Distance between {p1} and {p2}: {distance:.2f}")

print(f"\nMinimum distance: {min_distance:.2f} between points {point1} and {point2}")
