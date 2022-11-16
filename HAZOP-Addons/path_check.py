import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_nodes_from([
     ('A', {"NodeClass": "Pump"}),
     ('B', {"NodeClass": "Vessel"}),
     ('C', {"NodeClass": "Column"}),
     ('D', {"NodeClass": "Valve"}),
     ('E', {"NodeClass": "Vessel"}),
     ('F', {"NodeClass": "Pump"}),
     ('G', {"NodeClass": "Vessel"}),
     ('H', {"NodeClass": "Valve"}),     
     ])
    
G.add_edges_from(
    [('A', 'B'), ('A', 'C'), ('D', 'B'), ('E', 'C'), ('E', 'F'),
     ('B', 'H'), ('B', 'G'), ('B', 'F'), ('C', 'G')])

p_influence = ['Pump', 'Valve']

nx.draw(G, cmap = plt.get_cmap('jet'), with_labels=True)

boundary_nodes = []
for node in G.nodes():
    if G._node[node]['NodeClass'] in p_influence:
        boundary_nodes.append(node)

p_zone_list = []
p_zone=[]

for b in boundary_nodes:
    boundary_nodes_wb=boundary_nodes
    boundary_nodes_wb.remove(b)
    for c in boundary_nodes_wb:
        path=nx.all_simple_paths(G,b,c)
        