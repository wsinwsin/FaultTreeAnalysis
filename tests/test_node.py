import pytest
from ft_bdd import node as nd


def test_node1():
    te = nd.Or()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    te.addchild(a, b)
    te.deletechild(a)
    assert b in te.child and a not in te.child


def test_node2():
    te = nd.And()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    te.addchild(a, b)
    te.alldelete()
    assert te.child == set()


def test_node3():
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    c = nd.BasicEvent('c')
    te = nd.Not()
    g1 = nd.k_out_of_n(2, a, b, c)
    te.addchild(g1)
    assert type(te) == nd.Not and len(g1.child) == 3


#   result
'''
---------- coverage: platform darwin, python 3.8.2-final-0 -----------
Name                        Stmts   Miss Branch BrPart  Cover   Missing
-----------------------------------------------------------------------
ft_bdd/FaultTree_BDD.py        46     46     26      0     0%   1-54
ft_bdd/FaultTree_check.py      60     60     42      0     0%   1-75
ft_bdd/FaultTree_print.py      66     66     28      0     0%   1-81
ft_bdd/__init__.py              0      0      0      0   100%
ft_bdd/check_coherent.py       73     73     50      0     0%   1-90
ft_bdd/mybdd.py               179    179     42      0     0%   1-229
ft_bdd/node.py                 28      0      4      0   100%
-----------------------------------------------------------------------
TOTAL                         452    424    192      0     5%
'''
