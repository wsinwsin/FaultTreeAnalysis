import pytest
import sys
sys.path.append('..')
from ft_bdd.node import BasicEvent
from ft_bdd import node as nd
from ft_bdd import mybdd as mb
from ft_bdd import FaultTree_print as fp
from ft_bdd import FaultTree_check as fc
from ft_bdd import FaultTree_BDD as fb
from ft_bdd import check_coherent as ch

def test_node1():
    te = nd.Or()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    te.addchild(a,b)
    te.deletechild(a)
    assert b in te.child and not a in te.child

def test_node2():
    te = nd.And()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    te.addchild(a,b)
    te.alldelete()
    assert te.child == set()

def test_node3():
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    c = nd.BasicEvent('c')
    te = nd.Not()
    g1 = nd.k_out_of_n(2,a,b,c)
    te.addchild(g1)
    assert type(te) == nd.Not and len(g1.child)==3

def test_mybdd1():
    bdd = mb.BDD()
    a = bdd.var('a')
    b = bdd.var('b')
    c = bdd.And(a,b)
    c.todot()
    assert type(c) == mb.Variable

def test_mybdd2():
    bdd = mb.BDD()
    a = bdd.var('a')
    b = bdd.var('b')
    c = bdd.Or(a,b)
    c.todot()
    assert type(c) == mb.Variable

def test_mybdd3():
    bdd = mb.BDD()
    a = bdd.var('a')
    b = bdd.var('b')
    c = bdd.var('c')
    d = bdd.Not(c)
    e = mb.createOrGate(bdd,[a,b,d])
    e.todot()
    assert type(c) == mb.Variable

def test_mybdd4():
    bdd = mb.BDD()
    a = bdd.var('a')
    b = bdd.var('b')
    c = bdd.var('c')
    d = bdd.Not(c)
    e = mb.createAndGate(bdd,[a,b,d])
    e.todot()
    assert type(c) == mb.Variable

def test_mybdd5():
    bdd = mb.BDD()
    a = bdd.var('a')
    b = bdd.var('b')
    c = bdd.var('c')
    d = bdd.var('d')
    e = bdd.var('e')
    f = bdd.var('f')
    g = bdd.var('g')
    g1 = bdd.And(a,b)
    g2 = bdd.And(c,d)
    g3 = bdd.Not(e)
    g4 = bdd.And(g3,f)
    g5 = bdd.Not(g2)
    te = mb.createOrGate(bdd,[g1,g4,g5])
    te.todot()
    assert type(te) == mb.Variable

def test_mybdd6():
    bdd = mb.BDD()
    a = bdd.var('a')
    print(a.low)
    repr(a.low)
    print(a)
    repr(a)
    assert True

def test_mybdd7():
    bdd = mb.BDD()
    a = bdd.var('a')
    b = bdd.var('b')
    c = bdd.var('c')
    d = bdd.var('d')
    e = bdd.var('e')
    f = bdd.var('f')
    g1 = bdd.Or(a,b)
    g2 = bdd.Or(c,d)
    g3 = bdd.Not(e)
    g4 = bdd.Or(g3,f)
    g5 = bdd.Not(g2)
    te = mb.createAndGate(bdd,[g1,g4,g5])
    te.todot()
    assert type(te) == mb.Variable

def test_mybdd8():
    bdd = mb.BDD()
    a = bdd.var('a')
    b = bdd.var('b')
    c = bdd.var('c')
    g1 = bdd.Or(a,b)
    g2 = bdd.And(a,c)
    te = mb.createOrGate(bdd,[a,g1,g2])
    te.todot()
    assert type(te) == mb.Variable

def test_mybdd9():
    bdd = mb.BDD()
    a = bdd.var('a')
    a = bdd.var('a')
    b = bdd.var('b')
    c = bdd.var('c')
    d = bdd.var('d')
    bdd.And(a,a)
    g1 = bdd.And(a,b)
    g2 = bdd.And(c,d)
    te = bdd.And(g1,g2)
    assert True

def test_mybdd10():
    bdd = mb.BDD()
    a = bdd.var('a')
    b = bdd.var('b')
    g1 = bdd.And(b,a)
    g2 = bdd.Or(b,a)
    assert True

def test_FaultTree_print1():
    te = nd.BasicEvent('te')
    fp.drawFaultTree(te)
    assert True

def test_FaultTree_print2():
    te = nd.And()
    g1 = nd.Or()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    c = nd.BasicEvent('c')
    te.addchild(a,g1)
    g1.addchild(b,c)
    fp.drawFaultTree(te)
    assert True

def test_FaultTree_print3():
    te = nd.Or()
    g1 = nd.And()
    g2 = nd.And()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    c = nd.BasicEvent('c')
    te.addchild(g1,g2)
    g1.addchild(b,c)
    g2.addchild(a,c)
    fp.drawFaultTreeRepeated(te)
    assert True

def test_FaultTree_print4():
    te = nd.Not()
    g1 = nd.Not()
    te.addchild(g1)
    fp.drawFaultTreeRepeated(te)
    assert True

def test_FaultTree_print5():
    te = 1
    fp.drawFaultTreeRepeated(te)
    assert True

def test_FaultTree_print6():
    te = nd.And()
    te.addchild(1)
    fp.drawFaultTree(te)
    assert True

def test_FaultTree_check1():
    te = nd.Or()
    g1 = nd.And()
    g2 = nd.Not()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    te.addchild(a,g1,g2)
    g1.addchild(b,a)
    g2.addchild(a)
    result = fc.searchRepeatedEvent(te)
    assert result == {a}

def test_FaultTree_check2():
    te = nd.Or()
    g1 = nd.And()
    g2 = nd.Not()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    te.addchild(a,g1,g2)
    g1.addchild(b,1)
    g2.addchild(a)
    result = fc.searchRepeatedEvent(te)
    assert result == {a}

def test_FaultTree_check3():
    te = nd.Or()
    g1 = nd.And()
    g2 = nd.Not()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    c = nd.BasicEvent('c')
    te.addchild(a,g1,g2)
    g1.addchild(b,c)
    g2.addchild(a)
    result = fc.searchBasicEventcount(te)
    assert result == {'a':2,'b':1,'c':1}

def test_FaultTree_check4():
    te = nd.Or()
    g1 = nd.And()
    g2 = nd.Not()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    te.addchild(a,g1,g2)
    g1.addchild(b,2)
    g2.addchild(a)
    result = fc.searchBasicEventcount(te)
    assert result == {'a':2,'b':1}

def test_FaultTree_check5():
    te = nd.Or()
    g1 = nd.And()
    g2 = nd.Not()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    c = nd.BasicEvent('c')
    te.addchild(a,g1,g2)
    g1.addchild(b,c)
    g2.addchild(a)
    result = fc.CheckLoop(te)
    assert result == True

def test_FaultTree_check6():
    te = nd.Or()
    g1 = nd.And()
    g2 = nd.Not()
    g3 = nd.Or()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    te.addchild(2,g1)
    g1.addchild(b,2,te)
    g2.addchild(te)
    g3.addchild(2)
    result = fc.CheckLoop(g3)
    result = fc.CheckLoop(te)
    assert result == False

def test_FaultTree_check7():
    te = nd.Or()
    g1 = nd.And()
    g2 = nd.Not()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    c = nd.BasicEvent('c')
    te.addchild(a,g1,g2)
    g1.addchild(b,c)
    g2.addchild(a)
    result = fc.CheckTerminal(te)
    assert result == True

def test_FaultTree_check8():
    te = nd.Or()
    g1 = nd.And()
    g2 = nd.Not()
    g3 = nd.And()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    te.addchild(a,g1,g2)
    g1.addchild(b,2,g3)
    g2.addchild(2)
    result = fc.CheckTerminal(g2)
    result = fc.CheckTerminal(te)
    assert result == False

def test_FaultTree_BDD1():
    te = nd.Or()
    g1 = nd.And()
    g2 = nd.Not()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    c = nd.BasicEvent('c')
    te.addchild(g1,g2)
    g1.addchild(a,c)
    g2.addchild(b)
    bdd = fb.getBDD(te)
    fb.drawBDD(te)
    assert type(bdd) == fb.Variable

def test_FaultTree_BDD2():
    te = nd.And()
    g1 = nd.Or()
    g2 = nd.Or()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    c = nd.BasicEvent('c')
    te.addchild(g1,g2)
    g1.addchild(a,c)
    g2.addchild(b,3)
    bdd = fb.getBDD(te)
    fb.drawBDD(te)
    assert type(bdd) == fb.Variable

def test_FaultTree_BDD3():
    te = 2
    bdd = fb.getBDD(te)
    fb.drawBDD(te)
    assert bdd == None

def test_FaultTree_BDD4():
    te = nd.BasicEvent('te')
    bdd = fb.getBDD(te)
    fb.drawBDD(te)
    assert type(bdd) == fb.Variable

def test_check_coherentTT1():
    te = nd.Or()
    a = nd.BasicEvent('a')
    te.addchild(a)
    bdd = fb.getBDD(te)
    assert ch.check_coherent(bdd) == True

def test_check_coherentTT2():
    te = nd.Not()
    a = nd.BasicEvent('a')
    te.addchild(a)
    bdd = fb.getBDD(te)
    assert ch.check_coherent(bdd) == False

def test_check_coherentFT1():
    te = nd.Or()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    te.addchild(a,b)
    bdd = fb.getBDD(te)
    assert ch.check_coherent(bdd) == True
    
def test_check_coherentFT2():
    while True:
        te = nd.Or()
        g1 = nd.Not()
        a = nd.BasicEvent('a')
        b = nd.BasicEvent('b')
        g1.addchild(b)
        te.addchild(a,g1)
        if fb.getBDD(te).var == 'a':
            break
    bdd = fb.getBDD(te)
    assert ch. check_coherent(bdd) == False
    
def test_check_coherentFT3():
    while True:
        te = nd.And()
        g1 = nd.Not()
        a = nd.BasicEvent('a')
        b = nd.BasicEvent('b')
        te.addchild(a,g1)
        g1.addchild(b)
        if fb.getBDD(te).var == 'b':
            break
    bdd = fb.getBDD(te)
    assert ch.check_coherent(bdd) == False
    
def test_check_coherentTF1():
    te = nd.And()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    te.addchild(a,b)
    bdd = fb.getBDD(te)
    assert ch.check_coherent(bdd) == True
    
def test_check_coherentTF2():
    while True:
        te = nd.And()
        g1 = nd.Not()
        a = nd.BasicEvent('a')
        b = nd.BasicEvent('b')
        te.addchild(a,g1)
        g1.addchild(b)
        if fb.getBDD(te).var == 'a':
            break
    bdd = fb.getBDD(te)
    assert ch.check_coherent(bdd) == False

def test_check_coherentTF3():
    while True:
        te = nd.Or()
        g1 = nd.Not()
        a = nd.BasicEvent('a')
        b = nd.BasicEvent('b')
        te.addchild(a,g1)
        g1.addchild(b)
        if fb.getBDD(te).var == 'b':
            break
    bdd = fb.getBDD(te)
    assert ch.check_coherent(bdd) == False

def test_check_coherentFF1():
    while True:
        te = nd.Or()
        g1 = nd.And()
        a = nd.BasicEvent('a')
        b = nd.BasicEvent('b')
        c = nd.BasicEvent('c')
        te.addchild(a,g1)
        g1.addchild(c,b)
        if fb.getBDD(te).var =='c':
            break
    bdd = fb.getBDD(te)
    assert ch.check_coherent(bdd) == True

def test_check_coherentFF2():
    while True:
        te = nd.Or()
        g1 = nd.And()
        g2 = nd.Not()
        a = nd.BasicEvent('a')
        b = nd.BasicEvent('b')
        c = nd.BasicEvent('c')
        te.addchild(a,g1)
        g1.addchild(c,g2)
        g2.addchild(b)
        if fb.getBDD(te).var == 'c':
            break
    bdd = fb.getBDD(te)
    assert ch.check_coherent(bdd) == False

def test_check_coherentFF3():
    while True:
        te = nd.Or()
        g1 = nd.And()
        g2 = nd.Not()
        g3 = nd.Not()
        a = nd.BasicEvent('a')
        b = nd.BasicEvent('b')
        c = nd.BasicEvent('c')
        te.addchild(g3,g1)
        g1.addchild(c,g2)
        g2.addchild(b)
        g3.addchild(a)
        if fb.getBDD(te).var == 'c':
            break
    bdd = fb.getBDD(te)
    assert ch.check_coherent(bdd) == False

def test_check_coherentFF4():
    while True:
        te = nd.Or()
        g1 = nd.And()
        g2 = nd.Not()
        a = nd.BasicEvent('a')
        b = nd.BasicEvent('b')
        c = nd.BasicEvent('c')
        te.addchild(a,g1)
        g1.addchild(c,g2)
        g2.addchild(b)
        if fb.getBDD(te).var == 'b':
            break
    bdd = fb.getBDD(te)
    assert ch.check_coherent(bdd) == False