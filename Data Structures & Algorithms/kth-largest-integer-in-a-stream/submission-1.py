class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k

        self.nums = nums
        heapq.heapify(self.nums) # O(n) operation, makes the list a min heap

        while len(self.nums) > k: # remove the smallest elements from the min heap until the top k are left
            heapq.heappop(self.nums)
        
        # self.nums now only has the top k elements

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val) # push in the new value
        
        if len(self.nums) > self.k: # if the small list exceeds k we heappop to maintain k size
            heapq.heappop(self.nums) # the former kth + 1 element leaves
        
        return self.nums[0] # the first element in the min heap will always be the kth element


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)