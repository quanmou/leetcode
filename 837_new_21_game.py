# New 21 game
# To be continued...


class Solution:
    def step(self, point, W):
        if -1 * W <= point and point <= -1:
            return 0
        elif point == 0:
            return 1
        else:
            count = 0
            for i in range(W):
                count += self.step(point-i-1, W)
            return count

    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        if N < K:
            return 0.0
        elif N > (K + W - 1):
            return 1.0

        count = 0
        point_step = {}
        for point in range(K - W, K):
            po = self.step(point, W)
            count += po
            point_step[point] = po

        # for point in range(K - W, K):
        #     point_step[point] /= count * 1.0

        p = 0
        for key, value in point_step.items():
            num = 0
            for j in range(K - key, W + 1):
                if key + j <= N:
                    num += 1
            p += 1.0 * value * num / (W + 1 - (K - key))

        return p / count

        # if N > W+K-1:
        #     return 0
        #
        # dp = [1.0] + N*[0.0]
        # dp_sum = dp[0]
        #
        # for i in range(1,N+1):
        #     if i <= W:
        #         dp[i] = dp_sum / W
        #         dp_sum += dp[i]
        #
        #     if i>W:
        #         if i<=K:
        #             dp_sum = sum(dp[i-W:i])
        #             dp[i] = dp_sum / W
        #         else:
        #             dp_sum -= dp[i-W]
        #             dp[i] = dp_sum / W
        #
        # return sum(dp[K:])


solution = Solution()
print(solution.new21Game(21, 17, 10))
