class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = defaultdict(list)
        for string in strs:
            count = [0] * 26

            for ch in string:
                ind = ord(ch) - ord('a')
                count[ind] =+ 1
                
            key = tuple(count)
            map[key].append(string)

        return list(map.values())

        