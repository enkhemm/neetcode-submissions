class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch == "(" or ch =="[" or ch == "{":
                stack.append(ch)

            
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if (ch == ")" and popped != "(") or (ch == "]" and popped != "[") or (ch == "}" and popped != "{"):
                    return False

        if stack:
            return False

        return True
        