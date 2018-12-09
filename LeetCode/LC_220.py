class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 1 or t < 0:
            return False
        d = collections.OrderedDict()
        for n in nums:
            key = n if t < 1 else n // t
            if any(abs(n - v) <= t for v in [d.get(keyOff) for keyOff in range(key-1, key+2) if keyOff in d]):
                return True
            while len(d) >= k:
                d.popitem(False)
            d[key] = n
        return False