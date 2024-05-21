import numpy as np
import matplotlib.pyplot as plt

def coarsen_path(path):
    return path[::2,:]

def coarsen_path_iterative(path):
    paths = [path]
    while len(path)>1:
        path = coarsen_path(path)
        paths += [path]
    return paths

def coarsen_paths(paths):
    return [coarsen_path(path) for path in paths]