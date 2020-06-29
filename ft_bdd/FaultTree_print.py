from graphviz import Graph
from .node import And, Or, Not, BasicEvent
from .FaultTree_check import searchRepeatedEvent


def _createTE(g, topevent):
    #  Create TE and topevent nodes respectively
    name = '0'
    g.node('TE', shape='box')
    if type(topevent) == BasicEvent:
        g.node(str(name), label=topevent.name)
        g.edge('TE', str(name))
    elif type(topevent) == And:
        g.node(str(name), label='and', shape='trapezium')
        g.edge('TE', str(name))
    elif type(topevent) == Or:
        g.node(str(name), label='or', shape='trapezium')
        g.edge('TE', str(name))
    elif type(topevent) == Not:
        g.node(str(name), label='not', shape='triangle')
        g.edge('TE', str(name))
    else:
        print("This node is not correct")
        return


def _createChild(g, event, name, repeate):
    #  create each child node for event
    dic = {}
    parent = name
    count = 0
    for i in event.child:
        name += str(count)
        _createNode(g, i, name, repeate)
        dic[name] = i
        name = parent
        count += 1
    return dic


def _createNode(g, event, name, repeate):
    #  create a node depending on the type of event
    if type(event) == BasicEvent:
        if event in repeate:
            g.node(str(name), label=event.name, shape='invtriangle')
        else:
            g.node(str(name), label=event.name)
    elif type(event) == And:
        g.node(str(name), label='and', shape='trapezium')
    elif type(event) == Or:
        g.node(str(name), label='or', shape='trapezium')
    elif type(event) == Not:
        g.node(str(name), label='not', shape='triangle')
    else:
        print("This node is not correct")
        return


def _connectNode(g, event, name):
    #  connect the event node to its child node
    count = len(event.child)
    i = 0
    while i < count:
        g.edge(name, name+str(i))
        i += 1


def _drawEvent(g, event, name, repeate):
    if type(event) == Or or type(event) == And or type(event) == Not:
        dic = _createChild(g, event, name, repeate)
        _connectNode(g, event, name)
        for i in dic:
            _drawEvent(g, dic[i], i, repeate)


def drawFaultTree(event, repeate=set()):
    g = Graph(format='png')
    _createTE(g, event)
    _drawEvent(g, event, '0', repeate)
    return g


def drawFaultTreeRepeated(event):
    repeate = searchRepeatedEvent(event)
    if repeate == set():
        return drawFaultTree(event)
    else:
        return drawFaultTree(event, repeate=repeate)
