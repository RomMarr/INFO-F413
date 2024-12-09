class Edge:
    def __init__(self, id, start_node, end_node):
        self.id = id
        self.start_node = start_node
        self.end_node = end_node 
        
    def get_node(self, node):
        if node == self.start_node:
            return self.end_node
        else :
            return self.start_node 

class Nodes:
    def __init__(self, id):
        self.id = id
        self.edges : list[Edge] = []
        self.marked = False  # True if node has been visited

    def get_edges(self):
        return self.edges
    
    def get_neighbors(self):
        neighbors = []
        for edge in self.edges:
            neighbors.append(edge.get_node(self))
        return neighbors


class Graph:
    def __init__(self):
        self.nodes : list[Nodes] = []
        self.edges : list[Edge] = []
        #self.set_edges()

    def get_nb_nodes(self):
        return len(self.nodes)
    
    def set_edges(self):
        for node in self.nodes:
            for edge in node.get_edges():
                if edge.id not in self.edges:  # a retravailler
                    self.edges.append(edge)
            
    def contract_edge(self, edge):
        neighbors = []
        node1 = edge.start_node
        node2 = edge.end_node
        neighbors1 = node1.get_neighbors()
        neighbors2 = node2.get_neighbors()
        pass
        
    
            