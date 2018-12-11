class Solution(object):
    def calculateMinimumHP(self, d):
        w = len(d)-1
        h = len(d[0])-1
        for wi in range(w,-1,-1):
            for hi in range(h,-1,-1):
                req = []
                if hi < h:
                    req.append(d[wi][hi+1])
                if wi < w:
                    req.append(d[wi+1][hi])
                if req:
                    d[wi][hi] = max(1, min(req) - d[wi][hi])
                else:
                    d[wi][hi] = max(1, 1 - d[wi][hi])
        return d[0][0]