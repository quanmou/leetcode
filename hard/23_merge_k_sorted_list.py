import heapq
from queue import PriorityQueue

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def mergeKLists(self, lists: list) -> list:
        if len(lists) < 1:
            return []
        h, res = [], []
        for l in lists:
            for num in l:
                heapq.heappush(h, num)

        while h:
            res.append(heapq.heappop(h))

        return res


class Solution2:
    def mergeKLists(self, lists: list) -> list:
        heap = [(l.val, idx) for idx, l in enumerate(lists) if l]
        heapq.heapify(heap)
        p = dummy = ListNode(0)
        while heap:
            cur_val, idx = heapq.heappop(heap)
            p.next = ListNode(cur_val)
            p = p.next
            lists[idx] = lists[idx].next
            next_node = lists[idx]

            if next_node:
                heapq.heappush(heap, (next_node.val, idx))
        return dummy.next


class Solution3:
    def mergeKLists(self, lists):
        p = head = ListNode(0)
        q = PriorityQueue()
        for idx, l in enumerate(lists):
            if l:
                q.put((l.val, idx))
        while not q.empty():
            val, idx = q.get()
            p.next = ListNode(val)
            p = p.next
            lists[idx] = lists[idx].next
            node = lists[idx]
            if node:
                q.put((node.val, idx))
        return head.next


class Solution4:
    """lists中的元素是数组，非链表形式"""
    def mergeKLists(self, lists):
        heap = [(l[0], idx) for idx, l in enumerate(lists) if l]
        heapq.heapify(heap)
        res = []
        while heap:
            val, idx = heapq.heappop(heap)
            res.append(val)
            lists[idx].pop(0)
            if lists[idx]:
                heapq.heappush(heap, (lists[idx][0], idx))
        return res


S = Solution4()
print(S.mergeKLists([[1, 4, 5], [1, 3, 4], [2, 6]]))
