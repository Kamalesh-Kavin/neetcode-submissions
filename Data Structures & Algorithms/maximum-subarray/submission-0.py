class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSub=nums[0]
        curr=0
        for n in nums:
            if curr<0:
                curr=0
            curr+=n
            maxSub=max(curr,maxSub)
        return maxSub