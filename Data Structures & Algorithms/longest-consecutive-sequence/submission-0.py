class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest = 0
        numSet = set(nums) # store the numbers in a set, leave only unique values avoids miscounting

        for num in numSet:
            if num - 1 not in numSet: # if the curr num doesnt have anything before it (aka if the curr num is the start of the seq)
                seqLen = 1
                seq = num
                while seq + 1 in numSet: # keep checking if the next num in the seq and adding
                    seq += 1
                    seqLen += 1
                longest = max(longest, seqLen)

        return longest

# we dont need to remove numbeers as the if will make sure we dont waste our time with nums that have a - 1