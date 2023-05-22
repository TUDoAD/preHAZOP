# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:10:35 2022

@author: yangr
"""

import networkx as nx
import matplotlib.pyplot as plt
import os
import tkinter
from tkinter import ttk
from tkinter import messagebox






# Erfassung aller Eingangsinformationen und Überprüfung der Existenz der Datei
def enter_data():
    global name1
    global name2
    #accepted = accept_var.get()
    xml_for_networkx = graphri_entry.get()
    path1 = './'+xml_for_networkx+'.xml'
    isExist1 = os.path.exists(path1)

        
    if isExist1 == 1:
        
        name1 = xml_for_networkx
        
        """
        stoff1 = stoff1_combobox.get()
        stoff2 = stoff2_combobox.get()
        stoff3 = stoff3_combobox.get()
        stoff4 = stoff4_combobox.get()
        stoff5 = stoff5_combobox.get()
        stoff6 = stoff6_combobox.get()
        input_stoff__ = [stoff1, stoff2, stoff3, stoff4, stoff5, stoff6]
        input_stoff_exist = [x for x in input_stoff__ if x]
        print(input_stoff_exist)
        """
        tkinter.messagebox.showinfo(title="Successful", message="You can close the window")
    else:
        tkinter.messagebox.showerror(title="Error", message="Please check the file!")
        
        
        
        
        

window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()





link_input_frame = tkinter.LabelFrame(frame, text="Please enter the GraphML_Plus file name")
link_input_frame.grid(row = 0, column = 0, padx = 20, pady = 10)

graphri_label = tkinter.Label(link_input_frame, text="GraphML: ")
graphri_label.grid(row = 0, column = 0)

blank_label = tkinter.Label(link_input_frame, text=" ")
blank_label.grid(row = 0, column = 2)


graphri_entry = tkinter.Entry(link_input_frame, width=30)
graphri_entry.grid(row = 0, column = 1)


#Button
button = tkinter.Button(frame, text="Enter data", command= enter_data)
button.grid(row=2, column=0, padx=40, pady=10)


window.mainloop()




# Lesen GraphML Plus mit NetworkX
g = nx.read_graphml('./'+name1+'.xml')









#Die Funktion werden die Node und alle Edges von den Node gezeichnet, mit geeigneten Eigenschaften. 
def node_and_neighboors(g,name):

#um alle Nodes an HE9 rauszufinden und listen
    H=list(nx.all_neighbors(g,name))
    #print(H)
    H.append(name)   #HE9 in die List hinzufügen
    #print(H)


#um die Dictionary von Position aufzubauen, Key: names, Value: position (x,y)
    x = set()
    y = set()
    dic_position = {}
    for name in H:
        x.add(g._node[name]['X'])
        y.add(g._node[name]['Y'])
        a = float(g._node[name]['X'])
        b = float(g._node[name]['Y'])
        c = (a,b)
        #print("x-Wert:",a)
        #print("y-Wert:",b)
        #print(c)
        dic_position[name] = c
    #print("position",name, dic_position)
    #position = zip(x,y)     #falsche Reinfolgen 
    #print(list(zip(x,y)))     #falsche Reinfolgen
    #pos_dict = dict(zip(H,position))     #falsche Reinfolgen    


    #x(i) = g._node[name]['X']
    #y(i) = g._node[name]['Y']
    #i = i+1

    #leere Di-Graph öffnen
    v = nx.DiGraph()
    
    v.add_nodes_from(H)               #Nodes im Graph hinzufügen
    
    edges_in = list(g.in_edges(name))
    edges_out = list(g.out_edges(name))
    edges = edges_in + edges_out
    
    v.add_edges_from(edges)       #Nodes im Graph hinzufügen
    #v.add_edges_from(edges_out)
    Haupt_teil = ["Column", "Heat exchanger, detailed","Heat exchanger", "Vessel", "Silo", "Reactor"]
    color_list = []
    nodes_size = []
    for n in H:
        if g._node[n]['group'] in Haupt_teil:    
            color_list.append('red')
            nodes_size.append(100)
        elif g._node[n]['group'] in ["In-outlet", "Pipe tee", "Connector"]:
            color_list.append('lightBlue')
            nodes_size.append(50)
        elif g._node[n]['group'] in ["PCE Request", 'FIC', 'LICA+', 'LIC', 'TIC', 'MSR']:
            color_list.append('lightGreen')
            nodes_size.append(40)
        elif g._node[n]['group'] in ["Fluid pump", "Pump", "Filter"]:
            color_list.append('lightsalmon')
            nodes_size.append(80)
        else:
            color_list.append('orange')
            nodes_size.append(30)
    #print(color_list)
    
    neigh = list(nx.all_neighbors(g,name))
    #print("neighbors name:", neigh)

    edge_colors = []
    edge_form = [] 
    weight = [] 
    for name1 in neigh:
        if (name1,name) in edges:
            if g.get_edge_data(name1,name)['Class'] in ["Piping", "Pipe"]:
                edge_colors.append('black')
                edge_form.append('solid')
                weight.append(0.5)
            elif g.get_edge_data(name1,name)['Class'] =="Heat transfer medium":
                edge_colors.append('gold')
                edge_form.append('dashed')
                weight.append(0.3)
            elif g.get_edge_data(name1,name)['Class'] in ["Process connection line", "Signal line"]:
                edge_colors.append('gray')
                edge_form.append('dashed')
                weight.append(0.1)
            else:
                edge_colors.append('red')
                edge_form.append('dashed')
                weight.append(0.05)  
        elif (name,name1) in edges:
            if g.get_edge_data(name,name1)['Class'] in ["Piping", "Pipe"]:
                edge_colors.append('black')
                edge_form.append('solid')
                weight.append(0.5)
            elif g.get_edge_data(name,name1)['Class'] =="Heat transfer medium":
                edge_colors.append('gold')
                edge_form.append('dashed')
                weight.append(0.3)
            elif g.get_edge_data(name,name1)['Class'] in ["Process connection line", "Signal line"]:
                edge_colors.append('gray')
                edge_form.append('dashed')
                weight.append(0.1)
            else:
                edge_colors.append('red')
                edge_form.append('dashed')
                weight.append(0.05)
        
    #print(edge_colors)
    #print(edge_form)
    #print(weight)
    
    
    #edge_color = []

    #edge_color = ['green','green','green','green','green','green','red']
        
    nx.draw(v, dic_position, node_size=nodes_size, node_color=color_list, edge_color=edge_colors, style=edge_form, width=weight, with_labels=True, font_size=3)
    #print("Dadadada")
    #plt.savefig("picture_Digraph.png", dpi=300)
    
    




#um das ganze Fließbilder zu zeichnen
node_names = g.nodes()
for node in node_names:
    node_and_neighboors(g,node)
plt.savefig(name1+"_complete.png", dpi=300)
plt.close()
print("PID fertig gezeichnet")


#Zeichnen Drückräumen
main_nodes = ["Column", "Vessel","Heat exchanger", "Pump", "Reactor"]
ende_nodes = ["MSR", "n.a.", "Connector", "Valves", "Valve"]

nodes_exist_all = []
#zeichnen-Funktion von Druck-Raum
def draw_nodes_with_same_pressure(g,n):
    
    #main_node_names=[n]
    #global nodes_exist
    #nodes_exist = []
    nodes_exist = []
    copy_g = nx.read_graphml('./'+name1+'.xml')

    #um die Drucksensoren am Ende rauszufinden.
    def endnode_and_pressure(g,name):
    #um alle Nodes an HE9 rauszufinden und listen
        M=list(nx.all_neighbors(g,name))
        #print(H)
        H = []
        edges = []
        for n in M:
            if g._node[n]['group'] in ['FIC', 'LICA+', 'LIC', 'TIC', 'MSR']:
                H.append(n)
                if g.has_edge(name,n):
                    edges.append((name,n))
                    nodes_exist.append(n)
                    nodes_exist_all.append(n)
                elif g.has_edge(n,name):
                    edges.append((n,name))
                    nodes_exist.append(n)
                    nodes_exist_all.append(n)
            elif g._node[n]['group'] in ["Valve", "Valves"]:
                H.append(n)
                if g.has_edge(name,n):
                    edges.append((name,n))
                    nodes_exist.append(n)
                    nodes_exist_all.append(n)
                else:
                    edges.append((n,name))
                    nodes_exist.append(n)
                    nodes_exist_all.append(n)
        H.append(name)
        #print(H)
        #print(name)
        dic_position = {}
        for n in H:
            a = float(g._node[n]['X'])
            b = float(g._node[n]['Y'])
            #c = (a,b)
            dic_position[n] = (a,b)
    


        #x(i) = g._node[name]['X']
        #y(i) = g._node[name]['Y']
        #i = i+1

        #leere Di-Graph öffnen
        v = nx.DiGraph()
        
        v.add_nodes_from(H)               #Nodes im Graph hinzufügen    
        v.add_edges_from(edges)       #Nodes im Graph hinzufügen
        
        Haupt_teil = ["Column", "Heat exchanger", "Vessel", "Silo", "Reactor", "Pump"]
        color_list = []
        nodes_size = []
        for n in H:
            if g._node[n]['group'] in Haupt_teil:    
                color_list.append('red')
                nodes_size.append(100)
            elif g._node[n]['group'] in ["In-outlet", "Pipe tee", "Connector"]:
                color_list.append('lightBlue')
                nodes_size.append(50)
            elif g._node[n]['group'] in ["PCE Request", 'FIC', 'LICA+', 'LIC', 'TIC', 'MSR']:
                color_list.append('lightGreen')
                nodes_size.append(40)
            elif g._node[n]['group'] in ["Pump", "Filter"]:
                color_list.append('lightsalmon')
                nodes_size.append(80)
            else:
                color_list.append('orange')
                nodes_size.append(30)
                
        #neigh_end = list(nx.all_neighbors(g,name))
        edge_1 = list(g.in_edges(name))
        edge_2 = list(g.out_edges(name))
        #print("neighbors name:", neigh)

        edge_colors = []
        edge_form = [] 
        weight = [] 
        for name1 in edge_1:
            if name1[0] in H:
                if g.get_edge_data(*name1)['Class'] in ["Piping", "Pipe"]:
                    edge_colors.append('black')
                    edge_form.append('solid')
                    weight.append(0.5)
                elif g.get_edge_data(*name1)['Class'] =="Heat transfer medium":
                    edge_colors.append('gold')
                    edge_form.append('dashed')
                    weight.append(0.3)
                elif g.get_edge_data(*name1)['Class'] in ["Process connection line", "Signal line"]:
                    edge_colors.append('gray')
                    edge_form.append('dashed')
                    weight.append(0.1)
                else:
                    edge_colors.append('red')
                    edge_form.append('dashed')
                    weight.append(0.05)
        for name2 in edge_2:
            if name2[1] in H:
                if g.get_edge_data(*name2)['Class'] in ["Piping", "Pipe"]:
                    edge_colors.append('black')
                    edge_form.append('solid')
                    weight.append(0.5)
                elif g.get_edge_data(*name2)['Class'] =="Heat transfer medium":
                    edge_colors.append('gold')
                    edge_form.append('dashed')
                    weight.append(0.3)
                elif g.get_edge_data(*name2)['Class'] in ["Process connection line", "Signal line"]:
                    edge_colors.append('gray')
                    edge_form.append('dashed')
                    weight.append(0.1)
                else:
                    edge_colors.append('red')
                    edge_form.append('dashed')
                    weight.append(0.05)
            
        nx.draw(v, dic_position, node_size=nodes_size, node_color=color_list, edge_color=edge_colors, style=edge_form, width=weight, with_labels=True, font_size=3)
    
    
    #Druckraumdetektion
    #for node in main_node_names:
    main_node = g._node[n]['group']
    if main_node in main_nodes:
        node_and_neighboors(g,n)
        nodes_exist.append(n)
        nodes_exist_all.append(n)
        neighboor_of_main_node = list(nx.all_neighbors(g,n))
        for T in neighboor_of_main_node:
            if g._node[T]['group'] in ende_nodes:
                nodes_exist.append(T)
                nodes_exist_all.append(T)
                endnode_and_pressure(g,T) 
            elif T not in nodes_exist:
                node_and_neighboors(g,T)
                nodes_exist.append(T)
                nodes_exist_all.append(T)
                neighboor_of_sub_node_1 = list(nx.all_neighbors(g,T))
                for T1 in neighboor_of_sub_node_1:
                    if g._node[T1]['group'] in ende_nodes:
                        nodes_exist.append(T1)
                        nodes_exist_all.append(T1)
                        endnode_and_pressure(g,T1) 
                    elif T1 not in nodes_exist:
                        node_and_neighboors(g,T1)
                        nodes_exist.append(T1)
                        nodes_exist_all.append(T1)
                        neighboor_of_sub_node_2 = list(nx.all_neighbors(g,T1))
                        for T2 in neighboor_of_sub_node_2:
                            if g._node[T2]['group'] in ende_nodes:
                                nodes_exist.append(T2)
                                nodes_exist_all.append(T2)
                                endnode_and_pressure(g,T2) 
                            elif T2 not in nodes_exist:
                                node_and_neighboors(g,T2)
                                nodes_exist.append(T2)
                                nodes_exist_all.append(T2)
                                neighboor_of_sub_node_3 = list(nx.all_neighbors(g,T2))
                                for T3 in neighboor_of_sub_node_3:
                                    if g._node[T3]['group'] in ende_nodes:
                                        nodes_exist.append(T3)
                                        nodes_exist_all.append(T3)
                                        endnode_and_pressure(g,T3) 
                                    elif T3 not in nodes_exist:
                                        node_and_neighboors(g,T3)
                                        nodes_exist.append(T3)
                                        nodes_exist_all.append(T3)
                                        neighboor_of_sub_node_4 = list(nx.all_neighbors(g,T3))
                                        for T4 in neighboor_of_sub_node_4:
                                            if g._node[T4]['group'] in ende_nodes:
                                                nodes_exist.append(T4)
                                                nodes_exist_all.append(T4)
                                                endnode_and_pressure(g,T4) 
                                            elif T4 not in nodes_exist:
                                                node_and_neighboors(g,T4)
                                                nodes_exist.append(T4)
                                                nodes_exist_all.append(T4)
                                                neighboor_of_sub_node_5 = list(nx.all_neighbors(g,T4))
                                                for T5 in neighboor_of_sub_node_5:
                                                    if g._node[T5]['group'] in ende_nodes:
                                                        nodes_exist.append(T5)
                                                        nodes_exist_all.append(T5)
                                                        endnode_and_pressure(g,T5) 
                                                    elif T5 not in nodes_exist:
                                                        node_and_neighboors(g,T5)
                                                        nodes_exist.append(T5)
                                                        nodes_exist_all.append(T5)
                                                        neighboor_of_sub_node_6 = list(nx.all_neighbors(g,T5))
                                                        for T6 in neighboor_of_sub_node_6:
                                                            if g._node[T6]['group'] in ende_nodes:
                                                                nodes_exist.append(T6)
                                                                nodes_exist_all.append(T6)
                                                                endnode_and_pressure(g,T6) 
                                                            elif T6 not in nodes_exist:
                                                                node_and_neighboors(g,T6)
                                                                nodes_exist.append(T6)
                                                                nodes_exist_all.append(T6)
                                                                neighboor_of_sub_node_7 = list(nx.all_neighbors(g,T6))
                                                                for T7 in neighboor_of_sub_node_7:
                                                                    if g._node[T7]['group'] in ende_nodes:
                                                                        nodes_exist.append(T7)
                                                                        nodes_exist_all.append(T7)
                                                                        endnode_and_pressure(g,T7) 
                                                                    elif T7 not in nodes_exist:
                                                                        node_and_neighboors(g,T7)
                                                                        nodes_exist.append(T7)
                                                                        nodes_exist_all.append(T7)
                                                                        neighboor_of_sub_node_8 = list(nx.all_neighbors(g,T7))
                                                                        for T8 in neighboor_of_sub_node_8:
                                                                            if g._node[T8]['group'] in ende_nodes:
                                                                                nodes_exist.append(T8)
                                                                                nodes_exist_all.append(T8)
                                                                                endnode_and_pressure(g,T8) 
                                                                            elif T8 not in nodes_exist:
                                                                                node_and_neighboors(g,T8)
                                                                                nodes_exist.append(T8)
                                                                                nodes_exist_all.append(T8)
                                                                                neighboor_of_sub_node_9 = list(nx.all_neighbors(g,T8))
                                                                                for T9 in neighboor_of_sub_node_9:
                                                                                    if g._node[T9]['group'] in ende_nodes:
                                                                                        nodes_exist.append(T9)
                                                                                        nodes_exist_all.append(T9)
                                                                                        endnode_and_pressure(g,T9)
                                                                                    elif T9 not in nodes_exist:
                                                                                        node_and_neighboors(g,T9)
                                                                                        nodes_exist.append(T9)
                                                                                        nodes_exist_all.append(T9)
                                                                                        neighboor_of_sub_node_10 = list(nx.all_neighbors(g,T9))
                                                                                        for T10 in neighboor_of_sub_node_10:
                                                                                            if g._node[T10]['group'] in ende_nodes:
                                                                                                nodes_exist.append(T10)
                                                                                                nodes_exist_all.append(T10)
                                                                                                endnode_and_pressure(g,T10)
                                                                                            elif T10 not in nodes_exist:
                                                                                                node_and_neighboors(g,T10)
                                                                                                nodes_exist.append(T10)
                                                                                                nodes_exist_all.append(T10)
                                                                                                neighboor_of_sub_node_11 = list(nx.all_neighbors(g,T10))
                                                                                                for T11 in neighboor_of_sub_node_11:
                                                                                                    if g._node[T11]['group'] in ende_nodes:
                                                                                                        nodes_exist.append(T11)
                                                                                                        nodes_exist_all.append(T11)
                                                                                                        endnode_and_pressure(g,T11)
                                                                                                    elif T11 not in nodes_exist:
                                                                                                        node_and_neighboors(g,T11)
                                                                                                        nodes_exist.append(T11)
                                                                                                        nodes_exist_all.append(T11)
                                                                                                        neighboor_of_sub_node_12 = list(nx.all_neighbors(g,T11))
                                                                                                        for T12 in neighboor_of_sub_node_12:
                                                                                                            if g._node[T12]['group'] in ende_nodes:
                                                                                                                nodes_exist.append(T12)
                                                                                                                nodes_exist_all.append(T12)
                                                                                                                endnode_and_pressure(g,T12)
                                                                                                            elif T12 not in nodes_exist:
                                                                                                                node_and_neighboors(g,T12)
                                                                                                                nodes_exist.append(T12)
                                                                                                                nodes_exist_all.append(T12)
                                                                                                                neighboor_of_sub_node_13 = list(nx.all_neighbors(g,T12))
                                                                                                                for T13 in neighboor_of_sub_node_13:
                                                                                                                    if g._node[T13]['group'] in ende_nodes:
                                                                                                                        nodes_exist.append(T13)
                                                                                                                        nodes_exist_all.append(T13)
                                                                                                                        endnode_and_pressure(g,T13)
                                                                                                                    elif T13 not in nodes_exist:
                                                                                                                        node_and_neighboors(g,T13)
                                                                                                                        nodes_exist.append(T13)
                                                                                                                        nodes_exist_all.append(T13)
                                                                                                                        #neighboor_of_sub_node_14 = list(nx.all_neighbors(g,T13))

    # Erstellung neuer Ordner
    def createFolder(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print('Error: Creating directory.' + directory)            
            createFolder('./Druckraum/')
                                                                                                      
    script_dir = os.path.dirname(__file__) + '\Druckraum_'+name1 
    results_dir = os.path.join(script_dir, g._node[n]['group'] +'/')
    
    sample_file_name = "Druckraum_von_"
    #exist_bild_von = []    
    for n in nodes_exist:
        if g._node[n]['group'] in main_nodes:
            sample_file_name = sample_file_name + '_'+ n
            #exist_bild_von.append(n)
    #print(exist_bild_von)
    
        
    if not os.path.isdir(results_dir):
        os.makedirs(results_dir)

    # Bild für Drückräume speichern
    plt.savefig(results_dir + sample_file_name, dpi=300)
    #plt.savefig("Druckraum_11_10_10 "+n+" .png", dpi=300)
    plt.close()
    
    
    # Vorbereitung des Bildes für die nicht in die Druckräume eingefügten Knoten
    #to_remove = []
    node_names = g.nodes()
    #for node in node_names:
        #if node not in nodes_exist:
            #to_remove.append(node)
    #global to_remove      
    to_remove = [x for x in node_names if x not in nodes_exist]
    #print(to_remove)
    copy_g.remove_nodes_from(to_remove)
    nx.write_graphml_lxml(copy_g, results_dir + sample_file_name +'.xml')
    
    #main_nodes_with_same_pressure = [x for x in nodes_exist if g._node[x]['group'] in main_nodes]
    for x in nodes_exist: 
        if g._node[x]['group'] in main_nodes:
            main_nodes_with_same_pressure.append(x)
    #print(main_nodes_with_same_pressure)
    

main_node_names = []
node_names = g.nodes()
for node_name in node_names:
    k = g._node[node_name]['group']
    if k in main_nodes:
        main_node_names.append(node_name)
#print(main_node_names)

    # Alle Druckräume für die Haupteinrichtungen zu ermitteln und Redundanzen zu vermeiden
main_nodes_with_same_pressure=[]
for x in main_node_names:
    if x not in main_nodes_with_same_pressure:    
        draw_nodes_with_same_pressure(g,x)
    else:
        m = g._node[x]['group']
        print("das Bild von "+ m +" "+ x +" existiert schon")
        #draw_nodes_with_same_pressure(g,x)                

#um das ganze Fließbilder zu zeichnen

for i in node_names:
    if i not in nodes_exist_all:
        #print(i)
        node_and_neighboors(g,i)
plt.savefig(name1+"_rest_to_check.png", dpi=300)



print("ferig")


















"""
ende_nodes = ["MSR", "n.a.", "Pump", "Connector","Valves"]

neighboors=list(g.neighbors('HE139'))
print("HE139:",neighboors)
neighboors=list(g.neighbors('T1'))
print("T1:",neighboors)
new_neighboors=[x for x in neighboors if g._node[x]['group'] in ende_nodes]
print("new_neighboors:", new_neighboors)
if len(neighboors)==len(new_neighboors):
    print("Das Suchen ist fertig")
else: print("blablablabla")
"""

"""
m = list(nx.all_neighbors(g,'HE139'))
print(m)
print(g.in_edges('HE139'))
print(g.out_edges('HE139'))
k1 = g.in_edges('HE139')
k2 = g.out_edges('HE139')
k3=k1+k2
print(k3)
"""




"""  
ende_nodes = ["MSR", "n.a.", "Pump", "Connector","Valves"]



nodes_exsit = []
def find_nodes_with_same_pressure(g,n):
    if n not in nodes_exsit:
        neighboors=list(nx.all_neighbors(g,n))
        neighboors.append(n)
        new_neighboors=[x for x in neighboors if g._node[x]['group'] not in ende_nodes]
        if len(new_neighboors) > 0:
            for x in new_neighboors:
                if x not in nodes_exsit:
                    node_and_neighboors(g,x)
                    nodes_exsit.append(x)
                    print(nodes_exsit)
                    return x
        elif len(new_neighboors) == 0:
            print("Das Suchen ist fertig")
            plt.savefig("Drückraum.png", dpi=300)
    else:
        print("existiert")

        
find_nodes_with_same_pressure(g,'HE22')

"""











"""
#probiert, um die Farbe, Form und "Width" von Edges zu definieren,
print(g.edges('VE110'))
print(len(g.edges('VE110')))
print(list(g.neighbors('VE110')))

length = len(g.edges('VE110'))
n = length +1
print(n)

     

print(g.edges('VE110'))
#m = g.edges('VE110')
#h = list(g.edges(data=True))[0]
#print(g['VE110']['VV148']['Class'])
print(g.get_edge_data('VE110', 'VV148')['Class'])

m = list(g.neighbors('VE110'))
print(m)

edge_colors = []
edge_form = [] 
weight = [] 
for name in m:
    print(g.get_edge_data('VE110', name)['Class'])
    if g.get_edge_data('VE110', name)['Class'] == "Piping":
        edge_colors.append('black')
        edge_form.append('solid')
        weight.append(0.5)
    elif g.get_edge_data('VE110', name)['Class'] =="Heat transfer medium":
        edge_colors.append('yellow')
        edge_form.append('dashed')
        weight.append(0.3)
    elif g.get_edge_data('VE110', name)['Class'] =="Process connection line":
        edge_colors.append('gray')
        edge_form.append('dashed')
        weight.append(0.1)
print(edge_colors)
print(edge_form)
print(weight)

"""









