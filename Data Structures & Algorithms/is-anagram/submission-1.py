class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(t)==len(s)):
            if (sorted(t) == sorted(s)):
                return True
            else:
                return False
        else:
            return False