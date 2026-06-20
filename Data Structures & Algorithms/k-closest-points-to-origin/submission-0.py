class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ecd = []
        for point in points:
            x = point[0] ** 2
            y = point[1] ** 2
            euc = math.sqrt(x + y)
            heapq.heappush(ecd, (euc * -1, point))
            if len(ecd) > k:
                heapq.heappop(ecd) # biggest value, which is the easiest to remove, gets removed
        # curr max heap is 4 3 2. 5 comes in now its 5 4 3 2. 5 is popped bc its new max (and since k = 3) so its 4 3 2. 1 comes in now its 4 3 2 1. 4 popped since len > k 3 2 1.
        output = [tup[1] for tup in ecd]

        return output
        
    
# we could have stored all the points, heapify, print out 3. Interviewers prefer smaller space complexity for heap questions which is why a max heap solution is preferred (it maintains the )

# quick select is also viable here as an O(n) avg time