def E(a):
    for i in range(10):
        a +=1
    while a<20:
        a+=1
    return a

'''
Name         Stmts   Miss Branch BrPart  Cover   Missing
src/E.py         6        0      4          0       100%
for文,while文はブランチとしてカウント
'''