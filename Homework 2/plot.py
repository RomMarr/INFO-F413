import matplotlib.pyplot as plt
import math


# Plot the graph using NetworkX
def plot_graph(graph):
    nodes = graph.nodes
    edges = graph.edges
    # Plot the graph using Matplotlib
    plt.figure(figsize=(8, 6))

    # Calculate positions for nodes in a circular layout
    num_nodes = len(nodes)
    positions = {
        node.id: (
            0.5 + 0.4 * math.cos(2 * math.pi * i / num_nodes),  # x-coordinate
            0.5 + 0.4 * math.sin(2 * math.pi * i / num_nodes)   # y-coordinate
        )
        for i, node in enumerate(nodes)
    }

    # Draw edges
    for edge in edges:
        start_pos = positions[edge.start_node.id]
        end_pos = positions[edge.end_node.id]
        plt.plot([start_pos[0], end_pos[0]], [start_pos[1], end_pos[1]], color='gray', zorder=1)

    # Draw nodes
    for node in nodes:
        pos = positions[node.id]
        plt.scatter(*pos, color='lightblue', s=500, zorder=2)
        plt.text(pos[0], pos[1], node.id, color='black', ha='center', va='center', fontsize=10, zorder=3)

    plt.title("Complete 5-Node Graph")
    plt.axis('off')
    plt.show()

