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
from contract import Contract
from graph import Graph, Edge
from copy import deepcopy

def FastCut(G: Graph) -> list[Edge]:
    n = G.get_nb_nodes()
    if n <= 6:
        print("n <= 6")
        return Contract(G, 2) # min cut by brute force
    else:
        print("n > 6")
        t =  math.ceil(1 + (n/math.sqrt(2)))
        graph_copy = deepcopy(G)
        print("t =", t)
        H1 = Graph(Contract(G, t))
        print("H1 created")
        H2 = Graph(Contract(graph_copy, t))
        print("H2 created")
        cut1 : list[Edge] = FastCut(H1)
        cut2 : list[Edge] = FastCut(H2)
        return cut1 if len(cut1) <= len(cut2) else cut2