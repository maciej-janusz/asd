"""
    tankujemy ile chcemy
"""
import heapq
def greedy_truck(L, pos, price):
    n = len(pos)
    cost = 0
    tank = 0
    idx = 0
    while idx < n - 1:
        best = idx + 1
        found = False
        for i in range(idx+1, n):
            d = pos[i] - pos[idx]
            if d > L:
                break
            if price[i] <= price[idx]:
                if tank >= d:
                    tank -= d
                else:
                    cost += (d - tank) * price[idx]
                    tank = 0
                found = True
                idx = i
                break
            elif price[i] < price[best]:
                best = i
        if not found:
            d = pos[best]-pos[idx]
            fuel_needed = min(L, pos[n-1] - pos[idx])
            if tank >= fuel_needed:
                tank -= d
            else:
                cost += (fuel_needed - tank) * price[idx]
                tank = fuel_needed - d
            idx = best

    return cost


L = 50
pos = [0, 20, 40, 60, 70]
price = [7, 3, 2, 5, 10]

print(greedy_truck(L, pos, price))
