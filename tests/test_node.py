import pytest
from ft_bdd import node as nd

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

#result
'''
FaultTreeAnalysis/test % pytest --cov --cov-branch -v test_node.py============================== test session starts ===============================
platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.8.2, pluggy-0.13.1 -- /Users/wsiny/.pyenv/versions/3.8.2/bin/python3.8
cachedir: .pytest_cache
rootdir: /Users/wsiny/Desktop/b4soturon/FaultTreeAnalysis/test
plugins: cov-2.10.0
collected 3 items

test_node.py::test_node1 PASSED                                            [ 33%]
test_node.py::test_node2 PASSED                                            [ 66%]
test_node.py::test_node3 PASSED                                            [100%]

---------- coverage: platform darwin, python 3.8.2-final-0 -----------
Name                                                                  Stmts   Miss Branch BrPart  Cover
-------------------------------------------------------------------------------------------------------
/Users/wsiny/Desktop/b4soturon/FaultTreeAnalysis/ft_bdd/__init__.py       0      0      0      0   100%
/Users/wsiny/Desktop/b4soturon/FaultTreeAnalysis/ft_bdd/node.py          28      0      4      0   100%
test_node.py                                                             26      0      0      0   100%
-------------------------------------------------------------------------------------------------------
TOTAL                                                                    54      0      4      0   100%


=============================== 3 passed in 0.06s ================================
'''