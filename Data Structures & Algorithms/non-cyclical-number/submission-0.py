class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSq(digits): # behaves like a linked list structure, with graphs pointing to e/o
            output = 0
            while digits != 0:
                output += (digits % 10) ** 2
                digits //= 10

            return output
        
        slow = n
        fast = sumOfSq(n)
        while fast != slow:
            slow = sumOfSq(slow)
            fast = sumOfSq(fast)
            fast = sumOfSq(fast)

        if slow != 1:
            return False
        
        return True
