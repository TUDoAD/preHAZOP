def check_temperature_pressure(g, path):
    """function to check pressure and temperature limitations
    
    Parameters:
    g: NetworkX DiGraph representing a P&ID for HAZOP
    path: path of txt-file for storing results
    
    @Author: Jonas Oeing, TU Dortmund, BCI AG Apparatedesign
    
    """
    import os
    
    os.remove(path)
    file = open(path, 'w')
    file.write('Please check possible Issues:\n')
        
    for node in list(g.nodes):
        neighbors = list(g.neighbors(node))
        for n in neighbors:
            
            # check T_min_design
            if g._node[node]['T_min_design'] != 'n.a.' and g._node[n]['T_min_design'] != 'n.a.':     
                if g._node[node]['T_min_design'] < g._node[n]['T_min_design']:
                    string = 'T_min_design in ' + str(g._node[n]['PID_label']) + ': ' + str(g._node[n]['T_min_design']) + ' higher then T_min_design in ' + str(g._node[node]['PID_label']) + ': ' + str(g._node[node]['T_min_design']) + '\n'
                    file.write(str(string))
                    
            # check P_min_design
            if g._node[node]['P_min_design'] != 'n.a.' and g._node[n]['P_min_design'] != 'n.a.':   
                if g._node[node]['P_min_design'] < g._node[n]['P_min_design']:
                    string = 'p_min_design in ' + str(g._node[n]['PID_label']),': ' + str(g._node[n]['P_min_design']) + ' higher then p_min_design in ' + str(g._node[node]['PID_label']) + ': ' + str(g._node[node]['P_min_design']) +'\n'
                    file.write(str(string))
                    
            # check T_max_design
            if g._node[node]['T_max_design'] != 'n.a.' and g._node[n]['T_max_design'] != 'n.a.':
                if g._node[node]['T_max_design'] > g._node[n]['T_max_design']:
                    string = 'T_max_design in ' + str(g._node[n]['PID_label']) + ': ' + str(g._node[n]['T_max_design']) + ' lower then T_max_design in ' + str(g._node[node]['PID_label']) + ': ' + str(g._node[node]['T_max_design']) + '\n'
                    file.write(str(string))
                    
            # check P_max_design
            if g._node[node]['P_max_design'] != 'n.a.' and g._node[n]['P_max_design'] != 'n.a.':
                if g._node[node]['P_max_design'] > g._node[n]['P_max_design']:
                    string = 'P_max_design in ' + str(g._node[n]['PID_label']) + ': ' + str(g._node[n]['P_max_design']) + ' lower then P_max_design in ' + str(g._node[node]['PID_label']) + ': ' + str(g._node[node]['P_max_design']) + '\n'
                    file.write(str(string))
                        
    file.write('Check of inconsistence in design pressure and temperature completed!\n')
    file.close()
                    