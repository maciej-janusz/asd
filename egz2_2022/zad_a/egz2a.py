from egz2atesty import runtests
class SegmentTree:
    def parent(self, pos):
        return (pos-1)//2
    def left(self, pos):
        return 2*pos + 1
    def right(self, pos):
        return 2*pos + 2

    def getPos(self, idx):
        return self.size + idx - 1

    def getIdx(self, pos):
        return pos - self.size + 1

    def __init__(self, size, T):
        self.size = 1
        while self.size < size:
            self.size *= 2
        self.tree = [T] * (2 * self.size-1)

    def update(self, idx, value):
        pos = self.getPos(idx)
        self.tree[pos] -= value
        pos = self.parent(pos)
        while pos > 0:
            self.tree[pos] = max(self.tree[self.left(pos)], self.tree[self.right(pos)])
            pos = self.parent(pos)

    def query(self, value):
        pos = 0
        while pos < self.size-1:
            if self.tree[self.left(pos)] >= value:
                pos = self.left(pos)
            else:
                pos = self.right(pos)
        return self.getIdx(pos)


def coal(A, T):
    n = len(A)
    tree = SegmentTree(n, T)  # maksymalnie n magazynów

    for i, amount in enumerate(A):
        idx = tree.query(amount)
        tree.update(idx, amount)
        last_idx = idx

    return last_idx


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )
