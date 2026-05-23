class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = -1
        negativeSize = len(digits) * -1

        if digits[i] != 9: # if the last digit isnt a 9, we can just simply add and return
            digits[i] += 1
            return digits
        else:
            while i >= negativeSize and digits[i] == 9: # for every last 9, add 1
                digits[i] = 0
                i -= 1
            
            if i < negativeSize: # if i reached the end (aka the first element) num was 9..
                return [1] + digits
            
            digits[i] += 1 # else it was something like 1299
            return digits
            