class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for index in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[index]
            while stack and temperatures[stack[-1]] <= temp:
                stack.pop()

            if stack:
                res[index] = (stack[-1] - index) # since the res array already exists and is of 0's, we can directly index it backwards
            # else: not needed as res is already filled with 0's. We dont need to append then reverse vallues this way
            #     res.append(0)

            stack.append(index) # we only need to store indicies not temps as well as we can just access it again in the while by indexing again
            
        return res
        