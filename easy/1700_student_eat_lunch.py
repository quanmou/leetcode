from collections import Counter

class Solution:
    def countStudents(self, students, sandwiches) -> int:
        if not students or not sandwiches:
            return 0

        while students:
            top_san = sandwiches[0]
            if top_san == students[0]:
                students = students[1:]
                sandwiches = sandwiches[1:]
            else:
                if top_san not in students:
                    break
                idx = students.index(top_san)
                students = students[idx:] + students[:idx]

        return len(students)

    def countStudents_2(self, students, sandwiches) -> int:
        prefers = Counter(students)
        n, k = len(students), 0
        while k < n and prefers[sandwiches[k]]:
            prefers[sandwiches[k]] -= 1
            k += 1
        return n - k

s = Solution()
s.countStudents([1,1,0,0], [0,1,0,1])
