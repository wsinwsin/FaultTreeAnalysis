import pytest
from ft_bdd import node as nd
from ft_bdd import FaultTree_BDD as fb


def test_FaultTree_BDD1():
    te = nd.Or()
    g1 = nd.And()
    g2 = nd.Not()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    c = nd.BasicEvent('c')
    te.addchild(g1, g2)
    g1.addchild(a, c)
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
    te.addchild(g1, g2)
    g1.addchild(a, c)
    g2.addchild(b, 3)
    bdd = fb.getBDD(te)
    fb.drawBDD(te)
    assert type(bdd) == fb.Variable


def test_FaultTree_BDD3():
    te = 2
    bdd = fb.getBDD(te)
    fb.drawBDD(te)
    assert bdd is None


def test_FaultTree_BDD4():
    te = nd.BasicEvent('te')
    bdd = fb.getBDD(te)
    fb.drawBDD(te)
    assert type(bdd) == fb.Variable


#  result
'''
NameStmts   Miss Branch BrPart  Cover
--------------------------------------------------------------------------------------------------------------
/ft_bdd/FaultTree_BDD.py   46      0     26      0   100%
/ft_bdd/FaultTree_check.py   60     43     42      1    25%
/ft_bdd/__init__.py    0      0      0      0   100%
/ft_bdd/mybdd.py  181     23     42      6    85%
/ft_bdd/node.py   28      9      4      0    59%
test_FaultTree_BDD.py   41      0      0      0   100%
--------------------------------------------------------------------------------------------------------------
TOTAL  356     75    114      7    74%


============================= 4 passed in 0.64s =============================
'''
