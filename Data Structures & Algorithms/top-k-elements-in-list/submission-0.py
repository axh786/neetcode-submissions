class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_frq = {}
        
        for num in nums: # build a frq dict before making the max heap
            if num in num_frq:
                num_frq[num] += 1
            else:
                num_frq[num] = 1
        
        max_heap = []
        
        for num, frq in num_frq.items(): # n elements, so n log n
            heapq.heappush(max_heap, (frq * -1, num)) # log n operation
        
        output = []
        for i in range(k):
            frq, value = heapq.heappop(max_heap) # heapq pop returns a tuple we have to unpack it by frq, value. Another log n operation
            output.append(value) # append the top k items from the max_heap into the output
        
        return output
        