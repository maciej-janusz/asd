from zad2testy import runtests
from math import inf

class BNode:
    def __init__( self, value ):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


def visit(node):
    if node.left is None and node.right is None:
        return inf
    min_sum = 0
    if node.left is not None:
        min_sum += visit(node.left)
    if node.right is not None:
        min_sum += visit(node.right)
    if node.parent is None:
        return min_sum
    return min(min_sum, node.value)
def cutthetree(T):
    return visit(T)

    
runtests(cutthetree)


