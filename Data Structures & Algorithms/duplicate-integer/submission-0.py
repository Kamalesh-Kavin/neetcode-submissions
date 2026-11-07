class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        soln_set = set()
        for i in nums:
            if i in soln_set:
                return True
            soln_set.add(i)
        return False
            