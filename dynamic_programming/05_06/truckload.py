"""
ladujemy jak najwiecej kg i jak najmniej ladunkow
1. ladunki to potegi 2
2. ladunki dowolne
"""

#1
def truckload(capacity, packages):
    n = len(packages)
    packages = sorted(packages)
    kg = 0
    cnt = 0
    for i in range(n):
        if capacity >= kg + packages[i]:
            kg += packages[i]
            cnt += 1

    return kg, cnt

