class Solution:
    def isValid(self, s: str) -> bool:
        # stack = []

        # for ch in s:
        #     if ch == "(" or ch =="[" or ch == "{":
        #         stack.append(ch)

            
        #     else:
        #         if not stack:
        #             return False
        #         popped = stack.pop()
        #         if (ch == ")" and popped != "(") or (ch == "]" and popped != "[") or (ch == "}" and popped != "{"):
        #             return False

        # if stack:
        #     return False

        # return True



        stack = []
        
        data = { "(" : ")", "[" : "]", "{" : "}" }

        for c in s:
            if c in data:
                stack.append(c)

            else:
                if not stack:
                    return False
                if c == data[stack[-1]]:
                    stack.pop()
                else:
                    return False

        if stack:
            return False

        return True

        
        