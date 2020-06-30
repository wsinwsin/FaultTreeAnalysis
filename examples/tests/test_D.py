import pytest
import src.D_1 as D_1
import src.D_2 as D_2
import src.D_3 as D_3
import src.D_4 as D_4
import src.D_5 as D_5
import src.D_6 as D_6

def test_D_1_1():
    a = 12
    assert D_1.D_1(a)==True
def test_D_1_2():
    a = 7
    assert D_1.D_1(a)==True
def test_D_1_3():
    a = 3
    assert D_1.D_1(a)==None
'''
#Name                 Stmts   Miss Branch BrPart  Cover   Missing
#src/D_1.py             5        0       4          0      100%
'''
def test_D_2_1():
    a = 12
    assert D_2.D_2(a)==True
def test_D_2_2():
    a = 7
    assert D_2.D_2(a)==True
'''
Name                 Stmts   Miss Branch BrPart  Cover   Missing
src/D_2.py             5       0        4         1        89%     4->exit
'''
def test_D_3_1():
    a = 7
    assert D_3.D_3(a)==True
def test_D_3_2():
    a = 3
    assert D_3.D_3(a)==None
'''
Name                 Stmts   Miss Branch BrPart  Cover   Missing
src/D_3.py             5      　1       4        1        78%   2->3, 3
'''
def test_D_4_1():
    a = 12
    assert D_4.D_4(a)==True
'''
Name                 Stmts   Miss Branch BrPart  Cover   Missing
src/D_4.py             5        2       4         1        44%   2->4, 4-5
'''
def test_D_5_1():
    a = 7
    assert D_5.D_5(a)==True
'''
Name                 Stmts   Miss Branch BrPart  Cover   Missing
src/D_5.py             5       1        4          2       67%   2->3, 3, 4->exit
'''
def test_D_6_1():
    a = 3
    assert D_6.D_6(a)==None
'''
Name                 Stmts   Miss Branch BrPart  Cover   Missing
src/D_6.py             5        2       4         2        56%   2->3, 3, 4->5, 5
'''

'''
D_4の結果からCover = (Stmts + Branch - Mss - BrPart)/(Stmts + Branch)×100
が成立しない.
このとき,実際は条件分岐を3つしてないにもかかわらずBrPartは1である.
つまり,BrPartが表す物は『コード全体の通らなかった分岐の数』を表しているのではなく,テストのときに『実際に実行された行の中での通らなかった分岐の数』を表している.したがって
cover = (Stmts + Branch - Mss - 分岐で網羅できなかった数)/(Stmts + Branch)×100

Cover = (Stmts + Branch - Mss - BrPart)/(Stmts + Branch)×100の式はc0カバレッジが100%の時に使える.
'''