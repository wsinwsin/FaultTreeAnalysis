import pytest
from ft_bdd import FaultTree_check as fc
from ft_bdd import node as nd


def test_FaultTree_check1():
    te = nd.Or()
    g1 = nd.And()
    g2 = nd.Not()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    te.addchild(a, g1, g2)
    g1.addchild(b, a)
    g2.addchild(a)
    result = fc.searchRepeatedEvent(te)
    assert result == {a}


def test_FaultTree_check2():
    te = nd.Or()
    g1 = nd.And()
    g2 = nd.Not()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    te.addchild(a, g1, g2)
    g1.addchild(b, 1)
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
    te.addchild(a, g1, g2)
    g1.addchild(b, c)
    g2.addchild(a)
    result = fc.searchBasicEventcount(te)
    assert result == {'a': 2, 'b': 1, 'c': 1}


def test_FaultTree_check4():
    te = nd.Or()
    g1 = nd.And()
    g2 = nd.Not()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    te.addchild(a, g1, g2)
    g1.addchild(b, 2)
    g2.addchild(a)
    result = fc.searchBasicEventcount(te)
    assert result == {'a': 2, 'b': 1}


def test_FaultTree_check5():
    te = nd.Or()
    g1 = nd.And()
    g2 = nd.Not()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    c = nd.BasicEvent('c')
    te.addchild(a, g1, g2)
    g1.addchild(b, c)
    g2.addchild(a)
    result = fc.CheckLoop(te)
    assert result is True


def test_FaultTree_check6():
    te = nd.Or()
    g1 = nd.And()
    g2 = nd.Not()
    g3 = nd.Or()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    te.addchild(2, g1)
    g1.addchild(b, 2, te)
    g2.addchild(te)
    g3.addchild(2)
    result = fc.CheckLoop(g3)
    result = fc.CheckLoop(te)
    assert result is False


def test_FaultTree_check7():
    te = nd.Or()
    g1 = nd.And()
    g2 = nd.Not()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    c = nd.BasicEvent('c')
    te.addchild(a, g1, g2)
    g1.addchild(b, c)
    g2.addchild(a)
    result = fc.CheckTerminal(te)
    assert result is True


def test_FaultTree_check8():
    te = nd.Or()
    g1 = nd.And()
    g2 = nd.Not()
    g3 = nd.And()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    te.addchild(a, g1, g2)
    g1.addchild(b, 2, g3)
    g2.addchild(2)
    result = fc.CheckTerminal(g2)
    result = fc.CheckTerminal(te)
    assert result is False


#  result
'''
---------- coverage: platform darwin, python 3.8.2-final-0 -----------
Name                            Stmts   Miss Branch BrPart  Cover
-----------------------------------------------------------------
ft_bdd/FaultTree_check.py          60      0     42      0   100%
ft_bdd/__init__.py                  0      0      0      0   100%
ft_bdd/node.py                     28      9      4      0    59%
tests/__init__.py                   0      0      0      0   100%
tests/test_FaultTree_check.py     100      0      0      0   100%
-----------------------------------------------------------------
TOTAL                             188      9     46      0    94%
=================================================
=== 8 passed in 0.09s ===============================================
'''
