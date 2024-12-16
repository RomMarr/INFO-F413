from graph import Graph, Node, Edge
import random
import matplotlib.pyplot as plt
import networkx as nx



def draw_graph(graph):
    """
    Draws the graph with curved edges between nodes and ensures it stays in the drawing window.
    
    :param graph: A Graph object with nodes and edges
    """
    G = nx.Graph()

    # Add nodes and edges to the networkx graph
    for node in graph.nodes:
        G.add_node(node.id)  # Add nodes using their IDs
    for edge in graph.edges:
        G.add_edge(edge.start_node.id, edge.end_node.id)  # Add edges using the node IDs
    
    # Generate positions for the nodes using a spring layout
    pos = nx.spring_layout(G)  # You can change the layout here

    # Draw the graph with labels, node size, and other aesthetic options
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue", font_size=10, font_weight="bold", edge_color="gray")

    # Show the graph
    plt.title("Graph Visualization")
    plt.show()


def complete_graph(n):
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



def bipartite_graph(set1_size, set2_size, edge_probability=0.5):
    """
    Generates a random bipartite graph with two disjoint sets of nodes.
    
    :param set1_size: The number of nodes in the first set
    :param set2_size: The number of nodes in the second set
    :param edge_probability: The probability that an edge exists between a node in set 1 and a node in set 2
    :return: A Graph object containing the bipartite graph
    """
    # Create nodes for both sets
    set1 = [Node(str(i)) for i in range(1, set1_size + 1)]
    set2 = [Node(str(i + set1_size)) for i in range(1, set2_size + 1)]
    
    # Create edges between nodes in set1 and set2 with a certain probability
    edges = []
    for node1 in set1:
        for node2 in set2:
            if random.random() < edge_probability:  # Edge probability
                edge_id = len(edges) + 1
                edge = Edge(edge_id, node1, node2)
                edges.append(edge)
                node1.add_edge(edge)
                node2.add_edge(edge)
    
    # Create the graph
    bipartite_graph = Graph(edges)
    return bipartite_graph