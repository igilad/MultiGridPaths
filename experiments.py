from plotter import *
from pathCreatorManual import *
from multiGrid import *
from simple_problem import *
def diagonal_path_plotting_exp():
    origin = 1
    dest = 7
    paths = []
    for i in range(1, 8):
        j = 8 - i
        path = create_path_between_through_point(origin, origin, dest, dest, i, j)
        paths += [path]

    plot_paths(paths)


def coarsen_path_exp():

    path = create_corner_path_exp()

    paths = coarsen_path_iterative(path)
    labels = [f'coarsened {i} times' for i in range(len(paths))]
    if len(labels) > 1:
        labels[1] = labels[1][:-1]
    plot_paths(paths,labels)

def simple_problem_exp(n = 5):
    n = 500
    np.random.seed(2209)
    paths = create_random_paths(n,40,40)
    #print(create_collision_matrix(paths))
    #plot_paths(paths)
    #ex_sol = exhaustive_solver(paths)
    #print(ex_sol)
    #print(len(ex_sol))
    #all_sols = exhaustive_all_maximal_solutions(paths)
    #print([len(sol) for sol in all_sols])
    print(len(greedy_max_degree_solver(paths)))

def greedy_benchmark_exp():
    np.random.seed(2209)
    n_iterations = 40
    n_points = 10
    map_size = 40
    n_range = np.logspace(np.log10(40), np.log10(1000), n_points).round().astype(int)
    accuracies_n = []
    for n in n_range:
        accuracies = []
        for i in range(n_iterations):
            if i%5 == 0:
                print(f'***** n = {n}, i = {i}*****')
            paths = create_random_paths(n, map_size, map_size)
            accuracy = len(greedy_max_degree_solver(paths))/n
            accuracies += [accuracy]
        accuracies_n += [np.array(accuracies).mean()]
    plot_line_graph(n_range,accuracies_n,"Greedy Benchmark", "Greedy")

def coarsen_benchmark_exp():
    np.random.seed(2209)
    n_iterations = 10
    map_size = 40
    n_range = range(10,41)
    accuracies_n = []
    for n in n_range:
        accuracies = []
        for i in range(n_iterations):
            if i%5 == 0:
                print(f'***** n = {n}, i = {i}*****')
            paths = create_random_paths(n, map_size, map_size)
            accuracy = len(coarsen_solver(paths))/n
            accuracies += [accuracy]
        accuracies_n += [np.array(accuracies).mean()]
    plot_line_graph(n_range,accuracies_n,"Coarsen Benchmark", "Coarse")

def connect_points_exp():
    points = [[1,1], [3,3], [5,5]]
    path = connect_points(points)
    print(path)
    plot_paths([path])

def random_path_exp():
    np.random.seed(2209)
    map_size = 8
    paths = [create_random_step_path([1,1],[map_size,map_size], map_size,1) for i in range(5)]
    plot_paths(paths)
