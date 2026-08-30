class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] not in 'abcdefghijklmnopqrstuvwxyz0123456789':
                left += 1
            elif s[right] not in 'abcdefghijklmnopqrstuvwxyz0123456789':
                right -= 1
            elif s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True