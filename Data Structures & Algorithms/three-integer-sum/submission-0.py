class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]: # skip duplicate numbers on the first fixed point
                continue
            
            r = len(nums) - 1
            l = i + 1


            while l < r:
                sums = nums[i] + nums[l] + nums[r]
                
                if sums > 0:
                    r -= 1
                
                elif sums < 0:
                    l += 1 
                
                else:
                    res.append([nums[i],  nums[l], nums[r]])

                    l += 1 # we move both as we saw all possible combinations of those L and R. They cant match with another 
                    r -= 1 

                    while l < r and nums[l] == nums[l - 1]: # we skip the dupliactes of l until we find a unique value to compare it against the r
                        l += 1

        return res
