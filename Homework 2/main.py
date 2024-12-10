from contract import Contract
from graph import Graph, Node, Edge

def main():
    G = Graph()
    G.add_node(Node())
    G.add_node(Node())
    G.add_node(Node())
    G.add_node(Node())
    G.set_edges()
    print(Contract(G))