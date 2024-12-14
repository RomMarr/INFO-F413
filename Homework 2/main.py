from contract import Contract
from fastCut import FastCut
from graph import Graph, Node, Edge
from plot import plot_graph

def create_complete_graph(n):
    # Create nodes
    nodes = [Node(id=str(i)) for i in range(1, n+1)]  # Create 5 nodes with string IDs

    # Create edges (complete graph: every pair of nodes is connected)
    edges = []
    edge_id = 1
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            edge = Edge(id=edge_id, start_node=nodes[i], end_node=nodes[j])
            edges.append(edge)
            nodes[i].add_edge(edge)
            nodes[j].add_edge(edge)
            edge_id += 1

    # Create the graph
    graph = Graph()
    for node in nodes:
        graph.add_node(node)
    for edge in edges:
        graph.edges.append(edge)
    return graph

def printInfo(graph):
    print("Number of nodes:", graph.get_nb_nodes())
    print("Number of edges:", len(graph.edges))

    print("Edges in the graph:")
    for edge in graph.edges:
        print(f"Edge {edge.id}: {edge.start_node.id} -> {edge.end_node.id}")

    print("Neighbors of each node:")
    for node in graph.nodes:
        neighbors = [neighbor.id for neighbor in node.get_neighbors()]
        print(f"Node {node.id}: {neighbors}")


def main():
    graph = create_complete_graph(10)
    printInfo(graph)
    print()
    temp = FastCut(graph)
    print("Edges in the cut:", [edge.id for edge in temp])
    print("Nodes in the cut:", [edge.start_node.id for edge in temp] + [temp[-1].end_node.id])






if __name__ == "__main__":
    main()