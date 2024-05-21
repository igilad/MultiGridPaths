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


def create_path_between(x1, y1, x2, y2):
    path_1 = x_interp(x1,y1,x2)
    path_2 = y_interp(x2,y1,y2)
    return concat_paths([path_1,path_2])

def create_path_between_through_point(x1, y1, x2, y2, x_mid, y_mid):
    path_1 = create_path_between(x1, y1, x_mid, y_mid)
    path_2 = create_path_between(x_mid, y_mid, x2, y2)
    return concat_paths([path_1,path_2])

def concat_paths(paths):
    first_path = paths[0]
    first_point = np.array([first_path[0][0], first_path[0][1]]).reshape((1,2))
    paths = [path[1:] for path in paths]
    paths = [first_point] + paths
    return np.concatenate(paths,axis = 0)


def connect_points(points):
    paths = [create_path_between(points[i][0],points[i][1],points[i+1][0],points[i+1][1]) for i in range(len(points)-1)]
    return concat_paths(paths)

def softmax(x):
    return np.exp(x) / sum(np.exp(x))

def create_random_point_toward_end(cur_point,end, temp):
    end_x = end[0]
    end_y = end[1]
    cur_x = cur_point[0]
    cur_y = cur_point[1]
    if int(np.random.randint(0,2)) %2 == 0: # x coord
        delta = end_x-cur_x
        probs = softmax(np.array([0,delta/temp])) # coord 0 means left, 1 means right
                                             # negative delta, high chance for left, else right
        choice = int(np.random.choice(2, 1, p=probs))
        choice = 2 * choice -1 # -1 means left, 1 means right
        return np.array([cur_x+choice, cur_y])
    else:
        delta = end_y - cur_y
        probs = softmax(np.array([0, delta/temp]))  # coord 0 means left, 1 means right
        # negative delta, high chance for left, else right
        choice = int(np.random.choice(2, 1, p=probs))
        choice = 2 * choice - 1  # -1 means left, 1 means right
        return np.array([cur_x, cur_y + choice])

def is_point_valid(point, map_size):
    return 1 <= point[0] <= map_size and 1 <= point[1] <= map_size

def create_random_step_path(start, end, map_size, temp = 1):
    path = [start]

    cur_point = path[0]
    while not np.array_equal(cur_point,end):
        new_point = create_random_point_toward_end(cur_point,end, temp)
        if is_point_valid(new_point, map_size):
            cur_point = new_point
            path += [cur_point]
    return np.array(path)



def create_diag_path_exp():
    origin = 1
    dest = 9
    mid = 5
    part1 = create_path_between_through_point(origin, origin, mid, mid, 3, 3)
    part2 = create_path_between_through_point(mid, mid, dest, dest, 7, 7)

    return concat_paths([part1, part2])

def create_corner_path_exp():
    return  create_path_between_through_point(1, 1, 9, 9, 3, 7)