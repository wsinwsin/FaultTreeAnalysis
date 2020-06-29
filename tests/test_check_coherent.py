import pytest
from ft_bdd import check_coherent as ch
from ft_bdd import node as nd
from ft_bdd import FaultTree_BDD as fb


def test_check_coherentTT1():
    te = nd.Or()
    a = nd.BasicEvent('a')
    te.addchild(a)
    bdd = fb.getBDD(te)
    assert ch.check_coherent(bdd) is True


def test_check_coherentTT2():
    te = nd.Not()
    a = nd.BasicEvent('a')
    te.addchild(a)
    bdd = fb.getBDD(te)
    assert ch.check_coherent(bdd) is False


def test_check_coherentFT1():
    te = nd.Or()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    te.addchild(a, b)
    bdd = fb.getBDD(te)
    assert ch.check_coherent(bdd) is True


def test_check_coherentFT2():
    while True:
        te = nd.Or()
        g1 = nd.Not()
        a = nd.BasicEvent('a')
        b = nd.BasicEvent('b')
        g1.addchild(b)
        te.addchild(a, g1)
        if fb.getBDD(te).var == 'a':
            break
    bdd = fb.getBDD(te)
    assert ch. check_coherent(bdd) is False


def test_check_coherentFT3():
    while True:
        te = nd.And()
        g1 = nd.Not()
        a = nd.BasicEvent('a')
        b = nd.BasicEvent('b')
        te.addchild(a, g1)
        g1.addchild(b)
        if fb.getBDD(te).var == 'b':
            break
    bdd = fb.getBDD(te)
    assert ch.check_coherent(bdd) is False


def test_check_coherentTF1():
    te = nd.And()
    a = nd.BasicEvent('a')
    b = nd.BasicEvent('b')
    te.addchild(a, b)
    bdd = fb.getBDD(te)
    assert ch.check_coherent(bdd) is True


def test_check_coherentTF2():
    while True:
        te = nd.And()
        g1 = nd.Not()
        a = nd.BasicEvent('a')
        b = nd.BasicEvent('b')
        te.addchild(a, g1)
        g1.addchild(b)
        if fb.getBDD(te).var == 'a':
            break
    bdd = fb.getBDD(te)
    assert ch.check_coherent(bdd) is False


def test_check_coherentTF3():
    while True:
        te = nd.Or()
        g1 = nd.Not()
        a = nd.BasicEvent('a')
        b = nd.BasicEvent('b')
        te.addchild(a, g1)
        g1.addchild(b)
        if fb.getBDD(te).var == 'b':
            break
    bdd = fb.getBDD(te)
    assert ch.check_coherent(bdd) is False


def test_check_coherentFF1():
    while True:
        te = nd.Or()
        g1 = nd.And()
        a = nd.BasicEvent('a')
        b = nd.BasicEvent('b')
        c = nd.BasicEvent('c')
        te.addchild(a, g1)
        g1.addchild(c, b)
        if fb.getBDD(te).var == 'c':
            break
    bdd = fb.getBDD(te)
    assert ch.check_coherent(bdd) is True


def test_check_coherentFF2():
    while True:
        te = nd.Or()
        g1 = nd.And()
        g2 = nd.Not()
        a = nd.BasicEvent('a')
        b = nd.BasicEvent('b')
        c = nd.BasicEvent('c')
        te.addchild(a, g1)
        g1.addchild(c, g2)
        g2.addchild(b)
        if fb.getBDD(te).var == 'c':
            break
    bdd = fb.getBDD(te)
    assert ch.check_coherent(bdd) is False


def test_check_coherentFF3():
    while True:
        te = nd.Or()
        g1 = nd.And()
        g2 = nd.Not()
        g3 = nd.Not()
        a = nd.BasicEvent('a')
        b = nd.BasicEvent('b')
        c = nd.BasicEvent('c')
        te.addchild(g3, g1)
        g1.addchild(c, g2)
        g2.addchild(b)
        g3.addchild(a)
        if fb.getBDD(te).var == 'c':
            break
    bdd = fb.getBDD(te)
    assert ch.check_coherent(bdd) is False


def test_check_coherentFF4():
    while True:
        te = nd.Or()
        g1 = nd.And()
        g2 = nd.Not()
        a = nd.BasicEvent('a')
        b = nd.BasicEvent('b')
        c = nd.BasicEvent('c')
        te.addchild(a, g1)
        g1.addchild(c, g2)
        g2.addchild(b)
        if fb.getBDD(te).var == 'b':
            break
    bdd = fb.getBDD(te)
    assert ch.check_coherent(bdd) is False


#  result
'''
---------- coverage: platform darwin, python 3.8.2-final-0 -----------
Name                        Stmts   Miss Branch BrPart  Cover   Missing
-----------------------------------------------------------------------
ft_bdd/FaultTree_BDD.py        46     17     26      4    61%   9-11, 14-25,
29->30, 30,31->40,35->38, 38-40, 46->exit
ft_bdd/FaultTree_check.py      60     45     42      2    23%   5-20, 30->38,
31->32, 32-33,38-39, 43-59, 63-75
ft_bdd/FaultTree_print.py      66     66     28      0     0%   1-81
ft_bdd/__init__.py              0      0      0      0   100%
ft_bdd/check_coherent.py       73      0     50      0   100%
ft_bdd/mybdd.py               179     44     42      5    73%   14, 25, 28,
41, 44,82->83, 83,101, 108->109, 109, 110->111, 111, 120->121,
121-123,124->125, 125-127, 135,138-141, 151, 154-157, 170,
173-179,206-211, 214-217, 219-223
ft_bdd/node.py                 28      9      4      0    59%   9, 11, 24-30
-----------------------------------------------------------------------
TOTAL                         452    181    192     11    58%

'''
