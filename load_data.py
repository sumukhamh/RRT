# coding: utf-8
import numpy as np

f = open('input_maze.txt', 'r')
start = f.readline()
goal = f.readline()
obstacles = []
for line in f.readlines():
    points = line.split(',')
    points = [item.strip() for item in points]
    points = [np.array([float(item.split(' ')[0]), float(item.split(' ')[1])]) for item in points]
    points = np.array(points)
    obstacles.append(points)

start = start.split(' ')
start = np.array([float(item) for item in start])
goal = goal.split(' ')
goal = np.array([float(item) for item in goal])