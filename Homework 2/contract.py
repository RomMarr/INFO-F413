import random
from graph import Graph, Edge

def contract(G : Graph, t = None) -> list[Edge]:
   """ Contract edges of a graph until it reaches a 2 or t nodes. 
   The goal is to find the minimum cut of the graph G """
   min_nb : int = 2 if t == None else t  # min number of nodes
   while G.get_nb_nodes() > min_nb:
      edge : Edge = random.choice(G.edges)
      G.contract_edge(edge)
      if G.get_nb_nodes() == min_nb: # If the number of nodes remaining is reached
         return G.edges
   return G.edges

