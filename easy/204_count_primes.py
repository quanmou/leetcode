import math

class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(math.sqrt(n)) + 1):
            if primes[i]:
                primes[i*i:n:i] = [False] * len(primes[i*i:n:i])
        print(primes)
        return sum(primes)

s = Solution()
print(s.countPrimes(499979))