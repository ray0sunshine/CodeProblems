class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(self, a, b):
    if not a or not b:
        return None
    
    # traverse both lists and determine length
    al = 1
    ac = a
    while ac.next:
        al += 1
        ac = ac.next
        
    bl = 1
    bc = b
    while bc.next:
        bl += 1
        bc = bc.next
    
    # cut the longer list from the front (or rather set the pointer to be equidistant from the end)
    diff = al - bl
    ac = a
    bc = b
    if diff > 0:
        while diff > 0:
            ac = ac.next
            diff -= 1
    elif diff < 0:
        diff = -diff
        while diff > 0:
            bc = bc.next
            diff -= 1
        
    # compare each node by stepping through simultaneously
    print(ac.val, bc.val)
    while ac and bc:
        if ac == bc:
            return ac
        ac = ac.next
        bc = bc.next
    return None