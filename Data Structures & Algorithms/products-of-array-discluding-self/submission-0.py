class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = []
        
        multi = 1
        for num in nums: # prefix loop
            res.append(multi) # apply the prefix products
            multi *= num

        multi = 1
        for index in range(len(nums) - 1, -1, -1): # suffix loop
            res[index] *= multi # multiply the suffix products
            multi *= nums[index]

        return res 
        