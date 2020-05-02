import math


def get_closest_point_to_x(x, y, points, metric):
    distance_map = {(abs(x[0]) - point[0]) + abs(y[0] - point[0]) if metric == 'absolute' else math.sqrt(
        (x[0] - point[0] ** 2) + (y[0] - point[0]) ** 2): point for point in points}
    min_distance = min(distance_map.keys())
    return distance_map[min_distance]
