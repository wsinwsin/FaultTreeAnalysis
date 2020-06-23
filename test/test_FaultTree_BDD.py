import pytest
import sys
sys.path.append('..')
from ft_bdd import node as nd
from ft_bdd import FaultTree_BDD as fb

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

#result
'''
FaultTreeAnalysis/test % pytest --cov --cov-branch -v test_FaultTree_BDD.py
============================ test session starts ============================
platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.8.2, pluggy-0.13.1 -- /Users/wsiny/.pyenv/versions/3.8.2/bin/python3.8
cachedir: .pytest_cache
rootdir: /Users/wsiny/Desktop/b4soturon/FaultTreeAnalysis/test
plugins: cov-2.10.0
collected 4 items

test_FaultTree_BDD.py::test_FaultTree_BDD1 PASSED                     [ 25%]
test_FaultTree_BDD.py::test_FaultTree_BDD2 PASSED                     [ 50%]
test_FaultTree_BDD.py::test_FaultTree_BDD3 PASSED                     [ 75%]
test_FaultTree_BDD.py::test_FaultTree_BDD4 PASSED                     [100%]

---------- coverage: platform darwin, python 3.8.2-final-0 -----------
NameStmts   Miss Branch BrPart  Cover
--------------------------------------------------------------------------------------------------------------
/Users/wsiny/Desktop/b4soturon/FaultTreeAnalysis/ft_bdd/FaultTree_BDD.py   46      0     26      0   100%
/Users/wsiny/Desktop/b4soturon/FaultTreeAnalysis/ft_bdd/FaultTree_check.py   60     43     42      1    25%
/Users/wsiny/Desktop/b4soturon/FaultTreeAnalysis/ft_bdd/__init__.py    0      0      0      0   100%
/Users/wsiny/Desktop/b4soturon/FaultTreeAnalysis/ft_bdd/mybdd.py  181     23     42      6    85%
/Users/wsiny/Desktop/b4soturon/FaultTreeAnalysis/ft_bdd/node.py   28      9      4      0    59%
test_FaultTree_BDD.py   41      0      0      0   100%
--------------------------------------------------------------------------------------------------------------
TOTAL  356     75    114      7    74%


============================= 4 passed in 0.64s =============================
'''