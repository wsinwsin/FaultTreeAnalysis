import pytest
import src.A_1 as A_1
import src.A_2 as A_2
import src.A_3 as A_3

def test_A_1_1():
    a = 12
    assert A_1.A_1(a)==True
def test_A_1_2():
    a = 2
    assert A_1.A_1(a)==None
#Name                 Stmts   Miss Branch BrPart  Cover   Missing
#src/A_1.py            3        0        2         0       100%

def test_A_2():
    a = 12
    assert A_2.A_2(a)==True
#Name                 Stmts   Miss Branch BrPart  Cover   Missing
#src/A_2.py            3         0       2         1        80%     2->exit

def test_A_3():
    a = 2
    assert A_3.A_3(a)==None

#src/A_3.py               3      1      2      1    60%   2->3, 3

'''
これらの結果からCover = (Stmts + Branch - Mss - BrPart)/(Stmts + Branch)×100
'''