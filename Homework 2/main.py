from contract import Contract
from graph import Graph, Node, Edge

def main():
    # Create nodes
    nodes = [Node(id=i) for i in range(1, 7)]  # Create 6 nodes

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
        graph.add_edge(edge)

    # Output the graph information
    print("Number of nodes:", graph.get_nb_nodes())
    print("Number of edges:", graph.get_nb_edges())

    print("Edges in the graph:")
    for edge in graph.edges.values():
        print(f"Edge {edge.id}: {edge.start_node.id} -> {edge.end_node.id}")

    print("Neighbors of each node:")
    for node in graph.nodes.values():
        neighbors = [neighbor.id for neighbor in node.get_neighbors()]
        print(f"Node {node.id}: {neighbors}")

    # Contract an edge
    Contract(graph)

    # Display graph state after contraction
    print("\nAfter contracting edge 1:")
    print("Nodes:", graph.get_nb_nodes())
    print("Edges:", graph.get_nb_edges())


def printInfos(graph):
    # Output the graph information
    print("Number of nodes:", graph.get_nb_nodes())
    print("Number of edges:", len(graph.edges))

    print("Edges in the graph:")
    for edge in graph.edges:
        print(f"Edge {edge.id}: {edge.start_node.id} -> {edge.end_node.id}")

    print("Neighbors of each node:")
    for node in graph.nodes:
        neighbors = [neighbor.id for neighbor in node.get_neighbors()]
    print(f"Node {node.id}: {neighbors}")

if __name__ == "__main__":
    main()