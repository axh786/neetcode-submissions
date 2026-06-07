class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for num in nums: # build the max heap
            heapq.heappush(max_heap, num * -1) # log n operation
        
        # return max_heap
        
        output = 0
        for i in range(k): # iterate up to K
            output = heapq.heappop(max_heap) * -1 # multiple by negative since its coming out negative
        
        return output
        