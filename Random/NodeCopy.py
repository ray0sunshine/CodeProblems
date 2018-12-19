# Given a node structure with only a list of refs to it�s children, duplicate the graph structure. Watch for cycles

from collections import deque

class Node:
    def __init__(self):
        self.children = []

def dupe(head):
    if not head:
        return None

    # use a tracker and queue for iteration
    q = deque([head])
    m = {}

    # create a copy of each node
    while q:
        cur = q.popleft()
        if not cur in m:
            m[cur] = Node()
            if cur.children:
                q.extend(cur.children)

    # do connections
    for k,v in m.items():
        if k.children:
            v.children = [m[kc] for kc in k.children]

    return m[head]