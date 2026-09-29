class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for str in strs:
            num = len(str)
            encoded = f"{encoded}{num}#{str}"

        print(encoded)
        return encoded



    def decode(self, s: str) -> List[str]:

        decoded = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            num = int(s[i:j])
            
            j += 1
            decoded.append(s[j:j+num])
            i = j + num
             
        return decoded

