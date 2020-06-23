import pytest
from ft_bdd import node as nd
from ft_bdd import FaultTree_print as fp

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

##result
'''
FaultTreeAnalysis/test % pytest --cov --cov-branch -v test_FaultTree_print.py
=========================== test session starts ============================
platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.8.2, pluggy-0.13.1 -- /Users/wsiny/.pyenv/versions/3.8.2/bin/python3.8
cachedir: .pytest_cache
rootdir: /Users/wsiny/Desktop/b4soturon/FaultTreeAnalysis/test
plugins: cov-2.10.0
collected 6 items

test_FaultTree_print.py::test_FaultTree_print1 PASSED                [ 16%]
test_FaultTree_print.py::test_FaultTree_print2 PASSED                [ 33%]
test_FaultTree_print.py::test_FaultTree_print3 PASSED                [ 50%]
test_FaultTree_print.py::test_FaultTree_print4 PASSED                [ 66%]
test_FaultTree_print.py::test_FaultTree_print5 PASSED                [ 83%]
test_FaultTree_print.py::test_FaultTree_print6 PASSED                [100%]

---------- coverage: platform darwin, python 3.8.2-final-0 -----------
Name Stmts   Miss Branch BrPart  Cover
--------------------------------------------------------------------------------------------------------------
/Users/wsiny/Desktop/b4soturon/FaultTreeAnalysis/ft_bdd/FaultTree_print.py    64      0     28      0   100%
/Users/wsiny/Desktop/b4soturon/FaultTreeAnalysis/ft_bdd/FaultTree_test.py    52     35     42      0    29%
/Users/wsiny/Desktop/b4soturon/FaultTreeAnalysis/ft_bdd/__init__.py     0      0      0      0   100%
/Users/wsiny/Desktop/b4soturon/FaultTreeAnalysis/ft_bdd/node.py    28      9      4      0    59%
test_FaultTree_print.py    46      0      0      0   100%
--------------------------------------------------------------------------------------------------------------
TOTAL   190     44     74      0    70%


============================ 6 passed in 0.09s =============================
'''