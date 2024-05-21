import torch
import numpy as np
def x_interp(x1,y1,x2):
    x = x1
    y = y1
    path = [[x,y]]
    while not x == x2:
        if x>x2:
            x -= 1
        else:
            x += 1
        path += [[x,y]]
    return np.array(path)

def y_interp(x1,y1,y2):
    x = x1
    y = y1
    path = [[x,y]]
    while not y == y2:
        if y>y2:
            y -= 1
        else:
            y += 1
        path += [[x,y]]
    return np.array(path)

def concat_paths(path_1, path_2):
    return np.concatenate([path_1,path_2[1:]],axis = 0)

def create_path_between(x1, y1, x2, y2):
    path_1 = x_interp(x1,y1,x2)
    path_2 = y_interp(x2,y1,y2)
    return concat_paths(path_1,path_2)

def create_path_between_through_point(x1, y1, x2, y2, x_mid, y_mid):
    path_1 = create_path_between(x1, y1, x_mid, y_mid)
    path_2 = create_path_between(x_mid, y_mid, x2, y2)
    return concat_paths(path_1,path_2)

def create_diag_path_exp():
    origin = 1
    dest = 9
    mid = 5
    part1 = create_path_between_through_point(origin, origin, mid, mid, 3, 3)
    part2 = create_path_between_through_point(mid, mid, dest, dest, 7, 7)

    return concat_paths(part1, part2)

def create_corner_path_exp():
    return  create_path_between_through_point(1, 1, 9, 9, 3, 7)