import pytest
from ft_bdd import FaultTree_check as fc
from ft_bdd import node as nd

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

'''
FaultTreeAnalysis/test % pytest --cov --cov-branch -v test_FaultTree_check.py
============================ test session starts ============================
platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.8.2, pluggy-0.13.1 -- /Users/wsiny/.pyenv/versions/3.8.2/bin/python3.8
cachedir: .pytest_cache
rootdir: /Users/wsiny/Desktop/b4soturon/FaultTreeAnalysis/test
plugins: cov-2.10.0
collected 8 items

test_FaultTree_check.py::test_FaultTree_check1 PASSED                 [ 12%]
test_FaultTree_check.py::test_FaultTree_check2 PASSED                 [ 25%]
test_FaultTree_check.py::test_FaultTree_check3 PASSED                 [ 37%]
test_FaultTree_check.py::test_FaultTree_check4 PASSED                 [ 50%]
test_FaultTree_check.py::test_FaultTree_check5 PASSED                 [ 62%]
test_FaultTree_check.py::test_FaultTree_check6 PASSED                 [ 75%]
test_FaultTree_check.py::test_FaultTree_check7 PASSED                 [ 87%]
test_FaultTree_check.py::test_FaultTree_check8 PASSED                 [100%]

---------- coverage: platform darwin, python 3.8.2-final-0 -----------
NameStmts   Miss Branch BrPart  Cover
--------------------------------------------------------------------------------------------------------------
/Users/wsiny/Desktop/b4soturon/FaultTreeAnalysis/ft_bdd/FaultTree_check.py   60      0     42      0   100%
/Users/wsiny/Desktop/b4soturon/FaultTreeAnalysis/ft_bdd/__init__.py    0      0      0      0   100%
/Users/wsiny/Desktop/b4soturon/FaultTreeAnalysis/ft_bdd/node.py   28      9      4      0    59%
test_FaultTree_check.py   97      0      0      0   100%
--------------------------------------------------------------------------------------------------------------
TOTAL  185      9     46      0    94%


============================= 8 passed in 0.09s =============================
'''