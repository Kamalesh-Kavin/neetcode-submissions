class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        res, cnt = 0,0
        for i in nums:
            if cnt ==0:
                res=i
                cnt+=1
            elif res !=i:
                cnt-=1
            else: 
                cnt+=1
        return res