
import PySimpleGUI as psg
from Detection import eHazop
from Dexpi2graph import Dexpi2graph
from Process_graph import Graph_smart
from Link_simu import Link_simulation
from plot_graph import plot_graph
from Evaluation import Risk_assesement
import range_check
import networkx as nx

#Define window content
layout = [[psg.Text("DEXPI-Export")],
          [psg.Input(key='Path_DEXPI'), psg.FileBrowse(file_types=(("XML Files", "*.xml"),))],
          [psg.Text("Simulation results")],
          [psg.Input(key='Path_simulation'), psg.FileBrowse(file_types=(("XML Files", "*.xml"),))],         
          [psg.Button('Start')],
          [psg.ProgressBar(100, orientation='h', size=(30, 3), key='progressbar')],
          [psg.Output()],
          [psg.Image('./GUI_figs/AD_Logo_EN_600dpi_gui.png')],
          [psg.Text(' CC: TU Dortmund University, Laboratory of Equipment Design \n Authors: Jonas Oeing, Tim Holtermann')]]

# create window
window = psg.Window('preHAZOP - ad@TUDO', layout)
progress_bar = window['progressbar']

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    if event == 'Start':
        
        progress_bar.UpdateBar(10)       
        Path_simulation=values['Path_simulation']
        Path_DEXPI=values['Path_DEXPI']
        Path_HAZOP_data='./data_storage.xlsx' 
        Path_HAZOP_template='./HAZOP_template.xlsx'         
        Path_graph='./Output/GraphML/Graph_PID'
        Path_graph_smart='./Output/GraphML/Graph_HAZOP'
        Path_graph_link_simu='./Output/GraphML/Graph_PID+'        
        Path_plot_graph='./Output/Plots/Graph_PID.png'
        Path_plot_graph_smart='./Output/Plots/Graph_HAZOP.png'
        Path_plot_graph_link_simu='./Output/Plots/plot_graph_link_simu.png'         
        Path_results='./Output/HAZOP_results.xlsx'
        
        Dexpi2graph(Path_DEXPI, Path_graph, Path_results, Path_HAZOP_template)
        progress_bar.UpdateBar(20)        
        plot_graph(Path_graph, Path_plot_graph) 
        progress_bar.UpdateBar(30)
        Link_simulation(Path_graph, Path_simulation, Path_graph_link_simu, Path_results)
        progress_bar.UpdateBar(40)
        Graph_smart(Path_graph_link_simu, Path_graph_smart, Path_results)
        progress_bar.UpdateBar(50)
        plot_graph(Path_graph_smart, Path_plot_graph_smart)
        progress_bar.UpdateBar(60)        
        eHazop(Path_graph_smart, Path_HAZOP_data, Path_results) 
        progress_bar.UpdateBar(80)
        Risk_assesement(Path_graph_smart, Path_results, Path_HAZOP_data)

        progress_bar.UpdateBar(90)
        #range_check
        g = nx.read_graphml('./Output/GraphML/Graph_HAZOP')
        range_check.check_temperature_pressure(g, './Output/range_check_results.txt')
        
        progress_bar.UpdateBar(100)
        psg.popup('Run was successful! Results in output.')

        window.close()
    
       

    if event == psg.WINDOW_CLOSED:
        break

window.close()