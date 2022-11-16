def check_temperatur_pressure(g, txt_path):
    """function to check pressure and temperature limitations
    
    Parameters:
    g: NetworkX DiGraph representing a P&ID for HAZOP
    txt_path: path of txt-file for storing results
    
    """
    
    file = open(txt_path, 'w')
    print('Please check possible Issues:\n')
    
    for node in list(g.nodes):
        neighbors = list(g.neighbors(node))
        for n in neighbors:
            
            # check T_min_design
            if g._node[node]['T_min_design'] != 'n.a.' and g._node[n]['T_min_design'] != 'n.a.':     
                if g._node[node]['T_min_design'] < g._node[n]['T_min_design']:
                    file.write('T_min_design in ', g._node[n]['PID_label'],': ', g._node[n]['T_min_design'], ' higher then T_min_design in ', g._node[node]['PID_label'], ': ', g._node[node]['T_min_design'],'\n')
        
            # check P_min_design
            if g._node[node]['P_min_design'] != 'n.a.' and g._node[n]['P_min_design'] != 'n.a.':   
                if g._node[node]['P_min_design'] < g._node[n]['P_min_design']:
                    file.write('p_min_design in ', g._node[n]['PID_label'],': ', g._node[n]['P_min_design'], ' higher then p_min_design in ', g._node[node]['PID_label'], ': ', g._node[node]['P_min_design'],'\n')
                    
            # check T_max_design
            if g._node[node]['T_max_design'] != 'n.a.' and g._node[n]['T_max_design'] != 'n.a.':
                if g._node[node]['T_max_design'] > g._node[n]['T_max_design']:
                    file.write('T_max_design in ', g._node[n]['PID_label'],': ', g._node[n]['T_max_design'], ' lower then T_max_design in ', g._node[node]['PID_label'], ': ', g._node[node]['T_max_design'],'\n')
                    
            # check P_max_design
            if g._node[node]['P_max_design'] != 'n.a.' and g._node[n]['P_max_design'] != 'n.a.':
                if g._node[node]['P_max_design'] > g._node[n]['P_max_design']:
                    file.write('P_max_design in ', g._node[n]['PID_label'],': ', g._node[n]['P_max_design'], ' lower then P_max_design in ', g._node[node]['PID_label'], ': ', g._node[node]['P_max_design'],'\n')
    
    print('Check of inconsistence in design pressure and temperature completed!\n')
