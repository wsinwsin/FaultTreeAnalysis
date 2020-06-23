import functools
import io

class BDDNode:
    def __init__(self, bdd):
        self.bdd = bdd
    def __and__(self, other):
        return self.bdd.And(self, other)
    
    def __or__(self, other):
        return self.bdd.Or(self, other)
         
    def todot(self):
        return self.bdd.todot(self)

class Value(BDDNode):
    def __init__(self, bdd, value):
        super().__init__(bdd)
        self.value = value
    
    def isValue(self):
        return True

    def __str__(self):
        return 'BDD({})'.format(self.value)

    def __repr__(self):
        return 'BDD({})'.format(self.value)

class Variable(BDDNode):
    def __init__(self, bdd, var, low, high):
        super().__init__(bdd)
        self.var = var
        self.low = low
        self.high = high

    def isValue(self):
        return False
    
    def __str__(self):
        return 'BDD({})'.format(self.var)

    def __repr__(self):
        return 'BDD({})'.format(self.var)

class BDD:
    def __init__(self):
        self.cache = {}
        self.values = {}
        self.variables = {}
        self.index = {}
        self.op = {}
        self.addOperator('and', AndOperator())
        self.addOperator('or', OrOperator())
        self.addOperator('not',NotOperator())
        self.graphviz = GraphvizVisitor()
        self.one = self.createValue(True)
        self.zero = self.createValue(False)
        self.currentindex = 0
    
    def addOperator(self, name, op):
        self.cache[op] = {}
        self.op[name] = op

    def var(self, name):
        if not name in self.index:
            self.index[name] = self.currentindex
            self.currentindex += 1
        return self.createVariable(name, self.zero, self.one)

    def createValue(self, value):
        if value in self.values:
            return self.values[value]
        else:
            tmp = Value(self, value)
            self.values[value] = tmp
            return tmp
    
    def createVariable(self, var, low, high):
        if (var, low, high) in self.variables:
            return self.variables[(var, low, high)]
        elif low == high:
            return low
        else:
            tmp = Variable(self, var, low, high)
            self.variables[(var, low, high)] = tmp
            return tmp
    
    def And(self, f, g):
        return self.op['and'].apply(self, f, g)

    def Or(self, f, g):
        return self.op['or'].apply(self, f, g)
    
    def Not(self, f):
        op = self.op['not']
        cache = self.cache[op]
        return op.apply(self, f, cache)
    
    def todot(self, f):
        return self.graphviz.todot(self, f)

class BinOperator:
    def apply(self, bdd, f, g):
        cache = bdd.cache[self]
        if (f,g) in cache:
            return cache[(f,g)]
        if f.isValue() == True and g.isValue() == True:
            result = self.applyTT(bdd, f, g)
        elif f.isValue() == True and g.isValue() == False:
            result = self.applyTN(bdd, f, g)
        elif f.isValue() == False and g.isValue() == True:
            result = self.applyNT(bdd, f, g)
        else:
            result = self.applyNN(bdd, f, g)        
        cache[(f,g)] = result
        return result

    def applyNN(self, bdd, f, g):
        if f.var == g.var:
            low = self.apply(bdd, f.low, g.low)
            high = self.apply(bdd, f.high, g.high)
            return bdd.createVariable(f.var, low, high)
        elif bdd.index[f.var] > bdd.index[g.var]:
            low = self.apply(bdd, f.low, g)
            high = self.apply(bdd, f.high, g)
            return bdd.createVariable(f.var, low, high)
        else:
            low = self.apply(bdd, f, g.low)
            high = self.apply(bdd, f, g.high)
            return bdd.createVariable(g.var, low, high)

class AndOperator(BinOperator):
    def applyTT(self, bdd, f, g):
        return bdd.createValue(f.value and g.value)

    def applyTN(self, bdd, f, g):
        if f.value == False:
            return bdd.createValue(False)
        else:
            return bdd.createVariable(g.var, g.low, g.high)
    
    def applyNT(self, bdd, f, g):
        if g.value == False:
            return bdd.createValue(False)
        else:
            return bdd.createVariable(f.var, f.low, f.high)

class OrOperator(BinOperator):
    def applyTT(self, bdd, f, g):
        return bdd.createValue(f.value or g.value)

    def applyTN(self, bdd, f, g):
        if f.value == True:
            return bdd.createValue(True)
        else:
            return bdd.createVariable(g.var, g.low, g.high)
    
    def applyNT(self, bdd, f, g):
        if g.value == True:
            return bdd.createValue(True)
        else:
            return bdd.createVariable(f.var, f.low, f.high)
#IteOperator,NotOperatorに関する情報を削除
class Visitor:
    def __init__(self):
        self.visited = set()

    def clear_visited(self):
        self.visited.clear()

    def visit(self, bdd, f):
        if f in self.visited:
            return
        if f.isValue() == True:
            self.visitT(bdd, f)
        else:
            self.visitN(bdd, f)
        self.visited.add(f)

class UnaryOperator:
    def apply(self, bdd, f, cache):
        if f in cache:
            return cache[f]
        if f.isValue() == True:
            result = self.applyT(bdd, f, cache)
        else:
            result = self.applyN(bdd, f, cache)
        cache[f] = result
        return result

class NotOperator(UnaryOperator):
    def applyT(self, bdd, f, cache):
        return bdd.createValue(not f.value)
    
    def applyN(self, bdd, f, cache):
        low = self.apply(bdd, f.low, cache)
        high = self.apply(bdd, f.high, cache)
        return bdd.createVariable(f.var, low, high)
        
class GraphvizVisitor(Visitor):
    def __init__(self):
        super().__init__()

    def todot(self, bdd, f):
        self.clear_visited()
        self.str = io.StringIO()
        self.str.write('digraph { layout=dot; overlap=false; splines=true; node [fontsize=10];\n')
        self.visit(bdd, f)
        self.str.write('}')
        return self.str.getvalue()

    def visitT(self, bdd, f):
        if f.value == True:
            self.str.write('"obj{term}" [shape = square, label = "故障"];\n'.format(term=id(f)))
        else:
            self.str.write('"obj{term}" [shape = square, label = "正常"];\n'.format(term=id(f)))
    def visitN(self, bdd, f):
        self.str.write('"obj{term}" [shape = circle, label = "{value}"];\n'.format(term=id(f), value=f.var))
        self.visit(bdd, f.low)
        self.visit(bdd, f.high)
        self.str.write('"obj{term}" -> "obj{low}" [style = dotted];\n'.format(term=id(f), low=id(f.low)))
        self.str.write('"obj{term}" -> "obj{high}";\n'.format(term=id(f), high=id(f.high)))

def createOrGate(bdd, x):
    return functools.reduce(lambda a, b: a|b, x)

def createAndGate(bdd, x):
    return functools.reduce(lambda a, b: a&b, x)