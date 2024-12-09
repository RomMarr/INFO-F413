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

def FastCut(G):
    n = G.get_nb_nodes()
    if n <= 6:
        return Contract(G, 2) # min cut by brute force
    else:
        t =  math.ceil(1 + (n/math.sqrt(2)))
        H1 = Contract(G, t)
        H2 = Contract(G, t)
        cut1 = FastCut(H1)
        cut2 = FastCut(H2)
        return min(len(cut1), len(cut2))