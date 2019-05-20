# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: list) -> list:
        import heapq
        if len(lists) < 1:
            return []
        h, res = [], []
        for l in lists:
            for num in l:
                heapq.heappush(h, num)

        while h:
            res.append(heapq.heappop(h))

        return res

S = Solution()
print(S.mergeKLists([[1,4,5],[1,3,4],[2,6]]))
