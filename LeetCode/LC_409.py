def longestPalindrome(s):
    d = set()
    count = 0
    for c in s:
        if c in d:
            d.remove(c)
            count += 2
        else:
            d.add(c)
    if d:
        return count + 1
    else:
        return count