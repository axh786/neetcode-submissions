class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # we can plot the points onto a graph time vs position to help us visiualize 
        # sort the cars in sorted order by position
        # if a car before aanother car gets to a destination first it MUST mean they turn into a fleet

        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = [] # stack will tell us how many car fleets we have in the end
        
        for p, s in pair: # Reverse sorted order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # if the time is less than the second one pop
                stack.pop() # this now represents a fleet

        return len(stack)