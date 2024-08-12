import networkx as nx
import pickle
import chart_studio.plotly as py
import random
from plotly.graph_objs import Data, Figure, Layout, Line, Marker, Scatter, XAxis, YAxis
from plotly.offline import init_notebook_mode, plot, iplot
from typing import Optional, List

init_notebook_mode(connected=True)

class Map:
    def __init__(self, G: nx.Graph) -> None:
        """
        Initialize the Map object with a graph.

        Args:
            G (nx.Graph): A NetworkX graph representing the map.
        """
        self._graph = G
        self.intersections = nx.get_node_attributes(G, "pos")
        self.roads = [list(G[node]) for node in G.nodes()]

    def save(self, filename):
        """
        Save the map to a file.

        Args:
            filename (str): The name of the file to save the map to.
        """
        with open(filename, 'wb') as f:
            pickle.dump(self._graph, f)

def load_map(name: str) -> Map:
    """
    Load a map from a file.

    Args:
        name (str): The name of the file to load the map from.

    Returns:
        Map: The loaded map.
    """    
    with open(name, 'rb') as f:
        G = pickle.load(f)
    return Map(G)

def show_map(M: Map, start: Optional[int] = None, goal: Optional[int] = None, path: Optional[List[int]] = None) -> None:
    """
    Display the map using Plotly.

    Args:
        M (Map): The map to display.
        start (Optional[int]): The starting node (default is None).
        goal (Optional[int]): The goal node (default is None).
        path (Optional[List[int]]): The path to highlight (default is None).
    """    
    G = M._graph
    pos = nx.get_node_attributes(G, 'pos')
    edge_trace = Scatter(
    x=[],
    y=[],
    line=Line(width=0.5, color='#888'),
    # mode='lines',
    hoverinfo='none',
    mode='lines')

    for edge in G.edges():
        x0, y0 = G.nodes[edge[0]]['pos']
        x1, y1 = G.nodes[edge[1]]['pos']
        edge_trace['x'] += (x0, x1, None)
        edge_trace['y'] += (y0, y1, None)

    node_trace = Scatter(
        x=[],
        y=[],
        text=[],
        mode='markers',
        hoverinfo='text',
        marker=Marker(
            showscale=False,
            # colorscale options
            # 'Greys' | 'Greens' | 'Bluered' | 'Hot' | 'Picnic' | 'Portland' |
            # Jet' | 'RdBu' | 'Blackbody' | 'Earth' | 'Electric' | 'YIOrRd' | 'YIGnBu'
            colorscale='Hot',
            reversescale=True,
            color=[],
            size=10,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line=dict(width=2)))
    for node in G.nodes():
        x, y = G.nodes[node]['pos']
        node_trace['x'] = node_trace['x'] + (x,)
        node_trace['y'] = node_trace['y'] + (y,)

    for node, adjacencies in enumerate(G.adjacency()):
        color = 0
        if path and node in path:
            color = 2
        if node == start:
            color = 3
        elif node == goal:
            color = 1
        # node_trace['marker']['color'].append(len(adjacencies))
        node_trace['marker']['color'] = node_trace['marker']['color'] + (color,)
        node_info = "Intersection " + str(node)
        node_trace['text'] = node_trace['text'] + (node_info,)

    fig = Figure(data=Data([edge_trace, node_trace]),
                 layout=Layout(
                    title='<br>Network graph made with Python',
                    titlefont=dict(size=16),
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),
                   
                    xaxis=XAxis(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=YAxis(showgrid=False, zeroline=False, showticklabels=False)))

    iplot(fig)
