def get_items(parents, max_capacity):
    n = len(parents)
    items = []
    w = max_capacity
    for i in range(n-1, -1, -1):
        if parents[i][w] == w or parents[i][w] is None:
            continue
        items.append(i)
        w = parents[i][w]
    return items[::-1]



def knapsack(weights, values, max_capacity):
    n = len(weights)
    F = [[0]*(max_capacity+1) for _ in range(n)]
    P = [[None]*(max_capacity+1) for _ in range(n)]

    for w in range(weights[0], max_capacity+1):
        F[0][w] = values[0]
        P[0][w] = w - weights[0]

    for i in range(1, n):
        for w in range(max_capacity+1):
            F[i][w] = F[i-1][w]
            P[i][w] = w
            if w - weights[i] >= 0:
                if F[i-1][w-weights[i]]+values[i] > F[i][w]:
                    F[i][w] = F[i-1][w-weights[i]] + values[i]
                    P[i][w] = w-weights[i]

    return F[n-1][max_capacity], get_items(P, max_capacity)


max_capacity = 7
values = [19, 16, 28, 23]
weights = [3, 2, 5, 4]

print(knapsack(weights, values, max_capacity))