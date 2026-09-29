class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # return sorted(s) == sorted(t)

        table_s, table_t = {}, {}
        
        for ind in range(len(s)):
            if s[ind] in table_s:
                table_s[s[ind]] = table_s.get(s[ind]) + 1
            table_s[s[ind]] = 1

            if s[ind] in table_t:
                table_t[t[ind]] = table_t.get(s[ind]) + 1
            table_t[t[ind]] = 1

        return table_s == table_t

