class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = {}
        #map = defaultdict(list) #create hashmap
        # create array with freq for each word
        # key into map but key has to be a tuple because list is mutable
        # value of key is a list of the orginial word

        for word in strs:
            freq = [0] * 26 #list

            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            
            key = tuple(freq)
            
            if key in map:
                map[key].append(word)
            else:
                map[key] = [word]
        
        answer = list(map.values())
        return answer


        