#Maciej Janusz
"""
Puszczamy zmodyfikowana dijkstre.
Gdy odwiedzimy wierzcholek (wyciagniemy z kolejki priorytetowej) bedacy osrodkiem blokujemy mozliwosc przejscia przez niego i dodajemy jego podwojony koszt do lacznej ceny.
Wiemy ze najwczesniej odwiedzone sa wierzcholki o najmniejszym koszcie, wiec kolejnosc odwiedzin sie zgadza.
Zeby upewnic sie ze osrodki o rownym koszcie sa przetwarzane wedlug indexow jako priorytet ustawiamy krotke (koszt, index).
O(ElogV)
"""
from kol2testy import runtests
from math import inf
from queue import PriorityQueue

def lets_roll(start_city, flights, resorts):
    n = max([max(u,v) for u, v, _ in flights])+1 #liczba miast
    graph = [[] for _ in range(n)] #tworzymy liste sasiedztwa
    for u, v, weight in flights:
        graph[u].append((v, weight))
        graph[v].append((u, weight))

    sum_of_cost = 0 #laczny koszt
    is_resort = [False]*n #osrodki
    for r in resorts:
        is_resort[r] = True

    blocked = [False]*n #odwiedzone osrodki
    costs = [inf]*n #najnizsze koszty

    q = PriorityQueue()
    q.put(((0, start_city), start_city))
    costs[start_city] = 0
    while not q.empty():
        (d, _), u = q.get()
        if d > costs[u] or blocked[u]:
            continue

        #odwiedzamy osrodek
        if is_resort[u]:
            sum_of_cost += 2 * costs[u]
            blocked[u] = True
            continue

        for v, weight in graph[u]:
            if not blocked[v] and costs[v] > costs[u] + weight:
                costs[v] = costs[u] + weight
                q.put(((costs[v], v), v))

    return sum_of_cost

runtests(lets_roll, all_tests = True)
