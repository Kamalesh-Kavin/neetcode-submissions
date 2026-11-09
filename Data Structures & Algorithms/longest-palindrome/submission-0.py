class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}
        ans=0
        for i in s:
            hashmap[i] = hashmap.get(i,0)+1

        ans = 0
        odd_found = False

        for count in hashmap.values():
            if count % 2 == 0:
                ans += count
            else:
                ans += count - 1
                odd_found = True

        if odd_found:
            ans += 1
        return ans
        