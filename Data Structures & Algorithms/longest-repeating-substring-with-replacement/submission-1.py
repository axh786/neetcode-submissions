class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # output = 0
        # frq_dict = {} # storing the frq of the window
        # l = 0
        # for r in range(len(s)):
        #     if s[r] in frq_dict:
        #         frq_dict[s[r]] += 1
        #     else:
        #         frq_dict[s[r]] = 1

        #     # just gets the max char frq. Doesn't get the actual char but just the highest number
            
        #     while (r - l + 1) - max(frq_dict.values()) > k: # we check the window size against the highest frq char. This difference shows how many characters need to be replaced.
        #         frq_dict[s[l]] -= 1
        #         l += 1


        #     output = max(r-l+1, output)


        # return output

        # the biggest valid substring is maxf + k because we have the most characeters we can have and the most replacements added on. That has to be the biggest valid
        # this also means we are capped. If I have a maxf of 4 and k = 2, the max window i can possibly have is 6
        output = 0
        frq_dict = {}
        l = 0
        maxf = 0

        for r in range(len(s)):
            frq_dict[s[r]] = frq_dict.get(s[r], 0) + 1
            maxf = max(maxf, frq_dict[s[r]]) # maxf value can stay even after modification because it can only make us overestimate how good the window is

            # maxf can never cause an invalid answer because it only increases with the right pointer; it reps the largest frq that we have ever seen

            while (r - l + 1) - maxf > k:
                frq_dict[s[l]] -= 1
                l += 1
            

            output = max(r - l + 1, output)

        return output

