from .mybdd import*
from .node import And,Or,Not,BasicEvent
from .FaultTree_check import searchBasicEventcount
import pydotplus
from IPython.display import Image
from graphviz import Graph

def _draw(x):
    dotf = x.todot()
    g = pydotplus.graph_from_dot_data(dotf)
    return Image(g.create_png())

def drawBDD(event):
    if  type(event) == BasicEvent:
        g = Graph(format='png')
        g.node('True',shape='box')
        return g
    elif type(event) == And or type(event) == Or or type(event) == Not:
        bdd = BDD()
        count = searchBasicEventcount(event)
        for k,v in sorted(count.items(), key=lambda x: x[1]):
            bdd.var(k)
        return _draw(_Gate(event,bdd))
    else:
        print("This is not correct")

def _Gate(event,bdd):
    p=[]
    if type(event) == BasicEvent:
        return bdd.var(event.name)
    elif type(event) == And or type(event) == Or or type(event) == Not:
        for i in event.child:
            if type(i) == BasicEvent:
                p.append(bdd.var(i.name))
            elif type(i) == And or type(i) == Or or type(i) == Not:
                p.append(_Gate(i,bdd))
            else:
                print("This is not correct")
    else:
        print("This is not correct")
    #   p.sort(key = lambda x:bdd.index[x.var])
    if type(event) == And:
        return createAndGate(bdd,p)
    if type(event) == Or:
        return createOrGate(bdd,p)
    if type(event) == Not:
        return  bdd.Not(p[0])
    
def getBDD(event):#eventがBasicEventだった場合エラーになる
    bdd = BDD()
    count = searchBasicEventcount(event)
    for k,v in sorted(count.items(), key=lambda x: x[1]):
        bdd.var(k)
    return _Gate(event,bdd)