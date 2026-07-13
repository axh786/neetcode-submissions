class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        for num in reversed(nums2): # Traverse from right to left so the stack already contains all elements to the right
            while stack and stack[-1] <= num: # while the stack has values and whiel the top of the stack is less than the num pop
                stack.pop()

            if stack: # if the stack stil exists that means the bottom of the stack is the next largest value
                next_greater[num] = stack[-1]
            else: # stack is empty no larger values than the current num
                next_greater[num] = -1 

            stack.append(num) # we append the num regardless as it either found its next largest value or it is the largest and onyl value in the stack
            

        res = []
        for num in nums1: # dict at the beginning allows us to index to each value and see thier next largest value in O(1) time
            res.append(next_greater[num])

        return res