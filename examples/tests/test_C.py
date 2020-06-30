import pytest
import src.C_1 as C_1
import src.C_2 as C_2

def test_C_1_1():
    a = 12
    assert C_1.C_1(a)==True
def test_C_1_2():
    a = 2
    assert C_1.C_1(a)==True
#Name                 Stmts   Miss Branch BrPart  Cover   Missing
#src/C_1.py            4         0        2         0       100%

def test_C_2():
    a = 2
    assert C_2.C_2(a)==True
#Name                 Stmts   Miss Branch BrPart  Cover   Missing
#src/B_2.py            4         1       2         1        67%     3->4, 4

'''
これらの結果からCover = (Stmts + Branch - Mss - BrPart)/(Stmts + Branch)×100
ループ処理によるstmtsとbranchの増加はしない
'''