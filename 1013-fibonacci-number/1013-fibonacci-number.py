class Solution:
    def fib(self, n: int) -> int:
        #base case
        if n < 2 :
            return n

        #recursive case
        return self.fib(n - 1) + self.fib(n - 2)