import random
import itertools

from pathCreatorManual import *
from multiGrid import *

def create_random_path(max_x,max_y):
    origin_x = int(np.random.randint(1,max_x+1))
    origin_y = int(np.random.randint(1,max_y+1))
    dest_x = int(np.random.randint(1, max_x + 1))
    dest_y = int(np.random.randint(1, max_y + 1))
    return create_path_between(origin_x,origin_y,dest_x,dest_y)

def create_random_paths(n,max_x,max_y):
    return [create_random_path(max_x,max_y) for i in range(n)]

def calculate_collision(path1: np.array, path2):
    l = min(np.size(path1,0), np.size(path2,0))
    cols = np.array([np.array_equal(path1[i], path2[i]) for i in range(l)])
    if sum(cols) > 0:
        return 0
    else: return 1

def create_collision_matrix(paths):
    n = len(paths)
    collisions = np.ones((n,n))
    for i in range(n):
        for j in range(i):
            col = calculate_collision(paths[i], paths[j])
            collisions[i,j] = col
            collisions[j,i] = col
    return collisions

def check_solution(collisions,combination):
    for i in combination:
        for j in combination:
            if i != j:
                if collisions[i,j] == 0:
                    return False
    return True

def exhaustive_solver(paths):
    collisions = create_collision_matrix(paths)
    n = len(paths)
    points = range(n)
    size = n
    while size >= 0:
        combinations = list(itertools.combinations(points, size))
        for combination in combinations:
            if check_solution(collisions,combination):
                return combination
        size-=1

def exhaustive_all_solutions(paths):
    collisions = create_collision_matrix(paths)
    combinations_list = []
    n = len(paths)
    points = range(n)
    size = n
    while size >= 0:
        combinations = list(itertools.combinations(points, size))
        for combination in combinations:
            if check_solution(collisions,combination):
                combinations_list += [combination]
        size-=1
    return combinations_list

def exhaustive_all_maximal_solutions(paths):
    collisions = create_collision_matrix(paths)
    combinations_list = []
    n = len(paths)
    points = range(n)
    size = n
    while size >= 0:
        combinations = list(itertools.combinations(points, size))
        for combination in combinations:
            if check_solution(collisions,combination):
                combinations_list += [combination]
        size-=1
        if len(combinations_list)>0:
            break
    return combinations_list

def get_neighbors(collisions, points):
    n = np.size(collisions,0)
    neighbors = [i for i in range(n) if i not in points]
    for i in range(n):
        for point in points:
            if collisions[point,i] == 0:
                if i in neighbors:
                    neighbors.remove(i)
                continue
    return neighbors


def greedy_max_degree_solver(paths):
    collisions = create_collision_matrix(paths)

    solution = []
    while True:
        neighbors = get_neighbors(collisions,solution)
        if len(neighbors) == 0:
            break
        degrees = []
        for point1 in neighbors:
            degree = 0
            for point2 in neighbors:
                if collisions[point1,point2] == 1:
                    degree += 1
            degrees += [degree]
        if max(degrees) == 0:
            break

        max_index = int(np.argmax(degrees))
        max_point = neighbors[max_index]
        solution += [max_point]
    return solution

def coarsen_solver(paths):
    paths = coarsen_paths(paths)
    return greedy_max_degree_solver(paths)


