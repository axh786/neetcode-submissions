class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode a list of strings to a string
        if not strs:
            return "strs"

        encoded = ""
        for i in range(len(strs)):
            encoded += strs[i]
            
            encoded += "–"

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = s.split("–")
        print(decoded[:-1])
        return decoded[:-1]
