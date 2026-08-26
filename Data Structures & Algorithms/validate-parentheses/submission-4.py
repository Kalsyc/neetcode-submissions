class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p_map = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in p_map and stack:
                p = stack.pop()
                if p_map[i] != p:
                    return False
            else:
                stack.append(i)
        return len(stack) == 0