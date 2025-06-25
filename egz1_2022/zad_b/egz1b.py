from egz1btesty import runtests

class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # maksymalna glebokosc osiagalna z poddrzewa


def dfs(root, depths, depth):
    if depth > len(depths)-1:
        depths.append(0)
    depths[depth] += 1

    deepest = depth
    if root.left is not None:
        deepest = max(dfs(root.left, depths, depth+1), deepest)
    if root.right is not None:
        deepest = max(dfs(root.right, depths, depth+1), deepest)

    root.x = deepest
    return deepest


def cut(root, best_depth, delete_cnt, depth):
    if depth == best_depth:
        if root.left is not None:
            delete_cnt[0] += 1
            root.left = None
        if root.right is not None:
            delete_cnt[0] += 1
            root.right = None
    else:
        if root.left is not None:
            if best_depth > root.left.x:
                delete_cnt[0] += 1
                root.left = None
            else:
                cut(root.left, best_depth, delete_cnt, depth+1)
        if root.right is not None:
            if best_depth > root.right.x:
                delete_cnt[0] += 1
                root.right = None
            else:
                cut(root.right, best_depth, delete_cnt, depth+1)


def wideentall( T ):
    T.x = (0, 0)
    depths = []
    dfs(T, depths, 0)
    best_width = max(depths)
    best_depth = 0
    for i in range(len(depths)):
        if depths[i] == best_width:
            best_depth = i

    delete_cnt = [0]
    cut(T, best_depth, delete_cnt, 0)
    return delete_cnt[0]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = True )