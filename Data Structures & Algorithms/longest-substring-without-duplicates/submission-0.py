
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in hashet:
                hashet.remove(s[l])
                l += 1

            hashet.add(s[r])
            res = max(res, r - l + 1)

        return res
