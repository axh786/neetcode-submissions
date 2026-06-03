class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set() # O(1) lookups

        for num in nums:
            if num in nums_set:
                return True
            
            nums_set.add(num)
        
        return False