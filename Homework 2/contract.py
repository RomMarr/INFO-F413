"""
Input : a graph G
Output : a cut C

1 : for i in range (1, n-1) # n-2 but n-2 compris donc n-1 pour le range
   a) choose a random edge e
   b) contract e (voisins de e_u deviennent voisins de e_v) 
2 : Return set of edges connecting the two remaining vertices (nodes)
"""
import random
from graph import Graph, Edge

def Contract(G : Graph, t = None) :
   min_nb : int = 2 if t == None else t  # min number of nodes
   n = G.get_nb_nodes()
   print("min_nb = ", min_nb, "n = ", n)
   for _ in range(1, n-1): # can be changed to a while G.get_nb_nodes() > min_nb
      print("i", _)
      edge = random.choice(G.edges)
      print("edge", edge.id)
      G.contract_edge(edge)
      if G.get_nb_nodes() == min_nb:
         return G.edges
   return G.edges # a verif -> à priori pas utile

