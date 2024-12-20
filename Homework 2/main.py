from contract import contract
from fastCut import fastCut, fastCut2
from graph import Graph, Node, Edge
from copy import deepcopy
from generator import *
import time
#from draw import draw_graph

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
    all_times = []
    for vertices in range(1, 900, 10):
        #print("Nbr vertices :",vertices)
        #v1 = vertices//2
        #v2 = vertices-v1
        #print("V1 :",v1,"V2 :",v2)
        #v2 = int(vertices*(2*random.random()))
        #print("Vertices :",vertices,"v2",v2)
        v1 = vertices//random.randint(1,(vertices//4)+1)
        v2 = vertices-v1
        graph = multigraph(v1,v2)
        nb_edges = len(graph.edges)
        print("Nb edges :",nb_edges)
        try:
            whole_timer = 0
            if vertices > 20:
                if vertices <35:
                    n = 5
                else:
                    n = 3
            for _ in range(n):
                graph_copy = deepcopy(graph)
                timer = time.time()
                fastCut(graph_copy)
                timer = time.time() - timer
                whole_timer += timer
            all_times.append([nb_edges,whole_timer/n])
        except ValueError:
            #print(all_times)
            pass


    print(all_times)

def main():
    test(10)
    #G = planar_graph(5,7)
    #draw_graph(G)
    #G = planar_graph(25,100)
    #fastCut(G)
    #draw_graph(G)
    #graph = multigraph(6, 11)
    # graph = complete_graph(25)
    # #draw_graph(graph)
    # #printInfo(graph)
    # # print()
    # t1 = time.time()
    # temp = fastCut(deepcopy(graph))
    # t1 = time.time() - t1

    # # new_graph = Graph(temp)
    # count1 = 0
    # for edge in temp:
    #     count1 += 1
    #     #print(f"Edge {edge.id}: {edge.start_node.id} -> {edge.end_node.id}")
    # print(f"Cut {count1} : {prepare_node(temp)}")
    
    
    # t2 = time.time()
    # temp = fastCut2(deepcopy(graph))
    # t2 = time.time() - t2

    # new_graph = Graph(temp)
    # count2 = 0
    # for edge in temp:
    #     count2 += 1
    #     #print(f"Edge {edge.id}: {edge.start_node.id} -> {edge.end_node.id}")
    # print(f"Cut {count2} : {prepare_node(temp)}")

    # print("T1 :",t1 ,"Count :",count1)
    # print("T2 :",t2 ,"Count :",count2)



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