class Edge:
    def __init__(self, id, start_node, end_node):
        self.id : int = id
        self.start_node : Node = start_node
        self.end_node : Node = end_node 
    
    # def __eq__(self, other):
    #     return (isinstance(other, Edge) and 
    #             self.id == other.id and
    #             self.start_node == other.start_node and
    #             self.end_node == other.end_node)
    
    # def __hash__(self):
    #     return hash((self.id, self.start_node, self.end_node))
        
    def get_node(self, node):
        if node == self.start_node:
            return self.end_node
        else :
            return self.start_node 
        
    def create_loops(self, node1, node2):
        return (self.start_node == node1 and self.end_node == node2) or (self.start_node == node2 and self.end_node == node1)

class Node:
    def __init__(self, id):
        self.id : str = id
        self.edges : list[Edge] = []
        #self.marked = False  # True if node has been visited

    # def __eq__(self, other):
    #     return isinstance(other, Node) and self.id == other.id
    
    # def __hash__(self):
    #     return hash(self.id)

    def get_edges(self):
        return self.edges
    
    def add_edge(self, edge):
        self.edges.append(edge)
    
    def set_edges(self, edges):
        self.edges = edges
    
    def get_neighbors(self):
        neighbors :list[Node] = []
        for edge in self.edges:
            neighbors.append(edge.get_node(self))
        return neighbors


class Graph:
    def __init__(self, edges = None):
        self.nodes : list[Node] = []
        self.edges : list[Edge] = []
        if edges is not None:
            self.create_graph_from_edges(edges)


    def create_graph_from_edges(self, edges):
        #print("Creating graph from edges")
        for edge in edges:
            if edge.start_node not in self.nodes:
                #print("1.Adding node", edge.start_node.id)
                self.nodes.append(edge.start_node)
            if edge.end_node not in self.nodes:
                #print("2.Adding node", edge.end_node.id)
                self.nodes.append(edge.end_node)
            if edge not in self.edges:
                #print("Adding edge", edge.id)
                self.edges.append(edge)

    def get_nb_nodes(self):
        return len(self.nodes)
    
    def add_node(self, node):
        self.nodes.append(node)


    def set_edges(self):
        for node in self.nodes:
            for edge in node.get_edges():
                if edge.id not in self.edges:  # a retravailler
                    self.edges.append(edge)
            
    def contract_edge(self, edge):
        # print("Nodes before removal:", [node.id for node in self.nodes])
        # print("To remove : ", edge.start_node.id, edge.end_node.id)
        edges_to_update : list[Edge] = []
        edges_to_remove : list[Edge] = []
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
