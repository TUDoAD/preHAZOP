# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 08:12:06 2021

@author: tim11
"""

def Check_path(graph, path, counter_path_checking, IDs_between_forbidden, path_group, path_sub_group, row, path_change):
    
    path_group=path_group
    path_sub_group=path_sub_group
    start=path[0]
    end=path[-1]
        
    if len(path)>1:#avoiding start=end                    
        path_okay='Yes'
        
        #If a not regarded ID is within the path, the path is unnecessary
        #Therefore a list without beginning and end ID is created
        path_shortened=path.copy()
        path_shortened.remove(start)
        path_shortened.remove(end)
                        
        for ID_forbidden in IDs_between_forbidden:
            if ID_forbidden in path_shortened:
                path_okay='No'
                #print('Not regarded equipment within the path (row '+str(row+2)+')') 
        
        for node in path_shortened:#every node within the path
            if graph.nodes[node]['group'] in ['Vessel', 'Column', 'Shaping machines', 'Crushing/Grinding', 'Dryer', 'Centrifuge', 'Separator', 'Sieving', 'Mixer/Kneader']:                               
                        path_okay='No'        

        #Assuring that the edge (sub) class does not change within all checked paths
        #first edge of the overall path determine the (sub) class 
        for n in range(0, len(path)-1):
            step_FromID=path[n]
            step_ToID=path[n+1]
            
            #determine edge (sub) class 
            if n==0 and counter_path_checking==0:#avoid overwriting
                path_group=graph.edges[step_FromID, step_ToID]['group']
                path_sub_group=graph.edges[step_FromID, step_ToID]['sub_group']


            if path_sub_group=='Heat transfer pipe':
                path_okay='No'
            elif graph.edges[step_FromID, step_ToID]['group']!=path_group:
                path_okay='No'            
                                                       
        return [path_okay, path_group, path_sub_group, path_change]           