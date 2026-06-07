class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones: # build the max heap
            heapq.heappush(max_heap, stone * -1)
        
        # while the size of max_heap is larger than 1
        # in the loop compare the top 2 highest, then do the x <= y
        # y - x, heappush inserts that value back in
        
        while len(max_heap) > 1: # if length is 1 or 0
            y = heapq.heappop(max_heap) * -1 # values leave negative
            x = heapq.heappop(max_heap) * -1
            
            if x != y:
                y -= x
                heapq.heappush(max_heap, y * -1)
        
        if max_heap:
            return (max_heap[0] * -1) # values leave negative
        
        return 0
        