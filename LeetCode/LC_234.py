# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        # determine the length by traversing once
        L = 0
        cur = head
        while cur:
            L += 1
            cur = cur.next
        
        # basic cases are just true
        if L < 2:
            return True
        
        # reach the center while reversing the first half
        H = L // 2
        pre = None
        cur = head
        nex = None
        while H > 0:
            H -= 1
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        
        # skip the center node if length is odd
        if L % 2:
            nex = nex.next
        
        # pre is now the head of the first half
        while pre:
            if pre.val != nex.val:
                return False
            pre = pre.next
            nex = nex.next
        return True