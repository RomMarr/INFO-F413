import random

"""
Input : a graph G
Output : a cut C


1 : for i in range (1, n-1) # n-2 but n-2 compris donc n-1 pour le range
   a) choose a random edge e
   b) contract e (voisins de e_u deviennent voisins de e_v) 
2 : Return set of edges connecting the two remaining vertices (nodes)
"""