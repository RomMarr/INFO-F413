"""
Input : a multigraph G
Output : a cut C
1 : n = len(G.nodes)   # number of vertices (= nodes)
2 : if n <= 6 : 
    ->  return min cut by brute force
3 : else : 
    a) t = 1 + (n/sqrt(2)) le tout round up 
    b) using contract, perform two indep. contraction 
        sequences to obtain graphs H1 and H2, each with t vertices
        ATTENTION : exec of contract stops when t vertices are left
    c) Recursively compute cuts in each of H1 and H2
    d) Return the minimum (smaller) of the two cuts 
"""
import math
from contract import contract
from graph import Graph, Edge
from copy import deepcopy

def fastCut(G: Graph) -> list[Edge]:
    n = G.get_nb_nodes()
    if n <= 6:
        return minCutBruteForce(G) # min cut by brute force
    else:
        t :int =  math.ceil(1 + (n/math.sqrt(2)))
        g1 : Graph = deepcopy(G)
        g2 : Graph = deepcopy(G)
        H1 = Graph(contract(g1, t))
        H2 = Graph(contract(g2, t))
        cut1 : list[Edge] = fastCut(H1)
        cut2 : list[Edge] = fastCut(H2)
        return cut1 if len(cut1) <= len(cut2) else cut2
    

def fastCut2(G: Graph) -> list[Edge]:
    n = G.get_nb_nodes()
    if n <= 6:
        return contract(G,2) # min cut by brute force
    else:
        t :int =  math.ceil(1 + (n/math.sqrt(2)))
        g1 : Graph = deepcopy(G)
        g2 : Graph = deepcopy(G)
        H1 = Graph(contract(g1, t))
        H2 = Graph(contract(g2, t))
        cut1 : list[Edge] = fastCut(H1)
        cut2 : list[Edge] = fastCut(H2)
        return cut1 if len(cut1) <= len(cut2) else cut2

from itertools import combinations

def minCutBruteForce(graph: Graph) -> list[Edge]:
    """
    Compute the minimum cut of a small graph (n <= 6) using brute force.
    :param graph: An instance of the Graph class
    :return: (min_cut_edges, best_partition) - List of edges in the minimum cut and the corresponding partition
    """
    nodes = graph.nodes
    n = len(nodes)
    min_cut_edges = []
    min_cut_value = float('inf')

    # Generate all possible subsets S of nodes (except empty and full)
    for i in range(1, n):  # Subset sizes from 1 to n-1
        for subset in combinations(nodes, i):
            S = set(subset)
            T = set(nodes) - S  # The complementary subset

            # Calculate the edges crossing the cut
            cut_edges = []
            for edge in graph.edges:
                if (edge.start_node in S and edge.end_node in T) or (edge.start_node in T and edge.end_node in S):
                     cut_edges.append(edge)

            # Update the minimum cut if this one is better
            if len(cut_edges) < min_cut_value:
                min_cut_value = len(cut_edges)
                min_cut_edges = cut_edges

    return min_cut_edges
