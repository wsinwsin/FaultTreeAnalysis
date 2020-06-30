import pytest
import src.F as F
def test_F_1():
    a = 11
    assert F.F(a)==True

'''
Name         Stmts   Miss Branch BrPart  Cover   Missing
src/F.py         7        3       4         1         45%    2->4, 4-7
elifの場合も２つ追加される.
'''