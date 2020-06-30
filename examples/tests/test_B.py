import pytest
import src.B_1 as B_1
import src.B_2 as B_2
import src.B_3 as B_3

def test_B_1_1():
    a = 12
    assert B_1.B_1(a)==True
def test_B_1_2():
    a = 2
    assert B_1.B_1(a)==False
#Name                 Stmts   Miss Branch BrPart  Cover   Missing
#src/B_1.py            4         0        2         0       100%

def test_B_2():
    a = 12
    assert B_2.B_2(a)==True
#Name                 Stmts   Miss Branch BrPart  Cover   Missing
#src/B_2.py            4         1       2         1        67%     2->exit

def test_B_3():
    a = 2
    assert B_3.B_3(a)==False
#Name                 Stmts   Miss Branch BrPart  Cover   Missing
#src/B_3.py            4         1       2         1         67%    2->3, 3

'''
これらの結果からCover = (Stmts + Branch - Mss - BrPart)/(Stmts + Branch)×100
'''