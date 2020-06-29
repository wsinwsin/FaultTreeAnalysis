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
    te.addchild(a, g1)
    g1.addchild(b, c)
    fp.drawFaultTree(te)
    assert True


def test_FaultTree_print3():
    te = nd.Or()
    g1 = nd.And()
    g2 = nd.And()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    c = nd.BasicEvent('c')
    te.addchild(g1, g2)
    g1.addchild(b, c)
    g2.addchild(a, c)
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


#  result
'''
---------- coverage: platform darwin, python 3.8.2-final-0 -----------
Name                        Stmts   Miss Branch BrPart  Cover   Missing
-----------------------------------------------------------------------
ft_bdd/FaultTree_BDD.py        46     46     26      0     0%   1-54
ft_bdd/FaultTree_check.py      60     41     42      0    28%   24-
39, 43-59, 63-75
ft_bdd/FaultTree_print.py      66      0     28      0   100%
ft_bdd/__init__.py              0      0      0      0   100%
ft_bdd/check_coherent.py       73     73     50      0     0%   1-90
ft_bdd/mybdd.py               179    179     42      0     0%   1-229
ft_bdd/node.py                 28      9      4      0    59%   9, 11, 24-30
-----------------------------------------------------------------------
TOTAL                         452    348    192      0    22%
'''
