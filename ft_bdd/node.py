from itertools import combinations

class Operator():
    def __init__(self):
        self.child = set()
    def addchild(self,*args):
        self.child |= set(args)
    def deletechild(self,*args):
        self.child -= set(args)
    def alldelete   (self):
        self.child = set()
class And(Operator):
    pass
class Or(Operator):
    pass
class Not(Operator):
    def addchild(self,arg):
        self.child = set([arg])
class BasicEvent():
    def __init__(self,name):
        self.name = name

def k_out_of_n(k,*args):
    a = Or()
    for i in list(combinations(args,k)):
        b = And()
        for j in range(k):
            b.addchild(i[j])
        a.addchild(b)
    return a