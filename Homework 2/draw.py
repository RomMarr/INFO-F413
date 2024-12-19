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