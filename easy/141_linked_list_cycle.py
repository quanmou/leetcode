# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        p1 = head
        p2 = head.next
        while p1 and p2:
            if p1 == p2:
                return True
            p1 = p1.next
            try:
                p2 = p2.next.next
            except:
                return False
        return False

S = Solution()
print(S.hasCycle([3,2,0,-4]))
