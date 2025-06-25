class Emp:
    def __init__(self, fun):
        self.fun = fun
        self.childs = []
        self.f = -1
        self.g = -1

def g(v):
    if v.g != -1:
        return v.g

    v.g = 0
    for u in v.childs:
        v.g += f(u)

    return v.g

def f(v):
    if v.f != -1:
        return v.f

    total = v.fun
    for u in v.childs:
        total += g(u)

    v.f = max(g(v), total)
    return v.f



emp11 = Emp(0)
emp12 = Emp(1)
emp21 = Emp(10)
emp22 = Emp(0)
emp23 = Emp(43)
emp24 = Emp(13)
emp31 = Emp(2)
emp32 = Emp(15)
emp41 = Emp(10)

root = Emp(100)
root.childs = [emp11, emp12]
emp11.childs = [emp21, emp22]
emp12.childs = [emp23, emp24]
emp22.childs = [emp31, emp32]
emp32.childs = [emp41]

print(f(root))