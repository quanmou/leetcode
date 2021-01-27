class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for x in range(1, amount + 1):
            for coin in coins:
                if x >= coin:
                    dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] < amount + 1 else -1


class Solution:
    def coinChange(self, coins, amount) -> int:
        coins.sort(reverse=True)
        min_coins = float('inf')

        def count_coins(start_idx, coin_count, remaining_amount):
            nonlocal min_coins

            if remaining_amount == 0:
                min_coins = min(min_coins, coin_count)
                return

            # Iterate from largest coins to smallest coins
            for i in range(start_idx, len(coins)):
                # 最多还能允许使用几个硬币（因为要追求的是比当前最少的硬币数还要少）
                remaining_coin_allowance = min_coins - coin_count
                # 以当前的硬币数乘以最多还允许使用的硬币个数，就能得到最多还能凑够多少钱
                max_amount_possible = coins[i] * remaining_coin_allowance

                # 只有当前硬币面值小于等于还需要凑的金额，而且剩余金额小于目前最多还能凑的金额
                if coins[i] <= remaining_amount and remaining_amount < max_amount_possible:
                    count_coins(i, coin_count + 1, remaining_amount - coins[i])

        count_coins(0, 0, amount)
        return min_coins if min_coins < float('inf') else -1


class Solution:
    def coinChange(self, coins, amount: int) -> int:
        coins.sort(reverse=True)
        min_count = float('inf')

        def dfs(idx, cur_count, remain_amount):
            nonlocal min_count
            if remain_amount == 0:
                min_count = min(min_count, cur_count)
                return
            if idx == len(coins):
                return

            max_cur_coin = remain_amount // coins[idx]
            for k in range(max_cur_coin, -1, -1):
                if k + cur_count > min_count:
                    return
                dfs(idx + 1, cur_count + k, remain_amount - k * coins[idx])

        dfs(0, 0, amount)
        return min_count if min_count != float('inf') else -1


s = Solution()
print(s.coinChange([1, 2, 5], 11))
print(s.coinChange([186,419,83,408], 6249))
