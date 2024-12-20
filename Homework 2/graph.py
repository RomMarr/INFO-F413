class Edge:
    """ Class representing an edge in a graph """
    def __init__(self, id, start_node, end_node):
        """ Initialize an edge with an id, start node, and end node """
        self.id : int = id
        self.start_node : Node = start_node
        self.end_node : Node = end_node 
        
    def get_other_node(self, node):
        """ Get the other node connected to the edge """
        if node == self.start_node:
            return self.end_node
        else :
            return self.start_node 
        
    def create_loops(self, node1, node2):
        """ Check if the edge creates a self-loop with two nodes"""
        return (self.start_node == node1 and self.end_node == node2) or (self.start_node == node2 and self.end_node == node1)

class Node:
    """ Class representing a node in a graph """
    def __init__(self, id):
        """ Initialize a node with an id and an empty list of edges """
        self.id : str = id
        self.edges : list[Edge] = []

    def get_edges(self):
        """ Get the edges connected to the node """
        return self.edges
    
    def add_edge(self, edge):
        """ Add an edge to the node """
        self.edges.append(edge)
    
    def set_edges(self, edges):
        """ Set the edges of the node """
        self.edges = edges
    
    def get_neighbors(self):
        """ Get the neighbors (nodes connected to current one by an edge) of the node """
        neighbors :list[Node] = []
        for edge in self.edges:
            neighbors.append(edge.get_other_node(self))
        return neighbors


class Graph:
    """ Class representing a graph """
    def __init__(self, edges = None):
        """ Initialize a graph with an empty list of nodes and edges """
        self.nodes : list[Node] = []
        self.edges : list[Edge] = []
        if edges is not None:  # Create a graph from a list of edges if provided
            self.create_graph_from_edges(edges)


    def create_graph_from_edges(self, edges):
        """ Create a graph from a list of edges by adding nodes and edges """
        for edge in edges:
            if edge.start_node not in self.nodes:
                self.nodes.append(edge.start_node)
            if edge.end_node not in self.nodes:
                self.nodes.append(edge.end_node)
            if edge not in self.edges:
                self.edges.append(edge)

    def get_nb_nodes(self):
        """ Get the number of nodes in the graph """
        return len(self.nodes)
    
    def add_node(self, node):
        """ Add a node to the graph """
        self.nodes.append(node)


    def set_edges(self):
        """ Set the edges of the graph from the nodes"""
        for node in self.nodes:
            for edge in node.get_edges():
                if edge.id not in self.edges:  # a retravailler
                    self.edges.append(edge)
            
    def contract_edge(self, edge):
        """ Contract an edge by merging its two nodes and deleting the edge(s) connecting them"""
        edges_to_update : list[Edge] = []  # Edges to be updated (to connect to the new node)
        edges_to_remove : list[Edge] = []  # Edges to be removed ("self-loops")
        node1 : Node = edge.start_node 
        node2 : Node = edge.end_node
        for e in self.edges:  # Identify edges connected to the nodes being contracted
            if e.start_node in (node1, node2) or e.end_node in (node1, node2):
                if e.create_loops(node1, node2):  # Self-loop check
                    edges_to_remove.append(e)
                else:  # Edge to be updated (to connect to the new node)
                    edges_to_update.append(e)

        new_node = Node(node1.id + "$" + node2.id)  # Create a new node (contracted node)
        for e in edges_to_update:  # Update edges to connect to the new node
            if e.start_node in (node1, node2): 
                e.start_node = new_node
            if e.end_node in (node1, node2):
                e.end_node = new_node

        for e in edges_to_remove:  # Remove self-loops from edges and update graph structure
            self.edges.remove(e)

        new_node.set_edges(edges_to_update)  # Set the edges of the new node
        self.nodes.append(new_node)  # Add the new node to the graph
        self.nodes.remove(node1)  # Remove the old nodes
        self.nodes.remove(node2)
