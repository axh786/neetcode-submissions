class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode a list of strings to a string
        if not strs:
            return ""

        encoded = ""
        for i in range(len(strs)):
            length = len(strs[i])
            encoded += str(length)
            encoded += "#"
            encoded += strs[i]
            

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            length = ""
            while s[i].isdigit():
                 length += s[i]
                 i += 1
            
            i += 1
            
            length = int(length)
            string = ""            
            c = 0
            while c < length:
                string += s[i]
                i += 1
                c += 1
            
            decoded.append(string)
        
        return decoded
