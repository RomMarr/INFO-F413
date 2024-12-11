# class Edge:
#     def __init__(self, id, start_node, end_node):
#         self.id = id
#         self.start_node = start_node
#         self.end_node = end_node

#     def get_other_node(self, node):
#         return self.end_node if node == self.start_node else self.start_node


# class Node:
#     def __init__(self, id):
#         self.id = id
#         self.edges = []  # List of connected Edge objects
#         self.marked = False  # True if node has been visited

#     def add_edge(self, edge):
#         self.edges.append(edge)

#     def remove_edge(self, edge):
#         self.edges.remove(edge)

#     def get_neighbors(self):
#         return [edge.get_other_node(self) for edge in self.edges]


# class Graph:
#     def __init__(self):
#         self.nodes = {}  # Dictionary of nodes {node_id: Node}
#         self.edges = {}  # Dictionary of edges {edge_id: Edge}

#     def add_node(self, node):
#         self.nodes[node.id] = node

#     def add_edge(self, edge):
#         self.edges[edge.id] = edge
#         edge.start_node.add_edge(edge)
#         edge.end_node.add_edge(edge)

#     def contract_edge(self, edge):
#         """Contract the edge, merging its two nodes."""
#         node1 = edge.start_node
#         node2 = edge.end_node

#         # Move edges from node1 to node2
#         for e in list(node1.edges):
#             if e == edge:  # Skip the contracted edge
#                 continue

#             # Update edge to connect to node2 instead of node1
#             if e.start_node == node1:
#                 e.start_node = node2
#             if e.end_node == node1:
#                 e.end_node = node2

#             # Avoid self-loops
#             if e.start_node != e.end_node:
#                 node2.add_edge(e)

#         # Remove node1 and the contracted edge
#         del self.nodes[node1.id]
#         self.edges.pop(edge.id)

#         # Remove references to node1 from node2's edge list
#         node1.edges.clear()

#     def get_nb_nodes(self):
#         return len(self.nodes)

#     def get_nb_edges(self):
#         return len(self.edges)
