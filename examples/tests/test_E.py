import pytest
import src.E as E
def test_E_1():
    a = 1
    assert E.E(a)==20

'''
Name         Stmts   Miss Branch BrPart  Cover   Missing
src/E.py         6        0      4          0       100%
for文,while文はブランチとしてカウント
'''