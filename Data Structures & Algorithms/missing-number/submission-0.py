class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        
        missing = 0
        c = 0
        for num in nums: #XOR's group and order doesnt matter
            missing ^= num
            missing ^= c

            c+= 1
        
        return c^missing # has the XOR with the nth value (c is now 3 in the example of 3,0,1)
