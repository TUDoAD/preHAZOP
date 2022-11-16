# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 08:55:27 2021

@author: Tim Holtermann
"""

def plot_graph(Path_graph, Path_plot):
    import networkx as nx
    import matplotlib.pyplot as plt

    graph=nx.read_graphml(Path_graph)
    color=[]
    width=[]
    node_sizes=[]
    pos={}
    dict_group_color={"Vessel":'orange', 'Column':'orange', 'Pipe tee':'grey', 'Valves':'grey', 'Fittings':'grey', 'Pump':'blue', 
               'Filter':'yellow', 'Heat exchanger':'red', 'Connector':'brown', 'MSR':'green'}
    
    #color of nodes   
    for node in graph.nodes():
        Found='No'
        for group in dict_group_color:            
            if graph.nodes[node]['group']==group:
                color.append(dict_group_color[group])
                Found='Yes'
        if Found=='No':
            color.append('grey')
            
        if graph.nodes[node]['group'] in ['Filter', 'Vessel', 'Column', 'Pump','Heat exchanger', '...']:
            node_sizes.append(1500)
        else:
            node_sizes.append(500) 
        
        pos[node]=(float(graph.nodes[node]['X']), float(graph.nodes[node]['Y']))


  
    #width of the connections   
    for edge in graph.edges():
        if graph.edges[edge]['Class'] in ['Signal line', 'Process connection line']:
            width.append(1)
        elif graph.edges[edge]['Class']=='Piping' and graph.edges[edge]['Sub_class']=='Main pipe':
            width.append(3)
        elif graph.edges[edge]['Class']=='Piping' and graph.edges[edge]['Sub_class']=='Secondary pipe':
            width.append(1)
        elif graph.edges[edge]['Class']=='Heat transfer medium':
            width.append(1)           
        else:
            width.append(10) 
                
    plot_graph = plt.figure(figsize=(40,20))
    nx.draw(graph, pos=pos, node_color=color, edgecolors='none', node_shape='o', node_size=node_sizes, font_size=35, width=width, edge_color='black', arrowsize=20, with_labels=False, font_weight='bold')
    plot_graph.savefig(Path_plot)   