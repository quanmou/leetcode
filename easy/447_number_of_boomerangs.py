class Solution:
    def numberOfBoomerangs2(self, points) -> int:
        dis = {}
        count = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                d = self.distance(points[i], points[j])
                if d not in dis:
                    dis[d] = [[i, j]]
                else:
                    dis[d].append([i, j])
        for v in dis.values():
            for i in range(len(v)):
                for j in range(i + 1, len(v)):
                    if len(set(v[i]) & set(v[j])):
                        count += 2
        return count

    def distance(self, p1, p2):
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

    def numberOfBoomerangs(self, points):
        count = 0
        for i in points:
            a = {}
            for j in points:
                c = (i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2  ###Calculate the (distance)^2
                if c not in a:
                    a[c] = 1
                else:
                    count += a[c]
                    a[c] += 1  ### to find the number of all combinations
        return count * 2  ### order matters

s = Solution()
# print(s.numberOfBoomerangs([[0,0],[1,0],[2,2],[3,0],[4,0]]))
print(s.numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]]))
