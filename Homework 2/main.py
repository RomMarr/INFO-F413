from contract import contract
from fastCut import fastCut, fastCut2
from graph import Graph, Node, Edge
from copy import deepcopy
from generator import *

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


def test(n):
    graph = complete_graph(10)
    moyenne = [0,0,0]

    for _ in range(n):

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
            print(f"Edge {edge.id}: {edge.start_node.id} -> {edge.end_node.id}")
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

def main():
    test(100)
    #graph = complete_graph(10)
    #draw_graph(graph)
    #printInfo(graph)
    # print()
    # temp = fastCut2(deepcopy(graph))
    # new_graph = Graph(temp)
    # count = 0
    # for edge in temp:
    #     count += 1
    #     print(f"Edge {edge.id}: {edge.start_node.id} -> {edge.end_node.id}")
    # print(f"Cut {count} : {prepare_node(temp)}")
    # draw_graph(new_graph)
    

    # print("Edges in the cut:", [edge.id for edge in temp])
    # print("Nodes in the cut:", list(prepare_node(temp)))
    # print("Nodes in the cut:", [edge.start_node.id for edge in temp] + [temp[-1].end_node.id])
    # print()
    
    # print("Edges in the cut:", [edge.id for edge in temp2])
    # print("Nodes in the cut:", list(prepare_node(temp2)))
    # print("Nodes in the cut:", [edge.start_node.id for edge in temp2] + [temp2[-1].end_node.id])





if __name__ == "__main__":
    main()