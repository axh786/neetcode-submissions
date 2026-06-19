class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        
        output = []
        intervals.sort(key = lambda interval: interval[0]) # input needs to be sorted first
        
        output.append(intervals[0])

        for interval in intervals:
            top_interval = output[-1]

            if top_interval[1] >= interval[0]:
                x = min(top_interval[0], interval[0])
                y = max(top_interval[1], interval[1])

                output[-1] = [x, y]
            else:
                output.append(interval)

        return output
