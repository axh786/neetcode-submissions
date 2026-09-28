class Solution:
    def hammingWeight(self, n: int) -> int:
        oneBits = 0
        
        while n != 0: # & only returns 1 when both bits are 1
            if n & 1: # if n is an odd number ex 3 and we 3 & 1, res is 1. last bit signifies odd or even, if odd it has a 1 and its counted 
                oneBits += 1
            n >>= 1 # shift bits to the right, 011 turns into 001 (3 to 1)

        return oneBits
