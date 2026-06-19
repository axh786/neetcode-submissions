class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_dict = {}
        for letter in s1: # o(n)
            if letter in s1_dict:
                s1_dict[letter] += 1
            else:
                s1_dict[letter] = 1
        l = 0
        r = len(s1) - 1

        window_dict = {} # build the window dict
        for i in range(l, r):
            if s2[i] in window_dict:
                window_dict[s2[i]] += 1
            else:
                window_dict[s2[i]] = 1
        
        while r < len(s2):
            if s2[r] in window_dict: # add in the latest r
                window_dict[s2[r]] += 1
            else:
                window_dict[s2[r]] = 1
            
            if window_dict == s1_dict: # check if its the same, this is an O(26) operation worst case
                return True

            if window_dict[s2[l]] > 1: # remove the left most element (leaving window)
                window_dict[s2[l]] -= 1 
            else:
                window_dict.pop(s2[l])


            l += 1
            r += 1
        
        return False
