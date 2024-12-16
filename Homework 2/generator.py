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


def tree_graph(n):
    """
    Generates a random tree with 'n' nodes.
    
    :param n: Number of nodes in the tree.
    :return: A NetworkX graph object representing the tree.
    """
    # Create an empty graph
    tree = Graph()  # Create an empty graph
    
    # Add the first node
    root = Node("0")
    tree.add_node(root)
    
    # Add subsequent nodes
    for i in range(1, n):
        parent_node = random.choice(tree.nodes)  # Pick a random parent node
        new_node = Node(str(i))
        edge_id = len(tree.edges)  # Edge id as the current number of edges
        edge = Edge(edge_id, parent_node, new_node)

        parent_node.add_edge(edge)  # Add edge to the parent node's edge list
        new_node.add_edge(edge)  # Add edge to the new node's edge list
        tree.add_node(new_node)  # Add the new node to the tree
        tree.set_edges()

    return tree

def cycle_graph(n):
    """
    Generates a cycle graph with n nodes.
    
    :param n: Number of nodes in the cycle graph
    :return: A Graph object representing the cycle graph
    """
    nodes = [Node(str(i)) for i in range(n)]
    edges = []
    
    for i in range(n):
        start_node = nodes[i]
        end_node = nodes[(i + 1) % n]  # Ensures that the last node connects back to the first node
        edge = Edge(i, start_node, end_node)
        start_node.add_edge(edge)
        end_node.add_edge(edge)
        edges.append(edge)
    
    graph = Graph(edges)
    return graph

def multigraph(n, m):
    """
    Generates a multigraph with n nodes and m random edges, allowing multiple edges between nodes.
    
    :param n: Number of nodes in the graph
    :param m: Number of edges in the multigraph
    :return: A Graph object representing the multigraph
    """
    nodes = [Node(str(i)) for i in range(n)]
    edges = []
    
    for i in range(m):
        start_node = random.choice(nodes)
        end_node = random.choice(nodes)
        # Ensure there are multiple edges (if needed)
        edge = Edge(i, start_node, end_node)
        start_node.add_edge(edge)
        end_node.add_edge(edge)
        edges.append(edge)
    
    graph = Graph(edges)
    return graph

def planar_graph(n, m):  # n = number of nodes, m = number of edges
    """
    Generates a planar graph by starting with a tree and adding edges to ensure planarity.
    
    :param n: Number of nodes in the graph
    :param m: Number of edges in the planar graph
    :return: A Graph object representing the planar graph
    """
    nodes = [Node(str(i)) for i in range(n)]
    edges = []
    
    # Start by creating a tree (a connected acyclic graph)
    for i in range(1, n):
        start_node = nodes[i - 1]
        end_node = nodes[i]
        edge = Edge(i, start_node, end_node)
        start_node.add_edge(edge)
        end_node.add_edge(edge)
        edges.append(edge)
    
    # Add additional edges while maintaining planarity
    while len(edges) < m:
        start_node = random.choice(nodes)
        end_node = random.choice(nodes)
        if start_node != end_node:
            # Add the edge only if it doesn't create a cycle
            edge = Edge(len(edges), start_node, end_node)
            start_node.add_edge(edge)
            end_node.add_edge(edge)
            edges.append(edge)
    
    graph = Graph(edges)
    return graph