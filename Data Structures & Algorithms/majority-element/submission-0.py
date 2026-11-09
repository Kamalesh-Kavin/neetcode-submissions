class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hashmap = {}
        res, maxCnt=0,0
        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
            res = i if hashmap[i]>maxCnt else res
            maxCnt =  max( hashmap[i], maxCnt)
        return res