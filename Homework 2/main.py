from contract import contract
from fastCut import fastCut, fastCut2
from graph import Graph, Node, Edge
from copy import deepcopy

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

def prepare_node(temp):
    cut_nodes = set()
    for edge in temp:
        cut_nodes.add(edge.start_node.id)
        cut_nodes.add(edge.end_node.id)
    return cut_nodes

def main():
    graph = create_complete_graph(10)
    printInfo(graph)
    print()
    moyenne = [0,0,0]

    for i in range(100):

        temp = fastCut(deepcopy(graph))
        temp2 = fastCut2(deepcopy(graph))
        temp3 = contract(deepcopy(graph),2)


        print('FastCut -> bruteForce :')
        count = 0
        for edge in temp:
            count += 1
            #print(f"Edge {edge.id}: {edge.start_node.id} -> {edge.end_node.id}")
        moyenne[0] += count
        print(f"Cut {count} : {prepare_node(temp)}")
        print()
        print('FastCut2 -> contract :')
        count = 0
        for edge in temp2:
            count += 1
            #print(f"Edge {edge.id}: {edge.start_node.id} -> {edge.end_node.id}")
        moyenne[1] += count
        print(f"Cut {count} : {prepare_node(temp2)}")
        print()
        print('Contract :')
        count = 0
        for edge in temp3:
            count += 1
            #print(f"Edge {edge.id}: {edge.start_node.id} -> {edge.end_node.id}")
        moyenne[2] += count
        print(f"Cut {count} : {prepare_node(temp3)}")
    
    moyenne = [i/100 for i in moyenne]
    print(moyenne)

    # print("Edges in the cut:", [edge.id for edge in temp])
    # print("Nodes in the cut:", list(prepare_node(temp)))
    # print("Nodes in the cut:", [edge.start_node.id for edge in temp] + [temp[-1].end_node.id])
    # print()
    
    # print("Edges in the cut:", [edge.id for edge in temp2])
    # print("Nodes in the cut:", list(prepare_node(temp2)))
    # print("Nodes in the cut:", [edge.start_node.id for edge in temp2] + [temp2[-1].end_node.id])





if __name__ == "__main__":
    main()