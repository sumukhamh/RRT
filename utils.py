# coding: utf-8
import numpy as np
import random
import matplotlib.pyplot as plt
import load_data

class Node:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.parent = None
        self.children = []
        
    def __init__(self, point):
        self.x = point[0]
        self.y = point[1]
        self.parent = None
        self.children = []
        
class Line:
    def __init__(self, x1, y1, x2, y2):
        self.a = y2 - y1
        self.b = x1 - x2
        self.c = self.a*x1 + self.b*y1
        
    def slope(self):
        if self.a == 0:
            return None
        else:
            return -self.b/self.a

def sample(grid_size):
    point = np.random.uniform(-grid_size/2,grid_size/2, size=2)
    sample_node = Node(point)
    return sample_node

def get_distance(node1, node2):
    return np.sqrt(np.power(node1.x - node2.x, 2) + np.power(node1.y - node2.y, 2))

def get_nearest_node(nodes, new_node, min_distance):
    for node in nodes:
        distance = get_distance(node, new_node)
        if distance < min_distance:
            min_distance = distance
            min_node = node
    return min_node

def steer(node_to_steer, node, eps):
    theta = np.arctan2((node.y - node_to_steer.y),(node.x - node_to_steer.x))
    x = node_to_steer.x + eps*np.cos(theta)
    y = node_to_steer.y + eps*np.sin(theta)
    advanced_node = Node([x, y])
    return advanced_node

def check_collision(node1, node2, obstacles):
    line1 = Line(node1.x, node1.y, node2.x, node2.y)
    for obstacle in obstacles:
        for i in range(np.shape(obstacle)[0]):
            j = (i + 1) % np.shape(obstacle)[0]
            x1 = obstacle[i][0]
            y1 = obstacle[i][1]
            x2 = obstacle[j][0]
            y2 = obstacle[j][1]
            line2 = Line(x1, y1, x2, y2)
            
            if line1.slope() != line2.slope():
                x_int, y_int = get_intersection(line1, line2)
                if is_inrange(node1.x, node1.y, node2.x, node2.y, x_int, y_int) and is_inrange(x1, y1, x2, y2, x_int, y_int):
                    return True
    return False

def get_intersection(line1, line2):
    x_int = (line2.b*line1.c - line1.b*line2.c)/(line2.b*line1.a - line1.b*line2.a)
    y_int = (line2.a*line1.c - line1.a*line2.c)/(line2.a*line1.b - line1.a*line2.b)
    return x_int, y_int

def is_inrange(x1, y1, x2, y2, x_int, y_int):
    b1 = (x_int - x1)*(x2 - x_int) > 0
    b2 = (y_int - y1)*(y2 - y_int) > 0
    if b1 and b2:
        return True
    else:
        return False
    
def plot_nodes(nodes):
    points = []
    path_x, path_y = get_path(nodes)
    for node in nodes:
        points.append((node.x, node.y))
    plt.scatter(*(zip(*points)), s=1.5)
    plt.plot(path_x, path_y)
    
def get_path(nodes):
    goal_node = nodes[-1]
    start_node = nodes[0]
    path_x = []
    path_y = []
    node = goal_node
    while True:
        path_x.append(node.x)
        path_y.append(node.y)
        if node == start_node:
            break
        node = node.parent
    return path_x, path_y
