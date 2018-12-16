from heapq import *

class Solution(object):
    def swimInWater(self, g):
        L = len(g) - 1
        ret = 0
        heap = [(g[0][0], 0, 0)]
        seen = set([g[0][0]])
        while True:
            v, x, y = heappop(heap)
            ret = max(ret, v)
            if x == y == L:
                return ret
            for x, y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= x <= L and 0 <= y <= L and not g[x][y] in seen:
                    seen.add(g[x][y])
                    heappush(heap, (g[x][y], x, y))