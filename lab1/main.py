from os import getcwd
from os.path import join
from vertex_cover.better_recursion import better_recursion
from vertex_cover.kernelization import kernelize
from vertex_cover.optimized_recursion import optimized_recursion
from vertex_cover.simple_recursion import simple_recursion
from utils.dimacs import *

graph_names = [
    "e5",
    "e10",
    "e20",
    "e40",
    "e150",
    "s25",
    "s50",
    "s500",
    "b20",
    "b30",
    "b100",
    "k330_a",
    "k330_b",
    "k330_c",
    "m20",
    "m30",
    "m40",
    "m50",
    "m100",
    "p20",
    "p35",
    "p60",
    "p150",
    "r30_01",
    "r30_05",
    "r50_001",
    "r50_01",
    "r50_05",
    "r100_005"]

graph_dir = join(getcwd(), "graphs")
solution_dir = join(getcwd(), "solutions")
for name in graph_names:
    graph_filename = join(graph_dir, name)
    solution_filename = join(solution_dir, name + ".sol")
    G = loadGraph(graph_filename)
    G_edge_list = edgeList(G)
    print(name)
    for k in range(1, len(G)):
        kernel = kernelize(G_edge_list, k)
        if kernel:
            graph, new_k, solution = kernel
        else:
            continue

        solution = optimized_recursion(graph, new_k, solution)
        if not solution:
            continue

        print("solution k:", k)
        print("VC:", isVC(G_edge_list, solution))
        print()
        saveSolution(solution_filename, solution)
        break
