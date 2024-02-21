#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import math

def read_circle_info(file_path):
    with open(file_path, 'r') as file:
        x, y = map(float, file.readline().split())
        radius = float(file.readline())
    return x, y, radius

def read_points(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        points = [tuple(map(float, line.split())) for line in lines]
    return points

def point_position_relative_to_circle(point, circle_center, circle_radius):
    distance = math.sqrt((point[0] - circle_center[0])**2 + (point[1] - circle_center[1])**2)

    if math.isclose(distance, circle_radius):
        return 0  # Точка лежит на окружности
    elif distance < circle_radius:
        return 1  # Точка внутри окружности
    else:
        return 2  # Точка снаружи окружности

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python newtest.py <файл_окружности> <файл_точек>")
        sys.exit(1)

    circle_file_path = sys.argv[1]
    points_file_path = sys.argv[2]

    circle_center_x, circle_center_y, circle_radius = read_circle_info(circle_file_path)
    circle_center = (circle_center_x, circle_center_y)
    points = read_points(points_file_path)

    for point in points:
        position = point_position_relative_to_circle(point, circle_center, circle_radius)
        print(position)

