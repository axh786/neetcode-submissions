class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        output = 0 # first iteration (output ^ nums[0]) will evaluate to nums[0]

        for num in nums:
            output ^= num # using XOR on the entire array will naturally bring upon the non-repeated value. All of the other repeated values 0 out
        
        return output
    
    # x ^ x = 0 and x ^ 0 = x. 
    # XOR is associate and commutative, the order doesnt matter. 