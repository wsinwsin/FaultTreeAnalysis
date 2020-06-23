from .mybdd import*
from .FaultTree_BDD import*

def check_coherent(a):
    b = create_minimalcutset(a)          
    if not b:
        print('This is a non-coherent system')
        return False
    else:
        return True

def create_minimalcutset(a,cache = None):
    #lowを故障,highを正常とする
    if cache ==None:
        cache = {}
    if a in cache:
        return cache[a]
    if a.low.isValue()== True and a.high.isValue() == True:
        result = _check_TT(a,cache)
    if a.low.isValue() == True and a.high.isValue() == False:
        result = _check_TF(a,cache)
    if a.low.isValue() == False and a.high.isValue() == True:
        result = _check_FT(a,cache)
    if a.low.isValue() == False and a.high.isValue() == False:
        result = _check_FF(a,cache)
        if type(result) == list:
            result= _minimal(result)
    cache[a] = result
    return result

def _check_TT(a,cache):
    #故障したときに正常,正常なときに故障はnon-coherent
    if a.low.value == True and a.high.value == False:
        return False
    else:
        p =[]
        p.append([a.var])
        return p
    
def _check_TF(a,cache):
    if not create_minimalcutset(a.high,cache):
        return False
    #正常なとき故障することはnon-coherent
    if a.low.value == True:
        return False
    else:
        p =[]
        for i in create_minimalcutset(a.high,cache):
            p.append([a.var]+i)
    return p

def _check_FT(a,cache):
    if not create_minimalcutset(a.low,cache):
        return False
    #故障したときに正常であることはnon-coherent
    if a.high.value == False:
        return False
    else:
        p = []
        p.append([a.var])
        p +=create_minimalcutset(a.low,cache)
    return p

def _check_FF(a,cache):
    p0=create_minimalcutset(a.low,cache)
    p1=create_minimalcutset(a.high,cache)
    if not p0 or not p1:
        return False
    #aが正常のときに故障するa以外の組み合わせがaが故障するときのa以外の組み合わせの中に入っているとcoherent
    for i in p0:
        if [j for j in p1 if set(i)>=set(j)]==[]:
            return False
    p=[]
    for i in p1:
        p.append([a.var]+i)
    p += p0
    return p

def _minimal(a):
    #example: [[a,b],[a,b,c],[a,d]]→[[a,b],[a,d]]
    a = [tuple(sorted(i)) for i in a]
    a.sort(key=lambda t: len(t))
    i = 0
    while i < len(a):
        for j in [k for k in a if len(k)>len(a[i])]:
            if set(a[i])<set(j):
                a.remove(j)
        i +=1
    a = [list(i) for i in a]
    return a