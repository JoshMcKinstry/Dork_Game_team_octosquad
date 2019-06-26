import matplotlib.pyplot as plt
import networkx as nx
from yamlreader import YamlReader as yaml
from mapvalidation import ValidMaze as val



class MapGraph:

    yaml.yaml_loader('dork.')
    plt.tight_layout()

    G = nx.Graph()
    # explicitly set positions
    pos = {0: (4, 5),
        1: (4, 3),
        2: (4, 1),
        3: (2, 1),
        4: (6, 1),
        5: (2, 3),
        6: (6, 3)}

    nx.draw_networkx_nodes(G, pos, node_size=500, nodelist=[0, 1, 2, 3, 4], node_color='#808080')
    nx.draw_networkx_nodes(G, pos, node_size=1, nodelist=[5,6], node_color='k')


    # G.remove_edges_from(G.edges())
    G.number_of_edges()
    G.add_edge(0, 1)
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    G.add_edge(2, 4)
    G.add_edge(3, 5)
    G.add_edge(4, 6)
    G.add_edge(6, 1)
    G.add_edge(5, 1)

    labels={}
    labels[0]="Treasure room"
    labels[1]="Boss"
    labels[3]="     Roadrunner's \n Nest"
    labels[2]="Student Success \n Building"
    labels[4]="Lounge"


    G.number_of_edges()
    edges = G.edges()
    #labels = G.labels()

    nx.draw_networkx_edges(G, pos, edge_list=edges)
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=8)
    plt.tight_layout()
    plt.show()