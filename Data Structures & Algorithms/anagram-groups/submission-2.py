class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = {}

        for word in strs:
            sorted_word_list = sorted(word)
            sorted_word = "".join(sorted_word_list)

            if sorted_word in result:
                result[sorted_word].append(word)

            result[sorted_word] = [word]

        answer = list(result.values())
        return answer
