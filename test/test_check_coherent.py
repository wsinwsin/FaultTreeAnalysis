import pytest
from ft_bdd import check_coherent as ch
from ft_bdd import node as nd
from ft_bdd import FaultTree_BDD as fb

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
    
#result
'''
FaultTreeAnalysis/test % pytest --cov --cov-branch -v test_check_coherent.py
============================== test session starts ===============================
platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.8.2, pluggy-0.13.1 -- /Users/wsiny/.pyenv/versions/3.8.2/bin/python3.8
cachedir: .pytest_cache
rootdir: /Users/wsiny/Desktop/b4soturon/FaultTreeAnalysis/test
plugins: cov-2.10.0
collected 12 items

test_check_coherent.py::test_check_coherentTT1 PASSED                      [  8%]
test_check_coherent.py::test_check_coherentTT2 PASSED                      [ 16%]
test_check_coherent.py::test_check_coherentFT1 PASSED                      [ 25%]
test_check_coherent.py::test_check_coherentFT2 PASSED                      [ 33%]
test_check_coherent.py::test_check_coherentFT3 PASSED                      [ 41%]
test_check_coherent.py::test_check_coherentTF1 PASSED                      [ 50%]
test_check_coherent.py::test_check_coherentTF2 PASSED                      [ 58%]
test_check_coherent.py::test_check_coherentTF3 PASSED                      [ 66%]
test_check_coherent.py::test_check_coherentFF1 PASSED                      [ 75%]
test_check_coherent.py::test_check_coherentFF2 PASSED                      [ 83%]
test_check_coherent.py::test_check_coherentFF3 PASSED                      [ 91%]
test_check_coherent.py::test_check_coherentFF4 PASSED                      [100%]

---------- coverage: platform darwin, python 3.8.2-final-0 -----------
Name                                                                        Stmts  Miss Branch BrPart  Cover
-------------------------------------------------------------------------------------------------------------
/Users/wsiny/Desktop/b4soturon/FaultTreeAnalysis/ft_bdd/FaultTree_BDD.py       39    13     20      1    64%
/Users/wsiny/Desktop/b4soturon/FaultTreeAnalysis/ft_bdd/FaultTree_test.py      52    37     42      2    24%
/Users/wsiny/Desktop/b4soturon/FaultTreeAnalysis/ft_bdd/__init__.py             0     0      0      0   100%
/Users/wsiny/Desktop/b4soturon/FaultTreeAnalysis/ft_bdd/check_coherent.py      73     0     50      0   100%
/Users/wsiny/Desktop/b4soturon/FaultTreeAnalysis/ft_bdd/mybdd.py              181    45     42      5    73%
/Users/wsiny/Desktop/b4soturon/FaultTreeAnalysis/ft_bdd/node.py                28     9      4      0    59%
test_check_coherent.py                                                        132     0     16      4    97%
-------------------------------------------------------------------------------------------------------------
TOTAL                                                                         505   104    174     12    75%


=============================== 12 passed in 0.51s ===============================
'''