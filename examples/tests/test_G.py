import pytest
import src.G as G
def test_G_1():
    a = 11
    b = 11
    c = 11
    assert G.G(a,b,c)==None

'''
Name         Stmts   Miss  Cover   Missing
src/G.py         7       0      100%
Name         Stmts   Miss Branch BrPart  Cover   Missing
src/G.py         7        0        6        3        77%     2->4, 4->6, 6->exit
c0カバレッジが100 %のときc1カバレッジは
Cover = (Stmts + Branch - Miss - BrPart)/(Stmts + Branch)×100が成り立つ
'''