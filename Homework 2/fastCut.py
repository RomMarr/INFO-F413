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