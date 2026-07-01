class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            if n == 0:
                return 1

            half = power(x, n//2)

            if n % 2 == 0:
                return half * half
            else:
                return x * half * half
        
        if x == 0:
            return x

        if n < 0:
            return power(1/x, n * -1)
        
        return power(x, n)
