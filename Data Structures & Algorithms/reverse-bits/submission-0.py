class Solution:
    def reverseBits(self, n: int) -> int:
        # we are given a 32 bits signed integer, n is always even
        # bit & 1 gives us what the value of the bit is bit = 1 we get 1 vice versa with 0
        
        res = 0
        for i in range(32): # we go through every bit in the input (we know its 32 bit)
            bit = (n >> i) & 1 # extracts the bit at position i
            res += (bit << (31 - i)) # add the value to each 1 << 0 is 1 1 << 1 to 2 and so on 
        
        return res