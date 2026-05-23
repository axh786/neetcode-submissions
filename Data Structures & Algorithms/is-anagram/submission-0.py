class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_letters = {}

        for letter in s:
            if letter in s_letters:
                s_letters[letter] += 1
            
            else:
                s_letters[letter] = 1
        
        for letter in t:
            if letter in s_letters:
                s_letters[letter] -= 1
                
                if s_letters[letter] == 0:
                    del s_letters[letter]
            
            else:
                return False
        
        if s_letters:
            return False
         
        return True
        