from igraph import *
import unidecode
import plotly.plotly as py
from plotly.graph_objs import *


NUMBER_LETTER = 5


def read_dictionary_file(file):
    """Reads a txt file and loads all it's NUMBER_LETTER letters words into a list"""
    f = open(file, "r")
    words_list = []
    for word in f:
        word = word.strip('\n')
        if len(word) == NUMBER_LETTER:
            words_list.append(unicode(word.ascii_lowercase))
    return words_list


def build_graph(words_list):
    """Create a graph from a list of words."""
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    g = Graph()
    g.add_vertices(words_list)
    for word in words_list:
        print(word)
        for index in range(NUMBER_LETTER):
            for new_letter in alphabet:
                new_word = word[:index] + new_letter + word[index + 1:]
                if new_word in words_list and new_word != word:
                    print(word + "<->" + new_word)
                    g.add_edges([(word, new_word)])
    return g

def show_graph(g):
    """Simple graph rendering using igraph plotself.

    https://igraph.org/python/doc/tutorial/tutorial.html#drawing-a-graph-using-a-layout
    """
    layout = g.layout("lgl")
    plot(g, layout = layout)

def export_to_iplot(G):
    """ Export graph to plotly for interactive sharing.

    You need an account on plotly: https://plot.ly/python/getting-started/
    Using sample code from this exemple: https://plot.ly/python/igraph-networkx-comparison/
    """
    labels=list(G.vs['name'])
    N=len(labels)
    E=[e.tuple for e in G.es]# list of edges
    layt = G.layout()#kamada-kawai layout is very slow to render on my machine.
    Xn=[layt[k][0] for k in range(N)]
    Yn=[layt[k][1] for k in range(N)]
    Xe=[]
    Ye=[]
    for e in E:
        Xe+=[layt[e[0]][0],layt[e[1]][0], None]
        Ye+=[layt[e[0]][1],layt[e[1]][1], None]

    trace1=Scatter(x=Xe,
                   y=Ye,
                   mode='lines',
                   line= dict(color='rgb(210,210,210)', width=1),
                   hoverinfo='none'
                   )
    trace2=Scatter(x=Xn,
                   y=Yn,
                   mode='markers',
                   name='ntw',
                   marker=dict(symbol='circle-dot',
                                            size=5,
                                            color='#6959CD',
                                            line=dict(color='rgb(50,50,50)', width=0.5)
                                            ),
                   text=labels,
                   hoverinfo='text'
                   )

    axis=dict(showline=False, # hide axis line, grid, ticklabels and  title
              zeroline=False,
              showgrid=False,
              showticklabels=False,
              title=''
              )

    width=800
    height=800
    layout=Layout(title= "pyperec test 2",
        font= dict(size=12),
        showlegend=False,
        autosize=False,
        width=width,
        height=height,
        xaxis=layout.XAxis(axis),
        yaxis=layout.YAxis(axis),
        margin=layout.Margin(
            l=40,
            r=40,
            b=85,
            t=100,
        ),
        hovermode='closest',
        annotations=[
               dict(
               showarrow=False,
                text='From a 2401 list of 5 letters french words. Proper nouns not removed.',
                xref='paper',
                yref='paper',
                x=0,
                y=-0.1,
                xanchor='left',
                yanchor='bottom',
                font=dict(
                size=14
                )
                )
            ]
        )

    data=[trace1, trace2]
    fig=Figure(data=data, layout=layout)

    py.iplot(fig, filename='Pyperec-test-2')


# Exemples
# words_list = read_dictionary_file("french/liste_french.txt")
# g = build_graph(words_list)
# g.write_pickle("graph.pickle")
# g = load("graph.pickle")
