class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        stk = []
        ans=0
        for i in nums:
            if i ==1:
                stk.append(i)
            else:
                l=0
                while stk:
                    l+=1
                    stk.pop()
                ans = max(ans,l)
        return max(ans, len(stk))
        