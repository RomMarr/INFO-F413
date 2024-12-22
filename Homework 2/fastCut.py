import math
from contract import contract
from graph import Graph, Edge
from copy import deepcopy
from itertools import combinations

def fastCut(G: Graph) -> list[Edge]:
    """ Compute the minimum cut of a graph using the fastCut algorithm and returns the min-cut"""
    n = G.get_nb_nodes()
    if n <= 6:
        return minCutBruteForce(G) # min cut by brute force
    else:
        t :int =  math.ceil(1 + (n/math.sqrt(2)))
        g1 : Graph = deepcopy(G)
        g2 : Graph = deepcopy(G)
        H1 = Graph(contract(g1, t))  # Contract the graph G until it reaches t nodes
        H2 = Graph(contract(g2, t)) 
        cut1 : list[Edge] = fastCut(H1)  # Recursively call fastCut on the two subgraphs
        cut2 : list[Edge] = fastCut(H2)
        return cut1 if len(cut1) <= len(cut2) else cut2  # Return the min-cut of the two subgraphs
    

def minCutBruteForce(graph: Graph) -> list[Edge]:
    """
    Compute the minimum cut of a small graph using brute force and returns the min-cut 
    It uses the combinatorial approach to find the minimum cut.
    """
    nodes = graph.nodes
    n : int = len(nodes)
    min_cut_edges : list[Edge] = []
    min_cut_value = float('inf')

    # Generate all possible subsets S of nodes (except empty and full)
    for i in range(1, n):  # Subset sizes from 1 to n-1
        for subset in combinations(nodes, i):
            S = set(subset)
            T = set(nodes) - S  # The complement subset
            # Calculate the edges crossing the cut
            cut_edges :list[Edge] = []
            for edge in graph.edges:
                if (edge.start_node in S and edge.end_node in T) or (edge.start_node in T and edge.end_node in S):
                     cut_edges.append(edge)
            # Update the minimum cut if this one is better
            if len(cut_edges) < min_cut_value:
                min_cut_value = len(cut_edges)
                min_cut_edges = cut_edges
    return min_cut_edges
