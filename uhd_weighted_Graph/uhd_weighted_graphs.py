from algorithms.prims import prims_algorithm
import networkx as nx


#This runs my G1 graph#
G = nx.read_weighted_edgelist('data\G1.txt',nodetype = int)
T=prims_algorithm(G,4,draw=True, show_prop=True)

#This runs my G2 graph#
G = nx.read_weighted_edgelist('data\G2.txt',nodetype = int)

T=prims_algorithm(G,1,draw=True, show_prop=True)


#This runs my G3 graph#
G = nx.read_weighted_edgelist('data\G3.txt',nodetype = int)

T=prims_algorithm(G,4,draw=True, show_prop=True)