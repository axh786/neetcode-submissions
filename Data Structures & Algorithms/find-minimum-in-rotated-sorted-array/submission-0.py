class Solution:
    def findMin(self, nums: list[int]) -> int:
        # div = 0
        # for i in range(len(nums) - 1):
        #     if nums[i] > nums[i+1]:
        #         div = i
        #         break
        #     elif i == len(nums) - 2:
        #         div = len(nums) - 1
        
        # if div == len(nums) - 1:
        #     return nums[0]
        
        # return nums[div + 1]  
        l = 0
        r = len(nums) - 1

        while l != r:
            mid = (l + r)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid

        return nums[r]

