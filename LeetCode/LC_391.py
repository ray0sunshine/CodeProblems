class Solution(object):
    def isRectangleCover(self, rect):
        # determine the large rect by finding the min/max x/y
        # area of components should be exactly equal to area a large rect
        # all corner points should appear once, and all other points twice
        
        inf = float('inf')
        xmin, ymin, xmax, ymax = inf, inf, -inf, -inf
        areaT = 0
        c = {}
        for r in rect:
            x1, y1, x2, y2 = r
            xmin, ymin, xmax, ymax = min(xmin, x1), min(ymin, y1), max(xmax, x2), max(ymax, y2)
            areaT += (x2 - x1) * (y2 - y1)
            for co in [(x1, y1), (x2, y2), (x1, y2), (x2, y1)]:
                if not co in c:
                    c[co] = 0
                c[co] += 1
        
        if areaT != (xmax - xmin) * (ymax - ymin):
            return False
        
        ccs = set([(xmin, ymin), (xmax, ymax), (xmax, ymin), (xmin, ymax)])
        
        if any([(not cc in c) for cc in ccs]):
            return False
        
        if any([c[cc] != 1 for cc in ccs]):
            return False
        
        [c.pop(cc) for cc in ccs]
        
        for v in c.values():
            if v % 2:
                return False
            
        return True