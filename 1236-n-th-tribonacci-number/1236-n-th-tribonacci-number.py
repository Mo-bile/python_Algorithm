class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0 for _ in range(n + 1)]
        if n < 1:
            return t[n]
        t[1] = 1
        if n < 2:
            return t[n]
        t[2] = 1
        if n < 3:
            return t[n]

        i = 3
        while i < n + 1:
            t[i] = t[i-3] + t[i-2] + t[i-1]
            i += 1

        return t[-1]