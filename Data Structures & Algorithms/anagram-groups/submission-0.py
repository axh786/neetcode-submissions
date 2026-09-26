class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list) # default value of list, mapps the character count to a list of anagrams
        
        # key is a tuple of the counts, value is a list of the words that have that exact count
        for string in strs:
            count = [0] * 26 # counts letter with a ... z, add to it to map each letter

            for char in string:
                count[ord(char) - ord("a")] += 1 # counting for each character that we have
        
            res[tuple(count)].append(string) # anagrams now are grouped together (matching letter counts)

        return list(res.values())